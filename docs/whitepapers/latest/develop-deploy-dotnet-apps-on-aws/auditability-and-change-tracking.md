---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/auditability-and-change-tracking.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Auditability and Change Tracking
<a name="auditability-and-change-tracking"></a>

Effective DevOps requires that teams have a transparent view of changes made to the services and infrastructure running their applications. [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) helps provide this transparency by monitoring and logging AWS API calls, effectively recording actions taken by users, roles, or AWS Services as CloudTrail events. These events include actions in the AWS Management Console, AWS CLI, and AWS SDKs and APIs, allowing changes to be audited.

You can view and monitor CloudTrail events in the CloudTrail console, and you can store log files in Amazon S3 or send them to CloudWatch Logs. You can use CloudTrail events sent to CloudWatch to trigger alarms based on metrics, and to trigger CloudWatch events, allowing automated actions to be executed when specific API calls are logged. This combination of using CloudTrail and CloudWatch can be a highly effective approach for creating auto-healing scripts for your environment, or can form part of an advanced infrastructure automation strategy.

[AWS Config](https://aws.amazon.com/config/) is a service that evaluates the configuration of your AWS resources, monitors configuration changes and compares them against desired configurations. AWS Config can send notifications of changes using Amazon SNS, or you can create automated responses using CloudWatch Events, and automated remediation using [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html).
