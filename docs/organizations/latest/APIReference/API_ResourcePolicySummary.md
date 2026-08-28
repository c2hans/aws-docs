---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_ResourcePolicySummary.html
---

# ResourcePolicySummary
<a name="API_ResourcePolicySummary"></a>

A structure that contains resource policy ID and Amazon Resource Name (ARN).

## Contents
<a name="API_ResourcePolicySummary_Contents"></a>

 ** Arn **   <a name="organizations-Type-ResourcePolicySummary-Arn"></a>
The Amazon Resource Name (ARN) of the resource policy.
Type: String
Pattern: `^arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:resourcepolicy\/o-[a-z0-9]{10,32}\/rp-[0-9a-zA-Z_]{4,128}`
Required: No

 ** Id **   <a name="organizations-Type-ResourcePolicySummary-Id"></a>
The unique identifier (ID) of the resource policy.
Type: String
Length Constraints: Maximum length of 131.
Pattern: `^rp-[0-9a-zA-Z_]{4,128}$`
Required: No

## See Also
<a name="API_ResourcePolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/ResourcePolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/ResourcePolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/ResourcePolicySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
