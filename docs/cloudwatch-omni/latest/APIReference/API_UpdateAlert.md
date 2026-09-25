---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_UpdateAlert.html
---

# UpdateAlert
<a name="API_UpdateAlert"></a>

Updates an existing alert.

Only non-null fields overwrite existing values.

## Request Parameters
<a name="API_UpdateAlert_RequestParameters"></a>

 ** alertId **
The alert to update.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

 ** description **
A new description of the alert. Omit to leave unchanged.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** name **
A new display name for the alert. Omit to leave the name unchanged (apply-if-present / PATCH). Same constraints as CreateAlert.name; the name is not the alert's identity, so a rename never changes the alertId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.@~()-]+`
Required: No

 ** notificationRules **
Replaces the entire notification rule list when present; full-replace, not merge. Omitted = leave existing rules unchanged. An empty list clears all rules (the alert keeps evaluating; only notifications stop).
Type: Array of [NotificationRule](API_NotificationRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** notificationsEnabled **
Whether actions (notifications) are enabled for this alert. Omitted = leave existing value unchanged.
Type: Boolean
Required: No

 ** profileId **
The ID of the access profile associated with the alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** rule **
The rule that defines how the alert is evaluated. Omit to leave unchanged. Each sub-block is replaced whole when present: `query`, `condition`, `evaluation` and `noData` are applied only when supplied, and within a supplied block an omitted optional member is cleared to unset (null/absent) rather than preserved from the stored alert or defaulted. See `AlertCondition` and `AlertEvaluation`.
Type: [Rule](API_Rule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** spaceId **
The unique ID of the space.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Errors
<a name="API_UpdateAlert_Errors"></a>

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
<a name="API_UpdateAlert_Examples"></a>

### Raise an alert's thresholds
<a name="API_UpdateAlert_Example_1"></a>

The following example replaces only the condition of an alert's rule; the query, the evaluation cadence and the notification rules are left unchanged. A supplied condition is replaced whole rather than merged, so every threshold to keep is sent again. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_UpdateAlert_Example_1_Request"></a>

```
{
  "alertId": "c3d4e5f67a8b4c9d8e0f1a2b3c4d5e6f",
  "rule": {
    "telemetryRule": {
      "condition": {
        "comparator": "GT",
        "criticalThreshold": 400.0,
        "thresholdField": "error_count",
        "thresholdMode": "FIELD_VALUE",
        "warningThreshold": 100.0
      }
    }
  },
  "spaceId": "a1b2c3d4-5e6f-4a3b-8c9d-0e1f2a3b4c5d"
}
```

#### Sample Response
<a name="API_UpdateAlert_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateAlert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/UpdateAlert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/UpdateAlert)
