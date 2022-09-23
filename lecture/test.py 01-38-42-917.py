def time_calculator(sum_times, new_times):
    def calculator(longer_times, shorter_times, end, idx):
        carry = 0
        for i in range(end, -1, -1):
            if i or not idx:
                new_sum_time = int(longer_times[i]) + int(shorter_times[i+idx]) + carry
                if new_sum_time >= 60:
                    carry = 1
                    new_sum_time-=60
            else:
                new_sum_time = int(longer_times[i]) + carry
            longer_times[i] = new_sum_time
        return longer_times

    len_sum_times = len(sum_times)
    len_new_times = len(new_times)
    if len_sum_times == len_new_times:
        return calculator(sum_times, new_times, len_new_times, 0)
    elif len_sum_times > len_new_times:
        return calculator(sum_times, new_times, len_new_times, -1)
    else:
        return calculator(new_times, sum_times, len_sum_times, -1)


if __name__ == "__main__":
    sum_times_var = [20]
    new_time = '50'
    new_times_var = new_time.split(':')
    new_sum_times = time_calculator(sum_times_var, new_times_var)
    print(new_sum_times)
