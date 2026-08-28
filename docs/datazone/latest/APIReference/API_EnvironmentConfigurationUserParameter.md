---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentConfigurationUserParameter.html
---

# EnvironmentConfigurationUserParameter
<a name="API_EnvironmentConfigurationUserParameter"></a>

The environment configuration user parameters.

## Contents
<a name="API_EnvironmentConfigurationUserParameter_Contents"></a>

 ** environmentConfigurationName **   <a name="datazone-Type-EnvironmentConfigurationUserParameter-environmentConfigurationName"></a>
The environment configuration name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** environmentId **   <a name="datazone-Type-EnvironmentConfigurationUserParameter-environmentId"></a>
The ID of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** environmentParameters **   <a name="datazone-Type-EnvironmentConfigurationUserParameter-environmentParameters"></a>
The environment parameters.
Type: Array of [EnvironmentParameter](API_EnvironmentParameter.md) objects
Required: No

 ** environmentResolvedAccount **   <a name="datazone-Type-EnvironmentConfigurationUserParameter-environmentResolvedAccount"></a>
Specifies the account/Region that is to be used during project creation for a particular blueprint.
Type: [EnvironmentResolvedAccount](API_EnvironmentResolvedAccount.md) object
Required: No

## See Also
<a name="API_EnvironmentConfigurationUserParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentConfigurationUserParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentConfigurationUserParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentConfigurationUserParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
