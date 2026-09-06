---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchUpdateJobError.html
---

# BatchUpdateJobError
<a name="API_BatchUpdateJobError"></a>

The error details for a job that could not be updated in a batch update operation.

## Contents
<a name="API_BatchUpdateJobError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-BatchUpdateJobError-code"></a>
The error code.
Type: String
Valid Values: `ConflictException | InternalServerErrorException | ResourceNotFoundException | ValidationException | AccessDeniedException | ThrottlingException`
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchUpdateJobError-farmId"></a>
The farm ID of the job that could not be updated.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchUpdateJobError-jobId"></a>
The job ID of the job that could not be updated.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-BatchUpdateJobError-message"></a>
The error message.
Type: String
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchUpdateJobError-queueId"></a>
The queue ID of the job that could not be updated.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchUpdateJobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchUpdateJobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchUpdateJobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchUpdateJobError)
