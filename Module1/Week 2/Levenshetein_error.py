def levenshtein_distance(word1, word2):
    # Matrix
    m = len(word1)
    n = len(word2)
    mat = [[0 for j in range(n+1)] for i in range(m+1)]

    # First row and first line
    for i in range(m + 1):
        mat[i][0] = i
    for j in range(n + 1):
        mat[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1]
            else:
                mat[i][j] = min(mat[i - 1][j - 1], mat[i - 1][j], mat[i][j - 1]) + 1

    return mat[m][n]
