import pdb
import math

class PrimeGenerator:

	# public List<BigInteger> getPrimes()
	# {
		# List<BigInteger> copy = new List<BigInteger>();
		# for(int i = 0; i < primes.Count; ++i)
		# {
			# copy.Add(primes[i]);
		# }
		# return copy;
	# }

    def __init__(self, search):
        self.primes = []
        self.generatePrimes(search)

    def getPrime(self, n):
        return self.primes[n]

    # determines if a number is prime given a list of
    # primes less than or equal to the square root of the 
    # number in question
    # Note that this code makes some assumptions about its inputs!
    def isPrime(self, num):

        if (num <= 1):
            return False

        if num in self.primes:
            return True

        terminateEarly = int(math.sqrt(num))
        for x in self.primes:

            if x > terminateEarly:
                break

            if (num % x == 0):
                return False

        return True

    # prime computation via Sieve of Eratosthenes
    def generatePrimes(self, n):
        ret = [];
        ret.append(2);

        # populate the sieve
        i = 3
        while(i <= n):
            ret.append(i)
            i += 2

        primeIndex = 0
        prime = 2
        while (prime != ret[len(ret) - 1]):

	        # get next prime to work with
            primeIndex += 1
            prime = ret[primeIndex]					

	        # perform the sieve: remove all the elements that
	        # are multiples of the chosen prime
            marked = set()
            for x in ret:
                if (x % prime == 0 and x != prime):
                    marked.add(x)
            
            for p in marked:
                ret.remove(p)		

        self.primes = ret

	# static private Dictionary<BigInteger, List<BigInteger>> divisorLists = new Dictionary<BigInteger, List<BigInteger>>();

	# // returns a list of divisors of an integer
	# public List<BigInteger> getDivisors(BigInteger num)
	# {

		# // we use some memory to make using divisor lists
		# // far more efficient         
		# List<BigInteger> r;
		# if(divisorLists.TryGetValue(num, out r))
			# return r;

		# // we start with the factorization of the number
		# List<Tuple<BigInteger, BigInteger>> factorization = getFactorization(num);

		# // let k be the size of the list of factors, then we must visit each
		# // point in a kth dimensional cartesion space where the bounds are defined
		# // by the number of each factor in the factorization. Each point represents
		# // another divisor.          
		# int dimensions = factorization.Count;
		# int check = (int) factorization[dimensions - 1].Item2;
		# BigInteger[] point = new BigInteger[factorization.Count];

		# // initialize our starting point to the center of the space
		# for (int i = 0; i < dimensions; ++i )
		# {
			# point[i] = 0;
		# }

		# List<BigInteger> ret = new List<BigInteger>();
		# while (point[dimensions - 1] <= check)
		# {
			# // get divisor and add it to our list, then
			# // increment the point
			# BigInteger divisor = 1;
			# for(int i = 0; i < dimensions; ++i)
			# {
				# divisor *= BigInteger.Pow(factorization[i].Item1,  (int)point[i]);
			# }
			# ret.Add(divisor);
			
			# // now to increment the point
			# int j = 0;
			# ++point[j];

			# // this loop provides a mechanism to 'carry over'
			# // the increment
			# while (point[j] > factorization[j].Item2)
			# {
				# point[j] = 0;
				# ++j;

				# // ensures that we don't carry over into
				# // an out of bounds exception!
				# if (j == dimensions)
				# {
					# --j;
					# point[j] = check + 1; // this is also where / how we terminate the outer loop!
					# break;
				# }
				# ++point[j];
			# }

		# }

		# // store the divisor list in a dictionary
		# divisorLists.Add(num, ret);

		# return ret;
	# }

	# quick and dirty prime factorization
	def getFactorization(self, num):
		
		if (num <= 0):
			return []
		
		factorization = []
		count = 0
		for p in self.primes:	
			if(num % p == 0):
				num /= p
				count += 1
				while(num % p == 0):
					num /= p
					count+= 1
				pair = (p, count)
				factorization.append(pair)
				count = 0
				
		return factorization
			
	
		# ret = []           
		# factors = getFactors(num);
		# BigInteger previous = factors[0];
		# // factors is never empty! we'll be satisfied with an exception in this case
		# BigInteger count = 1;
		# for(int i = 1; i < factors.Count; ++i)
		# {
			# if(previous == factors[i])
			# {
				# ++count;
			# } else
			# {
				# Tuple<BigInteger, BigInteger> t = new Tuple<BigInteger, BigInteger>(previous, count);
				# ret.Add(t);
				# count = 1;
			# }
			# previous = factors[i];
		# }

		# // add the last tuple
		# ret.Add(new Tuple<BigInteger, BigInteger>(factors[factors.Count-1], count));

		# return ret;

	# // returns the prime factorization of the given number, although
	# // this list WILL contain duplicates
	# // we assume that our list of primes constitutes all of the primes that make-up
	# // the integer in question
	# // There is some strange overflow error that I'm not too worried about unless you want to use
	# // this code on larger numbers (although, you probably shouldn't)
	# public List<BigInteger> getFactors(BigInteger num)
	# {
		# List<BigInteger> ret = new List<BigInteger>();

		# if (isPrime(num) || num == 1)
		# {
			# ret.Add(num);
			# return ret;
		# }

		# foreach(BigInteger p in primes)
		# {
			# if(p <= (BigInteger)Math.Ceiling(
					 # Math.Exp(BigInteger.Log(num) / 2)
											# )
			  # )
			# {
				# while(num % p == 0)
				# {
					# // found a divisor, add it to the list
					# // and be sure to append all such divisors
					# ret.Add(p);
					# num /= p;
				# }

				# if (num == 1)
					# break;
			# }
		# }

		# // in the case that we didn't find all of the prime numbers that
		# // produce factors of the given number
		# if (num != 1)
			# ret.Add(num);

		# return ret;
	# }

	# public int getSize()
	# {
		# return primes.Count;
	# }

	# // computes that totient function of a number
	# // Assumes that the prime generator has all of the primes
	# // up to the square root of x!
	# public int totient(int x)
	# {
		# if (isPrime((BigInteger)x))
		# {
			# return x - 1;
		# }

		# // get the factors of x and make
		# // the list unique
		# List<BigInteger> factors = getFactors((BigInteger)x);
		# factors = factors.Distinct().ToList();

		# double multiplier = 1;
		# foreach (BigInteger f in factors)
		# {
			# multiplier *= (1 - (1 / (double)f));
		# }

		# return ((int)Math.Round(x * multiplier));
	# }

	# // computes that totient function of a number
	# // Assumes that the prime generator has all of the primes
	# // up to the square root of x!
	# public BigInteger totient(BigInteger x)
	# {
		# if (isPrime(x))
		# {
			# return x - 1;
		# }

		# // get the factors of x and make
		# // the list unique
		# List<BigInteger> factors = getFactors((BigInteger)x);
		# factors = factors.Distinct().ToList();

		# double multiplier = 1;
		# foreach (BigInteger f in factors)
		# {
			# multiplier *= (1 - (1 / (double)f));
		# }

		# return ((BigInteger)Math.Round((double)x * multiplier));
	# }

	# // determines whether two big integers are coprime
	# // not that this is pretty quick and dirty and there is
	# // probably a much better way to do this!
	# public bool isCoprime(BigInteger a, BigInteger b)
	# {
		# List<BigInteger> factorsA = this.getFactors(a);
		# List<BigInteger> factorsB = this.getFactors(b);
		# foreach(int factor in factorsA)
		# {
			# if (factorsB.Contains(factor))
				# return false;
		# }
		# return true;
	# }