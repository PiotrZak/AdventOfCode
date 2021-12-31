type Player = (Int, Int) -- position and score
type Game = (Player, Player, Int)  -- players and whose turn
type Memo = M.Map Game (Int, Int)  -- counts subgames by their outcome

-- possible sums of the 3 3-sided die's rolls
-- with the number of possible rolls leading to that sum
diracRolls = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

playDirac :: Memo -> Game -> (Memo, (Int, Int))
playDirac memo game@(player1@(p1, s1), player2@(p2, s2), turn)
  | s2 >= 21 = (memo, (0, 1))
  | s1 >= 21 = (memo, (1, 0))
  | otherwise = case memo !? game of
    Just v -> (memo, v)
    _ ->
      let subGames = map (first (makeTurn2 game)) diracRolls
          update (m, (r1, r2)) (sg, c) =
            let (m', (a, b)) = playDirac m sg in (m', (r1 + c * a, r2 + c * b))
          (memo', result) = foldl update (memo, (0, 0)) subGames
       in (M.insert game result memo', result)

solve2 = uncurry max . snd . playDirac M.empty . initGame