---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_JupyterServerAppSettings.html
---

# JupyterServerAppSettings
<a name="API_JupyterServerAppSettings"></a>

The JupyterServer app settings.

## Contents
<a name="API_JupyterServerAppSettings_Contents"></a>

 ** CodeRepositories **   <a name="sagemaker-Type-JupyterServerAppSettings-CodeRepositories"></a>
A list of Git repositories that SageMaker AI automatically displays to users for cloning in the JupyterServer application.
Type: Array of [CodeRepository](API_CodeRepository.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-JupyterServerAppSettings-DefaultResourceSpec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the JupyterServer app. If you use the `LifecycleConfigArns` parameter, then this parameter is also required.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** LifecycleConfigArns **   <a name="sagemaker-Type-JupyterServerAppSettings-LifecycleConfigArns"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the JupyterServerApp. If you use this parameter, the `DefaultResourceSpec` parameter is also required.
To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

## See Also
<a name="API_JupyterServerAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/JupyterServerAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/JupyterServerAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/JupyterServerAppSettings)
