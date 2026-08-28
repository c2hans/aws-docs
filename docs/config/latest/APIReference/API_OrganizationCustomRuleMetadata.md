---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationCustomRuleMetadata.html
---

# OrganizationCustomRuleMetadata
<a name="API_OrganizationCustomRuleMetadata"></a>

An object that specifies organization custom rule metadata such as resource type, resource ID of AWS resource, Lambda function ARN, and organization trigger types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

## Contents
<a name="API_OrganizationCustomRuleMetadata_Contents"></a>

 ** LambdaFunctionArn **   <a name="config-Type-OrganizationCustomRuleMetadata-LambdaFunctionArn"></a>
The lambda function ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** OrganizationConfigRuleTriggerTypes **   <a name="config-Type-OrganizationCustomRuleMetadata-OrganizationConfigRuleTriggerTypes"></a>
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
+  `ConfigurationItemChangeNotification` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
+  `OversizedConfigurationItemChangeNotification` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
+  `ScheduledNotification` - Triggers a periodic evaluation at the frequency specified for `MaximumExecutionFrequency`.
Type: Array of strings
Valid Values: `ConfigurationItemChangeNotification | OversizedConfigurationItemChangeNotification | ScheduledNotification`
Required: Yes

 ** Description **   <a name="config-Type-OrganizationCustomRuleMetadata-Description"></a>
The description that you provide for your organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** InputParameters **   <a name="config-Type-OrganizationCustomRuleMetadata-InputParameters"></a>
A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MaximumExecutionFrequency **   <a name="config-Type-OrganizationCustomRuleMetadata-MaximumExecutionFrequency"></a>
The maximum frequency with which AWS Config runs evaluations for a rule. Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see [ConfigSnapshotDeliveryProperties](API_ConfigSnapshotDeliveryProperties.md).
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

 ** ResourceIdScope **   <a name="config-Type-OrganizationCustomRuleMetadata-ResourceIdScope"></a>
The ID of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceTypesScope **   <a name="config-Type-OrganizationCustomRuleMetadata-ResourceTypesScope"></a>
The type of the AWS resource that was evaluated.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TagKeyScope **   <a name="config-Type-OrganizationCustomRuleMetadata-TagKeyScope"></a>
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagValueScope **   <a name="config-Type-OrganizationCustomRuleMetadata-TagValueScope"></a>
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_OrganizationCustomRuleMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationCustomRuleMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationCustomRuleMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationCustomRuleMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
