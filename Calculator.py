example = input('>>> ')
ex_list = []

signs = []
staples_list = []

for i in range(len(example)):
    if example[i] == '*' or example[i] == '/' or example[i] == '-' or example[i] == '+' or example[i] == '^': 
        signs.append(i)
    if example[i] == '(' or example[i] == ')':
        staples_list.append(i)

if len(signs) == 1:
    ex_list.append(example[:signs[0]])
    ex_list.append(example[signs[0]])
    ex_list.append(example[signs[0]+1:])

elif len(signs) == 0:
    ex_list.append(example)

else:

    for i in range(len(example) - len(signs)):
        if i == 0:
            ex_list.append(example[:signs[i]])
            ex_list.append(example[signs[i]])
        else:
            if i != len(signs) - 1:
                ex_list.append(example[signs[i-1] + 1:signs[i]])
                ex_list.append(example[signs[i]])
            else:
                break
    ex_list.append(example[signs[len(signs) - 2] + 1:signs[len(signs) - 1]])
    ex_list.append(example[signs[len(signs)-1]])
    ex_list.append(example[signs[len(signs)-1]+1:])

    for i in range(len(ex_list) + len(staples_list)):
 
        if '(' in ex_list[i]:
            count = ex_list[i]
            ex_list[i] = count[1:]
            ex_list.insert(i, '(')

        if ')' in ex_list[i]:
            if ex_list[i] != ')':
                count = ex_list[i]
                ex_list[i] = count[:len(count)-1]
                ex_list.insert(i+1, ')')

