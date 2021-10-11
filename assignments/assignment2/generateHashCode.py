
id_counter = 0

def idToShortURL(domain):

    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = ""
    global id_counter
    id_counter = id_counter + 1
    id = id_counter

    # for each digit find the base 62
    while (id > 0):
        shortURL += map[id % 62]
        id //= 62

    # reversing the shortURL
    shortURL = shortURL[len(shortURL):: -1]
    return domain + "/" + shortURL


