---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAppImageConfig.html
---

# CreateAppImageConfig
<a name="API_CreateAppImageConfig"></a>

Creates a configuration for running a SageMaker AI image as a KernelGateway app. The configuration specifies the Amazon Elastic File System storage volume on the image, and a list of the kernels in the image.

## Request Syntax
<a name="API_CreateAppImageConfig_RequestSyntax"></a>

```
{
   "AppImageConfigName": "{{string}}",
   "CodeEditorAppImageConfig": {
      "ContainerConfig": {
         "ContainerArguments": [ "{{string}}" ],
         "ContainerEntrypoint": [ "{{string}}" ],
         "ContainerEnvironmentVariables": {
            "{{string}}" : "{{string}}"
         }
      },
      "FileSystemConfig": {
         "DefaultGid": {{number}},
         "DefaultUid": {{number}},
         "MountPath": "{{string}}"
      }
   },
   "JupyterLabAppImageConfig": {
      "ContainerConfig": {
         "ContainerArguments": [ "{{string}}" ],
         "ContainerEntrypoint": [ "{{string}}" ],
         "ContainerEnvironmentVariables": {
            "{{string}}" : "{{string}}"
         }
      },
      "FileSystemConfig": {
         "DefaultGid": {{number}},
         "DefaultUid": {{number}},
         "MountPath": "{{string}}"
      }
   },
   "KernelGatewayImageConfig": {
      "FileSystemConfig": {
         "DefaultGid": {{number}},
         "DefaultUid": {{number}},
         "MountPath": "{{string}}"
      },
      "KernelSpecs": [
         {
            "DisplayName": "{{string}}",
            "Name": "{{string}}"
         }
      ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAppImageConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppImageConfigName](#API_CreateAppImageConfig_RequestSyntax) **   <a name="sagemaker-CreateAppImageConfig-request-AppImageConfigName"></a>
The name of the AppImageConfig. Must be unique to your account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [CodeEditorAppImageConfig](#API_CreateAppImageConfig_RequestSyntax) **   <a name="sagemaker-CreateAppImageConfig-request-CodeEditorAppImageConfig"></a>
The `CodeEditorAppImageConfig`. You can only specify one image kernel in the AppImageConfig API. This kernel is shown to users before the image starts. After the image runs, all kernels are visible in Code Editor.
Type: [CodeEditorAppImageConfig](API_CodeEditorAppImageConfig.md) object
Required: No

 ** [JupyterLabAppImageConfig](#API_CreateAppImageConfig_RequestSyntax) **   <a name="sagemaker-CreateAppImageConfig-request-JupyterLabAppImageConfig"></a>
The `JupyterLabAppImageConfig`. You can only specify one image kernel in the `AppImageConfig` API. This kernel is shown to users before the image starts. After the image runs, all kernels are visible in JupyterLab.
Type: [JupyterLabAppImageConfig](API_JupyterLabAppImageConfig.md) object
Required: No

 ** [KernelGatewayImageConfig](#API_CreateAppImageConfig_RequestSyntax) **   <a name="sagemaker-CreateAppImageConfig-request-KernelGatewayImageConfig"></a>
The KernelGatewayImageConfig. You can only specify one image kernel in the AppImageConfig API. This kernel will be shown to users before the image starts. Once the image runs, all kernels are visible in JupyterLab.
Type: [KernelGatewayImageConfig](API_KernelGatewayImageConfig.md) object
Required: No

 ** [Tags](#API_CreateAppImageConfig_RequestSyntax) **   <a name="sagemaker-CreateAppImageConfig-request-Tags"></a>
A list of tags to apply to the AppImageConfig.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAppImageConfig_ResponseSyntax"></a>

```
{
   "AppImageConfigArn": "string"
}
```

## Response Elements
<a name="API_CreateAppImageConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppImageConfigArn](#API_CreateAppImageConfig_ResponseSyntax) **   <a name="sagemaker-CreateAppImageConfig-response-AppImageConfigArn"></a>
The ARN of the AppImageConfig.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:app-image-config/.*`

## Errors
<a name="API_CreateAppImageConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

## See Also
<a name="API_CreateAppImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAppImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAppImageConfig)
