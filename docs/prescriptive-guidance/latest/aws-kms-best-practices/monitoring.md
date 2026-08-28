---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/monitoring.html
---

# Detection and monitoring best practices for AWS KMS
<a name="monitoring"></a>

Detection and monitoring are an important part of understanding the availability, state, and usage of your AWS Key Management Service (AWS KMS) keys. Monitoring helps maintain the security, reliability, availability, and performance of your AWS solutions. AWS provides several tools for monitoring your KMS keys and AWS KMS operations. This section describes how to configure and use these tools to gain greater visibility into your environment and monitor the usage of your KMS keys.

**This section discusses the following detection and monitoring topics:**
+ [Monitoring AWS KMS operations with AWS CloudTrail](#monitoring-cloudtrail)
+ [Monitoring access to KMS keys with IAM Access Analyzer](#monitoring-access-analyzer)
+ [Monitoring the encryption settings of other AWS services with AWS Config](#monitoring-config)
+ [Monitoring KMS keys with Amazon CloudWatch alarms](#monitoring-alarms)
+ [Automating responses with Amazon EventBridge](#monitoring-eventbridge)

## Monitoring AWS KMS operations with AWS CloudTrail
<a name="monitoring-cloudtrail"></a>

AWS KMS is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that can record all calls to AWS KMS by users, roles, and other AWS services. CloudTrail captures all API calls to AWS KMS as events, including calls from the AWS KMS console, AWS KMS APIs, AWS CloudFormation, the AWS Command Line Interface (AWS CLI), and AWS Tools for PowerShell.

CloudTrail logs all AWS KMS operations, including read-only operations, such as `ListAliases` and `GetKeyRotationStatus`. It also logs operations that manage KMS keys, such as `CreateKey` and `PutKeyPolicy, and cryptographic operations, such as GenerateDataKey` and `Decrypt`. It also logs internal operations that AWS KMS calls for you, such as `DeleteExpiredKeyMaterial`, `DeleteKey`, `SynchronizeMultiRegionKey`, and `RotateKey`.

CloudTrail is enabled on your AWS account when you create it. By default, the [Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management-event API activity in an AWS Region. To monitor or audit the usage of your KMS keys beyond the 90 days, we recommend [creating a CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) for your AWS account. If you have created an organization in AWS Organizations, you can [create an organization trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) or an [event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.html) that logs events for all AWS accounts in that organization.

After you establish a trail for your account or organization, you can use other AWS services to store, analyze, and automatically respond to events that are logged in the trail. For example, you can do the following:
+ You can set up Amazon CloudWatch alarms that notify you of certain events in the trail. For more information, see [Monitoring KMS keys with Amazon CloudWatch alarms](#monitoring-alarms) in this guide.
+ You can create Amazon EventBridge rules that automatically perform an action when an event occurs in the trail. For more information, see [Automating responses with Amazon EventBridge](#monitoring-eventbridge) in this guide.
+ You can use Amazon Security Lake to collect and store logs from multiple AWS services, including CloudTrail. For more information, see [Collecting data from AWS services in Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) in the Amazon Security Lake documentation.
+ To enhance your analysis of operational activity, you can query CloudTrail logs with Amazon Athena. For more information, see [Query AWS CloudTrail logs](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) in the Amazon Athena documentation.

For more information about monitoring AWS KMS operations with CloudTrail, see the following:
+ [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html)
+ [Examples of AWS KMS log entries](https://docs.aws.amazon.com/kms/latest/developerguide/understanding-kms-entries.html)
+ [Monitor KMS keys with Amazon EventBridge](https://docs.aws.amazon.com/kms/latest/developerguide/kms-events.html)
+ [CloudTrail integration with Amazon EventBridge](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-eventbridge)

## Monitoring access to KMS keys with IAM Access Analyzer
<a name="monitoring-access-analyzer"></a>

[AWS Identity and Access Management Access Analyzer (IAM Access Analyzer)](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) helps you identify the resources in your organization and accounts (such as KMS keys) that are shared with an external entity. This service can help you identify unintended or overly broad access to your resources and data, which is a security risk. IAM Access Analyzer identifies resources that are shared with external principals by using logic-based reasoning to analyze the resource-based policies in your AWS environment.

You can use IAM Access Analyzer to identify which external entities have access to your KMS keys. When you enable IAM Access Analyzer, you create an analyzer for an entire organization or for a target account. The organization or account you choose is known as the *zone of trust* for the analyzer. The analyzer monitors the supported resources within the zone of trust. Any access to resources by principals within the zone of trust is considered trusted.

For KMS keys, IAM Access Analyzer analyzes the [key policies and grants applied to a key](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html#access-analyzer-kms-key). It generates a finding if a key policy or grant allows an external entity to access the key. Use IAM Access Analyzer to determine if external entities have access to your KMS keys, and then verify whether those entities should have access.

For more information about using IAM Access Analyzer to monitor KMS key access, see the following:
+ [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
+ [IAM Access Analyzer resource types for external access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html)
+ [IAM Access Analyzer resource types: AWS KMS keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html#access-analyzer-kms-key)
+ [Findings for external and unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html)

## Monitoring the encryption settings of other AWS services with AWS Config
<a name="monitoring-config"></a>

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account. You can use AWS Config to verify that the AWS services that use your KMS keys have their encryption settings configured appropriately. For example, you can use the [encrypted-volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html) AWS Config rule to validate that your Amazon Elastic Block Store (Amazon EBS) volumes are encrypted.

AWS Config includes *managed rules* that help you quickly choose rules against which to assess your resources. Check AWS Config in your AWS Regions to determine if the managed rules you need are supported in that Region. Available managed rules include checks for configuration of Amazon Relational Database Service (Amazon RDS) snapshots, CloudTrail trail encryption, default encryption for Amazon Simple Storage Service (Amazon S3) buckets, Amazon DynamoDB table encryption, and more.

You can also create *custom rules* and apply your business logic to determine whether your resources are compliant with your requirements. Open source code for many managed rules is available in the [AWS Config Rules Repository](https://github.com/awslabs/aws-config-rules) on GitHub. These can be a useful starting point for developing your own custom rules.

When a resource is noncompliant with a rule, you can initiate responsive actions. AWS Config includes remediation actions that [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) carries out. For example, if you have applied the [cloud-trail-encryption-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html) rule and the rule returns a `NON_COMPLIANT` result, AWS Config can initiate an Automation document that remediates the problem by encrypting the CloudTrail logs for you.

AWS Config lets you proactively check for compliance with AWS Config rules before you provision resources. Applying rules in [proactive mode](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes) helps you evaluate the configurations of your cloud resources before they are created or updated. Applying rules in proactive mode as part of your deployment pipeline lets you test resource configurations before you deploy your resources.

You can also implement AWS Config rules as controls through [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). Security Hub CSPM offers security standards that you can apply to your AWS accounts. These standards help you assess your environment against recommend practices. The [AWS Foundational Security Best Practices](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) standard includes controls within the [protect control category](https://docs.aws.amazon.com/securityhub/latest/userguide/control-categories.html#control-category-protect) to verify that encryption at rest is configured and that KMS key policies follow recommended practices.

For more information about using AWS Config to monitor the encryption settings in AWS services, see the following:
+ [Getting started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html)
+ [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html)
+ [AWS Config custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html)
+ [Remediating noncompliant resources with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)

## Monitoring KMS keys with Amazon CloudWatch alarms
<a name="monitoring-alarms"></a>

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track *metrics*, which are variables that you can measure.

The expiration of imported key material, or the deletion of a key, are potentially catastrophic events if they are unintended or not properly planned for. We recommend that you configure [CloudWatch alarms](https://docs.aws.amazon.com/kms/latest/developerguide/monitoring-cloudwatch.html) to alert you to these events before they occur. We also recommend that you configure AWS Identity and Access Management (IAM) policies or AWS Organizations [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to prevent the deletion of important keys.

CloudWatch alarms help you take corrective action, such as cancelling key deletion, or remediation actions, such as reimporting deleted or expired key material.

## Automating responses with Amazon EventBridge
<a name="monitoring-eventbridge"></a>

You can also use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to notify you of important events that affect your KMS keys. EventBridge is an AWS service that delivers a near real-time stream of system events that describe changes to AWS resources. EventBridge automatically receives events from CloudTrail and Security Hub CSPM. In EventBridge, you can create rules that respond to events recorded by CloudTrail.

AWS KMS events include the following:
+ The key material in a KMS key was automatically rotated
+ The imported key material in a KMS key expired
+ A KMS key that had been scheduled for deletion was deleted

These events can initiate additional actions in your AWS account. These actions are different from the CloudWatch alarms described in the previous section because they can only be acted on after the event occurs. For example, you might want to delete resources that are connected to a specific key after that key has been deleted, or you might want to inform a compliance or auditing team that the key has been deleted.

You can also filter for any other API event that is logged in CloudTrail by using EventBridge. This means that if key policy-related API actions are of specific concern, you can filter for them. For example, you could filter in EventBridge for the `PutKeyPolicy` API action. More broadly, you can filter for any API action that starts with `Disable*` or `Delete*` to initiate automated responses.

Using EventBridge, you can monitor (which is a detective control) and investigate and respond (which are responsive controls) to unexpected or selected events. For example, you can alert security teams and take specific actions if an IAM user or role is created, when a KMS key is created, or when a key policy is changed. You can create an EventBridge event rule that filters the API actions you specify and then associate targets to the rule. Example targets include AWS Lambda functions, Amazon Simple Notification Service (Amazon SNS) notifications, Amazon Simple Queue Service (Amazon SQS) queues, and more. For more information about sending events to targets, see [Event bus targets in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html).

For more information about monitoring AWS KMS with EventBridge and automating responses, see [Monitor KMS keys with Amazon EventBridge](https://docs.aws.amazon.com/kms/latest/developerguide/kms-events.html) in the AWS KMS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