if '(' and ')' in ex_list:
    staples_indeces = []
    for i in range(len(ex_list)):
        if ex_list[i] == '(' or ex_list[i] == ')':
            staples_indeces.append(i)

    n = int(len(staples_indeces) / 2)

    for j in range(n):
        staples_in_list = []
        m = int(min(staples_indeces))
        for j1 in range(int(staples_indeces[1]) - int(staples_indeces[0]) - 1):
            staples_in_list.append(ex_list[m + 1])
            m += 1

        if '^' in staples_in_list:
            deg_indeces = []
            for i in range(len(staples_in_list)):        
                if staples_in_list[i] == '^':
                    deg_indeces.append(i)

            deg_ans_list = []
            deg_re_list = []
            flag_deg = 0

            for i in range(len(deg_indeces)):

                if i == 0:
                    ans_deg = float(staples_in_list[deg_indeces[i] - 1]) ** float(staples_in_list[deg_indeces[i] + 1])
                    deg_ans_list.append(ans_deg)
                    flag_deg += 1
                    flag_deg1 = 0

                    if len(deg_indeces) == 1:
                        flag_deg1 = 1
                        deg_re_list.append(flag_deg1)

                elif i != 0 and int(deg_indeces[i]) - int(deg_indeces[i - 1]) == 2:
                    ans_deg **= float(staples_in_list[deg_indeces[i] + 1])
                    deg_ans_list.pop()
                    deg_ans_list.append(ans_deg)
                    flag_deg1 += 1

                elif i != 0 and not(int(deg_indeces[i]) - int(deg_indeces[i - 1]) == 2):
                    ans_deg = float(staples_in_list[deg_indeces[i] - 1]) ** float(staples_in_list[deg_indeces[i] + 1])
                    deg_ans_list.append(ans_deg)
                    flag_deg += 1
    
                    flag_deg1 += 1
                    deg_re_list.append(flag_deg1)
                    flag_deg1 = 0

            if not(len(deg_indeces) == 1):

                flag_deg1 += 1
                deg_re_list.append(flag_deg1)
                flag_deg1 = 0

            for j in range(flag_deg):

                for j1 in range(int(deg_re_list[j]) * 2 + 1):
                    staples_in_list.pop(int(deg_indeces[0]) - 1) 
                staples_in_list.insert(int(deg_indeces[0]) - 1, float(deg_ans_list[j]))

                if '^' in staples_in_list:
                    deg_indeces = []
                    for i in range(len(staples_in_list)):
                        if staples_in_list[i] == '^':
                            deg_indeces.append(i)

        if '/' in staples_in_list:
            del_indeces = []
            for i in range(len(staples_in_list)):   
                if staples_in_list[i] == '/':
                    del_indeces.append(i)

            for i in range(len(del_indeces)):
                (staples_in_list[int(del_indeces[i]) + 1]) = 1 / float(staples_in_list[int(del_indeces[i]) + 1])

            for i in range(len(del_indeces)):
                staples_in_list[int(del_indeces[i])] = '*'
        
        if '*' in staples_in_list:
            mnoj_indeces = []
            for i in range(len(staples_in_list)):    
                if staples_in_list[i] == '*':
                    mnoj_indeces.append(i)

            mnoj_ans_list = []
            mnoj_re_list = []
            flag_mnoj = 0

            for i in range(len(mnoj_indeces)):

                if i == 0:
                    ans_mnoj = float(staples_in_list[mnoj_indeces[i] - 1]) * float(staples_in_list[mnoj_indeces[i] + 1])
                    mnoj_ans_list.append(ans_mnoj)
                    flag_mnoj += 1
                    flag_mnoj1 = 0

                    if len(mnoj_indeces) == 1:
                        flag_mnoj1 = 1
                        mnoj_re_list.append(flag_mnoj1)

                elif i != 0 and int(mnoj_indeces[i]) - int(mnoj_indeces[i - 1]) == 2:
                    ans_mnoj *= float(staples_in_list[mnoj_indeces[i] + 1])
                    mnoj_ans_list.pop()
                    mnoj_ans_list.append(ans_mnoj)
                    flag_mnoj1 += 1

                elif i != 0 and not(int(mnoj_indeces[i]) - int(mnoj_indeces[i - 1]) == 2):
                    ans_mnoj = float(staples_in_list[mnoj_indeces[i] - 1]) * float(staples_in_list[mnoj_indeces[i] + 1])
                    mnoj_ans_list.append(ans_mnoj)
                    flag_mnoj += 1
  
                    flag_mnoj1 += 1
                    mnoj_re_list.append(flag_mnoj1)
                    flag_mnoj1 = 0

            if not(len(mnoj_indeces) == 1):

                flag_mnoj1 += 1
                mnoj_re_list.append(flag_mnoj1)
                flag_mnoj1 = 0

            for j in range(flag_mnoj):

                for j1 in range(int(mnoj_re_list[j]) * 2 + 1):
                    staples_in_list.pop(int(mnoj_indeces[0]) - 1) 
                staples_in_list.insert(int(mnoj_indeces[0]) - 1, float(mnoj_ans_list[j]))

                if '*' in staples_in_list:
                    mnoj_indeces = []
                    for i in range(len(staples_in_liststaples_in_list)):
                        if staples_in_liststaples_in_list[i] == '*':
                            mnoj_indeces.append(i)

        if '-' in staples_in_list:
            minus_indeces = []
            for i in range(len(staples_in_list)):   
                if staples_in_list[i] == '-':
                    minus_indeces.append(i)

            minus_ans_list = []
            minus_re_list = []
            flag_minus = 0

            for i in range(len(minus_indeces)):
                if i == 0:
                    ans_minus = float(staples_in_list[minus_indeces[i] - 1]) - float(staples_in_list[minus_indeces[i] + 1])
                    minus_ans_list.append(ans_minus)
                    flag_minus += 1
                    flag_minus1 = 0

                    if len(minus_indeces) == 1:
                        flag_minus1 = 1
                        minus_re_list.append(flag_minus1)

                elif i != 0 and int(minus_indeces[i]) - int(minus_indeces[i - 1]) == 2:
                    ans_minus -= float(staples_in_list[minus_indeces[i] + 1])
                    minus_ans_list.pop()
                    minus_ans_list.append(ans_minus)
                    flag_minus1 += 1

                elif i != 0 and not(int(minus_indeces[i]) - int(minus_indeces[i - 1]) == 2):
                    ans_minus = float(staples_in_list[minus_indeces[i] - 1]) - float(staples_in_list[minus_indeces[i] + 1])
                    minus_ans_list.append(ans_minus)
                    flag_minus += 1
   
                    flag_minus1 += 1
                    minus_re_list.append(flag_minus1)
                    flag_minus1 = 0

            if not(len(minus_indeces) == 1):

                flag_minus1 += 1
                minus_re_list.append(flag_minus1)
                flag_minus1 = 0

            for j in range(flag_minus):
 
                for j1 in range(int(minus_re_list[j]) * 2 + 1):
                    staples_in_list.pop(int(minus_indeces[0]) - 1)

                staples_in_list.insert(int(minus_indeces[0]) - 1, float(minus_ans_list[j]))

                if '-' in staples_in_list:
                    minus_indeces = []
                    for i in range(len(staples_in_list)):
                        if staples_in_list[i] == '-':
                            minus_indeces.append(i)

        if '+' in staples_in_list:
            plus_indeces = []
            for i in range(len(staples_in_list)):   
                if staples_in_list[i] == '+':
                    plus_indeces.append(i)

            plus_ans_list = []
            plus_re_list = []
            flag_plus = 0

            for i in range(len(plus_indeces)):
                if i == 0:
                    ans_plus = float(staples_in_list[plus_indeces[i] - 1]) + float(staples_in_list[plus_indeces[i] + 1])
                    plus_ans_list.append(ans_plus)
                    flag_plus += 1
                    flag_plus1 = 0

                    if len(plus_indeces) == 1:
                        flag_plus1 = 1
                        plus_re_list.append(flag_plus1)

                elif i != 0 and int(plus_indeces[i]) - int(plus_indeces[i - 1]) == 2:
                    ans_plus += float(staples_in_list[plus_indeces[i] + 1])
                    plus_ans_list.pop()
                    plus_ans_list.append(ans_plus)
                    flag_plus1 += 1

                elif i != 0 and not(int(plus_indeces[i]) - int(plus_indeces[i - 1]) == 2):
                    ans_plus = float(staples_in_list[plus_indeces[i] - 1]) + float(staples_in_list[plus_indeces[i] + 1])
                    plus_ans_list.append(ans_plus)
                    flag_plus += 1
   
                    flag_plus1 += 1
                    plus_re_list.append(flag_plus1)
                    flag_plus1 = 0

            if not(len(plus_indeces) == 1):

                flag_plus1 += 1
                plus_re_list.append(flag_plus1)
                flag_plus1 = 0

            for j in range(flag_plus):
 
                for j1 in range(int(plus_re_list[j]) * 2 + 1):
                    staples_in_list.pop(int(plus_indeces[0]) - 1)

                staples_in_list.insert(int(plus_indeces[0]) - 1, float(plus_ans_list[j]))

                if '+' in staples_in_list:
                    plus_indeces = []
                    for i in range(len(staples_in_list)):
                        if staples_in_list[i] == '+':
                            plus_indeces.append(i)

        for j2 in range(int(staples_indeces[1]) - int(staples_indeces[0]) + 1):
            ex_list.pop(int(staples_indeces[0]))

        ex_list.insert(staples_indeces[0], float(staples_in_list[0]))
        staples_in_list = []

        if '(' and ')' in ex_list:
            staples_indeces = []
            for i in range(len(ex_list)):
                if ex_list[i] == '(' or ex_list[i] == ')':
                    staples_indeces.append(i)


