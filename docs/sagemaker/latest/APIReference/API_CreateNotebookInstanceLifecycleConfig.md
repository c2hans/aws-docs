---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html
---

# CreateNotebookInstanceLifecycleConfig
<a name="API_CreateNotebookInstanceLifecycleConfig"></a>

Creates a lifecycle configuration that you can associate with a notebook instance. A *lifecycle configuration* is a collection of shell scripts that run when you create or start a notebook instance.

Each lifecycle configuration script has a limit of 16384 characters.

The value of the `$PATH` environment variable that is available to both scripts is `/sbin:bin:/usr/sbin:/usr/bin`.

View Amazon CloudWatch Logs for notebook instance lifecycle configurations in log group `/aws/sagemaker/NotebookInstances` in log stream `[notebook-instance-name]/[LifecycleConfigHook]`.

Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.

For information about notebook instance lifestyle configurations, see [Step 2.1: (Optional) Customize a Notebook Instance](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html).

**Note**
Lifecycle configuration scripts execute with root access and the notebook instance's IAM execution role privileges. Grant this permission only to trusted principals. See [Customize a Notebook Instance Using a Lifecycle Configuration Script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) for security best practices.

## Request Syntax
<a name="API_CreateNotebookInstanceLifecycleConfig_RequestSyntax"></a>

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
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateNotebookInstanceLifecycleConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookInstanceLifecycleConfigName](#API_CreateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstanceLifecycleConfig-request-NotebookInstanceLifecycleConfigName"></a>
The name of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [OnCreate](#API_CreateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstanceLifecycleConfig-request-OnCreate"></a>
A shell script that runs only once, when you create a notebook instance. The shell script must be a base64-encoded string.
Type: Array of [NotebookInstanceLifecycleHook](API_NotebookInstanceLifecycleHook.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [OnStart](#API_CreateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstanceLifecycleConfig-request-OnStart"></a>
A shell script that runs every time you start a notebook instance, including when you create the notebook instance. The shell script must be a base64-encoded string.
Type: Array of [NotebookInstanceLifecycleHook](API_NotebookInstanceLifecycleHook.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [Tags](#API_CreateNotebookInstanceLifecycleConfig_RequestSyntax) **   <a name="sagemaker-CreateNotebookInstanceLifecycleConfig-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateNotebookInstanceLifecycleConfig_ResponseSyntax"></a>

```
{
   "NotebookInstanceLifecycleConfigArn": "string"
}
```

## Response Elements
<a name="API_CreateNotebookInstanceLifecycleConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotebookInstanceLifecycleConfigArn](#API_CreateNotebookInstanceLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-CreateNotebookInstanceLifecycleConfig-response-NotebookInstanceLifecycleConfigArn"></a>
The Amazon Resource Name (ARN) of the lifecycle configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateNotebookInstanceLifecycleConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateNotebookInstanceLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateNotebookInstanceLifecycleConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
