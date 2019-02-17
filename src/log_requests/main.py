"""
Expected output:

records_hosts_access_log_00.txt

burger.letters.com 3
d104.aa.net 3
unicomp6.unicomp.net 4
"""

# def main():
#     file_name = 'hosts_access_log_00.txt' # input()
#     output_file_name = 'records_{file_name}'.format(file_name=file_name)
#     log_counter = {}
#     with open(file_name) as logs_file:
#         for log_line in logs_file:
#             site_name = log_line.split(' ')[0]
#             log_counter[site_name] = log_counter.get(site_name, 0) + 1
#
#     with open(output_file_name,”w”) as log_output:
#         for site, count in log_counter.iteritems():
#             log_output.write('{0} {1}\n'.format(site, count))


# population age
# import operator
# def highestPopulation(citizens):
#     # Write your code here
#     population = {}
#     for born, death in citizens:
#         for year in range(born, death):
#             population[year] = population.get(year, 0) + 1
#
#     print(max(population.items(), key=operator.itemgetter(1))[0])

# digit sum
def sum_number_digits (num):
    return sum([int(a) for a in str(num)])

def digit_sum(a, b):
    sums_of_digits = (sumOfDigits(num) for num in range(a, b+1))
    repeats = {}
    times_get_repeated = 0
    ways_to_choose_n = 0
    for digit in sums_of_digits:
        repeat = repeats.get(digit, 0) + 1
        if repeat == times_get_repeated:
            ways_to_choose_n += 1
        if repeat > times_get_repeated:
            times_get_repeated = repeat
            ways_to_choose_n = 1

        repeats[digit] = repeat
    return ways_to_choose_n, times_get_repeated

### xxx

if __name__ == '__main__':
    # main()
    # highestPopulation([
    #     [1830, 1842],
    #     [1810, 1845],
    #     [1805, 1835],
    #     [1844, 1885]])

    print(digit_sum(1,5))
    print(digit_sum(2,5))
    print(digit_sum(1,10))
    print(digit_sum(3,12))
    print(digit_sum(20,30))
    print(digit_sum(7,20))
    print(digit_sum(1,1000))
    print(digit_sum(1,10**18))
