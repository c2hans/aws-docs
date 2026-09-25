---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateView.html
---

# UpdateView
<a name="API_UpdateView"></a>

Updates an existing view's definition and/or description.

Only the fields you provide are changed. Managed views cannot be updated.

## Request Parameters
<a name="API_UpdateView_RequestParameters"></a>

 ** definition **
The new SQL query that defines the view. Omit to leave unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** description **
The new description of the view. Omit to leave unchanged.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** name **
The name of the view to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 256.
Pattern: `view\.[a-z0-9][a-z0-9_-]{0,250}`
Required: Yes

## Response Elements
<a name="API_UpdateView_ResponseElements"></a>

The following elements are returned by the service.

 ** arn **
The ARN of the view.
Type: String

 ** createdAt **
The timestamp when the view was created.
Type: Timestamp

 ** definition **
The SQL query that defines the view.
Type: String

 ** description **
The description of the view.
Type: String

 ** name **
The name of the view.
Type: String

 ** type **
The ownership category of the view.
Type: String
Valid Values: `USER | MANAGED`

 ** updatedAt **
The timestamp when the view was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The operation could not be completed because of a conflict with the current state of the resource.
 ** conflictType **
The type of conflict that caused the request to fail. Not always present.
 ** errorCode **
The error code associated with the conflict. Not always present.
 ** message **
A human-readable description of the conflict.
 ** resourceId **
The identifier of the resource that is in conflict. Not always present.
 ** resourceType **
The type of the resource that is in conflict. Not always present.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** errorCode **
The error code associated with the failure.
 ** resourceId **
The identifier of the resource that could not be found. Not always present.
 ** resourceType **
The type of the resource that could not be found. Not always present.
HTTP Status Code: 404

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
<a name="API_UpdateView_Examples"></a>

### Update a view's definition
<a name="API_UpdateView_Example_1"></a>

The following example changes only the definition; the omitted description is left unchanged. Managed views cannot be updated. The response carries the view's effective configuration. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_UpdateView_Example_1_Request"></a>

```
{
  "definition": "SELECT resource['attributes']['service.name'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE status['code'] IN ('2', 'ERROR') GROUP BY service",
  "name": "view.service_errors"
}
```

#### Sample Response
<a name="API_UpdateView_Example_1_Response"></a>

```
{
  "arn": "arn:aws:cloudwatch:us-east-1:123456789012:view/view.service_errors",
  "createdAt": "2026-09-16T14:22:31Z",
  "definition": "SELECT resource['attributes']['service.name'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE status['code'] IN ('2', 'ERROR') GROUP BY service",
  "description": "Error counts by service",
  "name": "view.service_errors",
  "type": "USER",
  "updatedAt": "2026-09-17T09:11:52Z"
}
```

## See Also
<a name="API_UpdateView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/UpdateView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/UpdateView)
