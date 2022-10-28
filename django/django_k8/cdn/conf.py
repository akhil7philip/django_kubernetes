import os

AWS_QUERYSTRING_AUTH    = False
AWS_SECRET_KEY_ID       = os.environ.get("AWS_SECRET_KEY_ID")
AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'dj-k8-space'
AWS_S3_SIGNATURE_VERSION= 's3v4'
AWS_S3_REGION_NAME      = 'sgp1'
AWS_S3_ENDPOINT_URL     = "https://sgp1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS= {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION            = "https://dj-k8-space.sgp1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE    = 'django_k8.cdn.backends.MediaRootS3BotoStorage'
STATICFILES_STORAGE     = 'django_k8.cdn.backends.StaticRootS3BotoStorage'