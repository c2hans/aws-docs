---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeNotebookInstanceLifecycleConfig.html
---

# DescribeNotebookInstanceLifecycleConfig
<a name="API_DescribeNotebookInstanceLifecycleConfig"></a>

Returns a description of a notebook instance lifecycle configuration.

For information about notebook instance lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).

## Request Syntax
<a name="API_DescribeNotebookInstanceLifecycleConfig_RequestSyntax"></a>

```
{
   "NotebookInstanceLifecycleConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeNotebookInstanceLifecycleConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookInstanceLifecycleConfigName](#API_DescribeNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-request-NotebookInstanceLifecycleConfigName"></a>
The name of the lifecycle configuration to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

## Response Syntax
<a name="API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "LastModifiedTime": number,
   "NotebookInstanceLifecycleConfigArn": "string",
   "NotebookInstanceLifecycleConfigName": "string",
   "OnCreate": [
      {
         "Content": "string"
      }
   ],
   "OnStart": [
      {
         "Content": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeNotebookInstanceLifecycleConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-response-CreationTime"></a>
A timestamp that tells when the lifecycle configuration was created.
Type: Timestamp

 ** [LastModifiedTime](#API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-response-LastModifiedTime"></a>
A timestamp that tells when the lifecycle configuration was last modified.
Type: Timestamp

 ** [NotebookInstanceLifecycleConfigArn](#API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-response-NotebookInstanceLifecycleConfigArn"></a>
The Amazon Resource Name (ARN) of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [NotebookInstanceLifecycleConfigName](#API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-response-NotebookInstanceLifecycleConfigName"></a>
The name of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [OnCreate](#API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-response-OnCreate"></a>
The shell script that runs only once, when you create a notebook instance.
Type: Array of [NotebookInstanceLifecycleHook](API_NotebookInstanceLifecycleHook.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [OnStart](#API_DescribeNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeNotebookInstanceLifecycleConfig-response-OnStart"></a>
The shell script that runs every time you start a notebook instance, including when you create the notebook instance.
Type: Array of [NotebookInstanceLifecycleHook](API_NotebookInstanceLifecycleHook.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

## Errors
<a name="API_DescribeNotebookInstanceLifecycleConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeNotebookInstanceLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeNotebookInstanceLifecycleConfig)
