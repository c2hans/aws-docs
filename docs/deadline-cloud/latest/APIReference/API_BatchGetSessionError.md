---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionError.html
---

# BatchGetSessionError
<a name="API_BatchGetSessionError"></a>

The error details for a session that could not be retrieved in a batch get operation.

## Contents
<a name="API_BatchGetSessionError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-BatchGetSessionError-code"></a>
The error code.
Type: String
Valid Values: `InternalServerErrorException | ResourceNotFoundException | ValidationException`
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetSessionError-farmId"></a>
The farm ID of the session that could not be retrieved.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetSessionError-jobId"></a>
The job ID of the session that could not be retrieved.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-BatchGetSessionError-message"></a>
The error message.
Type: String
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetSessionError-queueId"></a>
The queue ID of the session that could not be retrieved.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionId **   <a name="deadlinecloud-Type-BatchGetSessionError-sessionId"></a>
The session ID of the session that could not be retrieved.
Type: String
Pattern: `session-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetSessionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionError)
