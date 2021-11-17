%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:10:31
# we can make a list like this
my_list = [0, 1, 2]
print(my_list)# Wed, 17 Nov 2021 05:10:45
# we can also make an empty list and add items to it
another_list = []
print(another_list)

for item in my_list:
    another_list.append(item)

print(another_list)# Wed, 17 Nov 2021 05:10:46
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False
        
    return True

def get_primes(n_start, n_end):
    list_ = []
    for number in range(n_start, n_end):
        if is_prime(number):
            list_.append(mersenne_number(number))
    return list_
            
print(get_primes(3, 65))# Wed, 17 Nov 2021 05:10:59
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False
        
    return True

def get_primes(n_start, n_end):
    list_ = []
    for number in range(n_start, n_end):
        if is_prime(number):
            list_.append(mersenne_number(number))
    return list_
            
print(get_primes(3, 65))# Wed, 17 Nov 2021 05:11:14
def mersenne_number(p):
    return 2**p - 1# Wed, 17 Nov 2021 05:11:15
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False
        
    return True

def get_primes(n_start, n_end):
    list_ = []
    for number in range(n_start, n_end):
        if is_prime(number):
            list_.append(mersenne_number(number))
    return list_
            
print(get_primes(3, 65))# Wed, 17 Nov 2021 05:11:29
mersennes = get_primes(3, 65)
print(mersennes)# Wed, 17 Nov 2021 05:11:33
grader.score.ip__mersenne_numbers(mersennes)# Wed, 17 Nov 2021 05:11:34
%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()
# we can make a list like this
my_list = [0, 1, 2]
print(my_list)
# we can also make an empty list and add items to it
another_list = []
print(another_list)

for item in my_list:
    another_list.append(item)

print(another_list)
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False
        
    return True

def get_primes(n_start, n_end):
    list_ = []
    for number in range(n_start, n_end):
        if is_prime(number):
            list_.append(mersenne_number(number))
    return list_
            
print(get_primes(3, 65))
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False
        
    return True

def get_primes(n_start, n_end):
    list_ = []
    for number in range(n_start, n_end):
        if is_prime(number):
            list_.append(mersenne_number(number))
    return list_
            
print(get_primes(3, 65))
def mersenne_number(p):
    return 2**p - 1
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False
        
    return True

def get_primes(n_start, n_end):
    list_ = []
    for number in range(n_start, n_end):
        if is_prime(number):
            list_.append(mersenne_number(number))
    return list_
            
print(get_primes(3, 65))
mersennes = get_primes(3, 65)
print(mersennes)
grader.score.ip__mersenne_numbers(mersennes)
%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:11:47
def lucas_lehmer(p):
    s = 4
    l = [s]
    for i in range(1, p-1):
        s = (s*s - 2) % mersenne_number(p)
        l.append(s)
    return l# Wed, 17 Nov 2021 05:11:53
lucas_lehmer(11)# Wed, 17 Nov 2021 05:12:05
ll_result = [4] * 16

grader.score.ip__lucas_lehmer(ll_result)# Wed, 17 Nov 2021 05:12:09
ll_result = [4] * 16

lucas_lehmer(11)

grader.score.ip__lucas_lehmer(ll_result)# Wed, 17 Nov 2021 05:12:27
lucas_lehmer(11)# Wed, 17 Nov 2021 05:12:29
ll_result = [4] * 16

grader.score.ip__lucas_lehmer(ll_result)# Wed, 17 Nov 2021 05:12:47
list_exp = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
def ll_prime(nbr):
    list_true_false = []
    for i in nbr:
        if lucas_lehmer(i)[i-2] == 0:
            list_true_false.append(1)
        else:
            list_true_false.append(0)
    return list_true_false

ll_prime(list_exp)  

result = list(zip(list_exp, ll_prime(list_exp)))
print(result)# Wed, 17 Nov 2021 05:12:56
mersenne_primes = list(zip(list_exp, ll_prime(list_exp)))

grader.score.ip__mersenne_primes(mersenne_primes)# Wed, 17 Nov 2021 05:13:25
def get_primes_fast(n):
    list_ = []
    for number in range(2, n+1):
        if is_prime_fast(number):
            list_.append(number)
    return list_# Wed, 17 Nov 2021 05:13:27
