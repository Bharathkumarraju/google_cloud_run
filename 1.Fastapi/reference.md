## Run

```
docker build -t serverless-python -f Dockerfile .
docker run --env PORT=5000 -it  -p 80:5000 serverless-python
```

## Push

#### via docker

```
docker build -t serverless-python -f Dockerfile .
docker tag serverless-python asia.gcr.io/srianjaneyam/serverless-python 
export GOOGLE_APPLICATION_CREDENTIALS=/Users/bharathkumarraju/Downloads/srianjaneyam-b63c432cb14c.json
gcloud auth activate-service-account --key-file=/Users/bharathkumarraju/Downloads/srianjaneyam-b63c432cb14c.json
docker login -u _json_key -p "`cat ${GOOGLE_APPLICATION_CREDENTIALS}`" https://asia.gcr.io
docker push asia.gcr.io/srianjaneyam/serverless-python
```

### via gcloud build
```
gcloud builds submit --tag asia.gcr.io/srianjaneyam/serverless-python2 .
```

```
bharathkumarraju@R77-NB193 google_cloud_run % gcloud builds submit --tag asia.gcr.io/srianjaneyam/serverless-python2 .
Creating temporary tarball archive of 7 file(s) totalling 2.7 KiB before compression.
Some files were not included in the source upload.

Check the gcloud log [/Users/bharathkumarraju/.config/gcloud/logs/2020.07.28/23.34.55.415405.log] to see which files and the contents of the
default gcloudignore file used (see `$ gcloud topic gcloudignore` to learn
more).

Uploading tarball of [.] to [gs://srianjaneyam_cloudbuild/source/1595950495.920288-6957783c7df647469fd366471c77183b.tgz]
API [cloudbuild.googleapis.com] not enabled on project [202016682554].
 Would you like to enable and retry (this will take a few minutes)? 
(y/N)?  y

Enabling service [cloudbuild.googleapis.com] on project [202016682554]...
Operation "operations/acf.cbb66473-fd4a-492f-88f2-48af68da7242" finished successfully.
Created [https://cloudbuild.googleapis.com/v1/projects/srianjaneyam/builds/e36151c4-7d60-4694-aa54-45b83dc3959e].
Logs are available at [https://console.cloud.google.com/cloud-build/builds/e36151c4-7d60-4694-aa54-45b83dc3959e?project=202016682554].
--------------------------------------------------------------------------- REMOTE BUILD OUTPUT ----------------------------------------------------------------------------
starting build "e36151c4-7d60-4694-aa54-45b83dc3959e"

FETCHSOURCE
Fetching storage object: gs://srianjaneyam_cloudbuild/source/1595950495.920288-6957783c7df647469fd366471c77183b.tgz#1595950498370206
Copying gs://srianjaneyam_cloudbuild/source/1595950495.920288-6957783c7df647469fd366471c77183b.tgz#1595950498370206...
/ [1 files][  1.9 KiB/  1.9 KiB]                                                
Operation completed over 1 objects/1.9 KiB.                                      
BUILD
Already have image (with digest): gcr.io/cloud-builders/docker

```

## Deploy cloud run

```
gcloud run deploy serverless-bharath --image asia.gcr.io/srianjaneyam/serverless-python \
--platform managed --region asia-southeast1

```

