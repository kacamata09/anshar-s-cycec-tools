
import argparse
import socket

# args function
import tools

import helper

description_lib = \
'''------------information gathering help--------------
should use -u <URL> or --url <URL> for add url or domain,
and should use -i <YOUR_OPTION> or --information <YOUR_OPTION> for choose
type of information gathering you want, there are options:
1. Ip Checker
2. Whois Checker
3. Admin Page Cheker'''

should_add_domain = \
"""------------------------SHOULD ADD DOMAIN---------------------------
You should add domain with argument -u <DOMAIN> atau --url <DOMAIN>
or show HELP with argument -h"""

class Main():
    def __init__(self):
        'Add argument in python execute'
        self.parser = argparse.ArgumentParser(description=description_lib,  formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Thanks you for using my library, love from @kacamata09")
        # self.parser.add_argument(
        #     "-h",
        #     "--help",
        #     action="help",
        #     help="See help message from my library",
        # )
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            help="See version from Information Gathering",
            version="Information Gathering version : 0.1",
        )
        self.parser.add_argument(
            "-D", "--dict", action="store", help="Add file dictionary txt"
        )
        self.parser.add_argument(
            "-u", "--url", action="store", help="Add url or domain"
        )
        self.parser.add_argument(
            "-i", "--information", action="store", choices=[1, 2, 3], type=int, help="Options for Information Gathering"
        )

    
        ### args register
        self.args_register()
        self.args = self.parser.parse_args()

        #### add dictionary
         
        if self.args.url == None:
            print(should_add_domain)
        elif self.args.information == None:
            print('SHOULD ADD -i <OPTION> or --information <OPTION>')
        else:
            try: 
                socket.gethostbyname(self.args.url)
                self.args_exec()
            except socket.gaierror:
                print('----------- =========  ERROR DOMAIN  ========= -----------')
                print('Domain you entered maybe wrong, please enter correct domain')
            except KeyboardInterrupt:
                print('Exit')
    

    def args_register(self):
        self.geoloc = tools.geo_location.argument(self.parser)

    def args_exec(self):
        dictionary_txt = False
        if self.args.dict:
            dictionary_txt = helper.dictionary_assign_in_list(self.args.dict)
            
        if self.args.information == 1:
            tools.ip_checker.ip_checker(self.args.url, self.args.geoloc)
        elif self.args.information == 2:
            tools.whois_checker.whois_check(self.args.url)
        elif self.args.information == 3:
            tools.admin_page_checker.admin_page_check(self.args.url, dictionary_txt)




if __name__ == '__main__':
    Main()
    

        
