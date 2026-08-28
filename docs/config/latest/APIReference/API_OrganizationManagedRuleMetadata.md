---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationManagedRuleMetadata.html
---

# OrganizationManagedRuleMetadata
<a name="API_OrganizationManagedRuleMetadata"></a>

An object that specifies organization managed rule metadata such as resource type and ID of AWS resource along with the rule identifier. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

## Contents
<a name="API_OrganizationManagedRuleMetadata_Contents"></a>

 ** RuleIdentifier **   <a name="config-Type-OrganizationManagedRuleMetadata-RuleIdentifier"></a>
For organization config managed rules, a predefined identifier from a list. For example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed rule, see [Using AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Description **   <a name="config-Type-OrganizationManagedRuleMetadata-Description"></a>
The description that you provide for your organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** InputParameters **   <a name="config-Type-OrganizationManagedRuleMetadata-InputParameters"></a>
A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MaximumExecutionFrequency **   <a name="config-Type-OrganizationManagedRuleMetadata-MaximumExecutionFrequency"></a>
The maximum frequency with which AWS Config runs evaluations for a rule. This is for an AWS Config managed rule that is triggered at a periodic frequency.
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

 ** ResourceIdScope **   <a name="config-Type-OrganizationManagedRuleMetadata-ResourceIdScope"></a>
The ID of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceTypesScope **   <a name="config-Type-OrganizationManagedRuleMetadata-ResourceTypesScope"></a>
The type of the AWS resource that was evaluated.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** TagKeyScope **   <a name="config-Type-OrganizationManagedRuleMetadata-TagKeyScope"></a>
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagValueScope **   <a name="config-Type-OrganizationManagedRuleMetadata-TagValueScope"></a>
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_OrganizationManagedRuleMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationManagedRuleMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationManagedRuleMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationManagedRuleMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
