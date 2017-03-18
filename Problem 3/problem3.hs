--Vinicius Sesti <vinicius.s.sesti@gmail.com>
--Project Euler: Problem 3
--The prime factors of 13195 are 5, 7, 13 and 29.
--What is the largest prime factor of the number 600851475143?

primeSieve::Int->[Int]
primeSieve n = (primeFilter [2..n])
  where
    primeFilter [] = []
    primeFilter (n:ns) = n:(primeFilter(filter (\x -> mod x n /= 0) ns))