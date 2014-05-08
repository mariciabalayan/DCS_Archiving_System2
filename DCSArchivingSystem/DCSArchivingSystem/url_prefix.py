def getUrlPrefix(path):
    apacheConf = open(path, 'r')
    for line in apacheConf:
        if line.startswith('WSGIScriptAlias'):
            lineParts = line.split(' ', 2)
            apacheConf.close()
            return lineParts[1]
