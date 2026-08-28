---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLContainerDefinition.html
---

# AutoMLContainerDefinition
<a name="API_AutoMLContainerDefinition"></a>

A list of container definitions that describe the different containers that make up an AutoML candidate. For more information, see [ ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html).

## Contents
<a name="API_AutoMLContainerDefinition_Contents"></a>

 ** Image **   <a name="sagemaker-Type-AutoMLContainerDefinition-Image"></a>
The Amazon Elastic Container Registry (Amazon ECR) path of the container. For more information, see [ ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\S]+`
Required: Yes

 ** ModelDataUrl **   <a name="sagemaker-Type-AutoMLContainerDefinition-ModelDataUrl"></a>
The location of the model artifacts. For more information, see [ ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** Environment **   <a name="sagemaker-Type-AutoMLContainerDefinition-Environment"></a>
The environment variables to set in the container. For more information, see [ ContainerDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_AutoMLContainerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLContainerDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLContainerDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLContainerDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
