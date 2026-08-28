---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/cloudtrail.html
---

# AWS CloudTrail
<a name="cloudtrail"></a>

[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service are recorded as *events* in CloudTrail. Events can include actions taken in the AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDKs and APIs.

## Using CloudTrail
<a name="using-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can easily view recent events in the CloudTrail console by going to **Event history**.

For an ongoing record of activity and events in your AWS account, you create a *trail*. You can create trails for a single AWS Region or for all Regions. Trails record the log files in each Region, and CloudTrail can deliver the log files to a single, consolidated Amazon Simple Storage Service (Amazon S3) bucket.

You can configure multiple trails differently so that the trails process and log only the events that you specify. This can be useful when you want to triage events that occur in your AWS account with events that occur in your application.

|
|
| Note CloudTrail has a validation feature that you can use to determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. For more information about this feature and how to enable it, see [Validating CloudTrail log file integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) (CloudTrail documentation). |
| --- |

## Use cases for CloudTrail
<a name="cloudtrail-use-cases"></a>
+ **Compliance aid** – Using CloudTrail can help you comply with internal policies and regulatory standards by providing a history of events in your AWS account.
+ **Security analysis** – You can perform security analysis and detect user behavior patterns by ingesting CloudTrail log files into a log management and analytics solutions, such as CloudWatch Logs, Amazon EventBridge, Amazon Athena, Amazon OpenSearch Service, or another third-party solution.
+ **Data exfiltration** – You can detect data exfiltration by collecting activity data on Amazon S3 objects through object-level API events recorded in CloudTrail. After the activity data is collected, you can use other AWS services, such as EventBridge and AWS Lambda, to trigger an automatic response.
+ **Operational issue troubleshooting **– You can troubleshoot operational issues by using the CloudTrail log files. For example, you can quickly identify the most recent changes made to the resources in your environment, including creation, modification, and deletion of AWS resources.

## Best practices for CloudTrail
<a name="cloudtrail-best-practices"></a>
+ Enable CloudTrail in all AWS Regions.
+ Enable log file integrity validation.
+ Encrypt logs.
+ Ingest CloudTrail log files into CloudWatch Logs.
+ Centralize logs from all AWS accounts and Regions.
+ Apply lifecycle policies to S3 buckets containing log files.
+ Prevent users from being able to turn off logging in CloudTrail. Apply the following [service control policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCP) in AWS Organizations. This SCP sets an explicit deny rule for the `StopLogging` and `DeleteTrail` actions across the organization.

  ```
  {
  "Version": "2012-10-17",
  "Statement":
         [
                   { "Action":
                       [
                       "cloudtrail:StopLogging",
                       "cloudtrail:DeleteTrail"
                        ],
                        "Resource": "*",
                        "Effect": "Deny"
                    }
          ]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
