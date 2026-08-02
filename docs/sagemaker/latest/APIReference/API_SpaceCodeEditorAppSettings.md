---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SpaceCodeEditorAppSettings.html
---

# SpaceCodeEditorAppSettings
<a name="API_SpaceCodeEditorAppSettings"></a>

The application settings for a Code Editor space.

## Contents
<a name="API_SpaceCodeEditorAppSettings_Contents"></a>

 ** AppLifecycleManagement **   <a name="sagemaker-Type-SpaceCodeEditorAppSettings-AppLifecycleManagement"></a>
Settings that are used to configure and manage the lifecycle of CodeEditor applications in a space.
Type: [SpaceAppLifecycleManagement](API_SpaceAppLifecycleManagement.md) object
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-SpaceCodeEditorAppSettings-DefaultResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

## See Also
<a name="API_SpaceCodeEditorAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SpaceCodeEditorAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SpaceCodeEditorAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SpaceCodeEditorAppSettings)
