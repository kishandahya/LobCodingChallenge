# LobCodingChallenge
This is a challenge I completed for the company Lob where I used their API to send a letter to the local U.S. representative of a given address. 

Prereqs to running the program:

1. Download and install Python 2.7

2. Configure pip installing for your computer

3. Run following commands in your terminal of choice. 
	1. `pip install argparse`
	2. `pip install lob`

Now you should be ready to use the program! Please don't hesitate to contact me for any information on how to run it or the code itself.

Example of the command to type in terminal:
`python LobCodingChallenge.py "Kishan Dahya" "555 Glenrock Avenue" "Los Angeles" "CA" "90024" "This is a test letter for Lob's coding challenge. Thank you legislator."`

positional arguments:

1.  name                 The name of the person sending the letter
2.  address1             The address from which the letter will be sent
3.  city                 The city from which the letter will be sent
4.  state                The state from which the letter will be sent. Must be the 2 letter postal abbreviation
5.  zip_code             The zip code from which the letter will be sent
6.  message              The actual body of the letter to be sent to the
                       representative. It must be less than 200 words long

optional arguments:

1. -h, --help           show this help message and exit
2. --address2 ADDRESS2  Optional argument for address line 2 for apt numbers, gate codes, etc

