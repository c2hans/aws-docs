---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HubAccessConfig.html
---

# HubAccessConfig
<a name="API_HubAccessConfig"></a>

The configuration for a private hub model reference that points to a public SageMaker JumpStart model.

For more information about private hubs, see [Private curated hubs for foundation model access control in JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html).

## Contents
<a name="API_HubAccessConfig_Contents"></a>

 ** HubContentArn **   <a name="sagemaker-Type-HubAccessConfig-HubContentArn"></a>
The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_HubAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HubAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HubAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HubAccessConfig)
