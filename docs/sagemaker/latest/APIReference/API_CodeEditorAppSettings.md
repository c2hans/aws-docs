---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CodeEditorAppSettings.html
---

# CodeEditorAppSettings
<a name="API_CodeEditorAppSettings"></a>

The Code Editor application settings.

For more information about Code Editor, see [Get started with Code Editor in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html).

## Contents
<a name="API_CodeEditorAppSettings_Contents"></a>

 ** AppLifecycleManagement **   <a name="sagemaker-Type-CodeEditorAppSettings-AppLifecycleManagement"></a>
Settings that are used to configure and manage the lifecycle of CodeEditor applications.
Type: [AppLifecycleManagement](API_AppLifecycleManagement.md) object
Required: No

 ** BuiltInLifecycleConfigArn **   <a name="sagemaker-Type-CodeEditorAppSettings-BuiltInLifecycleConfigArn"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

 ** CustomImages **   <a name="sagemaker-Type-CodeEditorAppSettings-CustomImages"></a>
A list of custom SageMaker images that are configured to run as a Code Editor app.
Type: Array of [CustomImage](API_CustomImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** DefaultResourceSpec **   <a name="sagemaker-Type-CodeEditorAppSettings-DefaultResourceSpec"></a>
Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** LifecycleConfigArns **   <a name="sagemaker-Type-CodeEditorAppSettings-LifecycleConfigArns"></a>
The Amazon Resource Name (ARN) of the Code Editor application lifecycle configuration.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`
Required: No

## See Also
<a name="API_CodeEditorAppSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CodeEditorAppSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CodeEditorAppSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CodeEditorAppSettings)
