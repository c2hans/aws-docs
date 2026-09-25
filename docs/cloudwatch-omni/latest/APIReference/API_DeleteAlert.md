---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteAlert.html
---

# DeleteAlert
<a name="API_DeleteAlert"></a>

Deletes an alert by its identifier.

Idempotent: deleting an alert that has already been removed succeeds without error.

## Request Parameters
<a name="API_DeleteAlert_RequestParameters"></a>

 ** alertId **
The alert to delete.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Errors
<a name="API_DeleteAlert_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_DeleteAlert_Examples"></a>

### Delete an alert
<a name="API_DeleteAlert_Example_1"></a>

The following example removes an alert from a space. Deleting an alert that has already been removed succeeds without error. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_DeleteAlert_Example_1_Request"></a>

```
{
  "alertId": "c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_DeleteAlert_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteAlert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/DeleteAlert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/DeleteAlert)
