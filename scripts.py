import json
import time
from google.cloud import storage


dj = {
    
    "floresBorja":
    {
        "1":
        {
            "IdaVuelta": ["iglesia", "cancha"],
            "u": [26.893101006158011, -101.41865053710945],
            "np": 10,
            "estado": "avería, no recibe a pasajeros"
        },
        "2":
        {
            "IdaVuelta": ["iglesia", "progreso"],
            "u": [26.925101006158011, -101.41865053710945],
            "np": 30,
            "estado": "funcional"
            
        }

    }
}


x = 26.893101006158011
y = -101.41865053710945

xn = 26.893101006158011
yn = -101.41865053710945


from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Subir un archivo a Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f'Archivo {source_file_name} subido a {destination_blob_name}.')


nombre_del_bucket = 'bustes'
nombre_en_cloud_storage = 'jsonTest.json'

upload_blob(nombre_del_bucket, 'gendabus/static/json/redT.json', nombre_en_cloud_storage)

###############

from google.cloud import storage

def bucket_metadata(bucket_name):
    """Prints out a bucket's metadata."""
    # bucket_name = 'your-bucket-name'

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    print(f"ID: {bucket.id}")
    print(f"Name: {bucket.name}")
    print(f"Storage Class: {bucket.storage_class}")
    print(f"Location: {bucket.location}")
    print(f"Location Type: {bucket.location_type}")
    print(f"Cors: {bucket.cors}")
    print(f"Default Event Based Hold: {bucket.default_event_based_hold}")
    print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
    print(f"Metageneration: {bucket.metageneration}")
    print(
        f"Public Access Prevention: {bucket.iam_configuration.public_access_prevention}"
    )
    print(f"Retention Effective Time: {bucket.retention_policy_effective_time}")
    print(f"Retention Period: {bucket.retention_period}")
    print(f"Retention Policy Locked: {bucket.retention_policy_locked}")
    print(f"Requester Pays: {bucket.requester_pays}")
    print(f"Self Link: {bucket.self_link}")
    print(f"Time Created: {bucket.time_created}")
    print(f"Versioning Enabled: {bucket.versioning_enabled}")
    print(f"Labels: {bucket.labels}")

bucket_metadata("bustes")
###############


while True:
    x+=0.0001
    y+=0.0001
    xn-=0.0001
    yn-=0.0001
    time.sleep(.5)


    dj["floresBorja"]["1"]["u"] = [x,y]
    dj["floresBorja"]["2"]["u"] = [xn,yn]
    with open('gendabus/static/json/redT.json', 'w') as f:
        json.dump(dj, f)



