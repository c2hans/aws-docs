---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

Contains information about a rule in Amazon EventBridge.

## Contents
<a name="API_Rule_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-Rule-Arn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** Description **   <a name="eventbridge-Type-Rule-Description"></a>
The description of the rule.
Type: String
Length Constraints: Maximum length of 512.
Required: No

 ** EventBusName **   <a name="eventbridge-Type-Rule-EventBusName"></a>
The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[/\.\-_A-Za-z0-9]+`
Required: No

 ** EventPattern **   <a name="eventbridge-Type-Rule-EventPattern"></a>
The event pattern of the rule. For more information, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html) in the * *Amazon EventBridge User Guide* *.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** ManagedBy **   <a name="eventbridge-Type-Rule-ManagedBy"></a>
If the rule was created on behalf of your account by an AWS service, this field displays the principal name of the service that created the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Name **   <a name="eventbridge-Type-Rule-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** RoleArn **   <a name="eventbridge-Type-Rule-RoleArn"></a>
The Amazon Resource Name (ARN) of the role that is used for target invocation.
If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a `RoleArn` with proper permissions in the `Target` structure, instead of here in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** ScheduleExpression **   <a name="eventbridge-Type-Rule-ScheduleExpression"></a>
The scheduling expression. For example, "cron(0 20 \* \* ? \*)", "rate(5 minutes)". For more information, see [Creating an Amazon EventBridge rule that runs on a schedule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html).
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** State **   <a name="eventbridge-Type-Rule-State"></a>
The state of the rule.
Valid values include:
+  `DISABLED`: The rule is disabled. EventBridge does not match any events against the rule.
+  `ENABLED`: The rule is enabled. EventBridge matches events against the rule, *except* for AWS management events delivered through CloudTrail.
+  `ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS`: The rule is enabled for all events, including AWS management events delivered through CloudTrail.

  Management events provide visibility into management operations that are performed on resources in your AWS account. These are also known as control plane operations. For more information, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) in the *CloudTrail User Guide*, and [Filtering management events from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-cloudtrail) in the * *Amazon EventBridge User Guide* *.

  This value is only valid for rules on the [default](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html#eb-bus-concepts-buses) event bus or [custom event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html). It does not apply to [partner event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html).
Type: String
Valid Values: `ENABLED | DISABLED | ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS`
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Rule)
