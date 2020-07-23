def i_will_raise_exception(num):
    if num == 0:
        raise Exception("here is the exception for num %d" % num)
    else:
        return num+2
