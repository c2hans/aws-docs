---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIWorkloadConfigSummary.html
---

# AIWorkloadConfigSummary
<a name="API_AIWorkloadConfigSummary"></a>

Summary information about an AI workload configuration.

## Contents
<a name="API_AIWorkloadConfigSummary_Contents"></a>

 ** AIWorkloadConfigArn **   <a name="sagemaker-Type-AIWorkloadConfigSummary-AIWorkloadConfigArn"></a>
The Amazon Resource Name (ARN) of the AI workload configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-workload-config/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AIWorkloadConfigName **   <a name="sagemaker-Type-AIWorkloadConfigSummary-AIWorkloadConfigName"></a>
The name of the AI workload configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-AIWorkloadConfigSummary-CreationTime"></a>
A timestamp that indicates when the configuration was created.
Type: Timestamp
Required: Yes

## See Also
<a name="API_AIWorkloadConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIWorkloadConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIWorkloadConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIWorkloadConfigSummary)
