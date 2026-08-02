---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/auditing.html
---

# Auditing and alerting
<a name="auditing"></a>

The Audit account is tailored for auditors and security administrators. In this account, you can give auditors read-only access to all accounts in the organization, so they can conduct thorough reviews. Additionally, the Audit account can be the delegated administrator for several security services that monitor the accounts in the organization for threats and compliance.

Centralizing auditing and security services in a central AWS account offers numerous benefits, including:
+ It isolates security functions from production workloads, to help collectively ensure robust and efficient security, compliance, and resource management across the organization's AWS environment.
+ It simplifies visibility, security management, and incident response from one central place.
+ It provides cost efficiency by eliminating redundancies.
+ It enables automated remediations and alerts.

**Note**
When you set up alerts, you should also consider automating remediation actions by using AWS Config Rules, AWS Lambda functions, and AWS Systems Manager Automation documents.

The following table shows a recommended list of services to help manage and secure your landing zone. You should extend this table with additional monitoring solutions according to your landing zone requirements. For more guidance on security tooling you can include in the Audit account, see the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html).

|
|
| Type | Description | Monitoring setup | Notification setup |
| --- |--- |--- |--- |
| Control compliance notifications | Provides notifications when there is drift in AWS Control Tower control compliance. | AWS Control Tower has an `aws-controltower-AggregateSecurityNotifications` SNS topic in the Audit account. | You should set up notifications after you create the AWS Control Tower landing zone to ensure that you can catch controls that are not compliant and in need of remediation.<br />Note: You can [automatically remediate non-compliant resources by using AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html). |
| Threat detection (Amazon GuardDuty) | Monitors VPC Flow Logs, CloudTrail, and DNS logs to detect suspicious or unexpected behavior in the accounts (for example, backdoor access, trojan programs, or unauthorized access).<br />For more information, see the [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html). | We recommend that you set up and configure GuardDuty when you create the landing zone. | You should set up notifications after setting up GuardDuty to ensure that you receive alerts for potential threats to remediate.<br />Note: You can [integrate GuardDuty findings with AWS Security Hub CSPM](https://docs.aws.amazon.com/guardduty/latest/ug/securityhub-integration.html). |
| Security and compliance monitoring (AWS Security Hub CSPM) | Brings together security findings from multiple AWS services and third-party sources into a single centralized dashboard to help proactively identify and address security issues, vulnerabilities, and compliance concerns.<br />For more information, see the [AWS Security Hub CSPM documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). | We recommend that you set up and configure Security Hub CSPM when you create the landing zone. | You should set up notifications after setting up Security Hub CSPM to ensure that you receive alerts for potential vulnerabilities to remediate.<br />Note: You can [automate remediation in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html). |
| Root user activity | Sends notifications when an account is accessed by the root user through the AWS Management Console. | We recommend that you set up an Amazon CloudWatch Events rule to monitor the `userIdentity` element in CloudTrail for root logins. | If there is root user account activity, CloudWatch Events writes to an SNS topic.<br />For more information and an CloudFormation script that you can use to set up this monitoring, see [How do I create an EventBridge event rule to notify me that my AWS root user account was used?](https://repost.aws/knowledge-center/root-user-account-eventbridge-rule) in the AWS Knowledge Center. |
| Billing alerts | Sends billing alerts if the cost and usage of AWS services exceeds your budget threshold. | We recommend that you set up a monthly customized budget that specifies a threshold that can be tracked by [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html). | AWS Budgets generates an alert by using Amazon Simple Notification Service (Amazon SNS) if the budget threshold is exceeded.<br />You can use CloudFormation stacks and an CloudFormation template to set notifications at the organization or OU level. You can also choose to automatically apply this check to new accounts. For more information, see the [AWS::Budgets::Budget resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html) in the CloudFormation documentation. |

**Note**
You can configure Amazon SNS to send out security alerts from the services listed in the table. The alerts can be sent to either one centralized email (if you have one single security team responsible), or to multiple emails (if different parts of your security organization are responsible for different services).
