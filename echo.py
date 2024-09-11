try:
    while True:
        user_input = input()  # (STDIN)
        print(user_input)     # (STDOUT)
except KeyboardInterrupt:
    print("\nScript terminated by user.")
# Exit Ctrl+C