-- Writeup at https://work.njae.me.uk/2021/12/23/advent-of-code-2021-day-20/
   2 
   3 import Control.Monad.State.Strict
   4 import Control.Monad.Reader
   5 -- import Control.Monad.Writer
   6 import Control.Monad.RWS.Strict
   7 import Data.List
   8 import Data.Ix
   9 import Data.Maybe
  10 
  11 import qualified Data.Set as S
  12 import Linear (V2(..), (^+^))
  13 
  14 type Pixel = V2 Int -- row, column
  15 
  16 data Image = Image 
  17   { grid :: S.Set Pixel
  18   , distantPixel :: Bool
  19   , explicitRegion :: (Pixel, Pixel)
  20   } deriving (Eq, Show)
  21 
  22 type Enhancement = [Bool]
  23 
  24 type ImageEnhancer = RWS Enhancement [Int] Image
  25 
  26 main :: IO ()
  27 main = 
  28   do  text <- readFile "data/advent20.txt"
  29       let (enhancement, image) = parse text
  30       print $ part1 enhancement image
  31       print $ part2 enhancement image
  32 
  33 -- part1 enhancement image = s
  34 --   where (s, image', _) = runRWS (enhanceImage 2) enhancement image
  35 
  36 part1 enhancement image = fst $ evalRWS (enhanceImage 2) enhancement image
  37 
  38 part2 enhancement image = fst $ evalRWS (enhanceImage 50) enhancement image
  39 
  40 enhanceImage :: Int -> ImageEnhancer Int
  41 enhanceImage 0 = do image <- get
  42                     return $ S.size $ grid image
  43 enhanceImage n = do newImage
  44                     enhanceImage (n - 1)
  45 
  46 
  47 newImage :: ImageEnhancer ()
  48 newImage =
  49   do  region <- gets explicitRegion
  50       let region' = expandRegion region
  51       let heres = range region'
  52       newPixels <- mapM newPixel heres
  53       let grid' = S.fromList $ catMaybes newPixels
  54       distant <- gets distantPixel
  55       enhancement <- ask
  56       let distant' = if distant then (last enhancement) else (head enhancement)
  57       put $ Image {grid = grid', distantPixel = distant', explicitRegion = region'}
  58 
  59 showImage :: Image -> String
  60 showImage image = 
  61   unlines $ [ [showPixel (V2 r c) | c <- [minC..maxC] ] | r <- [minR..maxR]]
  62   where (V2 minR minC, V2 maxR maxC) = explicitRegion image
  63         g = grid image
  64         showPixel here = if here `S.member` g then '█' else ' '
  65 
  66 newPixel :: Pixel -> ImageEnhancer (Maybe Pixel)
  67 newPixel here =
  68   do  stencil <- findStencil here
  69       let i = intify stencil
  70       enh <- ask
  71       return $ if enh!!i then Just here else Nothing
  72 
  73 findStencil :: Pixel -> ImageEnhancer [Bool]
  74 findStencil here = 
  75   do  let nbrs = map (here ^+^) neighbours
  76       g <- gets grid
  77       d <- gets distantPixel
  78       r <- gets explicitRegion
  79       return $ map (findContents g d r) nbrs
  80       -- mapM findContents nbrs
  81 
  82 findContents :: S.Set Pixel -> Bool -> (Pixel, Pixel) -> Pixel -> Bool
  83 findContents grid distant region here 
  84   | inRange region here = here `S.member` grid
  85   | otherwise           = distant
  86 
  87 -- more consitent but much slower
  88 -- findContents :: Pixel -> ImageEnhancer Bool
  89 -- findContents here =
  90 --  do  g <- gets grid
  91 --      distant <- gets distantPixel
  92 --      region <- gets explicitRegion
  93 --      return $ if inRange region here 
  94 --               then (here `S.member` g)
  95 --               else distant
  96 
  97 neighbours :: [Pixel]
  98 neighbours = [V2 r c | r <- [-1, 0, 1], c <- [-1, 0, 1]]
  99 
 100 expandRegion :: (Pixel, Pixel) -> (Pixel, Pixel)
 101 expandRegion ((V2 r0 c0), (V2 r1 c1)) = (V2 (r0 - 1) (c0 - 1), V2 (r1 + 1) (c1 + 1))
 102 
 103 parse :: String -> (Enhancement, Image)
 104 parse text = (enhancement, image)
 105   where ls = lines text
 106         enhancement = [ c == '#' | c <- head ls]
 107         image = mkImage $ drop 2 ls
 108 
 109 
 110 mkImage :: [String] -> Image
 111 mkImage rows = Image { grid = grid, distantPixel = False
 112                      , explicitRegion = ((V2 0 0), (V2 maxRow maxCol))
 113                      }
 114   where maxRow = length rows - 1
 115         maxCol = (length $ head rows) - 1
 116         grid = S.fromList [V2 r c | r <- [0..maxRow], c <- [0..maxCol], (rows!!r)!!c == '#']
 117 
 118 intify :: [Bool] -> Int
 119 intify pixels = foldl' addBit 0 pixels
 120   where addBit w b = (w * 2) + (if b then 1 else 0)