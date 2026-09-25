---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListOmniDashboards.html
---

# ListOmniDashboards
<a name="API_ListOmniDashboards"></a>

Returns the dashboards in a space, optionally filtered by name prefix.

## Request Parameters
<a name="API_ListOmniDashboards_RequestParameters"></a>

 ** maxResults **
The maximum number of dashboards to return per page. Defaults to 100. A page can contain fewer results than this value even when more results remain; continue while nextToken is present.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** namePrefix **
Filter to dashboards whose name starts with this prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: No

 ** nextToken **
A token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_ListOmniDashboards_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of dashboard summaries.
Type: Array of [OmniDashboardSummary](API_OmniDashboardSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListOmniDashboards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_ListOmniDashboards_Examples"></a>

### List dashboards in a space
<a name="API_ListOmniDashboards_Example_1"></a>

The following example lists the first page of dashboards in a space and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListOmniDashboards_Example_1_Request"></a>

```
{
  "maxResults": 50,
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_ListOmniDashboards_Example_1_Response"></a>

```
{
  "items": [
    {
      "arn": "arn:aws:cloudwatch:us-east-1:123456789012:omni-dashboard/c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
      "createdAt": "2026-09-16T14:22:31Z",
      "createdBy": "arn:aws:iam::123456789012:role/ObservabilityAdmin",
      "dashboardId": "c3d4e5f6-7a8b-4c9d-8e0f-1a2b3c4d5e6f",
      "description": "Overview of service health metrics.",
      "name": "service-health-overview",
      "updatedAt": "2026-09-16T14:22:31Z"
    },
    {
      "arn": "arn:aws:cloudwatch:us-east-1:123456789012:omni-dashboard/d4e5f6a7-8b9c-4d0e-9f1a-2b3c4d5e6f70",
      "createdAt": "2026-09-16T14:22:31Z",
      "createdBy": "arn:aws:iam::123456789012:role/ObservabilityAdmin",
      "dashboardId": "d4e5f6a7-8b9c-4d0e-9f1a-2b3c4d5e6f70",
      "description": "Monthly cost breakdown by service.",
      "name": "cost-explorer-dashboard",
      "updatedAt": "2026-09-16T14:22:31Z"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

## See Also
<a name="API_ListOmniDashboards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListOmniDashboards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListOmniDashboards)
