import qualified Data.Vector.Unboxed as V


binarySearch ::  Int -> V.Vector Int-> Int
binarySearch number arr = binSearch number arr 0 (V.length arr - 1)

binSearch :: Int -> V.Vector Int -> Int -> Int -> Int
binSearch number arr low_index high_index
            |low_index == high_index = -1
            |number > testedNumber = binSearch number arr (index + 1) high_index
            |number < testedNumber = binSearch number arr low_index (index - 1)
            |(number == testedNumber) = index
            where index = (low_index + high_index) `div` 2
                  testedNumber = arr V.! index
