# 1) prints arguments to the console
import sys
print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
   print(f"Argument {i}: {arg}")
   

# 2) arguments parsing 
import argparse

parser = argparse.ArgumentParser(description='Some dummy program')
parser.add_argument('--print', help='text to print')
parser.add_argument('--N', help='how many times to print', type=int)
args = parser.parse_args()

if args.print is None or args.N is None:
    parser.print_help()
    exit()

for x in range(args.N):
    print(args.print)

