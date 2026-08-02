---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/amazon-ec2-target.html
---

# Amazon EC2 as the target
<a name="amazon-ec2-target"></a>

If the target is an Amazon EC2 instance, make sure the AWS CLI is configured on Amazon EC2 before proceeding, and a create directory for the source Oracle Database dump files.

After AWS CLI is set up and you have created the directory, copy the Oracle Database dump files from Amazon S3 to the EC2 instance by running the following code.

```
aws s3 cp s3://DOC-EXAMPLE-SOURCE-BUCKET/ <Directory name that you created to place the dump files> – recursive
```

|
|
| Note: The parameter `– recursive` is to copy all the files from the source bucket. |
| --- |

## Data protection on Amazon EC2
<a name="data-protection-amazon-ec2"></a>

On Amazon EC2, you have the following data encryption options:
+ **Encrypt data at rest on Amazon EC2** – To encrypt data at rest on the Amazon EC2 instances, you can use Amazon Elastic Block Store (Amazon EBS). With Amazon EBS encryption, you can encrypt your attached volumes and as their snapshots. The encryption uses AWS KMS keys. For more information, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).
+ **Encrypt data in transit on Amazon EC2** – AWS offers multiple encryption options to keep your data secure as it travels between your network and AWS. For more information, see the [AWS documentation](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html).
