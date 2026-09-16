---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_CancelJobsErrorDetail.html
---

# CancelJobsErrorDetail
<a name="API_CancelJobsErrorDetail"></a>

An object that contains the details of a job that couldn't be cancelled by a `CancelJobs` operation.

## Contents
<a name="API_CancelJobsErrorDetail_Contents"></a>

 ** code **   <a name="Batch-Type-CancelJobsErrorDetail-code"></a>
An error code that identifies the reason the job couldn't be cancelled. Valid values are:
+  `ValidationException` – A job identifier in the request is malformed or isn't valid.
+  `ClientException` – The request failed because of a client error.
+  `ThrottlingException` – The request was throttled. Retry the request.
+  `ServerException` – An internal error occurred. Retry the request.
+  `AccessDenied` – The caller isn't authorized to perform the action on the specified job.
Type: String
Required: Yes

 ** job **   <a name="Batch-Type-CancelJobsErrorDetail-job"></a>
The AWS Batch job ID of the job that couldn't be cancelled.
Type: String
Required: Yes

 ** message **   <a name="Batch-Type-CancelJobsErrorDetail-message"></a>
A message that describes the reason the job couldn't be cancelled.
Type: String
Required: Yes

## See Also
<a name="API_CancelJobsErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CancelJobsErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CancelJobsErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CancelJobsErrorDetail)
