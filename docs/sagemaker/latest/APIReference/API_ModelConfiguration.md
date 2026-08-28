---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelConfiguration.html
---

# ModelConfiguration
<a name="API_ModelConfiguration"></a>

Defines the model configuration. Includes the specification name and environment parameters.

## Contents
<a name="API_ModelConfiguration_Contents"></a>

 ** CompilationJobName **   <a name="sagemaker-Type-ModelConfiguration-CompilationJobName"></a>
The name of the compilation job used to create the recommended model artifacts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** EnvironmentParameters **   <a name="sagemaker-Type-ModelConfiguration-EnvironmentParameters"></a>
Defines the environment parameters that includes key, value types, and values.
Type: Array of [EnvironmentParameter](API_EnvironmentParameter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** InferenceSpecificationName **   <a name="sagemaker-Type-ModelConfiguration-InferenceSpecificationName"></a>
The inference specification name in the model package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_ModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
