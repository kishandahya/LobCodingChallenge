import argparse
import requests
import lob


def main():
    parser = argparse.ArgumentParser(
        description='This program sends a letter to the local state representative of the ' +
                    'address given as a command line argument',
        usage = 'python LobCodingChallenge.py "Kishan Dahya" "555 Glenrock Avenue" "Los Angeles" "CA" "90024" ' +
               '"This is a test letter for Lob\'s coding challenge. Thank you legislator."')
    parser.add_argument('name', help='The name of the person sending the letter')
    parser.add_argument('address1', help='The address from which the letter will be sent')
    parser.add_argument('--address2', help='Optional argument for address line 2 for apt numbers, gate codes, etc')
    parser.add_argument('city', help='The city from which the letter will be sent')
    parser.add_argument('state', help='The state from which the letter will be sent')
    parser.add_argument('zip_code', help='The zip code from which the letter will be sent')
    parser.add_argument('message', help='The actual body of the letter to be sent to the representative. It must ' +
                                        'be less than 200 words long\n\n')
    args = parser.parse_args()
    try:
        lob.api_key = 'test_94b2323311c60601dee8872601969bbf38a'
        google_civic_info_api = 'AIzaSyD9iaO1L3fWLxDOelv9GjYIUxcD3W8GjbA'
        from_address = create_address(args)
        if count_words(args.message) > 200:
            raise Exception('Message over 200 words long')
        google_request = 'https://www.googleapis.com/civicinfo/v2/representatives?address=' + \
                         args.address1.replace(' ', '+') + '+' + args.city.replace(' ', '+') + '+' + args.state.replace(
            ' ', '+') + '+' + \
                         args.zip_code.replace(' ', '+') + \
                         '&includeOffices=true&levels=country&roles=legislatorLowerBody&key=' + google_civic_info_api
        response = requests.request("GET", google_request)
        create_letter(args.message, response.json(), from_address)
    except Exception as error:
        parser.print_help()
        print('\n')
        print('You got this error: ' + repr(error))
        print('PLease try again')


def count_words(sentence):
    return len(sentence.split())


# # Creating an Address Object
def create_address(args):
    from_name = args.name
    from_address1 = args.address1
    from_city = args.city
    from_state = args.state
    from_zip_code = args.zip_code
    message = args.message
    from_address = lob.Address.create(
        name=from_name,
        description='Letter to Representative',
        address_line1=from_address1,
        address_city=from_city,
        address_state=from_state,
        address_country='US',  # country not an input argument, so I have it defaulted to the US
        address_zip=from_zip_code
    )
    print('\n')
    print('Address Response')
    print('\n')
    print('=======================================================')
    print('\n')
    print(from_address)
    print('\n')
    print('======================================================')
    print('\n')
    return from_address


# Creating a Letter
def create_letter(message, response_json, from_address):
    rep_name = response_json['officials'][0]['name']
    rep_address = response_json['officials'][0]['address'][0]
    rep_address_line1 = rep_address['line1']
    rep_city = rep_address['city']
    rep_state = rep_address['state']
    rep_zip_code = rep_address['zip']
    example_letter = lob.Letter.create(
        description='Letter to Representative',
        to_address={
            'name': rep_name,
            'address_line1': rep_address_line1,
            'address_city': rep_city,
            'address_zip': rep_zip_code,
            'address_state': rep_state,
        },
        from_address=from_address,
        file="""
            <html>
            <head>
            <meta charset="UTF-8">
            <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
            <title>Kishan Lob example</title>
            <style>
              *, *:before, *:after {
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box;
              }

              body {
                width: 8.5in;
                height: 11in;
                margin: 0;
                padding: 0;
              }

              .page {
                page-break-after: always;
              }

              .page-content {
                position: relative;
                width: 8.125in;
                height: 10.625in;
                left: 0.1875in;
                top: 0.1875in;
                background-color: rgba(0,0,0,0.2);
              }

              .text {
                position: relative;
                left: 20px;
                top: 20px;
                width: 6in;
                font-family: sans-serif;
                font-size: 30px;
              }

              #return-address-window {
                position: absolute;
                left: .625in;
                top: .5in;
                width: 3.25in;
                height: .875in;
                background-color: rgba(0,0,0,0.0);
              }

              #return-address-text {
                position: absolute;
                left: .07in;
                top: .34in;
                width: 2.05in;
                height: .44in;
                background-color: white;
                font-size: .11in;
              }

              #return-logo {
                position: absolute;
                left: .07in;
                top: .02in;
                width: 2.05in;
                height: .3in;
                background-color: white;
              }

              #recipient-address-window {
                position: absolute;
                left: .625in;
                top: 1.75in;
                width: 4in;
                height: 1in;
                background-color: rgba(0,0,0,0);
              }

              #recipient-address-text {
                position: absolute;
                left: .07in;
                top: .05in;
                width: 2.92in;
                height: .9in;
                background-color: white;
              }

            </style>
            </head>

            <body>
              <div class="page">
                <div class="page-content">
                  <div class="text" style="top: 3in">
                   """ + message + """
                  </div>
                </div>
                <div id="return-address-window">
                  <div id="return-address-text">
                  </div>
                </div>
                <div id="recipient-address-window">
                  <div id="recipient-address-text">
                  </div>
                </div>
              </div>
            </html>
          """,
        data={
            'company': 'ACME'
        },
        color=True
    )

    print("Letter Response")
    print("\n")
    print("=======================================================")
    print("\n")
    print(example_letter)
    print("\n")
    print("=======================================================")
    print("\n")


main()
