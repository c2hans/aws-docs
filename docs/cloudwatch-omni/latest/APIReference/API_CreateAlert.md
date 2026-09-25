---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateAlert.html
---

# CreateAlert
<a name="API_CreateAlert"></a>

Creates a new alert within a space.

Use GetAlert and ListAlerts to retrieve alerts, UpdateAlert to modify one, and DeleteAlert to remove it.

## Request Parameters
<a name="API_CreateAlert_RequestParameters"></a>

 ** clientToken **
Idempotency token for safe retries. Retrying with the same token within the idempotency window returns the original alert instead of creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** description **
An optional description of the alert.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** name **
Alert name, for display. Max 256 (the AlarmName budget). Not the alert's identity: the backend mints a separate uuid as the `AlertId`, so the name need not be unique within a space and addressing an alert never depends on it. UpdateAlert accepts a new name to rename the alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: Yes

 ** notificationRules **
The notification rules that determine when and where notifications are sent.
Type: Array of [NotificationRule](API_NotificationRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** notificationsEnabled **
Whether actions (notifications) are enabled for this alert. Defaults to true when omitted.
Type: Boolean
Required: No

 ** profileId **
The ID of the access profile the alert uses to evaluate its query and execute notifications. The caller supplies it: there is no managed alert profile, and the service does not pick one on the caller's behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** rule **
The rule that defines how the alert is evaluated.
Type: [Rule](API_Rule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** spaceId **
The unique ID of the space to create the alert in.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** tags **
The tags to associate with the alert.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateAlert_ResponseElements"></a>

The following elements are returned by the service.

 ** alert **
The alert that was created. The same `Alert` shape GetAlert returns, so a caller need not read the alert back to learn its timestamps or its minted alert id.
 `alert.state` is absent here — see the `state` member of `Alert`. Every other member is populated exactly as GetAlert populates it.
Type: [Alert](API_Alert.md) object

 ** alertArn **
Deprecated. Use `alert.alertArn`, which carries the same value. Kept so an existing caller keeps working while it moves to `alert`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`

## Errors
<a name="API_CreateAlert_Errors"></a>

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
<a name="API_CreateAlert_Examples"></a>

### Create an alert on a field value
<a name="API_CreateAlert_Example_1"></a>

The following example creates an alert whose threshold is compared against a named field of each result row, so every service the query groups by is tracked as its own contributor. FIELD\_VALUE requires thresholdField. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateAlert_Example_1_Request"></a>

```
{
  "clientToken": "3f2a9c1e-7b04-4d8a-9e15-6c2b8d0f4a73",
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
  "notificationsEnabled": true,
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
  "tags": {
    "Team": "observability"
  }
}
```

#### Sample Response
<a name="API_CreateAlert_Example_1_Response"></a>

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
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

### Create an alert on the number of matching rows
<a name="API_CreateAlert_Example_2"></a>

The following example creates an alert whose threshold is compared against how many rows the query returns, rather than a value within them. COUNT\_OF\_RESULTS takes no thresholdField. Notifications are created disabled, so the alert evaluates and records state without sending anything, and an empty result set is treated as OK rather than as missing data. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateAlert_Example_2_Request"></a>

```
{
  "description": "Counts checkout responses that returned a server error.",
  "name": "service-checkout-5xx-responses",
  "notificationsEnabled": false,
  "profileId": "analyst-readonly",
  "rule": {
    "telemetryRule": {
      "condition": {
        "comparator": "GT",
        "criticalThreshold": 50.0,
        "thresholdMode": "COUNT_OF_RESULTS",
        "warningThreshold": 10.0
      },
      "evaluation": {
        "intervalSeconds": 60,
        "pendingDurationSeconds": 120
      },
      "noData": {
        "treatAs": "OK"
      },
      "query": {
        "expression": "SELECT * FROM "logs.default" WHERE resource['attributes']['service.name'] = 'checkout' AND attributes['http.response.status_code'] >= 500",
        "language": "SQL"
      }
    }
  },
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_CreateAlert_Example_2_Response"></a>

```
{
  "alert": {
    "accountId": "123456789012",
    "alertArn": "arn:aws:cloudwatch:us-east-1:123456789012:alert/d4e5f6a78b9c4d0e9f1a2b3c4d5e6f70",
    "alertId": "d4e5f6a78b9c4d0e9f1a2b3c4d5e6f70",
    "createdAt": "2026-09-16T14:22:31Z",
    "description": "Counts checkout responses that returned a server error.",
    "name": "service-checkout-5xx-responses",
    "notificationStatus": "DISABLED",
    "profileId": "analyst-readonly",
    "rule": {
      "telemetryRule": {
        "condition": {
          "comparator": "GT",
          "criticalThreshold": 50.0,
          "thresholdMode": "COUNT_OF_RESULTS",
          "warningThreshold": 10.0
        },
        "evaluation": {
          "intervalSeconds": 60,
          "pendingDurationSeconds": 120
        },
        "noData": {
          "treatAs": "OK"
        },
        "query": {
          "expression": "SELECT * FROM "logs.default" WHERE resource['attributes']['service.name'] = 'checkout' AND attributes['http.response.status_code'] >= 500",
          "language": "SQL"
        }
      }
    },
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

### Create an alert from a PromQL query
<a name="API_CreateAlert_Example_3"></a>

The following example creates an alert from a PromQL expression instead of SQL. A PromQL rule compares against the series value, which is carried as the `value` field, so the condition is FIELD\_VALUE with thresholdField set to `value`. Notifications go to an Amazon SNS topic, whose ARN is the topic itself rather than an integration. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateAlert_Example_3_Request"></a>

```
{
  "description": "Alerts on the checkout server error rate over a five-minute window.",
  "name": "checkout-error-rate-promql",
  "notificationRules": [
    {
      "target": {
        "arn": "arn:aws:sns:us-east-1:123456789012:checkout-oncall",
        "type": "sns"
      },
      "trigger": {
        "stateValues": [
          "WARNING",
          "CRITICAL"
        ]
      }
    }
  ],
  "profileId": "analyst-readonly",
  "rule": {
    "telemetryRule": {
      "condition": {
        "comparator": "GT",
        "criticalThreshold": 0.1,
        "thresholdField": "value",
        "thresholdMode": "FIELD_VALUE",
        "warningThreshold": 0.05
      },
      "evaluation": {
        "intervalSeconds": 300,
        "pendingDurationSeconds": 300
      },
      "noData": {
        "treatAs": "NODATA"
      },
      "query": {
        "expression": "sum by (service_name) (rate(http_server_errors_total{service_name="checkout"}[5m]))",
        "language": "PROMQL"
      }
    }
  },
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_CreateAlert_Example_3_Response"></a>

```
{
  "alert": {
    "accountId": "123456789012",
    "alertArn": "arn:aws:cloudwatch:us-east-1:123456789012:alert/e5f6a78b9c0d4e1f8a2b3c4d5e6f7081",
    "alertId": "e5f6a78b9c0d4e1f8a2b3c4d5e6f7081",
    "createdAt": "2026-09-16T14:22:31Z",
    "description": "Alerts on the checkout server error rate over a five-minute window.",
    "name": "checkout-error-rate-promql",
    "notificationRules": [
      {
        "target": {
          "arn": "arn:aws:sns:us-east-1:123456789012:checkout-oncall",
          "type": "sns"
        },
        "trigger": {
          "stateValues": [
            "WARNING",
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
          "criticalThreshold": 0.1,
          "thresholdField": "value",
          "thresholdMode": "FIELD_VALUE",
          "warningThreshold": 0.05
        },
        "evaluation": {
          "intervalSeconds": 300,
          "pendingDurationSeconds": 300
        },
        "noData": {
          "treatAs": "NODATA"
        },
        "query": {
          "expression": "sum by (service_name) (rate(http_server_errors_total{service_name="checkout"}[5m]))",
          "language": "PROMQL"
        }
      }
    },
    "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d",
    "updatedAt": "2026-09-16T14:22:31Z"
  }
}
```

## See Also
<a name="API_CreateAlert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateAlert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateAlert)
