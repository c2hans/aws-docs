---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobError.html
---

# ProtectedJobError
<a name="API_ProtectedJobError"></a>

Details of the error that caused the protected job to fail.

## Contents
<a name="API_ProtectedJobError_Contents"></a>

 ** code **   <a name="API-Type-ProtectedJobError-code"></a>
A code that identifies the category of the failure. Valid values are:
+  `MALFORMED_SCRIPT` – The job script or its execution environment is not valid (code, imports, entry point, virtual environment, or dependencies).
+  `RESOURCE_NOT_FOUND` – A referenced resource doesn't exist.
+  `INVALID_RESOURCE` – A referenced resource exists, but you can't use it because its configuration, state, or data is not valid.
+  `RESOURCE_ACCESS_DENIED` – A required permission is missing for a data source or resource.
+  `INSUFFICIENT_COMPUTE` – The job exceeded the available compute (memory, disk, or time).
+  `TRANSIENT_ERROR` – A temporary condition caused the failure, such as throttling or a network interruption.
+  `INTERNAL_ERROR` – AWS Clean Rooms encountered an unexpected error. If the error persists, contact AWS Support.
+  `UNKNOWN_ERROR` – The failure couldn't be classified.
For more information about error codes, see [https://docs.aws.amazon.com/clean-rooms/latest/userguide/error-codes.html](https://docs.aws.amazon.com/clean-rooms/latest/userguide/error-codes.html) in the AWS Clean Rooms User Guide.
Type: String
Required: Yes

 ** message **   <a name="API-Type-ProtectedJobError-message"></a>
A description of why the protected job failed.
Type: String
Required: Yes

 ** retry **   <a name="API-Type-ProtectedJobError-retry"></a>
Contains information about whether running the same protected job again might succeed.
Type: [RetryInfo](API_RetryInfo.md) object
Required: No

## See Also
<a name="API_ProtectedJobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobError)
