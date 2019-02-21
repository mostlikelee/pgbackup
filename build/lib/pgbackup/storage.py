import boto3

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucketname, filename):
    client.upload_fileobj(infile, bucketname, filename)