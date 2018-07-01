from nba_py import game
import csv
import time

PREFIX = '002'
YEARS = ['96', '97', '98', '99', 
		 '00', '01', '02', '03', 
		 '04', '05', '06', '07',
		 '08', '09', '10', '11', 
		 '12', '13', '14', '15',
		 '16', '17', '18']

'''

EXAMPLE = http://stats.nba.com/stats/playbyplay?GameID=0029600001&StartPeriod=1&EndPeriod=10
'''


def pad_number(n):
	return '{:05d}'.format(n)


def main():

	for YEAR in YEARS:
		rows = []
		keep_going = 1
		game_num = 0
		
		with open('./data/recent/{}.csv'.format(YEAR), 'w') as outfile:
			writer = csv.writer(outfile)
			
			while keep_going == 1:
				game_num += 1
				game_num_form = pad_number(game_num)
				gid = '{}{}{}'.format(PREFIX, YEAR, game_num_form)
				try:
					print("Getting GAME_ID: {}".format(gid))
					res = game.PlayByPlay(gid)
					print("Recieved results {}".format(res))
					time.sleep(1)
				except Exception as e:
					print("Error getting JSON: {}".format(e))
				
				rows_curr = res.json['resultSets'][0]['rowSet']
				header = res.json['resultSets'][0]['headers']
				
				writer.writerow(header)
			
				if rows_curr == []:
					keep_going = 0
					continue
				else:
					writer.writerow(row)
				


if __name__ == '__main__':
	main()