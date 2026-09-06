---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobDetailsError.html
---

# JobDetailsError
<a name="API_JobDetailsError"></a>

The details of a job error.

## Contents
<a name="API_JobDetailsError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-JobDetailsError-code"></a>
The error code.
Type: String
Valid Values: `AccessDeniedException | InternalServerException | ValidationException | ResourceNotFoundException | MaxPayloadSizeExceeded | ConflictException`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-JobDetailsError-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-JobDetailsError-message"></a>
The error message detailing the error's cause.
Type: String
Required: Yes

## See Also
<a name="API_JobDetailsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobDetailsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobDetailsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobDetailsError)
