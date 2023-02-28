def web_search(inp):
    from webbrowser import open_new_tab
    open_new_tab(inp)

def search_on_disks(name, disk):
    from pathlib import Path
    k = 0
    flag = False
    a = None
    while k <= 10:
        alb = sorted(Path(f'{disk}:/').glob('*/' * k + f'{name}.*'))
        if alb:
            for a in alb:
                print(a)
                ans = input('это то?\n')
                if ans.lower() != 'нет':
                    flag = True
                    break
        if flag:
            break        
        k += 1
    return a
