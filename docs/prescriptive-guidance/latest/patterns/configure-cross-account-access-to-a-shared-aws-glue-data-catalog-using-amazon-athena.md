---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena.html
---

# Configure cross-account access to a shared AWS Glue Data Catalog using Amazon Athena
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena"></a>

*Denis Avdonin, Amazon Web Services*

## Summary
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-summary"></a>

This pattern provides step-by-step instructions, including AWS Identity and Access Management (IAM) policy samples, to configure cross-account sharing of a dataset stored in an Amazon Simple Storage Service (Amazon S3) bucket by using the AWS Glue Data Catalog. You can store the dataset in an S3 bucket. The metadata is collected by an AWS Glue crawler and put into the AWS Glue Data Catalog. The S3 bucket and the AWS Glue Data Catalog reside in an AWS account referred to as the *data account*. You can provide access to IAM principals in another AWS account referred to as the *consumer account*. Users can query the data in the consumer account by using the Amazon Athena serverless query engine.

## Prerequisites and limitations
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-prereqs"></a>

**Prerequisites**
+ Two active [AWS accounts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)
+ An [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in one of the AWS accounts
+ [Athena engine version 2](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference.html#engine-versions-reference-0002)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) (or [AWS CloudShell](https://aws.amazon.com/cloudshell/) for running AWS CLI commands)

**Product versions**

This pattern works with [Athena engine version 2](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference-0002.html) and [Athena engine version 3](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference-0003.html) only. We recommend that you upgrade to Athena engine version 3. If you can’t upgrade from Athena engine version 1 to Athena engine version 3, follow the approach discussed in [Cross-account AWS Glue Data Catalog access with Amazon Athena](https://aws.amazon.com/blogs/big-data/cross-account-aws-glue-data-catalog-access-with-amazon-athena/) in the AWS Big Data Blog.

## Architecture
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-architecture"></a>

**Target technology stack**
+ Amazon Athena
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Glue
+ AWS Identity and Access Management (IAM)
+ AWS Key Management Service (AWS KMS)

The following diagram shows an architecture that uses IAM permissions to share data in an S3 bucket in one AWS account (data account) with another AWS account (consumer account) through the AWS Glue Data Catalog.

![Sharing a dataset in an S3 bucket between a data account and a consumer account by using the AWS Glue Data Catalog.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4ee1d6f5-f8e1-4acb-8a9c-7601c832a87d/images/e73a2b47-c0b1-49f1-be66-9c563c11c9f9.png)

The diagram shows the following workflow:

1. The S3 bucket policy in the data account grants permissions to an IAM role in the consumer account and to the AWS Glue crawler service role in the data account.

1. The AWS KMS key policy in the data account grants permissions to the IAM role in the consumer account and to the AWS Glue crawler service role in the data account.

1. The AWS Glue crawler in the data account discovers the schema of the data that’s stored in the S3 bucket.

1. The resource policy of the AWS Glue Data Catalog in the data account grants access to the IAM role in the consumer account.

1. A user creates a named catalog reference in the consumer account by using an AWS CLI command.

1. An IAM policy grants an IAM role in the consumer account access to resources in the data account. The IAM role’s trust policy allows users in the consumer account to assume the IAM role.

1. A user in the consumer account assumes the IAM role and accesses objects in the data catalog by using SQL queries.

1.  The Athena serverless engine runs the SQL queries.

**Note**
[IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) recommend that you grant permissions to an IAM role and use [identity federation](https://aws.amazon.com/identity/federation/).

## Tools
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-tools"></a>
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to protect your data.

## Epics
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-epics"></a>

### Set up permissions in the data account
<a name="set-up-permissions-in-the-data-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Grant access to data in the S3 bucket. | [Create an S3 bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/add-bucket-policy.html) based on the following template and assign the policy to the bucket where the data is stored.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "AWS": [<br />                     "arn:aws:iam::<consumer account id>:role/<role name>",<br />                     "arn:aws:iam::<data account id>:role/service-role/AWSGlueServiceRole-data-bucket-crawler"<br />                ]<br />            },<br />            "Action": "s3:GetObject",<br />            "Resource": "arn:aws:s3:::data-bucket/*"<br />        },<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "AWS": [<br />                      "arn:aws:iam::<consumer account id>:role/<role name>",<br />                      "arn:aws:iam::<data account id>:role/service-role/AWSGlueServiceRole-data-bucket-crawler"<br />                ]<br />            },<br />            "Action": "s3:ListBucket",<br />            "Resource": "arn:aws:s3:::data-bucket"<br />        }<br />    ]<br />}</pre><br />The bucket policy grants permissions to the IAM role in the consumer account and to the AWS Glue crawler service role in the data account. | Cloud administrator |
| (If required) Grant access to the data encryption key. | If the S3 bucket is encrypted by an AWS KMS key, grant `kms:Decrypt` permission on the key to the IAM role in the consumer account and to the AWS Glue crawler service role in the data account.<br />Update the [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) with the following statement:<pre>{<br />    "Effect": "Allow",<br />    "Principal": {<br />        "AWS": [<br />            "arn:aws:iam::<consumer account id>:role/<role name>",<br />            "arn:aws:iam::<data account id>:role/service-role/AWSGlueServiceRole-data-bucket-crawler"<br />        ]<br />    },<br />    "Action": "kms:Decrypt",<br />    "Resource": "arn:aws:kms:<region>:<data account id>:key/<key id>"<br />}</pre> | Cloud administrator |
| Grant the crawler access to the data. | Attach the following IAM policy to the crawler’s service role:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": "s3:GetObject",<br />            "Resource": "arn:aws:s3:::data-bucket/*"<br />        },<br />        {<br />            "Effect": "Allow",<br />            "Action": "s3:ListBucket",<br />            "Resource": "arn:aws:s3:::data-bucket"<br />        }<br />    ]<br />} </pre> | Cloud administrator |
| (If required) Grant the crawler access to the data encryption key. | If the S3 bucket is encrypted by an AWS KMS key, grant `kms:Decrypt` permission on the key to the crawler’s service role by attaching the following policy to it:<pre>{<br />    "Effect": "Allow",<br />    "Action": "kms:Decrypt",<br />    "Resource": "arn:aws:kms:<region>:<data account id>:key/<key id>"<br />}</pre> | Cloud administrator |
| Grant the IAM role in the consumer account and the crawler access to the data catalog. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena.html)<pre>{<br />    "Version" : "2012-10-17",<br />    "Statement" : [ <br />        {<br />            "Effect" : "Allow",<br />            "Principal" : {<br />                "AWS" : [<br />                     "arn:aws:iam::<consumer account id>:role/<role name>",<br />                    "arn:aws:iam::<data account id>:role/service-role/AWSGlueServiceRole-data-bucket-crawler"<br />                ]<br />            },<br />            "Action" : "glue:*",<br />            "Resource" : [ <br />                 "arn:aws:glue:<region>:<data account id>:catalog", <br />                 "arn:aws:glue:<region>:<data account id>:database/*", <br />                 "arn:aws:glue:<region>:<data account id>:table/*" <br />            ]<br />        } <br />    ]<br />}</pre>This policy allows all AWS Glue actions on all databases and tables in the data account. You can customize the policy to grant only required permissions to the consumer principals. For example, you can provide read-only access to specific tables or views in a database. | Cloud administrator |

### Access data from the consumer account
<a name="access-data-from-the-consumer-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a named reference for the data catalog. | To create a named data catalog reference, use [CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html) or a locally installed AWS CLI to run the following command:<pre>aws athena create-data-catalog --name <shared catalog name> --type GLUE --parameters catalog-id=<data account id></pre> | Cloud administrator |
| Grant the IAM role in the consumer account access to the data. | Attach the following policy to the IAM role in the consumer account to grant the role cross-account access to the data:<pre>{<br />     "Version": "2012-10-17",		 	 	 <br />     "Statement": [<br />        {<br />             "Effect": "Allow",<br />             "Action": "s3:GetObject",<br />             "Resource": "arn:aws:s3:::data-bucket/*"<br />        },<br />        {<br />             "Effect": "Allow",<br />             "Action": "s3:ListBucket",<br />             "Resource": "arn:aws:s3:::data-bucket"<br />        },<br />        {<br />            "Effect": "Allow",<br />            "Action": "glue:*",<br />            "Resource": [<br />                 "arn:aws:glue:<region>:<data account id>:catalog",<br />                 "arn:aws:glue:<region>:<data account id>:database/*",<br />                 "arn:aws:glue:<region>:<data account id>:table/*"<br />            ]<br />        }<br />    ]<br />}</pre><br />Next, use the following template to specify what users can accept the IAM role in its trust policy:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />       {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "AWS": "arn:aws:iam::<consumer account id>:user/<IAM user>"<br />            },<br />            "Action": "sts:AssumeRole"<br />        }<br />    ]<br />}</pre><br />Finally, grant user permissions to assume the IAM role by attaching the same policy to the user group they belong to. | Cloud administrator |
| (If required) Grant the IAM role in the consumer account access to the data encryption key. | If the S3 bucket is encrypted by an AWS KMS key, grant `kms:Decrypt` permission on the key to the IAM role in the consumer account by attaching the following policy to it:<pre>{<br />     "Effect": "Allow",<br />     "Action": "kms:Decrypt",<br />     "Resource": "arn:aws:kms:<region>:<data account id>:key/<key id>"<br />}</pre> | Cloud administrator |
| Switch to the IAM role in the consumer account to access data. | As a data consumer, [switch to the IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) to access data in the data account. | Data consumer |
| Access the data. | Query data using Athena. For example, open the Athena query editor and run the following query:<pre>SELECT *<br />  FROM <shared catalog name>.<database name>.<table name></pre><br />Instead of using a named catalog reference, you can also refer to the catalog by its Amazon Resource Name (ARN).If you use a dynamic catalog reference in a query or view, surround the reference with escaped double quotation marks (\\"). For example:<pre>SELECT * <br />  FROM \"glue:arn:aws:glue:<region>:<data account id>:catalog\".<database name>.<table name></pre><br />For more information, see [Cross-account access to AWS Glue data catalogs](https://docs.aws.amazon.com/athena/latest/ug/security-iam-cross-account-glue-catalog-access.html) in the Amazon Athena User Guide. | Data consumer |

## Related resources
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-resources"></a>
+ [Cross-account access to AWS Glue data catalogs](https://docs.aws.amazon.com/athena/latest/ug/security-iam-cross-account-glue-catalog-access.html) (Athena documentation)
+ [(AWS CLI) create-data-catalog](https://docs.aws.amazon.com/cli/latest/reference/athena/create-data-catalog.html) (AWS CLI Command Reference)
+ [Cross-account AWS Glue Data Catalog access with Amazon Athena](https://aws.amazon.com/blogs/big-data/cross-account-aws-glue-data-catalog-access-with-amazon-athena/) (AWS Big Data Blog)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)

## Additional information
<a name="configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena-additional"></a>

**Using Lake Formation as an alternative for cross-account sharing**

You can also use AWS Lake Formation to share access to AWS Glue catalog objects across accounts. Lake Formation provides fine-grained access control at the column and row level, tag-based access control, governed tables for ACID transactions, and other functionality. Although Lake Formation is well-integrated with Athena, it does require additional configuration compared to this pattern’s IAM-only approach. We recommend that you consider the decision to use Lake Formation or IAM-only access controls within the wider context of your overall solution architecture. Considerations include what other services are involved and how they integrate with both approaches.
