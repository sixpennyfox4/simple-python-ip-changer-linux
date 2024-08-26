from tornet import initialize_environment, change_ip_repeatedly, change_ip

def main():
    print('!TO USE THIS INSTALL TORNET(sudo pip install tornet) AND MAKE YOUR BROWSER PROXY TO BE: 127.0.01, 9050, socks5!')
    print()
    
    print('(1): Single ip change')
    print('(2): Repeatable ip change')
    
    choice = int(input('Choice: '))
    
    def change_ip_repeat():
        print()
        
        interval = int(input('Interval: '))
        count = int(input('Count(0 for inf): '))
        print()
    
        initialize_environment()
    
        change_ip_repeatedly(interval=interval, count=count)
    
    def change_ip_single():
        print()
        
        initialize_environment()
    
        change_ip()

    if choice == 1:
        change_ip_single()
    elif choice == 2:
        change_ip_repeat()
    else:
        print()
        main()

main()
