#Python Time Lapse by Patrick Dugan. Just a wrapper for imageio

import imageio
import argparse
import sys
import pathlib

class TimeLapseWorker():
    def __init__(self, sourcefolder, outfile, duration):
        self.sourcefolder = sourcefolder
        self.outfile = outfile
        self.duration = duration

    def createGIF(self):
        pics= []
        sourcefolder = pathlib.Path(self.sourcefolder)
        for pic in sourcefolder.iterdir():
            pics.append(imageio.imread(pic))
        durAmt = 1/(len(pics) / int(self.duration))
        imageio.mimsave(self.outfile, pics, duration=durAmt)
        

if __name__ =='__main__':
    parser= argparse.ArgumentParser(add_help= True, description= "Creates a GIF timelapse.")
    parser.add_argument('-s','--sourcefolder', help="Folder with pics.")
    parser.add_argument('-o','--outfile', help="File to save as.")
    parser.add_argument('-d','--duration', default = 15, help='Duration of timelapse in seconds.')

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    try:
        process = TimeLapseWorker(args.sourcefolder, args.outfile, args.duration)
        if args.outfile.lower().endswith('.gif'):
            process.createGIF()
        else:
            parser.print_help()
            sys.exit(1)

    except Exception as e:
        print(e)

