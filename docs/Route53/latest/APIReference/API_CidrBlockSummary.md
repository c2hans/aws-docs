---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CidrBlockSummary.html
---

# CidrBlockSummary
<a name="API_CidrBlockSummary"></a>

A complex type that lists the CIDR blocks.

## Contents
<a name="API_CidrBlockSummary_Contents"></a>

 ** CidrBlock **   <a name="Route53-Type-CidrBlockSummary-CidrBlock"></a>
Value for the CIDR block.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** LocationName **   <a name="Route53-Type-CidrBlockSummary-LocationName"></a>
The location name of the CIDR block.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `[0-9A-Za-z_\-]+`
Required: No

## See Also
<a name="API_CidrBlockSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CidrBlockSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CidrBlockSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CidrBlockSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