if '^' in ex_list:
    deg_indeces = []
    for i in range(len(ex_list)):          
        if ex_list[i] == '^':
            deg_indeces.append(i)

    deg_ans_list = []
    deg_re_list = []
    flag_deg = 0

    for i in range(len(deg_indeces)):

        if i == 0:
            ans_deg = float(ex_list[deg_indeces[i] - 1]) ** float(ex_list[deg_indeces[i] + 1])
            deg_ans_list.append(ans_deg)
            flag_deg += 1
            flag_deg1 = 0

            if len(deg_indeces) == 1:
                flag_deg1 = 1
                deg_re_list.append(flag_deg1)

        elif i != 0 and int(deg_indeces[i]) - int(deg_indeces[i - 1]) == 2:
            ans_deg **= float(ex_list[deg_indeces[i] + 1])
            deg_ans_list.pop()
            deg_ans_list.append(ans_deg)
            flag_deg1 += 1

        elif i != 0 and not(int(deg_indeces[i]) - int(deg_indeces[i - 1]) == 2):
            ans_deg = float(ex_list[deg_indeces[i] - 1]) ** float(ex_list[deg_indeces[i] + 1])
            deg_ans_list.append(ans_deg)
            flag_deg += 1
  

            flag_deg1 += 1
            deg_re_list.append(flag_deg1)
            flag_deg1 = 0

    if not(len(deg_indeces) == 1):

        flag_deg1 += 1
        deg_re_list.append(flag_deg1)
        flag_deg1 = 0

    for j in range(flag_deg):

        for j1 in range(int(deg_re_list[j]) * 2 + 1):
            ex_list.pop(int(deg_indeces[0]) - 1) 
        ex_list.insert(int(deg_indeces[0]) - 1, float(deg_ans_list[j]))

        if '^' in ex_list:
            deg_indeces = []
            for i in range(len(ex_list)):
                if ex_list[i] == '^':
                    deg_indeces.append(i)


