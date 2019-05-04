def is_isbn_or_key(word):
    '''
    判断传输进来的参数类型
    :param word:
    :return:
    '''
    isbn_or_key = 'key'
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些 '-'
    #判断请求参数是否为13位数字
    if len(word)==13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-','')
    if '-' in word and len(short_word)==10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key