%%timeit
is_prime_fast(67867967)# Wed, 17 Nov 2021 05:13:30
import math
def is_prime_fast(number):
    if (number > 2 and (number % 2 == 0)) or number <=1:
        return False
    n = math.sqrt(number)
    for factor in range(3, int(n) + 1, 2):
        if number % factor == 0:
            return False
    return True# Wed, 17 Nov 2021 05:13:32
for n in range(1515):
    assert is_prime(n) == is_prime_fast(n)# Wed, 17 Nov 2021 05:13:33
%%timeit
is_prime(67867967)# Wed, 17 Nov 2021 05:14:12
%%timeit
is_prime(67867967)# Wed, 17 Nov 2021 05:14:49
%%timeit
is_prime_fast(67867967)# Wed, 17 Nov 2021 05:14:51
def get_primes_fast(n):
    list_ = []
    for number in range(2, n+1):
        if is_prime_fast(number):
            list_.append(number)
    return list_# Wed, 17 Nov 2021 05:14:51
assert get_primes_fast(65) == get_primes(3,65)# Wed, 17 Nov 2021 05:14:53
get_primes(3, 65)# Wed, 17 Nov 2021 05:15:00
get_primes_fast(65)# Wed, 17 Nov 2021 05:15:19
%%timeit
get_primes_fast(65)# Wed, 17 Nov 2021 05:15:27
%%timeit
get_primes(3, 65)# Wed, 17 Nov 2021 05:15:33
grader.score.ip__is_prime_fast(get_primes_fast)# Wed, 17 Nov 2021 05:15:42
ll_result = [4] * 16

grader.score.ip__lucas_lehmer(ll_result)# Wed, 17 Nov 2021 05:16:02
def list_true(n):
    list_ = [False, False]
    for i in range(n-1):
        list_.append(True) 
    return list_# Wed, 17 Nov 2021 05:16:06
print(list_true(20))# Wed, 17 Nov 2021 05:16:09
assert len(list_true(20)) == 21
assert list_true(20)[0] is False
assert list_true(20)[1] is False# Wed, 17 Nov 2021 05:16:27
list_true(6)# Wed, 17 Nov 2021 05:16:36
def mark_false(bool_list, p):
    n = len(bool_list)
    i = 2
    while i*p < n:
        bool_list[i*p] = False
        i = i + 1
    return bool_list# Wed, 17 Nov 2021 05:16:48
mark_false(list_true(6), 3)# Wed, 17 Nov 2021 05:16:58
assert mark_false(list_true(7), 2) == [False, False, True, True, False, True, False, True]# Wed, 17 Nov 2021 05:17:05
def find_next(bool_list, p):
    for n in range(len(bool_list)):
        if (n>p and bool_list[n] == True):
            return n
    return None# Wed, 17 Nov 2021 05:17:12
assert find_next([True, True, True, True], 2) == 3
assert find_next([True, True, True, False], 2) is None# Wed, 17 Nov 2021 05:17:16
def prime_from_list(bool_list):
    l = []
    for n in range(len(bool_list)):
        if bool_list[n] == True:
            l.append(n)
    return l# Wed, 17 Nov 2021 05:17:22
assert prime_from_list([False, False, True, True, False]) ==  [2, 3]# Wed, 17 Nov 2021 05:17:30
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)# Wed, 17 Nov 2021 05:17:41
%%timeit 
sieve(1000)# Wed, 17 Nov 2021 05:17:45
%%timeit 
get_primes(0, 1000)# Wed, 17 Nov 2021 05:17:50
grader.score.ip__eratosthenes(sieve)%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:41:39
def lucas_lehmer(p):
    ll_seq = [4]
    if p>2:
        for i in range(1, (p-2)+1):
            n_i = ((ll_seq[i-1]) ** 2 - 2) % ((2 ** p) - 1)
            ll_seq.append(n_i)
    return ll_seq# Wed, 17 Nov 2021 05:41:49
ll_result = lucas_lehmer(17)# Wed, 17 Nov 2021 05:41:53


grader.score.ip__lucas_lehmer(ll_result)%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()
