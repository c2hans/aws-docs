---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalWebAclDetails.html
---

# AwsWafRegionalWebAclDetails
<a name="API_AwsWafRegionalWebAclDetails"></a>

Provides information about the web access control list (web ACL). The web ACL contains the rules that identify the requests that you want to allow, block, or count.

## Contents
<a name="API_AwsWafRegionalWebAclDetails_Contents"></a>

 ** DefaultAction **   <a name="securityhub-Type-AwsWafRegionalWebAclDetails-DefaultAction"></a>
The action to perform if none of the rules contained in the web ACL match.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MetricName **   <a name="securityhub-Type-AwsWafRegionalWebAclDetails-MetricName"></a>
A name for the metrics for this web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRegionalWebAclDetails-Name"></a>
A descriptive name for the web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RulesList **   <a name="securityhub-Type-AwsWafRegionalWebAclDetails-RulesList"></a>
An array that contains the action for each rule in a web ACL, the priority of the rule, and the ID of the rule.
Type: Array of [AwsWafRegionalWebAclRulesListDetails](API_AwsWafRegionalWebAclRulesListDetails.md) objects
Required: No

 ** WebAclId **   <a name="securityhub-Type-AwsWafRegionalWebAclDetails-WebAclId"></a>
The ID of the web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRegionalWebAclDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalWebAclDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalWebAclDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalWebAclDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
