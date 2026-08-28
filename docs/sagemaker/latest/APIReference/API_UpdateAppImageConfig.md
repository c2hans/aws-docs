---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateAppImageConfig.html
---

# UpdateAppImageConfig
<a name="API_UpdateAppImageConfig"></a>

Updates the properties of an AppImageConfig.

## Request Syntax
<a name="API_UpdateAppImageConfig_RequestSyntax"></a>

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
   }
}
```

## Request Parameters
<a name="API_UpdateAppImageConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppImageConfigName](#API_UpdateAppImageConfig_RequestSyntax) **   <a name="sagemaker-UpdateAppImageConfig-request-AppImageConfigName"></a>
The name of the AppImageConfig to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [CodeEditorAppImageConfig](#API_UpdateAppImageConfig_RequestSyntax) **   <a name="sagemaker-UpdateAppImageConfig-request-CodeEditorAppImageConfig"></a>
The Code Editor app running on the image.
Type: [CodeEditorAppImageConfig](API_CodeEditorAppImageConfig.md) object
Required: No

 ** [JupyterLabAppImageConfig](#API_UpdateAppImageConfig_RequestSyntax) **   <a name="sagemaker-UpdateAppImageConfig-request-JupyterLabAppImageConfig"></a>
The JupyterLab app running on the image.
Type: [JupyterLabAppImageConfig](API_JupyterLabAppImageConfig.md) object
Required: No

 ** [KernelGatewayImageConfig](#API_UpdateAppImageConfig_RequestSyntax) **   <a name="sagemaker-UpdateAppImageConfig-request-KernelGatewayImageConfig"></a>
The new KernelGateway app to run on the image.
Type: [KernelGatewayImageConfig](API_KernelGatewayImageConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateAppImageConfig_ResponseSyntax"></a>

```
{
   "AppImageConfigArn": "string"
}
```

## Response Elements
<a name="API_UpdateAppImageConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppImageConfigArn](#API_UpdateAppImageConfig_ResponseSyntax) **   <a name="sagemaker-UpdateAppImageConfig-response-AppImageConfigArn"></a>
The ARN for the AppImageConfig.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:app-image-config/.*`

## Errors
<a name="API_UpdateAppImageConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAppImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateAppImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateAppImageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
