---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_KernelGatewayAppSettings.html
---

# KernelGatewayAppSettings
<a name="API_KernelGatewayAppSettings"></a>

The KernelGateway app settings.

## Contents
<a name="API_KernelGatewayAppSettings_Contents"></a>

 ** CustomImages **   <a name="sagemaker-Type-KernelGatewayAppSettings-CustomImages"></a>
A list of custom SageMaker AI images that are configured to run as a KernelGateway app.
The maximum number of custom images are as follows.
+ On a domain level: 200
+ On a space level: 5
+ On a user profile level: 5
Type: Array of [CustomImage](API_CustomImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-KernelGatewayAppSettings-DefaultResourceSpec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the KernelGateway app.
The Amazon SageMaker AI Studio UI does not use the default instance type value set here. The default instance type set here is used when Apps are created using the AWS CLI or CloudFormation and the instance type parameter value is not passed.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** LifecycleConfigArns **   <a name="sagemaker-Type-KernelGatewayAppSettings-LifecycleConfigArns"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the the user profile or domain.
To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

## See Also
<a name="API_KernelGatewayAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/KernelGatewayAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/KernelGatewayAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/KernelGatewayAppSettings)
