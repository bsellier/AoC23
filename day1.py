
def txt_to_call(txt: str):
    callibration = ''
    for c in txt:
        if c.isdigit():
            callibration += c
    final = callibration[0] + callibration[len(callibration)-1]
    print(final)
    return int(final)

def read_input(f_name: str):
    with open(f_name) as file:
        return file.read()

def main():
    txt = read_input("input")
    callibrations = []
    for line in txt.split('\n'):
        if line == '': continue
        call = txt_to_call(line)
        print(call)
        callibrations.append(call)
    print(sum(callibrations)) 

if __name__ == "__main__":
    main()
