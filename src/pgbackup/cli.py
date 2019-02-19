import argparse

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = argparse.ArgumentParser(description="""
        Backup PostgreSQL databases locally or to AWS S3
        """)
    parser.add_argument('url',help='URL of database to Backup')
    parser.add_argument('--driver','-d',
                        help='how and where to store Backup',
                        nargs=2,
                        action=DriverAction,
                        required=True)
    return parser
