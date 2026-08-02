---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html
---

# Copy data from an Amazon S3 bucket to another account and Region by using the AWS CLI
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli"></a>

*Appasaheb Bagali and Purushotham G K, Amazon Web Services*

## Summary
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-summary"></a>

This pattern describes how to migrate data from a source Amazon Simple Storage Service (Amazon S3) bucket in an AWS account to a destination Amazon S3 bucket in another AWS account, either in the same AWS Region or in a different Region.

The source Amazon S3 bucket allows AWS Identity and Access Management (IAM) access by using an attached resource policy. A user in the destination account has to assume a role that has `PutObject` and `GetObject` permissions for  the source bucket. Finally, you run `copy` and `sync` commands to transfer data from the source Amazon S3 bucket to the destination Amazon S3 bucket.

Accounts own the objects that they upload to Amazon S3 buckets. If you copy objects across accounts and Regions, you grant the destination account ownership of the copied objects. You can change the ownership of an object by changing its [access control list (ACL)](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html) to `bucket-owner-full-control`. However, we recommend that you grant programmatic cross-account permissions to the destination account because ACLs can be difficult to manage for multiple objects.

**Warning**
This scenario requires IAM users with programmatic access and long-term credentials, which present a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the IAM documentation.

## Prerequisites and limitations
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-prereqs"></a>

*Prerequisites*
+ Two active AWS accounts in the same or different AWS Regions.
+ An existing Amazon S3 bucket in the source account.
+ If your source or destination Amazon S3 bucket has [default encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) enabled, you must modify the AWS Key Management Service (AWS KMS) key permissions. For more information, see the [AWS re:Post article](https://repost.aws/knowledge-center/s3-bucket-access-default-encryption) on this topic.
+ Familiarity with cross-account permissions.

*Limitations*
+ This pattern covers one-time migration. For scenarios that require continuous and automatic migration of new objects from a source bucket to a destination bucket, you can use [Amazon S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html).
+ This patterns uses session credentials (`AccessKeyId`, `SecretAccessKey`, and `SessionToken`) that are temporary and non-persistent. The expiration timestamp in the output indicates when these credentials expire. The role is configured with the maximum session duration. The copy job will be canceled if the session expires.

## Architecture
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-architecture"></a>

![Copying Amazon S3 data to another account or Region](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a574c26b-fdd9-4472-842b-b34c3eb2bfe9/images/5e4dec53-dfc8-478b-a7c4-503d63c8ac4e.png)

## Tools
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

## Best practices
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-best-practices"></a>
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)
+ [Applying least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) (IAM documentation)

## Epics
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-epics"></a>

### Create an IAM user and role in the destination AWS account
<a name="create-an-iam-user-and-role-in-the-destination-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM user and get the access key. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html) | AWS DevOps |
| Create an IAM identity-based policy. | Create an IAM identity-based policy named `S3MigrationPolicy` by using the following permissions. Modify the source and destination bucket names according to your use case. This identity-based policy allows the user who is assuming this role to access the source bucket and destination bucket. For detailed instructions, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the IAM documentation. <pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:ListBucket",<br />                "s3:ListObjectsV2",<br />                "s3:GetObject",<br />                "s3:GetObjectTagging",<br />                "s3:GetObjectVersion",<br />                "s3:GetObjectVersionTagging"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::amazon-s3-demo-source-bucket",<br />                "arn:aws:s3:::amazon-s3-demo-source-bucket/*"<br />            ]<br />        },<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:ListBucket",<br />                "s3:PutObject",<br />                "s3:PutObjectAcl",<br />                "s3:PutObjectTagging",<br />                "s3:GetObjectTagging",<br />                "s3:ListObjectsV2",<br />                "s3:GetObjectVersion",<br />                "s3:GetObjectVersionTagging"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::amazon-s3-demo-destination-bucket",<br />                "arn:aws:s3:::amazon-s3-demo-destination-bucket/*"<br />            ]<br />        }<br />    ]<br />}</pre> | AWS DevOps |
| Create an IAM role. | Create an IAM role named `S3MigrationRole` by using the following trust policy. Modify the Amazon Resource Name (ARN) of the destination IAM role or user name in the trust policy according to your use case. This trust policy allows the newly created IAM user to assume `S3MigrationRole`. Attach the previously created `S3MigrationPolicy`. For detailed steps, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the IAM documentation.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "AWS": "arn:aws:iam::<destination_account>:user/<user_name>"<br />            },<br />            "Action": "sts:AssumeRole",<br />            "Condition": {}<br />        }<br />    ]<br />}</pre> | AWS DevOps |

### Create and attach the Amazon S3 bucket policy in the source account
<a name="create-and-attach-the-s3-bucket-policy-in-the-source-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and attach an Amazon S3 bucket policy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html) | Cloud administrator |

### Configure the destination Amazon S3 bucket
<a name="configure-the-destination-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a destination Amazon S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html) | Cloud administrator |

### Copy data to the destination Amazon S3 bucket
<a name="copy-data-to-the-destination-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the AWS CLI with the newly created user credentials. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html) | AWS DevOps |
| Assume the Amazon S3 migration role. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html)For more information, see [How do I use the AWS CLI to assume an IAM role?](https://repost.aws/knowledge-center/iam-assume-role-cli) | AWS administrator |
| Copy and synchronize data from the source bucket to the destination bucket. | When you have assumed the role `S3MigrationRole` you can copy the data using the [copy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html) (`cp`) or [synchronize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html) (`sync`) command.<br />Copy:<pre>aws s3 cp s3://amazon-s3-demo-source-bucket/ \<br />    s3://amazon-s3-demo-destination-bucket/ \<br />    --recursive --source-region SOURCE-REGION-NAME --region DESTINATION-REGION-NAME</pre><br />Synchronize:<pre>aws s3 sync s3://amazon-s3-demo-source-bucket/ \<br />    s3://amazon-s3-demo-destination-bucket/ \<br />    --source-region SOURCE-REGION-NAME --region DESTINATION-REGION-NAME</pre> | Cloud administrator |

## Troubleshooting
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| An error occurred (`AccessDenied`) when calling the `ListObjects` operation | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli.html) |

## Related resources
<a name="copy-data-from-an-s3-bucket-to-another-account-and-region-by-using-the-aws-cli-resources"></a>
+ [Creating an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) (Amazon S3 documentation)
+ [Amazon S3 bucket policies and user policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html) (Amazon S3 documentation)
+ [IAM identities (users, groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html?icmpid=docs_iam_console) (IAM documentation)
+ [cp command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html) (AWS CLI documentation)
+ [sync command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html) (AWS CLI documentation)
