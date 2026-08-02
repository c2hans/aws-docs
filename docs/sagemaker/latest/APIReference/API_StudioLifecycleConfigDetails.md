---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StudioLifecycleConfigDetails.html
---

# StudioLifecycleConfigDetails
<a name="API_StudioLifecycleConfigDetails"></a>

Details of the Amazon SageMaker AI Studio Lifecycle Configuration.

## Contents
<a name="API_StudioLifecycleConfigDetails_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-StudioLifecycleConfigDetails-CreationTime"></a>
The creation time of the Amazon SageMaker AI Studio Lifecycle Configuration.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-StudioLifecycleConfigDetails-LastModifiedTime"></a>
This value is equivalent to CreationTime because Amazon SageMaker AI Studio Lifecycle Configurations are immutable.
Type: Timestamp
Required: No

 ** StudioLifecycleConfigAppType **   <a name="sagemaker-Type-StudioLifecycleConfigDetails-StudioLifecycleConfigAppType"></a>
The App type to which the Lifecycle Configuration is attached.
Type: String
Valid Values: `JupyterServer | KernelGateway | CodeEditor | JupyterLab`
Required: No

 ** StudioLifecycleConfigArn **   <a name="sagemaker-Type-StudioLifecycleConfigDetails-StudioLifecycleConfigArn"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

 ** StudioLifecycleConfigName **   <a name="sagemaker-Type-StudioLifecycleConfigDetails-StudioLifecycleConfigName"></a>
The name of the Amazon SageMaker AI Studio Lifecycle Configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_StudioLifecycleConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StudioLifecycleConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StudioLifecycleConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StudioLifecycleConfigDetails)
