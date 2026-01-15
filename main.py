# ============================================================
#  Prime Field Model — Publication Version (JIS-ready)
#  Full comparison with true primes up to N
# ============================================================

# ------------------------------------------------------------
#  Absorption: arithmetic coherence
# ------------------------------------------------------------
def absorption(n, P):
    for p in P:
        if n % p == 0:
            return 1
    return 0


# ------------------------------------------------------------
#  Organic observables: D (density), R (roughness), F (fractal pressure)
# ------------------------------------------------------------
def organic_observables(n, P):
    residues = [n % p for p in P]

    D = sum(1 for r in residues if r != 0)
    F = sum(1 for r in residues if r <= 1)

    R = 0
    for i in range(len(residues) - 1):
        if abs(residues[i+1] - residues[i]) <= 1:
            R += 1

    return D, R, F


# ------------------------------------------------------------
#  Organic threshold S_n
# ------------------------------------------------------------
def S_of_F(P, D, R, F):
    if len(P) < 3:
        return 2

    S = 2
    if D < len(P) // 3:
        S += 1
    if F == 0:
        S += 1
    if R < len(P) // 5:
        S += 1
    return S


# ------------------------------------------------------------
#  Amortissement (reset after event)
# ------------------------------------------------------------
def amortissement(P, D, R, F):
    T = 2
    if F > 1:
        T += 1
    if R < len(P) // 5:
        T += 1
    return T


# ------------------------------------------------------------
#  Tension update (no event)
# ------------------------------------------------------------
def tension_update(T, P, D, R, F):
    T += 1
    if D > len(P) // 2:
        T += 1
    if F > 1:
        T += 1
    if R < len(P) // 5:
        T -= 1
    return max(1, T)


# ------------------------------------------------------------
#  Main simulation
# ------------------------------------------------------------
def generate_events(N=200000):
    P = []
    T = 5
    events = []

    for n in range(2, N+1):
        absn = absorption(n, P)
        D, R, F = organic_observables(n, P)
        S = S_of_F(P, D, R, F)

        if absn == 0 and T >= S:
            P.append(n)
            events.append((n, T, S))
            T = amortissement(P, D, R, F)
        else:
            T = tension_update(T, P, D, R, F)

    return P, events


# ------------------------------------------------------------
#  True primes (simple sieve)
# ------------------------------------------------------------
def true_primes(N):
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False

    return [i for i in range(2, N+1) if sieve[i]]


# ------------------------------------------------------------
#  Full comparison
# ------------------------------------------------------------
def compare_lists(model_primes, true_primes):
    if len(model_primes) != len(true_primes):
        return False, f"Different lengths: model={len(model_primes)}, true={len(true_primes)}"

    for i, (a, b) in enumerate(zip(model_primes, true_primes)):
        if a != b:
            return False, f"Difference at index {i}: model={a}, true={b}"

    return True, "Perfect match: all primes identical."


# ------------------------------------------------------------
#  Execution
# ------------------------------------------------------------
if __name__ == "__main__":
    N = 200000

    print(f"Running model up to N = {N}...")
    model_P, data = generate_events(N)

    print("Generating true primes...")
    true_P = true_primes(N)

    print("Comparing...")
    ok, msg = compare_lists(model_P, true_P)

    print(msg)
    print("First 20 primes:", model_P[:20])
    print("Last 20 primes:", model_P[-20:])
