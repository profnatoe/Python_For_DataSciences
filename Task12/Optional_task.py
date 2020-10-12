filenames = ['numbers1.txt', 'numbers2.txt']
num_lists = [[int(x) for x in open(f).read().strip().split('\n')] \
             for f in filenames]
with open('all_numbers.txt', 'w') as outfile:
    outfile.write('\n'.join(str(x) for x in sorted(sum(num_lists, []))) + '\n')

print('Your file is saved under all_numbers.txt')