'''
두 문자열을 파라메터로 받아서 공통된 문자열 중 가장 긴 문자열을 반환하는 함수를 작성한다.

예를 들면 "penpineapple" 와 "applepen" 두 문자열이 주어졌을때,
"apple", "pen" 등이 공통된 문자열로 추출이 될 수 있다.
이 중 최대의 길이를 갖는 문자열은 "apple"이 된다. 이러한 문자열을 반환하는 함수를 작성하시요.
'''

'''
def solution(word1, word2):
    max = 0
    index = 0

    text = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                text[i+1][j+1] = text[i][j]+1
            if max < text[i+1][j+1]:
                max = text[i+1][j+1]
                index = i+1

    answer = word1[index-max:index]
    return answer


print(solution('penpineapple','applepen'))
'''

'''
int 형 숫자를 하나 입력받아 1인 비트 개수를 세는 매서드를 작성하세요.
단 Integer.toBinaryString 또는 Interger.toString 함수를 사용하지 않고 구현합니다.

Ex) 입력 7 -> 0111 
결과 : 3
'''


def solution(number):
    number_arr = []
    decimal_num = number

    while decimal_num:
        get_num = decimal_num % 2
        if get_num == 1:
            number_arr.append(get_num)

        decimal_num //= 2

    answer = len(number_arr)
    return answer

print(solution(7))
