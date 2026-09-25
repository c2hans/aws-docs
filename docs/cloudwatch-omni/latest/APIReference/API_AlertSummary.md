---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AlertSummary.html
---

# AlertSummary
<a name="API_AlertSummary"></a>

Summary representation of an alert used in list responses.

## Contents
<a name="API_AlertSummary_Contents"></a>

 ** alertArn **   <a name="cloudwatchomni-Type-AlertSummary-alertArn"></a>
The Amazon Resource Name (ARN) of the alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-AlertSummary-createdAt"></a>
The timestamp when the alert was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-AlertSummary-name"></a>
The name of the alert.
Type: String
Required: Yes

 ** state **   <a name="cloudwatchomni-Type-AlertSummary-state"></a>
Live evaluation state (read-only, system-managed).
Type: [AlertStateInfo](API_AlertStateInfo.md) object
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-AlertSummary-updatedAt"></a>
The timestamp when the alert was last updated.
Type: Timestamp
Required: Yes

 ** alertId **   <a name="cloudwatchomni-Type-AlertSummary-alertId"></a>
The stable alert identifier (see `Alert.alertId`). Use it to address the alert; it is also the ARN's resource id.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** notificationStatus **   <a name="cloudwatchomni-Type-AlertSummary-notificationStatus"></a>
Whether notifications are enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** profileId **   <a name="cloudwatchomni-Type-AlertSummary-profileId"></a>
The ID of the access profile associated with the alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** spaceId **   <a name="cloudwatchomni-Type-AlertSummary-spaceId"></a>
The ID of the space the alert belongs to.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_AlertSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AlertSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AlertSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AlertSummary)
