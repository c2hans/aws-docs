---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-vpc-flow-logs-for-centralization-across-aws-accounts.html
---

# Configure VPC Flow Logs for centralization across AWS accounts
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts"></a>

*Benjamin Morris and Aman Kaur Gandhi, Amazon Web Services*

## Summary
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-summary"></a>

In an AWS virtual private cloud (VPC), the VPC Flow Logs feature can provide useful data for operational and security troubleshooting. However, there are limitations on using VPC Flow Logs in a multi-account environment. Specifically, cross-account flow logs from Amazon CloudWatch Logs are not supported. Instead, you can centralize the logs by configuring an Amazon Simple Storage Service (Amazon S3) bucket with the appropriate bucket policy.

**Note**
This pattern discusses the requirements for sending flow logs to a centralized location. However, if you also want logs to be available locally in member accounts, you can create multiple flow logs for each VPC. Users who don’t have access to the Log Archive account can see traffic logs for troubleshooting. Alternatively, you can configure a single flow log for each VPC that sends logs to CloudWatch Logs. You can then use an Amazon Data Firehose subscription filter to forward the logs to an S3 bucket. For more information, see the [Related resources](#configure-vpc-flow-logs-for-centralization-across-aws-accounts-resources) section.

## Prerequisites and limitations
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An AWS Organizations organization with an account that is used to centralize logs (for example, Log Archive)

**Limitations **

If you use the AWS Key Management Service (AWS KMS) managed key `aws/s3` to encrypt your central bucket, it won’t receive logs from a different account. Instead, you will see an `Unsuccessful` error code 400 with a message such as `"LogDestination: <bucketName> is undeliverable"` for your given `ResourceId`. This is because an account’s AWS managed keys can’t be shared across accounts. The solution is to use either Amazon S3 managed encryption (SSE-S3) or an AWS KMS customer managed key that you can share with member accounts.

## Architecture
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-architecture"></a>

**Target architecture**

In the following diagram, two flow logs are deployed for each VPC. One sends logs to a local CloudWatch Logs group. The other sends logs to an S3 bucket in a centralized logging account. The bucket policy permits the log delivery service to write logs to the bucket.

**Note**
As of November 2023, AWS now supports the [aws:SourceOrgID condition key](https://aws.amazon.com/about-aws/whats-new/2023/11/organization-wide-iam-condition-keys-restrict-aws-service-to-service-requests/). This condition allows you to deny writing to the centralized bucket for accounts outside of your AWS Organizations organization.

![From each VPC one flow log sends logs to CloudWatch and another sends logs to the S3 bucket.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/718c29f4-a035-47ab-9c58-bd7d5c1ca77e/images/0b502d82-a6ce-4832-b854-99181d2ed834.png)

**Automation and scale**

Each VPC is configured to send logs to the S3 bucket in the central logging account. Use one of the following automation solutions to help ensure that flow logs are configured appropriately:
+ [CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
+ [AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/taf-account-provisioning.html)
+ [An AWS Config rule with remediation](https://aws.amazon.com/blogs/mt/how-to-enable-vpc-flow-logs-automatically-using-aws-config-rules/)

## Tools
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-tools"></a>

**Tools**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. This pattern uses the [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) feature to capture information about the IP traffic going to and from network interfaces in your VPC.

## Best practices
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-best-practices"></a>

Using infrastructure as code (IaC) can greatly simplify the VPC Flow Logs deployment process. Abstracting your VPC deployment definitions to include a flow log resource construct will deploy your VPCs with flow logs automatically. This is demonstrated in the next section.

**Centralized flow logs**

Example syntax for adding centralized flow logs to a VPC module in HashiCorp Terraform: This code creates a flow log that sends logs from a VPC to a centralized S3 bucket. Note that this pattern doesn’t cover the creation of the S3 bucket. For recommended bucket policy statements, see the [Additional information](#configure-vpc-flow-logs-for-centralization-across-aws-accounts-additional) section.

```
variable "vpc_id" { type = string }
locals { custom_log_format_v5 = "$${version} $${account-id} $${interface-id} $${srcaddr} $${dstaddr} $${srcport} $${dstport} $${protocol} $${packets} $${bytes} $${start} $${end} $${action} $${log-status} $${vpc-id} $${subnet-id} $${instance-id} $${tcp-flags} $${type} $${pkt-srcaddr} $${pkt-dstaddr} $${region} $${az-id} $${sublocation-type} $${sublocation-id} $${pkt-src-aws-service} $${pkt-dst-aws-service} $${flow-direction} $${traffic-path}" }
resource "aws_flow_log" "centralized_flow_log" {
  log_destination      = "arn:aws:s3:::centralized-vpc-flow-logs-<log_archive_account_id>" # Optionally, a prefix can be added after the ARN.
  log_destination_type = "s3"
  traffic_type         = "ALL"
  vpc_id               = var.vpc_id
  log_format           = local.custom_log_format_v5 # If you want fields from VPC Flow Logs v3+, you will need to create a custom log format.
}
```

For more information about the custom log format, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-custom).

**Local flow logs**

Example syntax for adding local flow logs to a VPC module in Terraform with required permissions: This code creates a flow log that sends logs from a VPC to a local CloudWatch Logs group.

```
data "aws_region" "current" {}
variable "vpc_id" { type = string }
resource "aws_iam_role" "local_flow_log_role" {
  name = "flow-logs-policy-${var.vpc_id}"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "vpc-flow-logs.amazonaws.com"},
      "Action": "sts:AssumeRole"
  }]
}
EOF
}
resource "aws_iam_role_policy" "logs_permissions" {
  name = "flow-logs-policy-${var.vpc_id}"
  role = aws_iam_role.local_flow_log_role.id
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
      "Action": ["logs:CreateLog*", "logs:PutLogEvents", "logs:DescribeLog*", "logs:DeleteLogDelivery"],
      "Effect": "Allow",
      "Resource": "arn:aws:logs:${data.aws_region.current.name}:*:log-group:vpc-flow-logs*"
  }]
}
EOF
}
resource "aws_cloudwatch_log_group" "local_flow_logs" {
  name              = "vpc-flow-logs/${var.vpc_id}"
  retention_in_days = 30
}
resource "aws_flow_log" "local_flow_log" {
  iam_role_arn    = aws_iam_role.local_flow_log_role.arn
  log_destination = aws_cloudwatch_log_group.local_flow_logs.arn
  traffic_type    = "ALL"
  vpc_id          = var.vpc_id
}
```

## Epics
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-epics"></a>

### Deploy VPC Flow Logs infrastructure
<a name="deploy-vpc-flow-logs-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine the encryption strategy and create the policy for the central S3 bucket. | The central bucket doesn’t support the AWS KMS `aws/s3` key, so you must use either SSE-S3 or an AWS KMS customer managed key. If you use an AWS KMS key, the key policy must allow member accounts to use the key. | Compliance |
| Create the central flow log bucket. | Create the central bucket that flow logs will be sent to, and apply the encryption strategy that you chose in the previous step. This should be in a Log Archive or similarly purposed account.<br />Obtain the bucket policy from the [Additional information](#configure-vpc-flow-logs-for-centralization-across-aws-accounts-additional) section, and apply it to your central bucket after you update placeholders with your environment specific values. | General AWS |
| Configure VPC Flow Logs to send logs to the central flow log bucket. | Add flow logs to each VPC that you want to gather data from. The most scalable way to do this is to use IaC tools such as AFT or AWS Cloud Development Kit (AWS CDK). For example, you can create a Terraform module that deploys a VPC alongside a flow log. If necessary, you add the flow logs manually. | Network administrator |
| Configure VPC Flow Logs to send to local CloudWatch Logs. | (Optional) If you want flow logs to be visible in the accounts where the logs are being generated, create another flow log to send data to CloudWatch Logs in the local account. Alternatively, you can send the data to an account-specific S3 bucket in the local account. | General AWS |

## Related resources
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-resources"></a>
+ [How to Facilitate Data Analysis and Fulfill Security Requirements by Using Centralized Flow Log Data](https://aws.amazon.com/blogs/security/how-to-facilitate-data-analysis-and-fulfill-security-requirements-by-using-centralized-flow-log-data/) (AWS blog post)
+ [How to enable VPC Flow Logs automatically using AWS Config rules](https://aws.amazon.com/blogs/mt/how-to-enable-vpc-flow-logs-automatically-using-aws-config-rules/) (AWS blog post)

## Additional information
<a name="configure-vpc-flow-logs-for-centralization-across-aws-accounts-additional"></a>

**Bucket policy**

This example of a bucket policy can be applied to your central S3 bucket for flow logs, after you add values for placeholder names.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AWSLogDeliveryWrite",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<BUCKET_NAME>/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control",
                    "aws:SourceOrgID": "<ORG_ID>"
                }
            }
        },
        {
            "Sid": "AWSLogDeliveryCheck",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::<BUCKET_NAME>",
            "Condition": {
                "StringEquals": {
                    "aws:SourceOrgID": "<ORG_ID>"
                }
            }
        },
        {
            "Sid": "DenyUnencryptedTraffic",
            "Effect": "Deny",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::<BUCKET_NAME>/*",
                "arn:aws:s3:::<BUCKET_NAME>"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "false"
                }
            }
        }
    ]
}
```
