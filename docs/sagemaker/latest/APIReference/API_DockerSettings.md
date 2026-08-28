---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DockerSettings.html
---

# DockerSettings
<a name="API_DockerSettings"></a>

A collection of settings that configure the domain's Docker interaction.

## Contents
<a name="API_DockerSettings_Contents"></a>

 ** EnableDockerAccess **   <a name="sagemaker-Type-DockerSettings-EnableDockerAccess"></a>
Indicates whether the domain can access Docker.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** RootlessDocker **   <a name="sagemaker-Type-DockerSettings-RootlessDocker"></a>
Indicates whether to use rootless Docker.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** VpcOnlyTrustedAccounts **   <a name="sagemaker-Type-DockerSettings-VpcOnlyTrustedAccounts"></a>
The list of AWS accounts that are trusted when the domain is created in VPC-only mode.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## See Also
<a name="API_DockerSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DockerSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DockerSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DockerSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
