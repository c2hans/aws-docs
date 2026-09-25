---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAlerts.html
---

# ListAlerts
<a name="API_ListAlerts"></a>

Lists alerts within a space, optionally filtered by exact name(s), a single name prefix, or exact alertId(s), with pagination.

Use GetAlert to retrieve a single alert's full detail.

## Request Parameters
<a name="API_ListAlerts_RequestParameters"></a>

 ** filterCriteria **
Filter criteria narrowing which alerts are returned. All members are optional; the three name/id filters are mutually exclusive.
Type: [AlertFilterCriteria](API_AlertFilterCriteria.md) object
Required: No

 ** maxResults **
The maximum number of alerts to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** sortBy **
The field to sort results by.
Type: String
Valid Values: `NAME | STATE`
Required: No

 ** sortOrder **
The order in which to sort results.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_ListAlerts_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
The list of alert summaries.
Type: Array of [AlertSummary](API_AlertSummary.md) objects

 ** nextToken **
A token to retrieve the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAlerts_Errors"></a>

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
<a name="API_ListAlerts_Examples"></a>

### List alerts in a space
<a name="API_ListAlerts_Example_1"></a>

The following example lists the first page of alerts in a space, sorted by state, and returns a nextToken to retrieve the next page. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_ListAlerts_Example_1_Request"></a>

```
{
  "filterCriteria": {
    "namePrefix": "service-",
    "stateValue": [
      "WARNING",
      "CRITICAL"
    ]
  },
  "maxResults": 50,
  "sortBy": "STATE",
  "sortOrder": "DESC",
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_ListAlerts_Example_1_Response"></a>

```
{
  "items": [
    {
      "alertArn": "arn:aws:cloudwatch:us-east-1:123456789012:alert/c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
      "alertId": "c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
      "createdAt": "2026-09-16T14:22:31Z",
      "name": "service-error-count-elevated",
      "notificationStatus": "ENABLED",
      "profileId": "analyst-readonly",
      "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
      "state": {
        "contributorSummary": {
          "criticalCount": 1,
          "warningCount": 3
        },
        "transitionedAt": "2026-09-17T09:11:52Z",
        "value": "CRITICAL"
      },
      "updatedAt": "2026-09-17T09:11:52Z"
    },
    {
      "alertArn": "arn:aws:cloudwatch:us-east-1:123456789012:alert/d4e5f6a78b9c4d0e9f1a2b3c4d5e6f70",
      "alertId": "d4e5f6a78b9c4d0e9f1a2b3c4d5e6f70",
      "createdAt": "2026-09-16T14:22:31Z",
      "name": "service-checkout-5xx-responses",
      "notificationStatus": "DISABLED",
      "profileId": "analyst-readonly",
      "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
      "state": {
        "data": {
          "thresholdBreached": 14.0
        },
        "transitionedAt": "2026-09-17T09:11:52Z",
        "value": "WARNING"
      },
      "updatedAt": "2026-09-16T14:22:31Z"
    }
  ],
  "nextToken": "eyJvZmZzZXQiOjIwfQ=="
}
```

## See Also
<a name="API_ListAlerts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/ListAlerts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/ListAlerts)
