---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_EnvironmentVariable.html
---

# EnvironmentVariable
<a name="API_EnvironmentVariable"></a>

Information about an environment variable for a project or a run.

## Contents
<a name="API_EnvironmentVariable_Contents"></a>

 ** name **   <a name="devicefarm-Type-EnvironmentVariable-name"></a>
The name of the environment variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_][a-zA-Z_0-9]*`
Required: Yes

 ** value **   <a name="devicefarm-Type-EnvironmentVariable-value"></a>
The value of the environment variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_EnvironmentVariable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/EnvironmentVariable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/EnvironmentVariable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/EnvironmentVariable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
