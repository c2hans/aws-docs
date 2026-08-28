---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_EventRuleStructure.html
---

# EventRuleStructure
<a name="API_EventRuleStructure"></a>

Contains a complete list of fields related to an `EventRule`.

## Contents
<a name="API_EventRuleStructure_Contents"></a>

 ** arn **   <a name="Notifications-Type-EventRuleStructure-arn"></a>
The Amazon Resource Name (ARN) of the `EventRule`. AWS CloudFormation stack generates this ARN and then uses this ARN to associate with the `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`
Required: Yes

 ** creationTime **   <a name="Notifications-Type-EventRuleStructure-creationTime"></a>
The creation time of the `EventRule`.
Type: Timestamp
Required: Yes

 ** eventPattern **   <a name="Notifications-Type-EventRuleStructure-eventPattern"></a>
An additional event pattern used to further filter the events this `EventRule` receives.
For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: Yes

 ** eventType **   <a name="Notifications-Type-EventRuleStructure-eventType"></a>
The event type this rule should match with the EventBridge events. It must match with atleast one of the valid EventBridge event types. For example, Amazon EC2 Instance State change Notification and Amazon CloudWatch State Change. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the * Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([a-zA-Z0-9 \-\(\)])+`
Required: Yes

 ** managedRules **   <a name="Notifications-Type-EventRuleStructure-managedRules"></a>
A list of Amazon EventBridge Managed Rule ARNs associated with this `EventRule`.
These are created by AWS User Notifications within your account so your `EventRules` can function.
Type: Array of strings
Pattern: `arn:[a-z-]{3,10}:events:[a-z-\d]{2,25}:\d{12}:rule\/[a-zA-Z-\d]{1,1024}`
Required: Yes

 ** notificationConfigurationArn **   <a name="Notifications-Type-EventRuleStructure-notificationConfigurationArn"></a>
The ARN for the `NotificationConfiguration` associated with this `EventRule`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

 ** regions **   <a name="Notifications-Type-EventRuleStructure-regions"></a>
A list of AWS Regions that send events to this `EventRule`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: Yes

 ** source **   <a name="Notifications-Type-EventRuleStructure-source"></a>
The event source this rule should match with the EventBridge event sources. It must match with atleast one of the valid EventBridge event sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the * Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`
Required: Yes

 ** statusSummaryByRegion **   <a name="Notifications-Type-EventRuleStructure-statusSummaryByRegion"></a>
A list of an `EventRule`'s status by Region. Regions are mapped to `EventRuleStatusSummary`.
Type: String to [EventRuleStatusSummary](API_EventRuleStatusSummary.md) object map
Key Length Constraints: Minimum length of 2. Maximum length of 25.
Key Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: Yes

## See Also
<a name="API_EventRuleStructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/EventRuleStructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/EventRuleStructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/EventRuleStructure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
