---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SpaceJupyterLabAppSettings.html
---

# SpaceJupyterLabAppSettings
<a name="API_SpaceJupyterLabAppSettings"></a>

The settings for the JupyterLab application within a space.

## Contents
<a name="API_SpaceJupyterLabAppSettings_Contents"></a>

 ** AppLifecycleManagement **   <a name="sagemaker-Type-SpaceJupyterLabAppSettings-AppLifecycleManagement"></a>
Settings that are used to configure and manage the lifecycle of JupyterLab applications in a space.
Type: [SpaceAppLifecycleManagement](API_SpaceAppLifecycleManagement.md) object
Required: No

 ** CodeRepositories **   <a name="sagemaker-Type-SpaceJupyterLabAppSettings-CodeRepositories"></a>
A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.
Type: Array of [CodeRepository](API_CodeRepository.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-SpaceJupyterLabAppSettings-DefaultResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

## See Also
<a name="API_SpaceJupyterLabAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SpaceJupyterLabAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SpaceJupyterLabAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SpaceJupyterLabAppSettings)
