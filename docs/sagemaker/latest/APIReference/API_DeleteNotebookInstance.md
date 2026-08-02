---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteNotebookInstance.html
---

# DeleteNotebookInstance
<a name="API_DeleteNotebookInstance"></a>

 Deletes an SageMaker AI notebook instance. Before you can delete a notebook instance, you must call the `StopNotebookInstance` API.

**Important**
When you delete a notebook instance, you lose all of your data. SageMaker AI removes the ML compute instance, and deletes the ML storage volume and the network interface associated with the notebook instance.

## Request Syntax
<a name="API_DeleteNotebookInstance_RequestSyntax"></a>

```
{
   "NotebookInstanceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteNotebookInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookInstanceName](#API_DeleteNotebookInstance_RequestSyntax) **   <a name="sagemaker-DeleteNotebookInstance-request-NotebookInstanceName"></a>
The name of the SageMaker AI notebook instance to delete.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

## Response Elements
<a name="API_DeleteNotebookInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteNotebookInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteNotebookInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteNotebookInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteNotebookInstance)
