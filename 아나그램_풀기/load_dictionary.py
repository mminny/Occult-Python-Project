import sys

def load(file):
    """텍스트 파일을 열고 작은 순서대로 문자열을 배열로 구성한다."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt

    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
                file=sys.stderr)
        sys.exit(1)
