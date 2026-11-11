---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/amazon-ec2-target.html
---

# Amazon EC2 as the target
<a name="amazon-ec2-target"></a>

If the target is an Amazon EC2 instance, configure the AWS CLI on Amazon EC2 before you proceed, and create a directory for the source Oracle Database dump files.

After you set up the AWS CLI and create the directory, copy the Oracle Database dump files from Amazon S3 to the Amazon EC2 instance by running the following command.

```
aws s3 cp s3://DOC-EXAMPLE-BUCKET/ <target-directory-for-dump-files> --recursive
```

|
|
| Note: The `--recursive` parameter copies all files from the source bucket. Replace `DOC-EXAMPLE-BUCKET` with the name of your bucket, and replace `<target-directory-for-dump-files>` with the directory that you created on the Amazon EC2 instance. |
| --- |

## Data protection on Amazon EC2
<a name="data-protection-amazon-ec2"></a>

On [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), you have the following data encryption options:
+ **Encrypt data at rest on Amazon EC2** – To encrypt data at rest on the Amazon EC2 instances, you can use Amazon Elastic Block Store (Amazon EBS). With Amazon EBS encryption, you can encrypt your attached volumes and their snapshots. The encryption uses [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS) keys. For more information, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).
+ **Encrypt data in transit on Amazon EC2** – AWS offers multiple encryption options to help protect your data as it travels between your network and AWS. For more information, see the [AWS documentation](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html).
