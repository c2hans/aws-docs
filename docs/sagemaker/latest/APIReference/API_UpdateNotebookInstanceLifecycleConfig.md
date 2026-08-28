---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateNotebookInstanceLifecycleConfig.html
---

# UpdateNotebookInstanceLifecycleConfig
<a name="API_UpdateNotebookInstanceLifecycleConfig"></a>

Updates a notebook instance lifecycle configuration created with the [CreateNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html) API.

**Note**
Updates to lifecycle configurations affect all notebook instances using that configuration upon their next start. Lifecycle configuration scripts execute with root access and the notebook instance's IAM execution role privileges. Grant this permission only to trusted principals. See [Customize a Notebook Instance Using a Lifecycle Configuration Script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) for security best practices.

## Request Syntax
<a name="API_UpdateNotebookInstanceLifecycleConfig_RequestSyntax"></a>

```
{
   "NotebookInstanceLifecycleConfigName": "{{string}}",
   "OnCreate": [
      {
         "Content": "{{string}}"
      }
   ],
   "OnStart": [
      {
         "Content": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateNotebookInstanceLifecycleConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookInstanceLifecycleConfigName](#API_UpdateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstanceLifecycleConfig-request-NotebookInstanceLifecycleConfigName"></a>
The name of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [OnCreate](#API_UpdateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstanceLifecycleConfig-request-OnCreate"></a>
The shell script that runs only once, when you create a notebook instance. The shell script must be a base64-encoded string.
Type: Array of [NotebookInstanceLifecycleHook](API_NotebookInstanceLifecycleHook.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [OnStart](#API_UpdateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-UpdateNotebookInstanceLifecycleConfig-request-OnStart"></a>
The shell script that runs every time you start a notebook instance, including when you create the notebook instance. The shell script must be a base64-encoded string.
Type: Array of [NotebookInstanceLifecycleHook](API_NotebookInstanceLifecycleHook.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Elements
<a name="API_UpdateNotebookInstanceLifecycleConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateNotebookInstanceLifecycleConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNotebookInstanceLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateNotebookInstanceLifecycleConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
