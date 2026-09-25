---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateOmniDashboard.html
---

# CreateOmniDashboard
<a name="API_CreateOmniDashboard"></a>

Creates a new dashboard within a space.

Use GetOmniDashboard and ListOmniDashboards to retrieve dashboards, UpdateOmniDashboard to modify one, and DeleteOmniDashboard to remove it.

## Request Parameters
<a name="API_CreateOmniDashboard_RequestParameters"></a>

 ** body **
The dashboard definition, as a JSON document. Maximum 1 MiB.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: Yes

 ** clientToken **
Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** description **
An optional description of the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **
A name that identifies the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: Yes

 ** spaceId **
The unique ID of the space to create the dashboard in.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** tags **
The tags to associate with the dashboard.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateOmniDashboard_ResponseElements"></a>

The following element is returned by the service.

 ** omniDashboard **
The dashboard.
Type: [OmniDashboard](API_OmniDashboard.md) object

## Errors
<a name="API_CreateOmniDashboard_Errors"></a>

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
<a name="API_CreateOmniDashboard_Examples"></a>

### Create a dashboard
<a name="API_CreateOmniDashboard_Example_1"></a>

The following example creates a dashboard in a space from a JSON dashboard definition. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateOmniDashboard_Example_1_Request"></a>

```
{
  "body": "{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/Lambda","Errors","FunctionName","OrderProcessor"]],"region":"us-east-1","title":"Lambda Errors"}}]}",
  "clientToken": "3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73",
  "description": "Overview of service health metrics.",
  "name": "service-health-overview",
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
  "tags": {
    "Team": "observability"
  }
}
```

#### Sample Response
<a name="API_CreateOmniDashboard_Example_1_Response"></a>

```
{
  "omniDashboard": {
    "arn": "arn:aws:cloudwatch:us-east-1:123456789012:omni-dashboard/c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
    "body": "{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/Lambda","Errors","FunctionName","OrderProcessor"]],"region":"us-east-1","title":"Lambda Errors"}}]}",
    "createdAt": "2026-09-16T14:22:31Z",
    "createdBy": "arn:aws:iam::123456789012:role/ObservabilityAdmin",
    "dashboardId": "c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
    "description": "Overview of service health metrics.",
    "name": "service-health-overview",
    "tags": {
      "Team": "observability"
    },
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_CreateOmniDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateOmniDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateOmniDashboard)
