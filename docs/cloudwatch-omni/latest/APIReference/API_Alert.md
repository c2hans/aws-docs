---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Alert.html
---

# Alert
<a name="API_Alert"></a>

Full alert entity, returned by both CreateAlert and GetAlert. A create and a read of the same alert describe it identically except for `state`, which only the read paths populate. UpdateAlert returns an empty response.

## Contents
<a name="API_Alert_Contents"></a>

 ** accountId **   <a name="cloudwatchomni-Type-Alert-accountId"></a>
The AWS account ID that owns the alert.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** alertArn **   <a name="cloudwatchomni-Type-Alert-alertArn"></a>
The Amazon Resource Name (ARN) of the alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-Alert-createdAt"></a>
The timestamp when the alert was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-Alert-name"></a>
The name of the alert.
Type: String
Required: Yes

 ** rule **   <a name="cloudwatchomni-Type-Alert-rule"></a>
The rule that defines how the alert is evaluated.
Type: [Rule](API_Rule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-Alert-updatedAt"></a>
The timestamp when the alert was last updated.
Type: Timestamp
Required: Yes

 ** alertId **   <a name="cloudwatchomni-Type-Alert-alertId"></a>
The stable alert identifier (see `AlertId`), minted on create and immutable across updates. Use it (not `name`) to address the alert on GetAlert/UpdateAlert/DeleteAlert; it is also the ARN's resource id.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** description **   <a name="cloudwatchomni-Type-Alert-description"></a>
An optional description of the alert.
Type: String
Required: No

 ** notificationRules **   <a name="cloudwatchomni-Type-Alert-notificationRules"></a>
The notification rules for the alert.
Type: Array of [NotificationRule](API_NotificationRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** notificationStatus **   <a name="cloudwatchomni-Type-Alert-notificationStatus"></a>
Whether notifications are enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** profileId **   <a name="cloudwatchomni-Type-Alert-profileId"></a>
The ID of the access profile associated with the alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** spaceId **   <a name="cloudwatchomni-Type-Alert-spaceId"></a>
The ID of the space the alert belongs to.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** state **   <a name="cloudwatchomni-Type-Alert-state"></a>
Live evaluation state (read-only, system-managed). Populated by GetAlert. ListAlerts reports state on `AlertSummary` instead, where it stays required.
Absent on CreateAlert: a newly created alert has never been evaluated, so any state reported there would be a default rather than an observation. Call GetAlert for live state. Not @required for that reason — GetAlert always populates it.
 `contributorSummary` is nested inside this member, so it too is absent on CreateAlert.
Type: [AlertStateInfo](API_AlertStateInfo.md) object
Required: No

## See Also
<a name="API_Alert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Alert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Alert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Alert)