if '/' in ex_list:
    del_indeces = []
    for i in range(len(ex_list)):  
        if ex_list[i] == '/':
            del_indeces.append(i)

    for i in range(len(del_indeces)):
        (ex_list[int(del_indeces[i]) + 1]) = 1 / float(ex_list[int(del_indeces[i]) + 1])

    for i in range(len(del_indeces)):
        ex_list[int(del_indeces[i])] = '*'      

if '*' in ex_list:
    mnoj_indeces = []
    for i in range(len(ex_list)):     
        if ex_list[i] == '*':
            mnoj_indeces.append(i)

    mnoj_ans_list = []
    mnoj_re_list = []
    flag_mnoj = 0

    for i in range(len(mnoj_indeces)):

        if i == 0:
            ans_mnoj = float(ex_list[mnoj_indeces[i] - 1]) * float(ex_list[mnoj_indeces[i] + 1])
            mnoj_ans_list.append(ans_mnoj)
            flag_mnoj += 1
            flag_mnoj1 = 0

            if len(mnoj_indeces) == 1:
                flag_mnoj1 = 1
                mnoj_re_list.append(flag_mnoj1)

        elif i != 0 and int(mnoj_indeces[i]) - int(mnoj_indeces[i - 1]) == 2:
            ans_mnoj *= float(ex_list[mnoj_indeces[i] + 1])
            mnoj_ans_list.pop()
            mnoj_ans_list.append(ans_mnoj)
            flag_mnoj1 += 1

        elif i != 0 and not(int(mnoj_indeces[i]) - int(mnoj_indeces[i - 1]) == 2):
            ans_mnoj = float(ex_list[mnoj_indeces[i] - 1]) * float(ex_list[mnoj_indeces[i] + 1])
            mnoj_ans_list.append(ans_mnoj)
            flag_mnoj += 1
  
            flag_mnoj1 += 1
            mnoj_re_list.append(flag_mnoj1)
            flag_mnoj1 = 0

    if not(len(mnoj_indeces) == 1):

        flag_mnoj1 += 1
        mnoj_re_list.append(flag_mnoj1)
        flag_mnoj1 = 0

    for j in range(flag_mnoj):

        for j1 in range(int(mnoj_re_list[j]) * 2 + 1):
            ex_list.pop(int(mnoj_indeces[0]) - 1) 
        ex_list.insert(int(mnoj_indeces[0]) - 1, float(mnoj_ans_list[j]))

        if '*' in ex_list:
            mnoj_indeces = []
            for i in range(len(ex_list)):
                if ex_list[i] == '*':
                    mnoj_indeces.append(i)


