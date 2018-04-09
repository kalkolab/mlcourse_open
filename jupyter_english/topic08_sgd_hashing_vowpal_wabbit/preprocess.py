from tqdm import tqdm
from argparse import ArgumentParser

def main(argv=None):
    parser = ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("dest")
    
    args = parser.parse_args()

    langs = ['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift']
    
    source_file = args.source
    dest_file = args.dest

    with open(source_file, 'r') as source, open(dest_file, 'w') as dest:
        for line in tqdm(source.readlines()):
            cells = line.split("\t")
            if len(cells) == 2:
                lang_tags = list(filter(lambda t: t in langs, cells[1].split()))
                if (len(lang_tags)==1):
                    dest.write("%s | %s\n" % (langs.index(lang_tags[0])+1, \
                                              cells[0].replace(":", " ").replace("|", " ").replace("\n", " ").replace("\r", " ")))

if __name__ == '__main__':
    main()