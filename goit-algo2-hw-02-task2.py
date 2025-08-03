from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal cutting strategy using memoization
    """
    # validation
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    if not prices or len(prices) != length:
        raise ValueError("Prices array must be non-empty and correspond to rod length")
    if any(p <= 0 for p in prices):
        raise ValueError("All prices must be greater than 0")

    from functools import lru_cache

    @lru_cache(None)
    def helper(n: int) -> (int, List[int]):
        if n == 0:
            return 0, []
        max_profit = -1
        best_cuts: List[int] = []
        for cut in range(1, n + 1):
            price_here = prices[cut - 1]
            remaining_profit, remaining_cuts = helper(n - cut)
            total_profit = price_here + remaining_profit
            candidate_cuts = [cut] + remaining_cuts
            # Choose better profit or lexicographically smaller cuts on tie
            if total_profit > max_profit or (total_profit == max_profit and candidate_cuts < best_cuts):
                max_profit = total_profit
                best_cuts = candidate_cuts
        return max_profit, best_cuts

    max_profit, cuts = helper(length)
    number_of_cuts = max(len(cuts) - 1, 0)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal cutting strategy using tabulation
    """
    # validation
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    if not prices or len(prices) != length:
        raise ValueError("Prices array must be non-empty and correspond to rod length")
    if any(p <= 0 for p in prices):
        raise ValueError("All prices must be greater than 0")

    # dp[i] = max profit for length i
    dp = [0] * (length + 1)
    first_cut = [0] * (length + 1)  # store first cut size to achieve dp[i]
    for i in range(1, length + 1):
        max_profit = -1
        best_cut = 1
        for cut in range(1, i + 1):
            profit = prices[cut - 1] + dp[i - cut]
            if profit > max_profit:
                max_profit = profit
                best_cut = cut
        dp[i] = max_profit
        first_cut[i] = best_cut

    # reconstruct cuts (bottom-up gives [1,2,2] for base case); reverse to match expected tabulation order
    cuts = []
    remaining = length
    while remaining > 0:
        c = first_cut[remaining]
        cuts.append(c)
        remaining -= c
    cuts = list(reversed(cuts))
    number_of_cuts = max(len(cuts) - 1, 0)
    return {
        "max_profit": dp[length],
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }


def run_tests():
    """Function to run all tests"""
    test_cases = [
        # Test 1: Base case
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Base case"
        },
        # Test 2: Optimal to not cut
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Optimal to not cut"
        },
        # Test 3: All cuts of length 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Even Cuts"
        }
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Rod Length: {test['length']}")
        print(f"Prices: {test['prices']}")

        # Testing memoization
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nMemoization Result:")
        print(f"Maximum Profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of Cuts: {memo_result['number_of_cuts']}")

        # Testing tabulation
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nTabulation Result:")
        print(f"Maximum Profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of Cuts: {table_result['number_of_cuts']}")

        # Basic verification
        assert memo_result["max_profit"] == table_result["max_profit"], "Profit mismatch between methods"
        # Optionally could compare cuts ignoring order for profit correctness
        print("\nTest passed successfully!")

if __name__ == "__main__":
    run_tests()

