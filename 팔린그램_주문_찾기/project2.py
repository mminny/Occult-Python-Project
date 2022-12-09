try: 
    with open(file) as in_file:
        #do something
except IOError as e:
    print("{}\nError opening {}. Terminating program.".format(e, file),
    file = sys.stderr)
    sys.exit(1)