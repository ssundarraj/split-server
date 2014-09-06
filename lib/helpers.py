def flatten(rows):
    return [item for sublist in [d.values() for d in rows] for item in sublist]

def hasher(string_to_be_hashed):
    import md5
    return md5.md5(string_to_be_hashed).hexdigest()


if __name__=='__main__':
    a=[{'a':'1', 'b':'2'}, {'p':'9', 'q':'8'}, {'x':'4', 'y':'5'}]
    print flatten(a)
