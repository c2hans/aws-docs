---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DelegationSet.html
---

# DelegationSet
<a name="API_DelegationSet"></a>

A complex type that lists the name servers in a delegation set, as well as the `CallerReference` and the `ID` for the delegation set.

## Contents
<a name="API_DelegationSet_Contents"></a>

 ** NameServers **   <a name="Route53-Type-DelegationSet-NameServers"></a>
A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Maximum length of 1024.
Required: Yes

 ** CallerReference **   <a name="Route53-Type-DelegationSet-CallerReference"></a>
The value that you specified for `CallerReference` when you created the reusable delegation set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Id **   <a name="Route53-Type-DelegationSet-Id"></a>
The ID that Amazon Route 53 assigns to a reusable delegation set.
Type: String
Length Constraints: Maximum length of 32.
Required: No

## See Also
<a name="API_DelegationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DelegationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DelegationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DelegationSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
