---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteProcessingJob.html
---

# DeleteProcessingJob
<a name="API_DeleteProcessingJob"></a>

Deletes a processing job. After Amazon SageMaker deletes a processing job, all of the metadata for the processing job is lost. You can delete only processing jobs that are in a terminal state (`Stopped`, `Failed`, or `Completed`). You cannot delete a job that is in the `InProgress` or `Stopping` state. After deleting the job, you can reuse its name to create another processing job.

## Request Syntax
<a name="API_DeleteProcessingJob_RequestSyntax"></a>

```
{
   "ProcessingJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProcessingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProcessingJobName](#API_DeleteProcessingJob_RequestSyntax) **   <a name="sagemaker-DeleteProcessingJob-request-ProcessingJobName"></a>
The name of the processing job to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Elements
<a name="API_DeleteProcessingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProcessingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProcessingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteProcessingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteProcessingJob)
