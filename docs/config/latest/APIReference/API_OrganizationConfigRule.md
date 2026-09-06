---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationConfigRule.html
---

# OrganizationConfigRule
<a name="API_OrganizationConfigRule"></a>

An organization AWS Config rule that has information about AWS Config rules that AWS Config creates in member accounts.

## Contents
<a name="API_OrganizationConfigRule_Contents"></a>

 ** OrganizationConfigRuleArn **   <a name="config-Type-OrganizationConfigRule-OrganizationConfigRuleArn"></a>
Amazon Resource Name (ARN) of organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** OrganizationConfigRuleName **   <a name="config-Type-OrganizationConfigRule-OrganizationConfigRuleName"></a>
The name that you assign to organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** ExcludedAccounts **   <a name="config-Type-OrganizationConfigRule-ExcludedAccounts"></a>
A comma-separated list of accounts excluded from organization AWS Config rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** LastUpdateTime **   <a name="config-Type-OrganizationConfigRule-LastUpdateTime"></a>
The timestamp of the last update.
Type: Timestamp
Required: No

 ** OrganizationCustomPolicyRuleMetadata **   <a name="config-Type-OrganizationConfigRule-OrganizationCustomPolicyRuleMetadata"></a>
An object that specifies metadata for your organization's AWS Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.
Type: [OrganizationCustomPolicyRuleMetadataNoPolicy](API_OrganizationCustomPolicyRuleMetadataNoPolicy.md) object
Required: No

 ** OrganizationCustomRuleMetadata **   <a name="config-Type-OrganizationConfigRule-OrganizationCustomRuleMetadata"></a>
An `OrganizationCustomRuleMetadata` object.
Type: [OrganizationCustomRuleMetadata](API_OrganizationCustomRuleMetadata.md) object
Required: No

 ** OrganizationManagedRuleMetadata **   <a name="config-Type-OrganizationConfigRule-OrganizationManagedRuleMetadata"></a>
An `OrganizationManagedRuleMetadata` object.
Type: [OrganizationManagedRuleMetadata](API_OrganizationManagedRuleMetadata.md) object
Required: No

## See Also
<a name="API_OrganizationConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationConfigRule)
