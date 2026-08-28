---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/logging-and-monitoring-controls.html
---

# Security control recommendations for logging and monitoring
<a name="logging-and-monitoring-controls"></a>

Logging and monitoring are important aspects of threat detection. Threat detection is one of the security perspective capabilities in the [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/). By using log data, your organization can monitor your environment to understand and identify potential security misconfigurations, threats, and unexpected behaviors. Understanding potential threats can help your organization prioritize security controls, and effective threat detection can help you respond to threats more quickly.

Controls in this section:
+ [Configure at least one multi-Region trail in CloudTrail](#multi-region-trail)
+ [Configure logging at the service and application level](#logging-level)
+ [Establish a centralized location for analyzing logs and responding to security events](#centralized-logging)
+ [Prevent unauthorized access to S3 buckets that contain CloudTrail log files](#access-to-log-files)
+ [Configure alerts for changes to security groups or network ACLs](#alert-sec-group-changes)
+ [Configure alerts for CloudWatch alarms that enter the ALARM state](#alert-cloudwatch-alarms)

## Configure at least one multi-Region trail in CloudTrail
<a name="multi-region-trail"></a>

[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDKs and APIs. This event history helps you analyze your security posture, track resource changes, and audit compliance.

For an ongoing record of events in your AWS account, you must create a trail. Each trail should be configured to log events in all AWS Regions. By logging events in all AWS Regions, you ensure that all events that occur in your AWS account are logged, regardless of which AWS Region they occurred in. A multi-Region trail ensures that [global service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events) are logged.

For more information, see the following resources:
+ [CloudTrail detective security best practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html#best-practices-security-detective) in the CloudTrail documentation
+ [Converting a trail that applies to one Region to apply to all Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.html#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-convert) in the CloudTrail documentation
+ [Enabling and disabling global service event logging](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-update-trail.html#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-gses) in the CloudTrail documentation

## Configure logging at the service and application level
<a name="logging-level"></a>

The AWS Well-Architected Framework recommends that you retain security event logs from services and applications. This is a fundamental principle of security for audit, investigations, and operational use cases. Service and application log retention is a common security requirement that is driven by governance, risk, and compliance (GRC) standards, policies, and procedures.

Security operations teams rely on logs and search tools to discover potential events of interest that might indicate unauthorized activity or unintentional change. You can enable logging for different services, depending on the use case. For example, you can log Amazon S3 bucket access, AWS WAF web ACL traffic, Amazon API Gateway traffic at the network layer, or Amazon CloudFront distributions.

For more information, see the following resources:
+ [Stream Amazon CloudWatch Logs to a centralized account for audit and analysis](https://aws.amazon.com/blogs/architecture/stream-amazon-cloudwatch-logs-to-a-centralized-account-for-audit-and-analysis/) in the AWS Architecture Blog
+ [Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) in the AWS Well-Architected Framework

## Establish a centralized location for analyzing logs and responding to security events
<a name="centralized-logging"></a>

Manually analyzing logs and processing information is insufficient to keep up with the volume of information associated with complex architectures. Analysis and reporting alone don't facilitate event assignment to the correct resource in a timely fashion. The AWS Well-Architected Framework recommends that you integrate AWS security events and findings into a notification and workflow system, such as a ticketing, bug, or security information and event management (SIEM) system. These systems help you assign, route, and manage security events.

For more information, see the following resources:
+ [Analyze logs, findings, and metrics centrally](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_analyze_all.html) in the AWS Well-Architected Framework
+ [Analyze security, compliance, and operational activity using CloudTrail and Amazon Athena](https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/) in the AWS Security Blog
+ [AWS Partners that provide threat detection and response services](https://partners.amazonaws.com/search/partners?facets=Use%20Case%20%3A%20Security%20%3A%20Threat%20Detection%20and%20Response) in the AWS Partners Portfolio

## Prevent unauthorized access to S3 buckets that contain CloudTrail log files
<a name="access-to-log-files"></a>

By default, CloudTrail log files are stored in Amazon S3 buckets. It is a security best practice to prevent unauthorized access to any Amazon S3 bucket that contains CloudTrail log files. This helps you maintain the integrity, completeness, and availability of these logs, which is crucial for forensic and auditing purposes. If you want to log data events for S3 buckets that contain CloudTrail log files, you can create a CloudTrail trail for this purpose.

For more information, see the following resources:
+ [Configuring block public access settings for your S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html) in the Amazon S3 documentation
+ [CloudTrail preventative security best practices in the CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html#best-practices-security-preventative) documentation
+ [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the CloudTrail documentation

## Configure alerts for changes to security groups or network ACLs
<a name="alert-sec-group-changes"></a>

A *security group *in Amazon Virtual Private Cloud (Amazon VPC) controls the traffic that is allowed to reach and leave the resources that it is associated with. A *network access control list (ACL)* allows or denies specific inbound or outbound traffic at the subnet level of the VPC. These resources are critical to managing access in your AWS environment.

Create and configure an Amazon CloudWatch alarm that notifies you if a security group or network ACL configuration changes. Configure this alarm to alert you every time an AWS API call is performed to update security groups. You can also use services, such as [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html), to automatically respond to these types of security events.

For more information, see the following resources:
+ [Automatically revert and receive notifications about changes to your Amazon VPC security groups](https://aws.amazon.com/blogs/security/how-to-automatically-revert-and-receive-notifications-about-changes-to-your-amazon-vpc-security-groups/) in the AWS Security Blog
+ [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the CloudWatch documentation
+ [Implement actionable security events](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_actionable_events.html) in the AWS Well-Architected Framework
+ [Automate response to events](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_auto_response.html) in the AWS Well-Architected Framework

## Configure alerts for CloudWatch alarms that enter the ALARM state
<a name="alert-cloudwatch-alarms"></a>

In CloudWatch, you can specify what actions an alarm takes when it changes state between the `OK`, `ALARM`, and `INSUFFICIENT_DATA` states. The most common type of alarm action is to notify one or more people by sending a message to an Amazon Simple Notification Service (Amazon SNS) topic. You can also configure alarms to create [OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html) or [incidents](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html) in AWS Systems Manager.

We recommend that you activate alarm actions to automatically alert if a monitored metric is outside of the defined threshold. Monitoring alarms helps you identify unusual activities and quickly respond to security and operational issues.

For more information, see the following resources:
+ [Implement actionable security events](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_actionable_events.html) in the AWS Well-Architected Framework
+ [Alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions) in the CloudWatch documentation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
