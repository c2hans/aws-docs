---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionActionError.html
---

# BatchGetSessionActionError
<a name="API_BatchGetSessionActionError"></a>

The error details for a session action that could not be retrieved in a batch get operation.

## Contents
<a name="API_BatchGetSessionActionError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-BatchGetSessionActionError-code"></a>
The error code.
Type: String
Valid Values: `InternalServerErrorException | ResourceNotFoundException | ValidationException`
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetSessionActionError-farmId"></a>
The farm ID of the session action that could not be retrieved.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetSessionActionError-jobId"></a>
The job ID of the session action that could not be retrieved.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-BatchGetSessionActionError-message"></a>
The error message.
Type: String
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetSessionActionError-queueId"></a>
The queue ID of the session action that could not be retrieved.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionActionId **   <a name="deadlinecloud-Type-BatchGetSessionActionError-sessionActionId"></a>
The session action ID of the session action that could not be retrieved.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## See Also
<a name="API_BatchGetSessionActionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionActionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionActionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionActionError)
