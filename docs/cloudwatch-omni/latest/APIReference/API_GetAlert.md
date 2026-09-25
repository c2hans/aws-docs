---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAlert.html
---

# GetAlert
<a name="API_GetAlert"></a>

Retrieves a single alert by its identifier.

Use ListAlerts to enumerate alerts in the space.

## Request Parameters
<a name="API_GetAlert_RequestParameters"></a>

 ** alertId **
The alert to retrieve.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Elements
<a name="API_GetAlert_ResponseElements"></a>

The following element is returned by the service.

 ** alert **
The full alert entity.
Type: [Alert](API_Alert.md) object

## Errors
<a name="API_GetAlert_Errors"></a>

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
<a name="API_GetAlert_Examples"></a>

### Retrieve an alert
<a name="API_GetAlert_Example_1"></a>

The following example retrieves an alert by its identifier, including the live evaluation state that CreateAlert does not report. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_GetAlert_Example_1_Request"></a>

```
{
  "alertId": "c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_GetAlert_Example_1_Response"></a>

```
{
  "alert": {
    "accountId": "123456789012",
    "alertArn": "arn:aws:cloudwatch:us-east-1:123456789012:alert/c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
    "alertId": "c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
    "createdAt": "2026-09-16T14:22:31Z",
    "description": "Alerts when a service logs more errors than its accepted rate.",
    "name": "service-error-count-elevated",
    "notificationRules": [
      {
        "target": {
          "arn": "arn:aws:cloudwatch:us-east-1:123456789012:integration/a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
          "metadata": {
            "channel": "oncall-alerts"
          },
          "type": "slack"
        },
        "trigger": {
          "stateValues": [
            "CRITICAL"
          ]
        }
      }
    ],
    "notificationStatus": "ENABLED",
    "profileId": "analyst-readonly",
    "rule": {
      "telemetryRule": {
        "condition": {
          "comparator": "GT",
          "criticalThreshold": 200.0,
          "thresholdField": "error_count",
          "thresholdMode": "FIELD_VALUE",
          "warningThreshold": 50.0
        },
        "evaluation": {
          "intervalSeconds": 300,
          "pendingDurationSeconds": 600,
          "recoveryDurationSeconds": 300
        },
        "noData": {
          "treatAs": "NODATA"
        },
        "query": {
          "expression": "SELECT resource['attributes']['service.name'] AS service, COUNT(*) AS error_count FROM "logs.default" WHERE severityText = 'ERROR' GROUP BY service",
          "language": "SQL"
        }
      }
    },
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
  }
}
```

## See Also
<a name="API_GetAlert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/GetAlert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/GetAlert)
