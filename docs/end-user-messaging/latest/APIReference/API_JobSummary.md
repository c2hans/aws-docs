---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_JobSummary.html
---

# JobSummary
<a name="API_JobSummary"></a>

Contains summary information about an asynchronous job in a list response.

## Contents
<a name="API_JobSummary_Contents"></a>

 ** createdAt **   <a name="endusermessaging-Type-JobSummary-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** jobId **   <a name="endusermessaging-Type-JobSummary-jobId"></a>
The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** operationType **   <a name="endusermessaging-Type-JobSummary-operationType"></a>
The type of mutating operation that created the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** status **   <a name="endusermessaging-Type-JobSummary-status"></a>
The current lifecycle status of the job.
Type: String
Valid Values: `SUCCESS | PROCESSING | FAILED`
Required: Yes

 ** updatedAt **   <a name="endusermessaging-Type-JobSummary-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** brandProfileId **   <a name="endusermessaging-Type-JobSummary-brandProfileId"></a>
The brand profile that the job operates on. This value is absent for operations that create a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** errorCode **   <a name="endusermessaging-Type-JobSummary-errorCode"></a>
A machine-readable code that identifies why the job failed. This value is present only when the job status is FAILED.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** errorMessage **   <a name="endusermessaging-Type-JobSummary-errorMessage"></a>
A human-readable description of why the job failed. This value is present only when the job status is FAILED.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** resources **   <a name="endusermessaging-Type-JobSummary-resources"></a>
The resources that were created or updated by the job.
Type: Array of [JobResource](API_JobResource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_JobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/JobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/JobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/JobSummary)
