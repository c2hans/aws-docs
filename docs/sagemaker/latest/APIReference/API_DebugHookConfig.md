---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DebugHookConfig.html
---

# DebugHookConfig
<a name="API_DebugHookConfig"></a>

Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).

## Contents
<a name="API_DebugHookConfig_Contents"></a>

 ** S3OutputPath **   <a name="sagemaker-Type-DebugHookConfig-S3OutputPath"></a>
Path to Amazon S3 storage location for metrics and tensors.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** CollectionConfigurations **   <a name="sagemaker-Type-DebugHookConfig-CollectionConfigurations"></a>
Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the `CollectionConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
Type: Array of [CollectionConfiguration](API_CollectionConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** HookParameters **   <a name="sagemaker-Type-DebugHookConfig-HookParameters"></a>
Configuration information for the Amazon SageMaker Debugger hook parameters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

 ** LocalPath **   <a name="sagemaker-Type-DebugHookConfig-LocalPath"></a>
Path to local storage location for metrics and tensors. Defaults to `/opt/ml/output/tensors/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `.*`
Required: No

## See Also
<a name="API_DebugHookConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DebugHookConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DebugHookConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DebugHookConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
