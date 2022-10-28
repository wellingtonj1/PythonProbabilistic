import operator as op
from functools import reduce
import math
import matplotlib.pyplot as plt


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

# calculate the binomial distribution
def binomial_distribution(n, p, k):
    # n = numero de tentativas, p = probabilidade de sucesso, k = numero de sucessos
    return ncr(n, k) * (p ** k) * ((1 - p) ** (n - k))

# calculate the union of two events
def union_of_events(event1, event2, is_independent_events=False):
    if is_independent_events:
        return event1 + event2
    return event1 + event2 - intersection_of_events(event1, event2)

# calculate intersection of events
def intersection_of_events(event1, event2):
    return event1 * event2

# calculate the conditional probability of A given B
def conditional_probability(event_a, event_b):
    return intersection_of_events(event_a, event_b) / event_b

# calculate bayes theorem
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    p_not_a = 1 - p_a
    p_a_given_b = conditional_probability(p_b_given_a * p_a, p_b_given_a * p_a + p_b_given_not_a * p_not_a)
    return p_a_given_b

# calculates the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

# calculate poison distribution
def poison_distribution(lamb, x):
    # lamb = lambda, x = numero de sucessos
    return ((lamb ** x) * (math.e ** (-lamb))) / factorial(x)

# calculate the bernoulli distribution
def bernoulli_distribution(p, k):
    # p = probabilidade de sucesso, k = numero de sucessos
    return (p ** k) * ((1 - p) ** (1 - k))

# # calculate the aproach of the Poisson distribution to the binomial distribution
# def poisson_distribution_approach_to_binomial_distribution():
#     print("Calculate the aproach of the Poisson distribution to the binomial distribution\n\n")
#     n = int(input("Enter the number of trials: "))
#     p = float(input("Enter the probability of success: "))
#     k = int(input("Enter the number of successes: "))
#     lamb = n * p
#     print("Poisson distribution: " + str(poison_distribution(lamb, k)))
#     print("Binomial distribution: " + str(binomial_distribution(n, p, k)))

# calculate the matemati
# nHoras = [200, 152, 60, 30, 13, 9, 7, 5, 4]
# cal hope 
def matematical_hope(n, p):
    # n = numero de tentativas, p = probabilidade de sucesso
    return n * p

# calculate the standard deviation
def standard_deviation(n, p):
    # n = numero de tentativas, p = probabilidade de sucesso
    return math.sqrt(matematical_hope(n, p) * (1 - p))

def calculate_integral(x, f):
    # x = array of values of the random variable, f = array of values of the probability density function
    return sum([f[i] * (x[i + 1] - x[i]) for i in range(len(x) - 1)])

def matematical_hope_continuous_random_variable(x, f):
    # x = valores da variavel aleatoria, f = funcao de densidade de probabilidade
    return calculate_integral(x, f)
    
def main():
    
    print("Welcome Wellington!\n\n")
    
    # print the integral of the function f(x) = 2x + x between 0 and 1
    print("The integral of the function f(x) = 2x + x between 0 and 1 is: " + str(calculate_integral([0, 1], [2, 3])) + "\n\n")
    
    
    
    
    
    # # 4000 is the medicines are produced in a factory
    # # 0,00001 is the probability of a medicine being defective
    # # using poison distribution, calculate the probability of at most 1 drug leave without the active ingredient
    # print("Using poison distribution, calculate the probability of at most 0 drug leave without the active ingredient: " + str(poison_distribution(4000 * 0.00001, 0)))
    # print("Using poison distribution, calculate the probability of at least 1 drug leave without the active ingredient: " + str(1 - poison_distribution(4000 * 0.00001, 0)))
    # print(poison_distribution(4000 * 0.00001, 0) + poison_distribution(4000 * 0.00001, 1))
    
    # print("Using binomial distribution, calculate the probability of at most 0 drug leave without the active ingredient: " + str(binomial_distribution(4000, 0.00001, 0)))
    # print("Using binomial distribution, calculate the probability of at least 1 drug leave without the active ingredient: " + str(1 - binomial_distribution(4000, 0.00001, 0)))
    # print((200+152+60+30+13+9+7+5+4) / 24)
    
    # nHoras = [200, 152, 60, 30, 13, 9, 7, 5, 4]
    
    # eX = matematical_hope(0, 200) + matematical_hope(1, 152) + matematical_hope(2, 60) + matematical_hope(3, 30) + matematical_hope(4, 13) + matematical_hope(5, 9) + matematical_hope(6, 7) + matematical_hope(7, 5) + matematical_hope(8, 4)
    # eX = eX / 480
    
    # # using poison distribution
    # print("p(0) = " + str(poison_distribution(eX, 0)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 0)*480))
    # print("p(2) = " + str(poison_distribution(eX, 2)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 2)*480))
    # print("p(1) = " + str(poison_distribution(eX, 1)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 1)*480))
    # print("p(4) = " + str(poison_distribution(eX, 4)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 4)*480))
    # print("p(3) = " + str(poison_distribution(eX, 3)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 3)*480))
    # print("p(6) = " + str(poison_distribution(eX, 6)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 6)*480))
    # print("p(5) = " + str(poison_distribution(eX, 5)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 5)*480))
    # print("p(8) = " + str(poison_distribution(eX, 8)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 8)*480))
    # print("p(7) = " + str(poison_distribution(eX, 7)) + "   x:P(lambda=1,18) = " + str(poison_distribution(eX, 7)*480))

if __name__ == "__main__":
    main()
    
    
# bernoulli 
# binomial
# poison
# hipergeometric
# geometric
# pascal
# multinomial

# # general case
# uniform -> importante para geração de numeros aleatorios 
# experimental
# normal

