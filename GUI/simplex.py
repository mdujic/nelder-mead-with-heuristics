

import numpy as np
import math



lowerBound, upperBound = -30, 30
x = np.random.uniform(low=lowerBound, high=upperBound, size=(10,))
N = len(x)




l = [lowerBound for i in range(10)]
u = [upperBound for i in range(10)]



def _e(index, size):
    arr = np.zeros(size)
    arr[index] = 1.0
    return arr

def Delta(x):
    Sum = 0
# no general, only box constraints
    for i in range(0, N):
        Sum = Sum + max(x[i] - u[i], 0) + max(l[i] - x[i], 0)
    return Sum

def better(f, x, y):
    Dx = Delta(x)
    Dy = Delta(y)
    if (Dx < Dy):
        return True
    elif (Dx == Dy and f(x) < f(y)):
        return True
    else:
        return False

def findExtremes(f, s):
    Ds = np.empty([N + 1])
    fs = np.empty([N + 1])

    for i in range(0, N + 1):
        Ds[i] = Delta(s[i])
        fs[i] = f(s[i])

    arg_b = np.argmin(Ds)
    for i in range(0, N + 1):
        if Ds[i] == Ds[arg_b] and i != arg_b:
            if (fs[i] < fs[arg_b]):
                arg_b = i;

    arg_w = np.argmax(Ds)
    for i in range(0, N + 1):
        if Ds[i] == Ds[arg_w] and i != arg_w:
            if (fs[i] > fs[arg_w]):
                arg_w = i;

    # mask the worst to find the second worst
    Ds[arg_w] = 0

    arg_sw = np.argmax(Ds)
    for i in range(0, N + 1):
        if Ds[i] == Ds[arg_sw] and i != arg_w:
            if (fs[i] > fs[arg_sw]):
                arg_sw = i;

    return arg_b, arg_w, arg_sw

def centroid(s, argWorst):
    return np.mean(np.delete(s, argWorst), axis=0)

def SimplexLocalSearchForDirectional(f, option, x, Epsilon, Lambda, M, Alpha=1, Gamma=2, Beta=-0.5):
    N = len(x)
    s = np.empty([N + 1, N])
    s[0] = x
    for j in range(1, N + 1):
        s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * _e(j - 1, N);
    k = 0

    argBest, argWorst, argSecondWorst = findExtremes(f, s)
    sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
    # set_trace()
    while abs(f(sBest) - f(sWorst)) > Epsilon and k < M and k < 1000:
        # set_trace()
        # if(k%1000 == 0):print(f(sBest),'\n')
        r = (1 + Alpha) * centroid(s, argWorst) - Alpha * sWorst
        if (better(f, sBest, r) and better(f, r, sSecondWorst)):
            s[argWorst] = r
        elif (better(f, r, sBest)):
            e = (1 + Gamma) * centroid(s, argWorst) - Gamma * sWorst
            if (better(f, e, r)):
                s[argWorst] = e
            else:
                s[argWorst] = r
        else:
            c = (1 + Beta) * centroid(s, argWorst) - Beta * sWorst
            if (better(f, c, sWorst)):
                s[argWorst] = c
            else:
                if (option == 1):
                    print(f(sBest))
                    return sBest, k, s, argBest, argWorst, argSecondWorst
                for j in range(0, N + 1):
                    s[j] = (s[j] + sBest) / 2

        # set_trace()
        argBest, argWorst, argSecondWorst = findExtremes(f, s)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        k = k + 1
    # print(f(sBest))
    return sBest, k, s, argBest, argWorst, argSecondWorst

import copy
def DirectionalEscape(f, Epsilon, EpsilonApostrophe, Lambda, M, Gamma=1.25, Beta=-0.5):
    k = 0
    it = 0
    x = np.random.uniform(low=lowerBound, high=upperBound, size=(10,))
    while (k < M):
        # set_trace()
        temp, _k, s, argBest, argWorst, argSecondWorst = SimplexLocalSearchForDirectional(f, 1, x, Epsilon, Lambda, M - k)
        x = copy.copy(temp)

        k = k + _k
        try:
            xBest
        except NameError:
            xBest = None

        if xBest is None or f(x) < f(xBest):
            temp, _k, s, argBest, argWorst, argSecondWorst = SimplexLocalSearchForDirectional(f, 2, x, EpsilonApostrophe, Lambda,
                                                                                    M - k)
            xBest = np.zeros(N)
            xBest = xBest + temp
            k = k + _k
            print("***NEW BEST VALUE*** iteration: ", k, "| best found value: ", f(xBest))

        if xBest is not None and k // 1000 > it:
            it = k // 1000
            print("iteration:", it * 1000, "| best found value: ", f(xBest))

                # if f(xBest) < 1:
                #    for i in range(0,N):
                #        s[i][i] = s[i][i] + 10e-2*f(xBest)
                # else:
                # for i in range(0,N):
                #    s[i][i] = s[i][i] + 10e-15

        argBest, argWorst, argSecondWorst = findExtremes(f, s)

        xWorst = None

        while xWorst is None or better(f, x, xWorst):
            xWorst = copy.copy(x)
            x = Gamma * s[argBest] + (1 - Gamma) * centroid(s, argBest)
            # if Delta(x)==0: print("+", k)
            s[argBest] = copy.copy(x)
            argBest, argWorst, argSecondWorst = findExtremes(f, s)

    return xBest


