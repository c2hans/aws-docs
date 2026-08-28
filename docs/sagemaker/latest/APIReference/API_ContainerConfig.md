---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerConfig.html
---

# ContainerConfig
<a name="API_ContainerConfig"></a>

The configuration used to run the application image container.

## Contents
<a name="API_ContainerConfig_Contents"></a>

 ** ContainerArguments **   <a name="sagemaker-Type-ContainerConfig-ContainerArguments"></a>
The arguments for the container when you're running the application.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`
Required: No

 ** ContainerEntrypoint **   <a name="sagemaker-Type-ContainerConfig-ContainerEntrypoint"></a>
The entrypoint used to run the application in the container.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!\s*$).+`
Required: No

 ** ContainerEnvironmentVariables **   <a name="sagemaker-Type-ContainerConfig-ContainerEnvironmentVariables"></a>
The environment variables to set in the container
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `(?!\s*$).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ContainerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ContainerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ContainerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ContainerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
