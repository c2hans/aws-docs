---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-first-channel.html
---

# Create your first Channel
<a name="msk-data-delivery-first-channel"></a>

1. Create the destination (S3 Table bucket or general-purpose S3 bucket) and the DLQ S3 bucket. For Iceberg, also register your JSON schema in AWS Glue Schema Registry.

1. Create the IAM service role with the required permissions and trust policy (see [IAM permissions for Channel](msk-data-delivery-iam.md)).

1. In the Amazon MSK console, open your Express cluster, choose the **Channel** tab, and choose **Create Channel** (see [Manage Channels](msk-data-delivery-manage.md) for full steps).

1. Wait for the Channel to transition from **Creating** to **Active**.

1. Produce records to the topic and verify delivery (query the Iceberg table in Athena or Spark, or inspect objects in the S3 bucket).
