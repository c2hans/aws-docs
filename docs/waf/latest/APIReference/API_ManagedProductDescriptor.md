---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedProductDescriptor.html
---

# ManagedProductDescriptor
<a name="API_ManagedProductDescriptor"></a>

The properties of a managed product, such as an AWS Managed Rules rule group or an AWS Marketplace managed rule group.

## Contents
<a name="API_ManagedProductDescriptor_Contents"></a>

 ** IsAdvancedManagedRuleSet **   <a name="WAF-Type-ManagedProductDescriptor-IsAdvancedManagedRuleSet"></a>
Indicates whether the rule group provides an advanced set of protections, such as the the AWS Managed Rules rule groups that are used for AWS WAF intelligent threat mitigation.
Type: Boolean
Required: No

 ** IsVersioningSupported **   <a name="WAF-Type-ManagedProductDescriptor-IsVersioningSupported"></a>
Indicates whether the rule group is versioned.
Type: Boolean
Required: No

 ** ManagedRuleSetName **   <a name="WAF-Type-ManagedProductDescriptor-ManagedRuleSetName"></a>
The name of the managed rule group. For example, `AWSManagedRulesAnonymousIpList` or `AWSManagedRulesATPRuleSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

 ** ProductDescription **   <a name="WAF-Type-ManagedProductDescriptor-ProductDescription"></a>
A short description of the managed rule group.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `.*\S.*`
Required: No

 ** ProductId **   <a name="WAF-Type-ManagedProductDescriptor-ProductId"></a>
A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** ProductLink **   <a name="WAF-Type-ManagedProductDescriptor-ProductLink"></a>
For AWS Marketplace managed rule groups only, the link to the rule group product page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** ProductTitle **   <a name="WAF-Type-ManagedProductDescriptor-ProductTitle"></a>
The display name for the managed rule group. For example, `Anonymous IP list` or `Account takeover prevention`.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `.*\S.*`
Required: No

 ** SnsTopicArn **   <a name="WAF-Type-ManagedProductDescriptor-SnsTopicArn"></a>
The Amazon resource name (ARN) of the Amazon Simple Notification Service SNS topic that's used to provide notification of changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** VendorName **   <a name="WAF-Type-ManagedProductDescriptor-VendorName"></a>
The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ManagedProductDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedProductDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedProductDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedProductDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
