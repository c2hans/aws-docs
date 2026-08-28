---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateStudioLifecycleConfig.html
---

# CreateStudioLifecycleConfig
<a name="API_CreateStudioLifecycleConfig"></a>

Creates a new Amazon SageMaker AI Studio Lifecycle Configuration.

## Request Syntax
<a name="API_CreateStudioLifecycleConfig_RequestSyntax"></a>

```
{
   "StudioLifecycleConfigAppType": "{{string}}",
   "StudioLifecycleConfigContent": "{{string}}",
   "StudioLifecycleConfigName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateStudioLifecycleConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [StudioLifecycleConfigAppType](#API_CreateStudioLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateStudioLifecycleConfig-request-StudioLifecycleConfigAppType"></a>
The App type that the Lifecycle Configuration is attached to.
Type: String
Valid Values: `JupyterServer | KernelGateway | CodeEditor | JupyterLab`
Required: Yes

 ** [StudioLifecycleConfigContent](#API_CreateStudioLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateStudioLifecycleConfig-request-StudioLifecycleConfigContent"></a>
The content of your Amazon SageMaker AI Studio Lifecycle Configuration script. This content must be base64 encoded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\S\s]+`
Required: Yes

 ** [StudioLifecycleConfigName](#API_CreateStudioLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateStudioLifecycleConfig-request-StudioLifecycleConfigName"></a>
The name of the Amazon SageMaker AI Studio Lifecycle Configuration to create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Tags](#API_CreateStudioLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateStudioLifecycleConfig-request-Tags"></a>
Tags to be associated with the Lifecycle Configuration. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the Search API.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateStudioLifecycleConfig_ResponseSyntax"></a>

```
{
   "StudioLifecycleConfigArn": "string"
}
```

## Response Elements
<a name="API_CreateStudioLifecycleConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StudioLifecycleConfigArn](#API_CreateStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-CreateStudioLifecycleConfig-response-StudioLifecycleConfigArn"></a>
The ARN of your created Lifecycle Configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`

## Errors
<a name="API_CreateStudioLifecycleConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

## See Also
<a name="API_CreateStudioLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateStudioLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateStudioLifecycleConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
