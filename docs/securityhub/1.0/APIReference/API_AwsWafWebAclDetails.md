---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafWebAclDetails.html
---

# AwsWafWebAclDetails
<a name="API_AwsWafWebAclDetails"></a>

Provides information about an AWS WAF web access control list (web ACL).

## Contents
<a name="API_AwsWafWebAclDetails_Contents"></a>

 ** DefaultAction **   <a name="securityhub-Type-AwsWafWebAclDetails-DefaultAction"></a>
The action to perform if none of the rules contained in the web ACL match.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafWebAclDetails-Name"></a>
A friendly name or description of the web ACL. You can't change the name of a web ACL after you create it.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Rules **   <a name="securityhub-Type-AwsWafWebAclDetails-Rules"></a>
An array that contains the action for each rule in a web ACL, the priority of the rule, and the ID of the rule.
Type: Array of [AwsWafWebAclRule](API_AwsWafWebAclRule.md) objects
Required: No

 ** WebAclId **   <a name="securityhub-Type-AwsWafWebAclDetails-WebAclId"></a>
A unique identifier for a web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafWebAclDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafWebAclDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafWebAclDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafWebAclDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
