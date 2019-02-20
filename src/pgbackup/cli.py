import argparse

known_drivers = ['local', 's3']

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("unknown driver")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = argparse.ArgumentParser(description="""
        Backup PostgreSQL databases locally or to AWS S3
        """)
    parser.add_argument('url',help='URL of database to Backup')
    parser.add_argument('--driver',
                        help='how and where to store Backup',
                        nargs=2,
                        # choices=['s3', 'local'],
                        metavar=("DRIVER", "DESTINATION"),
                        action=DriverAction,
                        required=True)
    return parser

def main():
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'w')
        storage.local(dump.stdout, outfile)
        