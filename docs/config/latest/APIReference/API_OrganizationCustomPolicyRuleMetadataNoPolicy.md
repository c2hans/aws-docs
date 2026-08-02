---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationCustomPolicyRuleMetadataNoPolicy.html
---

# OrganizationCustomPolicyRuleMetadataNoPolicy
<a name="API_OrganizationCustomPolicyRuleMetadataNoPolicy"></a>

 metadata for your organization AWS Config Custom Policy rule including the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata such as resource type, resource ID of AWS resource, and organization trigger types that trigger AWS Config to evaluate AWS resources against a rule.

## Contents
<a name="API_OrganizationCustomPolicyRuleMetadataNoPolicy_Contents"></a>

 ** DebugLogDeliveryAccounts **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-DebugLogDeliveryAccounts"></a>
A list of accounts that you can enable debug logging for your organization AWS Config Custom Policy rule. List is null when debug logging is enabled for all accounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Description **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-Description"></a>
The description that you provide for your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** InputParameters **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-InputParameters"></a>
A string, in JSON format, that is passed to your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MaximumExecutionFrequency **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-MaximumExecutionFrequency"></a>
The maximum frequency with which AWS Config runs evaluations for a rule. Your AWS Config Custom Policy rule is triggered when AWS Config delivers the configuration snapshot. For more information, see [ConfigSnapshotDeliveryProperties](API_ConfigSnapshotDeliveryProperties.md).
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

 ** OrganizationConfigRuleTriggerTypes **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-OrganizationConfigRuleTriggerTypes"></a>
The type of notification that triggers AWS Config to run an evaluation for a rule. For AWS Config Custom Policy rules, AWS Config supports change triggered notification types:
+  `ConfigurationItemChangeNotification` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
+  `OversizedConfigurationItemChangeNotification` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
Type: Array of strings
Valid Values: `ConfigurationItemChangeNotification | OversizedConfigurationItemChangeNotification`
Required: No

 ** PolicyRuntime **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-PolicyRuntime"></a>
The runtime system for your organization AWS Config Custom Policy rules. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `guard\-2\.x\.x`
Required: No

 ** ResourceIdScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-ResourceIdScope"></a>
The ID of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceTypesScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-ResourceTypesScope"></a>
The type of the AWS resource that was evaluated.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TagKeyScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-TagKeyScope"></a>
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagValueScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadataNoPolicy-TagValueScope"></a>
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_OrganizationCustomPolicyRuleMetadataNoPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationCustomPolicyRuleMetadataNoPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationCustomPolicyRuleMetadataNoPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationCustomPolicyRuleMetadataNoPolicy)
