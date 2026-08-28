---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyParameter.html
---

# PolicyParameter
<a name="API_PolicyParameter"></a>

Contains information about a policy parameter used to customize delegated permissions.

## Contents
<a name="API_PolicyParameter_Contents"></a>

 ** Name **
The name of the policy parameter.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 256.
Pattern: `[ -~]+`
Required: No

 ** Type **
The data type of the policy parameter value.
Type: String
Valid Values: `string | stringList`
Required: No

 ** Values.member.N **
The allowed values for the policy parameter.
Type: Array of strings
Pattern: `[ -~]+`
Required: No

## See Also
<a name="API_PolicyParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PolicyParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PolicyParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PolicyParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
