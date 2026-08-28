---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UniqueProblem.html
---

# UniqueProblem
<a name="API_UniqueProblem"></a>

A collection of one or more problems, grouped by their result.

## Contents
<a name="API_UniqueProblem_Contents"></a>

 ** message **   <a name="devicefarm-Type-UniqueProblem-message"></a>
A message about the unique problems' result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** problems **   <a name="devicefarm-Type-UniqueProblem-problems"></a>
Information about the problems.
Type: Array of [Problem](API_Problem.md) objects
Required: No

## See Also
<a name="API_UniqueProblem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UniqueProblem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UniqueProblem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UniqueProblem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
