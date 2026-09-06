---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalWebAclRulesListDetails.html
---

# AwsWafRegionalWebAclRulesListDetails
<a name="API_AwsWafRegionalWebAclRulesListDetails"></a>

A combination of `ByteMatchSet`, `IPSet`, and/or `SqlInjectionMatchSet` objects that identify the web requests that you want to allow, block, or count.

## Contents
<a name="API_AwsWafRegionalWebAclRulesListDetails_Contents"></a>

 ** Action **   <a name="securityhub-Type-AwsWafRegionalWebAclRulesListDetails-Action"></a>
The action that AWS WAF takes when a web request matches all conditions in the rule, such as allow, block, or count the request.
Type: [AwsWafRegionalWebAclRulesListActionDetails](API_AwsWafRegionalWebAclRulesListActionDetails.md) object
Required: No

 ** OverrideAction **   <a name="securityhub-Type-AwsWafRegionalWebAclRulesListDetails-OverrideAction"></a>
Overrides the rule evaluation result in the rule group.
Type: [AwsWafRegionalWebAclRulesListOverrideActionDetails](API_AwsWafRegionalWebAclRulesListOverrideActionDetails.md) object
Required: No

 ** Priority **   <a name="securityhub-Type-AwsWafRegionalWebAclRulesListDetails-Priority"></a>
The order in which AWS WAF evaluates the rules in a web ACL.
Type: Integer
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRegionalWebAclRulesListDetails-RuleId"></a>
The ID of an AWS WAF Regional rule to associate with a web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsWafRegionalWebAclRulesListDetails-Type"></a>
For actions that are associated with a rule, the action that AWS WAF takes when a web request matches all conditions in a rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRegionalWebAclRulesListDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalWebAclRulesListDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalWebAclRulesListDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalWebAclRulesListDetails)
