---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAppImageConfig.html
---

# DescribeAppImageConfig
<a name="API_DescribeAppImageConfig"></a>

Describes an AppImageConfig.

## Request Syntax
<a name="API_DescribeAppImageConfig_RequestSyntax"></a>

```
{
   "AppImageConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAppImageConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppImageConfigName](#API_DescribeAppImageConfig_RequestSyntax) **   <a name="sagemaker-DescribeAppImageConfig-request-AppImageConfigName"></a>
The name of the AppImageConfig to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeAppImageConfig_ResponseSyntax"></a>

```
{
   "AppImageConfigArn": "string",
   "AppImageConfigName": "string",
   "CodeEditorAppImageConfig": {
      "ContainerConfig": {
         "ContainerArguments": [ "string" ],
         "ContainerEntrypoint": [ "string" ],
         "ContainerEnvironmentVariables": {
            "string" : "string"
         }
      },
      "FileSystemConfig": {
         "DefaultGid": number,
         "DefaultUid": number,
         "MountPath": "string"
      }
   },
   "JupyterLabAppImageConfig": {
      "ContainerConfig": {
         "ContainerArguments": [ "string" ],
         "ContainerEntrypoint": [ "string" ],
         "ContainerEnvironmentVariables": {
            "string" : "string"
         }
      },
      "FileSystemConfig": {
         "DefaultGid": number,
         "DefaultUid": number,
         "MountPath": "string"
      }
   },
   "KernelGatewayImageConfig": {
      "FileSystemConfig": {
         "DefaultGid": number,
         "DefaultUid": number,
         "MountPath": "string"
      },
      "KernelSpecs": [
         {
            "DisplayName": "string",
            "Name": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeAppImageConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppImageConfigArn](#API_DescribeAppImageConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAppImageConfig-response-AppImageConfigArn"></a>
The ARN of the AppImageConfig.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:app-image-config/.*`

 ** [AppImageConfigName](#API_DescribeAppImageConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAppImageConfig-response-AppImageConfigName"></a>
The name of the AppImageConfig.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [CodeEditorAppImageConfig](#API_DescribeAppImageConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAppImageConfig-response-CodeEditorAppImageConfig"></a>
The configuration of the Code Editor app.
Type: [CodeEditorAppImageConfig](API_CodeEditorAppImageConfig.md) object

 ** [JupyterLabAppImageConfig](#API_DescribeAppImageConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAppImageConfig-response-JupyterLabAppImageConfig"></a>
The configuration of the JupyterLab app.
Type: [JupyterLabAppImageConfig](API_JupyterLabAppImageConfig.md) object

 ** [KernelGatewayImageConfig](#API_DescribeAppImageConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAppImageConfig-response-KernelGatewayImageConfig"></a>
The configuration of a KernelGateway app.
Type: [KernelGatewayImageConfig](API_KernelGatewayImageConfig.md) object

## Errors
<a name="API_DescribeAppImageConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAppImageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAppImageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAppImageConfig)
