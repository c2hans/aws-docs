---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationCustomPolicyRuleMetadata.html
---

# OrganizationCustomPolicyRuleMetadata
<a name="API_OrganizationCustomPolicyRuleMetadata"></a>

An object that specifies metadata for your organization's AWS Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.

## Contents
<a name="API_OrganizationCustomPolicyRuleMetadata_Contents"></a>

 ** PolicyRuntime **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-PolicyRuntime"></a>
The runtime system for your organization AWS Config Custom Policy rules. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the [Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `guard\-2\.x\.x`
Required: Yes

 ** PolicyText **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-PolicyText"></a>
The policy definition containing the logic for your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: Yes

 ** DebugLogDeliveryAccounts **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-DebugLogDeliveryAccounts"></a>
A list of accounts that you can enable debug logging for your organization AWS Config Custom Policy rule. List is null when debug logging is enabled for all accounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Description **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-Description"></a>
The description that you provide for your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** InputParameters **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-InputParameters"></a>
A string, in JSON format, that is passed to your organization AWS Config Custom Policy rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MaximumExecutionFrequency **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-MaximumExecutionFrequency"></a>
The maximum frequency with which AWS Config runs evaluations for a rule. Your AWS Config Custom Policy rule is triggered when AWS Config delivers the configuration snapshot. For more information, see [ConfigSnapshotDeliveryProperties](API_ConfigSnapshotDeliveryProperties.md).
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

 ** OrganizationConfigRuleTriggerTypes **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-OrganizationConfigRuleTriggerTypes"></a>
The type of notification that initiates AWS Config to run an evaluation for a rule. For AWS Config Custom Policy rules, AWS Config supports change-initiated notification types:
+  `ConfigurationItemChangeNotification` - Initiates an evaluation when AWS Config delivers a configuration item as a result of a resource change.
+  `OversizedConfigurationItemChangeNotification` - Initiates an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
Type: Array of strings
Valid Values: `ConfigurationItemChangeNotification | OversizedConfigurationItemChangeNotification`
Required: No

 ** ResourceIdScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-ResourceIdScope"></a>
The ID of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceTypesScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-ResourceTypesScope"></a>
The type of the AWS resource that was evaluated.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TagKeyScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-TagKeyScope"></a>
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagValueScope **   <a name="config-Type-OrganizationCustomPolicyRuleMetadata-TagValueScope"></a>
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_OrganizationCustomPolicyRuleMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationCustomPolicyRuleMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationCustomPolicyRuleMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationCustomPolicyRuleMetadata)
