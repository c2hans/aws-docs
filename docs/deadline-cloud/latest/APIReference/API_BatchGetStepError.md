---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetStepError.html
---

# BatchGetStepError
<a name="API_BatchGetStepError"></a>

The error details for a step that could not be retrieved in a batch get operation.

## Contents
<a name="API_BatchGetStepError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-BatchGetStepError-code"></a>
The error code.
Type: String
Valid Values: `InternalServerErrorException | ResourceNotFoundException | ValidationException | AccessDeniedException | ThrottlingException`
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetStepError-farmId"></a>
The farm ID of the step that could not be retrieved.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetStepError-jobId"></a>
The job ID of the step that could not be retrieved.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-BatchGetStepError-message"></a>
The error message.
Type: String
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetStepError-queueId"></a>
The queue ID of the step that could not be retrieved.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-BatchGetStepError-stepId"></a>
The step ID of the step that could not be retrieved.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetStepError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetStepError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetStepError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetStepError)
