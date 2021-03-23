def interpret(text, list_=False):
    if not list_: code = text.split('\n')
    else: code = text

    stack = []

    line_num = 0

    while line_num < len(code):
        if '#' in code[line_num]: line_num += 1
        if 'push' in code[line_num]: stack.append(float(code[line_num].strip('push')))
        if 'pop' in code[line_num]: 
            if len(stack) != 0:
                del(stack[-1])

            else:
                print(f'Error on `{code[line_num]}` On Line {line_num}, Nothing In Stack!')
                break

        if 'add' in code[line_num]:
            if len(stack) < 2:
                print(f'Error on `{code[line_num]}` On Line {line_num}, Two Few Elements In Stack!')
                break
            
            else:
                stack.append(stack[-2]+stack[-1])

        if 'ifeq' in code[line_num]:
            if len(stack) != 0:
                if stack[-1] != 0:
                    if int(code[line_num].strip('ifeq')) > len(code)-1:
                        print(f'Error on `{code[line_num]}` On Line {line_num}, Line Number Does Not Exist!')
                        break
                    
                    else:
                        line_num = int(code[line_num].strip('ifeq'))
        
            else:
                print(f'Error on `{code[line_num]}` On Line {line_num}, Nothing In Stack!')
                break

        if 'jump' in code[line_num]:
            if int(code[line_num].strip('jump')) > len(code)-1:
                print(f'Error on `{code[line_num]}` On Line {line_num}, Line Number Does Not Exist!')
                break

            else:
                line_num = int(code[line_num].strip('jump'))

        if 'print' in code[line_num]:
            if len(stack) != 0:
                print(chr(int(stack[-1])), end="")

            else:
                print(f'Error on `{code[line_num]}` On Line {line_num}, Nothing In Stack!')
                break

        if 'dup' in code[line_num]:
            if len(stack) != 0:
                stack.append(stack[-1])

            else:
                print(f'Error on `{code[line_num]}` On Line {line_num}, Nothing In Stack!')
                break
        
        line_num += 1 # Advance
        
def interpret_file(filepath):
    file = open(filepath)
    interpret(file.readlines(), list_=True)

if __name__ == '__main__':
    interpret_file('helloworld.si')
