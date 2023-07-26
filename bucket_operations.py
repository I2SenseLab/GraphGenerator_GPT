# Upload and Download files to and from crosswords-images bucket on google storage. 

from google.cloud import storage

def upload_to_bucket(source_file_name, destination_blob_name, bucket_name = "graphgpt-images", project = "atkin-1"):
    """Uploads a file to the bucket."""
    storage_client = storage.Client(project=project)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)


    blob.upload_from_filename(source_file_name)
    blob.make_public()
    return blob.public_url
