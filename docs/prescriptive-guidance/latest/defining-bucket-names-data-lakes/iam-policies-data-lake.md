---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/iam-policies-data-lake.html
---

# Mapping buckets to IAM policies
<a name="iam-policies-data-lake"></a>

We recommend that you map the data lake's Amazon Simple Storage Service (Amazon S3) buckets and paths to AWS Identity and Access Management (IAM) policies and roles. You use the bucket names or paths in the IAM policy or role name. The following table shows a sample Amazon S3 bucket name and a sample IAM policy that is used to access this bucket.

|
|
| Sample object path | Sample IAM policy |
| --- |--- |
| **Amazon S3 bucket name** – `<companyname>-raw-<aws_region>-<aws_accountid>-dev`<br />**Amazon S3 bucket path** – `nosql/us/customers/year=2020/month=03/day=01/table_customers_20210301.csv` | <pre>{<br />      "Version" : "2012-10-17",<br />      "Statement" : [<br />      {<br />      "Sid" : "s3-nosql-us-customers-get-list",<br />      "Effect" : "Allow",<br />      "Principal" : "*",<br />      "Action" : [<br />      "s3:GetObject",<br />      "s3:ListBucket"<br />      ],<br />      "Resource" : [<br />      "arn:aws:s3:::<companyname>-raw-<aws_region>-<aws_accountid>-dev/*"<br />      ]<br />      }<br />      ]<br />      }</pre> |

**Note**
This is a sample IAM policy that shows the recommended naming standard for Amazon S3 buckets. However, you should make sure that you correctly configure bucket policies according to your organization's policies and requirements.
