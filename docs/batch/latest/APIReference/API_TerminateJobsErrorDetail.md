---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_TerminateJobsErrorDetail.html
---

# TerminateJobsErrorDetail
<a name="API_TerminateJobsErrorDetail"></a>

An object that contains the details of a job that couldn't be terminated by a `TerminateJobs` operation.

## Contents
<a name="API_TerminateJobsErrorDetail_Contents"></a>

 ** code **   <a name="Batch-Type-TerminateJobsErrorDetail-code"></a>
An error code that identifies the reason the job couldn't be terminated. Valid values are:
+  `ValidationException` – A job identifier in the request is malformed or isn't valid.
+  `ClientException` – The request failed because of a client error.
+  `ThrottlingException` – The request was throttled. Retry the request.
+  `ServerException` – An internal error occurred. Retry the request.
+  `AccessDenied` – The caller isn't authorized to perform the action on the specified job.
Type: String
Required: Yes

 ** job **   <a name="Batch-Type-TerminateJobsErrorDetail-job"></a>
The AWS Batch job ID of the job that couldn't be terminated.
Type: String
Required: Yes

 ** message **   <a name="Batch-Type-TerminateJobsErrorDetail-message"></a>
A message that describes the reason the job couldn't be terminated.
Type: String
Required: Yes

## See Also
<a name="API_TerminateJobsErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TerminateJobsErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TerminateJobsErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TerminateJobsErrorDetail)
