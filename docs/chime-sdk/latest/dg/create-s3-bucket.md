---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-s3-bucket.html
---

# Creating an Amazon S3 bucket for Amazon Chime SDK media capture pipelines
<a name="create-s3-bucket"></a>

You can use the Amazon S3 console the AWS SDKs, or the AWS CLI to to create an Amazon S3 bucket. For more information, refer to [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html), in the *Amazon Simple Storage Service (S3) User Guide*.

The Amazon S3 bucket for your media capture pipeline must belong to the same AWS account as the Amazon Chime SDK meeting. In addition, you must give the `s3:PutObject` and `s3:PutObjectAcl` permission to the Amazon Chime SDK service principal [mediapipelines.chime.amazonaws.com](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html). You can do that with the Amazon S3 console or the AWS Command Line Interface (AWS CLI). The Amazon S3 bucket must belong to one of the available [Amazon Chime SDK media Regions](https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html).

**Note**
Make sure to add a policy to your IAM user to grant access to your bucket. Also, if you use a Region that AWS disables by default, you must have an Amazon S3 bucket in that Region.
By default, AWS disables the following Regions, and you can't host meeting resources in them until you enable them:
Africa (Cape Town)
Asia Pacific (Hong Kong)
Asia Pacific (Jakarta)
Europe (Milan)
Middle East (Bahrain)
If you use one of those Regions, it must have an Amazon S3 bucket. This applies even if you use the Amazon S3 APIs to communicate with Regions that aren't blocked by default and already have a bucket. For more information about enabling blocked regions, refer to [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference*.

Once you create a bucket, record its ARN. You use it to create a media capture pipeline.

The following example shows an Amazon S3 bucket policy.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Id": "{{AWSChimeMediaCaptureBucketPolicy}}",
    "Statement": [
        {
            "Sid": "{{AWSChimeMediaCaptureBucketPolicy}}",
            "Effect": "Allow",
            "Principal": {
                "Service": "mediapipelines.chime.amazonaws.com"
            },
            "Action": [ "s3:PutObject", "s3:PutObjectAcl" ],
            "Resource": "arn:aws:s3:::{{Bucket_Name}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "ArnLike": {
                "aws:SourceArn": "arn:aws:chime:*:{{123456789012}}:*"
                }
            }
        }
    ]
}
```

------
