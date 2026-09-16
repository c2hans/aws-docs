---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_TerminateServiceJobsErrorDetail.html
---

# TerminateServiceJobsErrorDetail
<a name="API_TerminateServiceJobsErrorDetail"></a>

An object that contains the details of a service job that couldn't be terminated by a `TerminateServiceJobs` operation.

## Contents
<a name="API_TerminateServiceJobsErrorDetail_Contents"></a>

 ** code **   <a name="Batch-Type-TerminateServiceJobsErrorDetail-code"></a>
An error code that identifies the reason the service job couldn't be terminated. Valid values are:
+  `ValidationException` – A service job identifier in the request is malformed or isn't valid.
+  `ClientException` – The request failed because of a client error.
+  `ThrottlingException` – The request was throttled. Retry the request.
+  `ServerException` – An internal error occurred. Retry the request.
+  `AccessDenied` – The caller isn't authorized to perform the action on the specified service job.
Type: String
Required: Yes

 ** job **   <a name="Batch-Type-TerminateServiceJobsErrorDetail-job"></a>
The service job ID of the service job that couldn't be terminated.
Type: String
Required: Yes

 ** message **   <a name="Batch-Type-TerminateServiceJobsErrorDetail-message"></a>
A message that describes the reason the service job couldn't be terminated.
Type: String
Required: Yes

## See Also
<a name="API_TerminateServiceJobsErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TerminateServiceJobsErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TerminateServiceJobsErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TerminateServiceJobsErrorDetail)
