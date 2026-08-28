---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicyFinding.html
---

# ValidatePolicyFinding
<a name="API_ValidatePolicyFinding"></a>

A finding in a policy. Each finding is an actionable recommendation that can be used to improve the policy.

## Contents
<a name="API_ValidatePolicyFinding_Contents"></a>

 ** findingDetails **   <a name="accessanalyzer-Type-ValidatePolicyFinding-findingDetails"></a>
A localized message that explains the finding and provides guidance on how to address it.
Type: String
Required: Yes

 ** findingType **   <a name="accessanalyzer-Type-ValidatePolicyFinding-findingType"></a>
The impact of the finding.
Security warnings report when the policy allows access that we consider overly permissive.
Errors report when a part of the policy is not functional.
Warnings report non-security issues when a policy does not conform to policy writing best practices.
Suggestions recommend stylistic improvements in the policy that do not impact access.
Type: String
Valid Values: `ERROR | SECURITY_WARNING | SUGGESTION | WARNING`
Required: Yes

 ** issueCode **   <a name="accessanalyzer-Type-ValidatePolicyFinding-issueCode"></a>
The issue code provides an identifier of the issue associated with this finding.
Type: String
Required: Yes

 ** learnMoreLink **   <a name="accessanalyzer-Type-ValidatePolicyFinding-learnMoreLink"></a>
A link to additional documentation about the type of finding.
Type: String
Required: Yes

 ** locations **   <a name="accessanalyzer-Type-ValidatePolicyFinding-locations"></a>
The list of locations in the policy document that are related to the finding. The issue code provides a summary of an issue identified by the finding.
Type: Array of [Location](API_Location.md) objects
Required: Yes

## See Also
<a name="API_ValidatePolicyFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ValidatePolicyFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ValidatePolicyFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ValidatePolicyFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