def SimplexLocalSearchForNonTabu(f, x, Epsilon, Lambda, M, Alpha=1, Gamma=2, Beta=-0.5):
    N = len(x)
    s = np.empty([N + 1, N])
    s[0] = x
    for j in range(1, N + 1):
        s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * _e(j - 1, N);
    k = 0

    argBest, argWorst, argSecondWorst = findExtremes(f, s)
    sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
    # set_trace()
    while abs(f(sBest) - f(sWorst)) > Epsilon and k < M and k < 1000:
        # set_trace()
        # if(k%1000 == 0):print(f(sBest),'\n')
        r = (1 + Alpha) * centroid(s, argWorst) - Alpha * sWorst
        if (better(f, sBest, r) and better(f, r, sSecondWorst)):
            s[argWorst] = r
        elif (better(f, r, sBest)):
            e = (1 + Gamma) * centroid(s, argWorst) - Gamma * sWorst
            if (better(f, e, r)):
                s[argWorst] = e
            else:
                s[argWorst] = r
        else:
            c = (1 + Beta) * centroid(s, argWorst) - Beta * sWorst
            if (better(f, c, sWorst)):
                s[argWorst] = c
            else:
                for j in range(0, N + 1):
                    s[j] = (s[j] + sBest) / 2

        # set_trace()
        argBest, argWorst, argSecondWorst = findExtremes(f, s)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        k = k + 1
    # print(f(sBest))
    return sBest, k


def NonTabuSearch(f, Epsilon, EpsilonApostrophe, Lambda, M, Gamma=2, Beta=-0.5, R=2, Sigma=1):
    k = 0
    it = 0
    x = np.random.uniform(low=lowerBound, high=upperBound, size=(10,))
    x, _k = SimplexLocalSearchForNonTabu(f, x, Epsilon, Lambda, M - k)
    k = k + _k
    xBest = np.zeros(10)
    xBest = xBest + x
    y = np.zeros(10)
    y = y + x
    running_first_time = True
    while (k < M):
        # set_trace()
        for i in range(1, R):
            x[i] = y[i] + Sigma * (u[i] - l[i])
            x, _k = SimplexLocalSearchForNonTabu(f, x, Epsilon, Lambda, M - k)
            k = k + _k
            if f(x) < f(xBest):
                print("***NEW BEST VALUE*** iteration: ", k, "| best found value: ", f(x))
                xBest, _k = SimplexLocalSearchForNonTabu(f, x, EpsilonApostrophe, Lambda, M - k)
                k = k + _k
            if running_first_time or f(x) < f(xWorst):
                running_first_time = False
                xWorst = np.zeros(10)
                xWorst = xWorst + x
        y = np.zeros(10)
        y = y + xWorst
        if (k // 1000 > it):
            it = k // 1000
            print("iteration:", it * 1000, "| best found value: ", f(xBest))

    return xBest


def SimplexLocalSearchForSimulatedAnnealing(f, x, Epsilon, Lambda, Alpha=1, Gamma=2, Beta=-0.5):
    N = len(x)
    s = np.empty([N + 1, N])
    s[0] = x
    for j in range(1, N + 1):
        s[j] = x + Lambda * (u[j - 1] - l[j - 1]) * _e(j - 1, N);
    k = 0

    argBest, argWorst, argSecondWorst = findExtremes(f, s)
    sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
    # set_trace()
    while abs(f(sBest) - f(sWorst)) > Epsilon and k < 1000:
        # set_trace()
        # if(k%1000 == 0):print(f(sBest),'\n')
        r = (1 + Alpha) * centroid(s, argWorst) - Alpha * sWorst
        if (better(f, sBest, r) and better(f, r, sSecondWorst)):
            s[argWorst] = r
        elif (better(f, r, sBest)):
            e = (1 + Gamma) * centroid(s, argWorst) - Gamma * sWorst
            if (better(f, e, r)):
                s[argWorst] = e
            else:
                s[argWorst] = r
        else:
            c = (1 + Beta) * centroid(s, argWorst) - Beta * sWorst
            if (better(f, c, sWorst)):
                s[argWorst] = c
            else:
                for j in range(0, N + 1):
                    s[j] = (s[j] + sBest) / 2

        # set_trace()
        argBest, argWorst, argSecondWorst = findExtremes(f, s)
        sBest, sWorst, sSecondWorst = s[argBest], s[argWorst], s[argSecondWorst]
        k = k + 1
    # print(f(sBest))
    return sBest

from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed


def SimulatedAnnealing(f, n_iterations, Epsilon, Lambda, Temperature):
    # generate an initial point
    best = np.random.uniform(low=lowerBound, high=upperBound, size=(10,))
    # evaluate the initial point
    best_eval = f(best)
    # current working solution
    curr, curr_eval = best, best_eval
    scores = list()
    # run the algorithm
    for i in range(n_iterations):
        # take a step
        candidate = SimplexLocalSearchForSimulatedAnnealing(f, best,Epsilon,Lambda)
        #set_trace()
        # evaluate candidate point
        candidate_eval = f(candidate)
        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            best, best_eval = candidate, candidate_eval
            # keep track of scores
            scores.append(best_eval)
            # report progress
            print('>%d f(%s) = %f' % (i, best, best_eval))
        # difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # calculate temperature for current epoch
        t = Temperature / float(i + 1)
        # calculate metropolis acceptance criterion
        metropolis = exp(-diff / t)
        # check if we should keep the new point
        if diff < 0 or rand() < metropolis:
            # store the new current point
            curr, curr_eval = candidate, candidate_eval
    return [best, best_eval, scores]