if '-' in ex_list:
    minus_indeces = []
    for i in range(len(ex_list)):
        if ex_list[i] == '-':
            minus_indeces.append(i)

    minus_ans_list = []
    minus_re_list = []
    flag_minus = 0

    for i in range(len(minus_indeces)):
        if i == 0:
            ans_minus = float(ex_list[minus_indeces[i] - 1]) - float(ex_list[minus_indeces[i] + 1])
            minus_ans_list.append(ans_minus)
            flag_minus += 1
            flag_minus1 = 0

            if len(minus_indeces) == 1:
                flag_minus1 = 1
                minus_re_list.append(flag_minus1)

        elif i != 0 and int(minus_indeces[i]) - int(minus_indeces[i - 1]) == 2:
            ans_minus -= float(ex_list[minus_indeces[i] + 1])
            minus_ans_list.pop()
            minus_ans_list.append(ans_minus)
            flag_minus1 += 1

        elif i != 0 and not(int(minus_indeces[i]) - int(minus_indeces[i - 1]) == 2):
            ans_minus = float(ex_list[minus_indeces[i] - 1]) - float(ex_list[minus_indeces[i] + 1])
            minus_ans_list.append(ans_minus)
            flag_minus += 1
   
            flag_minus1 += 1
            minus_re_list.append(flag_minus1)
            flag_minus1 = 0

    if not(len(minus_indeces) == 1):

        flag_minus1 += 1
        minus_re_list.append(flag_minus1)
        flag_minus1 = 0

    for j in range(flag_minus):
 
        for j1 in range(int(minus_re_list[j]) * 2 + 1):
            ex_list.pop(int(minus_indeces[0]) - 1)

        ex_list.insert(int(minus_indeces[0]) - 1, float(minus_ans_list[j]))

        if '-' in ex_list:
            minus_indeces = []
            for i in range(len(ex_list)):
                if ex_list[i] == '-':
                    minus_indeces.append(i)


if '+' in ex_list:
    plus_indeces = []
    for i in range(len(ex_list)):   
        if ex_list[i] == '+':
            plus_indeces.append(i)

    plus_ans_list = []
    plus_re_list = []
    flag_plus = 0

    for i in range(len(plus_indeces)):
        if i == 0:
            ans_plus = float(ex_list[plus_indeces[i] - 1]) + float(ex_list[plus_indeces[i] + 1])
            plus_ans_list.append(ans_plus)
            flag_plus += 1
            flag_plus1 = 0

            if len(plus_indeces) == 1:
                flag_plus1 = 1
                plus_re_list.append(flag_plus1)

        elif i != 0 and int(plus_indeces[i]) - int(plus_indeces[i - 1]) == 2:
            ans_plus += float(ex_list[plus_indeces[i] + 1])
            plus_ans_list.pop()
            plus_ans_list.append(ans_plus)
            flag_plus1 += 1

        elif i != 0 and not(int(plus_indeces[i]) - int(plus_indeces[i - 1]) == 2):
            ans_plus = float(ex_list[plus_indeces[i] - 1]) + float(ex_list[plus_indeces[i] + 1])
            plus_ans_list.append(ans_plus)
            flag_plus += 1
   
            flag_plus1 += 1
            plus_re_list.append(flag_plus1)
            flag_plus1 = 0

    if not(len(plus_indeces) == 1):

        flag_plus1 += 1
        plus_re_list.append(flag_plus1)
        flag_plus1 = 0

    for j in range(flag_plus):
 
        for j1 in range(int(plus_re_list[j]) * 2 + 1):
            ex_list.pop(int(plus_indeces[0]) - 1)

        ex_list.insert(int(plus_indeces[0]) - 1, float(plus_ans_list[j]))

        if '+' in ex_list:
            plus_indeces = []
            for i in range(len(ex_list)):
                if ex_list[i] == '+':
                    plus_indeces.append(i)

if not(float(ex_list[0]) == int(ex_list[0])):
    print('\nAnswer:', str(float(ex_list[0])))
else:
    print('\nAnswer:', str(int(ex_list[0])))

input()