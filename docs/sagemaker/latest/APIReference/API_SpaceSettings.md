---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SpaceSettings.html
---

# SpaceSettings
<a name="API_SpaceSettings"></a>

A collection of space settings.

## Contents
<a name="API_SpaceSettings_Contents"></a>

 ** AppType **   <a name="sagemaker-Type-SpaceSettings-AppType"></a>
The type of app created within the space.
If using the [ UpdateSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateSpace.html) API, you can't change the app type of your space by specifying a different value for this field.
Type: String
Valid Values: `JupyterServer | KernelGateway | DetailedProfiler | TensorBoard | CodeEditor | JupyterLab | RStudioServerPro | RSessionGateway | Canvas`
Required: No

 ** CodeEditorAppSettings **   <a name="sagemaker-Type-SpaceSettings-CodeEditorAppSettings"></a>
The Code Editor application settings.
Type: [SpaceCodeEditorAppSettings](API_SpaceCodeEditorAppSettings.md) object
Required: No

 ** CustomFileSystems **   <a name="sagemaker-Type-SpaceSettings-CustomFileSystems"></a>
A file system, created by you, that you assign to a space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.
Type: Array of [CustomFileSystem](API_CustomFileSystem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** JupyterLabAppSettings **   <a name="sagemaker-Type-SpaceSettings-JupyterLabAppSettings"></a>
The settings for the JupyterLab application.
Type: [SpaceJupyterLabAppSettings](API_SpaceJupyterLabAppSettings.md) object
Required: No

 ** JupyterServerAppSettings **   <a name="sagemaker-Type-SpaceSettings-JupyterServerAppSettings"></a>
The JupyterServer app settings.
Type: [JupyterServerAppSettings](API_JupyterServerAppSettings.md) object
Required: No

 ** KernelGatewayAppSettings **   <a name="sagemaker-Type-SpaceSettings-KernelGatewayAppSettings"></a>
The KernelGateway app settings.
Type: [KernelGatewayAppSettings](API_KernelGatewayAppSettings.md) object
Required: No

 ** RemoteAccess **   <a name="sagemaker-Type-SpaceSettings-RemoteAccess"></a>
A setting that enables or disables remote access for a SageMaker space. When enabled, this allows you to connect to the remote space from your local IDE.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** SpaceManagedResources **   <a name="sagemaker-Type-SpaceSettings-SpaceManagedResources"></a>
If you enable this option, SageMaker AI creates the following resources on your behalf when you create the space:
+ The user profile that possesses the space.
+ The app that the space contains.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** SpaceStorageSettings **   <a name="sagemaker-Type-SpaceSettings-SpaceStorageSettings"></a>
The storage settings for a space.
Type: [SpaceStorageSettings](API_SpaceStorageSettings.md) object
Required: No

## See Also
<a name="API_SpaceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SpaceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SpaceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SpaceSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
