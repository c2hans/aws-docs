---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/ota-updates-prerequisites-configuration.html
---

# Prerequisites
<a name="ota-updates-prerequisites-configuration"></a>

Before creating OTA tasks, you must configure the following prerequisites:

## Configure Amazon S3 access
<a name="configure-amazon-s3-access"></a>

To enable OTA updates, you must upload your job documents to an Amazon S3 bucket and configure appropriate access permissions:

1. Upload your OTA job document to an S3 bucket

1. Add an Amazon S3 bucket policy that grants managed integrations access to your job documents:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "PolicyForS3JobDocument",
      "Effect": "Allow",
      "Principal": {
        "Service": "iotmanagedintegrations.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": [
        "arn:aws:s3:::YOUR_BUCKET/*",
        "arn:aws:s3:::YOUR_BUCKET/ota_job_document.json",
        "arn:aws:s3:::YOUR_BUCKET"
      ]
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
