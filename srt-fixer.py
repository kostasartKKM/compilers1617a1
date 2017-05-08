

import sys
import re
import argparse

# SKENTERIDIS KONSTANTINOS
# A.M.: P2014221

# -- Edw ginetai o entopismos kathe grammhs xronikhs plhroforias mesw kanonikhs ekfrashs
# -- me morfh 00:00:00,000 --> 00:00:00,000
restr = r'(\d{2}):(\d{2}):(\d{2}),(\d{3})\s-->\s(\d{2}):(\d{2}):(\d{2}),(\d{3})$'
rexp = re.compile(restr)

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,'r+',newline='') as ifp:	
	for line in ifp:
		
		
		# -- Edw tha kanei anazhthsh se oloklhro to keimeno kai tha bgalei ta matches
		m = rexp.search(line)
		
		# -- Parakatw ginetai h metatroph tou string twn deuteroleptwn se float,
		# -- meta prostithetai to offset, kai sthn sunexeia metatrepetai pali pisw se string.
		
		if m is not None:
			# -- Gia ta seconds sta aristera
			left_seconds_old = m.group(3)
			left_seconds_new = float(left_seconds_old)+args.offset
			left_seconds_final = str(left_seconds_new)
			changing_left = re.sub(restr,r'\3'+left_seconds_final,line)
			
			# -- Gia ta seconds sta deksia
			right_seconds_old = m.group(7)
			right_seconds_new = float(right_seconds_old)+args.offset
			right_seconds_final = str(right_seconds_new)
			changing_right = re.sub(restr,r'\7'+right_seconds_final,line)
		
		

		sys.stdout.write(line)

		
ifp.close()		
		

