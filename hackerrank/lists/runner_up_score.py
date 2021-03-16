# problem:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def runner_up(scores):
    scores.sort(reverse=True)
    max = arr[0]

    for score in scores:
        if score < max:
            return score    

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    print(runner_up(arr))
