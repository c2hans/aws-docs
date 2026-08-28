---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-7.html
---

# Theme 7: Centralise logging and monitoring
<a name="theme-7"></a>

**Essential Eight strategies covered**: Application control, patch applications, restrict administrative privileges, multi-factor authentication

AWS provides tools and features that enable you to see what's happening in your AWS environment. These include:
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you monitor your AWS deployments by creating a historical trail of AWS API calls for your account, including API calls made through the AWS Management Console, AWS SDKs, and command line tools. For services that support CloudTrail, you can also identify which users and accounts called the service's API, the source IP address the calls were made from, and when the calls occurred.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyses and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment. GuardDuty integrates with Amazon EventBridge in order to start an automated response or notify a human.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your AWSenvironment against security industry standards and best practices.

These tools and features are designed to increase visibility and help you address issues before they negatively affect your environment. This helps you improve your organization's security posture in the cloud and reduces the risk profile of your environment.

## Related best practices in the AWS Well-Architected Framework
<a name="theme-7-best-practices"></a>
+ [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html)
+ [SEC04-BP02 Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_detect_investigate_events_logs.html)

## Implementing this theme
<a name="theme-7-implementation"></a>

### Enable logging
<a name="enable-logging.98faa189-2782-50c0-99b5-df3cc3a1edaa"></a>
+ [Use the CloudWatch agent to publish system-level logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
+ [Set up alerts for GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html#setup-sns)
+ [Create an organization trail in CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)

### Implement logging security best practices
<a name="implement-logging-security-best-practices.419632bd-70d0-5f1c-b623-f49a11dcb455"></a>
+ [Implement CloudTrail security best practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html)
+ [Use SCPs to prevent users from disabling security services](https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/) (AWS blog post)
+ [Encrypt log data in CloudWatch Logs by using AWS Key Management Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html)

### Centralise logs
<a name="centralise-logs.7bd31369-53e6-5e6e-84e0-dc9089f91291"></a>
+ [Receive CloudTrail logs from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)
+ [Send logs to a log archive account](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/security-ou-and-accounts.html#log-archive-account)
+ [Centralise CloudWatch Logs in an account for auditing and analysis](https://aws.amazon.com/blogs/architecture/stream-amazon-cloudwatch-logs-to-a-centralized-account-for-audit-and-analysis/) (AWS blog post)
+ [Centralize management of Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)
+ [Create an organisation-wide aggregator in AWS Config](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) (AWS blog post)
+ [Centralise management of Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html)
+ [Centralise management of GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)
+ [Consider using Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)

## Monitoring this theme
<a name="theme-7-monitoring"></a>

### Implement mechanisms
<a name="implement-mechanisms.445daf92-6204-5915-870c-bffd2f8b2829"></a>
+ Establish a mechanism to review log findings
+ Establish a mechanism to review Security Hub CSPM findings
+ Establish a mechanism to respond to GuardDuty findings

### Implement the following AWS Config rules
<a name="implement-the-following-9999999999999999cc--rules.0f0d8bb3-dd79-59d0-96ce-89ee17af0bf2"></a>
+ `CLOUDTRAIL_SECURITY_TRAIL_ENABLED`
+ `GUARDDUTY_ENABLED_CENTRALIZED`
+ `SECURITYHUB_ENABLED`
+ `ACCOUNT_PART_OF_ORGANIZATIONS`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
