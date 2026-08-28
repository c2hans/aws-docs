---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/compliance-auditing-and-security-analytics.html
---

# Compliance Auditing and Security Analytics
<a name="compliance-auditing-and-security-analytics"></a>

With [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), you can continuously monitor AWS account activity. A history of the AWS API calls for your account is captured, including API calls made through the AWS Management Console, the AWS SDKs, the command line tools, and higher-level AWS services. You can identify which users and accounts called AWS APIs for services that support CloudTrail, the source IP address the calls were made from, and when the calls occurred. You can integrate CloudTrail into applications using the API, automate trail creation for your organization, check the status of your trails, and control how administrators enable and disable CloudTrail logging.

CloudTrail logs can be aggregated from multiple Regions and multiple AWS accounts into a single Amazon S3 bucket. AWS recommends that you write logs – especially AWS CloudTrail logs – to an Amazon S3 bucket with restricted access in an AWS account designated for logging (Log Archive). The permissions on the bucket should prevent deletion of the logs, and they should also be encrypted at rest using Server-Side Encryption with Amazon S3-managed encryption keys (SSES3) or AWS KMS–managed keys (SSE-KMS). CloudTrail log file integrity validation can be used to determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally hard to modify, delete, or forge CloudTrail log files without detection. You can use the AWS command line interface (AWS CLI) to validate the files in the location where CloudTrail delivered them.

CloudTrail logs aggregated in an Amazon S3 bucket can be analyzed for auditing purposes or for troubleshooting activities. Once the logs are centralized, you can integrate with Security Information and Event Management (SIEM) solutions or use AWS services, such as [Amazon Athena](https://aws.amazon.com/athena/) or [AWS CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html), to analyze them and visualize them using [Amazon Quick Sight](https://aws.amazon.com/quicksight/?trk=4dd09b97-0ecf-4d2f-a27e-0d59a256daad&sc_channel=ps&ef_id=EAIaIQobChMIl5O7lomUjgMVL5GDBx0eSBqtEAAYASAAEgJjSfD_BwE%3AG%3As&s_kwcid=AL%214422%213%21651541907449%21p%21%21g%21%21quicksight%2119836375763%21147081249837&gad_campaignid=19836375763&gbraid=0AAAAADjHtp_FE307xbjooo9BU1YMU8Di3&gclid=EAIaIQobChMIl5O7lomUjgMVL5GDBx0eSBqtEAAYASAAEgJjSfD_BwE&ams%23interactive-card-vertical%23pattern-data.filter=%257B%2522filters%2522%253A%255B%255D%257D) Dashboards. Once you have CloudTrail logs centralized, you can also use the same Log Archive account to centralize logs from other sources, such as CloudWatch Logs and AWS load balancers.

![AWS architecture diagram showing user interaction with various AWS services and resources.](http://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/images/cloudtrail-architecture.png)

*Figure 2 – Example architecture for compliance auditing and security analytics with AWS CloudTrail *

AWS CloudTrail logs can also trigger rules configured in [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html), the event-driven service that replaced Amazon CloudWatch Events. You can use these events to notify users or systems that an event has occurred, or for remediation actions. For example, if you want to monitor activities on your Amazon EC2 instances, you can create a CloudWatch Event rule. When a specific activity happens on the Amazon EC2 instance and the event is captured in the logs, the rule triggers an [AWS Lambda](https://aws.amazon.com/lambda/) function, which sends a notification email about the event to the administrator. (See Figure 3.) The email includes details such as when the event happened, which user performed the action, Amazon EC2 details, and more. The following diagram shows the architecture of the event notification.

![AWS CloudTrail logs triggering CloudWatch events, leading to Lambda function and SNS notification.](http://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/images/cloudtrail-event-notification.png)

*Figure 3 – Example of AWS CloudTrail event notification *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
