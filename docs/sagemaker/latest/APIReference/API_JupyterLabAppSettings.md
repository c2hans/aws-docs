---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_JupyterLabAppSettings.html
---

# JupyterLabAppSettings
<a name="API_JupyterLabAppSettings"></a>

The settings for the JupyterLab application.

## Contents
<a name="API_JupyterLabAppSettings_Contents"></a>

 ** AppLifecycleManagement **   <a name="sagemaker-Type-JupyterLabAppSettings-AppLifecycleManagement"></a>
Indicates whether idle shutdown is activated for JupyterLab applications.
Type: [AppLifecycleManagement](API_AppLifecycleManagement.md) object
Required: No

 ** BuiltInLifecycleConfigArn **   <a name="sagemaker-Type-JupyterLabAppSettings-BuiltInLifecycleConfigArn"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

 ** CodeRepositories **   <a name="sagemaker-Type-JupyterLabAppSettings-CodeRepositories"></a>
A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.
Type: Array of [CodeRepository](API_CodeRepository.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** CustomImages **   <a name="sagemaker-Type-JupyterLabAppSettings-CustomImages"></a>
A list of custom SageMaker images that are configured to run as a JupyterLab app.
Type: Array of [CustomImage](API_CustomImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-JupyterLabAppSettings-DefaultResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** EmrSettings **   <a name="sagemaker-Type-JupyterLabAppSettings-EmrSettings"></a>
The configuration parameters that specify the IAM roles assumed by the execution role of SageMaker (assumable roles) and the cluster instances or job execution environments (execution roles or runtime roles) to manage and access resources required for running Amazon EMR clusters or Amazon EMR Serverless applications.
Type: [EmrSettings](API_EmrSettings.md) object
Required: No

 ** LifecycleConfigArns **   <a name="sagemaker-Type-JupyterLabAppSettings-LifecycleConfigArns"></a>
The Amazon Resource Name (ARN) of the lifecycle configurations attached to the user profile or domain. To remove a lifecycle config, you must set `LifecycleConfigArns` to an empty list.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

## See Also
<a name="API_JupyterLabAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/JupyterLabAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/JupyterLabAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/JupyterLabAppSettings)
