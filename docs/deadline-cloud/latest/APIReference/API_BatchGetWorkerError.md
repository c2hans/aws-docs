---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetWorkerError.html
---

# BatchGetWorkerError
<a name="API_BatchGetWorkerError"></a>

The error details for a worker that could not be retrieved in a batch get operation.

## Contents
<a name="API_BatchGetWorkerError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-BatchGetWorkerError-code"></a>
The error code.
Type: String
Valid Values: `InternalServerErrorException | ResourceNotFoundException | ValidationException`
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetWorkerError-farmId"></a>
The farm ID of the worker that could not be retrieved.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-BatchGetWorkerError-fleetId"></a>
The fleet ID of the worker that could not be retrieved.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-BatchGetWorkerError-message"></a>
The error message.
Type: String
Required: Yes

 ** workerId **   <a name="deadlinecloud-Type-BatchGetWorkerError-workerId"></a>
The worker ID of the worker that could not be retrieved.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetWorkerError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetWorkerError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetWorkerError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetWorkerError)
