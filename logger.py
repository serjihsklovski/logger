import time


def logger(file_name):
    def f(*args, **kwargs):
        file = open(file_name, 'a')
        t = time.localtime(time.time())
        d = dict(
            day=t.tm_mday,
            month=t.tm_mon,
            year=t.tm_year,
            hour=t.tm_hour,
            minute=t.tm_min,
            second=t.tm_sec
        )

        for k in d:
            d[k] = str(d[k])

            if len(d[k]) == 1:
                d[k] = '0' + d[k]

        print('{year}.{month}.{day}|{hour}:{minute}:{second} -'.format_map(d), *args, **kwargs, file=file)

        file.close()

    return f


if __name__ == '__main__':
    file_name = input('input file name: ')
    log = logger(file_name)

    while True:
        msg = input('> ')

        if msg == '<%quit>':
            break

        log(msg)
