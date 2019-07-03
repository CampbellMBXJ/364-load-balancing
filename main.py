from filebuilder import FileBuilder
import sys

def main(args):
    """Main funtion to initialise and ouptut"""
    builder = FileBuilder(*args)
    builder.build_lp()
    print(builder)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1:])
    else:
        print("Error: Program only takes exactly 3 inputs")
