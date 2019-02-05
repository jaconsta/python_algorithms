def pickingNumbers(a):
    count = {}
    # group
    for num in a:
        x = count.get(num, 0) + 1
        count[num] = x
    max_nums = 0
    for num in count:
        with_less = count[num] + count.get(num-1, 0)
        if with_less > max_nums:
            max_nums = with_less
    return max_nums

if __name__ == '__main__':
    a = [4, 6, 5, 3, 3, 1]
    result = pickingNumbers(a)
    print(result)



def climbingLeaderboard(scores, alice):
    alice_ranks = []
    greater_score = scores[0]
    rank = 1

    alice_scores = reversed(alice)
    al_score = alice_scores.__next__()
    try:
        for score in scores:
            ### score ( (0,100), (1, 80), (2, 24) )
            ### alice (101, 80, 10)
            if score < greater_score:
                rank += 1

            while al_score >= score:
                alice_ranks = [rank] + alice_ranks
                al_score = alice_scores.__next__()

            greater_score = score

    except StopIteration:
        pass

    rank += 1
    if al_score < greater_score:
        alice_ranks = [rank] + alice_ranks

    return alice_ranks + [rank for x in alice_scores]
