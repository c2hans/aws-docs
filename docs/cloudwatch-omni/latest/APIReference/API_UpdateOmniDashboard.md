---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateOmniDashboard.html
---

# UpdateOmniDashboard
<a name="API_UpdateOmniDashboard"></a>

Updates an existing dashboard within a space.

Only the provided fields are changed; omitted fields are left unchanged.

## Request Parameters
<a name="API_UpdateOmniDashboard_RequestParameters"></a>

 ** body **
The new dashboard definition, as a JSON document. Maximum 1 MiB. Omit to leave unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

 ** dashboardId **
The unique ID of the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** description **
A new description of the dashboard. Omit to leave unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **
A new name for the dashboard. Omit to leave unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: No

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_UpdateOmniDashboard_ResponseElements"></a>

The following element is returned by the service.

 ** omniDashboard **
The dashboard.
Type: [OmniDashboard](API_OmniDashboard.md) object

## Errors
<a name="API_UpdateOmniDashboard_Errors"></a>

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

 ** ServiceQuotaExceededException **
A service quota was exceeded.
HTTP Status Code: 402

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
<a name="API_UpdateOmniDashboard_Examples"></a>

### Update a dashboard body
<a name="API_UpdateOmniDashboard_Example_1"></a>

The following example updates only the body of a dashboard; the name and description are left unchanged. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_UpdateOmniDashboard_Example_1_Request"></a>

```
{
  "body": "{"widgets":[{"type":"metric","x":0,"y":0,"width":24,"height":6,"properties":{"metrics":[["AWS/Lambda","Errors","FunctionName","OrderProcessor"],["AWS/Lambda","Throttles","FunctionName","OrderProcessor"]],"region":"us-east-1","title":"Lambda Errors and Throttles"}}]}",
  "dashboardId": "c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_UpdateOmniDashboard_Example_1_Response"></a>

```
{
  "omniDashboard": {
    "arn": "arn:aws:cloudwatch:us-east-1:123456789012:omni-dashboard/c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
    "body": "{"widgets":[{"type":"metric","x":0,"y":0,"width":24,"height":6,"properties":{"metrics":[["AWS/Lambda","Errors","FunctionName","OrderProcessor"],["AWS/Lambda","Throttles","FunctionName","OrderProcessor"]],"region":"us-east-1","title":"Lambda Errors and Throttles"}}]}",
    "createdAt": "2026-09-16T14:22:31Z",
    "createdBy": "arn:aws:iam::123456789012:role/ObservabilityAdmin",
    "dashboardId": "c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
    "description": "Overview of service health metrics.",
    "name": "service-health-overview",
    "tags": {
      "Team": "observability"
    },
    "updatedAt": "2026-09-17T09:11:52Z"
  }
}
```

## See Also
<a name="API_UpdateOmniDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/UpdateOmniDashboard)
