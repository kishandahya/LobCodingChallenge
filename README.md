# LobCodingChallenge
This is a challenge I completed for the company Lob where I used their API to send a letter to the local U.S. representative of a given address. 

Prereqs to running the program:
1. Download and install Python 2.7
2. Configure pip installing for your computer
3. Run following commands in your terminal of choice. 
pip install argparse
pip install lob

Now you should be ready to use the program! Please don't hesitate to contact me for any information on how to run it or the code itself.

Example of the command to type in terminal:
python LobCodingChallenge.py "Kishan Dahya" "555 Glenrock Avenue" "Los Angeles" "CA" "90024" "This is a test letter for Lob's coding challenge. Thank you legislator."

positional arguments:
  name                 The name of the person sending the letter
  address1             The address from which the letter will be sent
  city                 The city from which the letter will be sent
  state                The state from which the letter will be sent. Must be the 2 letter postal abbreviation
  zip_code             The zip code from which the letter will be sent
  message              The actual body of the letter to be sent to the
                       representative. It must be less than 200 words long

optional arguments:
  -h, --help           show this help message and exit
  --address2 ADDRESS2  Optional argument for address line 2 for apt numbers,
                       gate codes, etc

