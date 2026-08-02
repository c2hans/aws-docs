---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-config-reference.html
---

# Configuration reference
<a name="notification-center-config-reference"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `notificationConfig.recipients`  | Yes | Array of recipient entries. Each entry specifies a user (`principalId` \+ `"principalType": "USER"`), a group (`principalId` \+ `"principalType": "GROUP"`), or a project role (`"role": "OWNER"` \| `"MANAGER"` \| `"VIEWER"`). |
|  `notificationConfig.channels`  | Yes | Array with exactly one channel entry. Specify `"type": "slack"`, `"type": "inApp"`, or `"type": "email"`. |
|  `notificationConfig.channels[].webhookUrlSecretArn`  | Slack only | ARN of the Secrets Manager secret containing the Slack webhook URL. |
|  `notificationConfig.messages`  | No | Message templates. Either a flat array of strings (applied to all events), or a per-resource-type object with keys `asset`, `project`, `file`, and/or `default`. Supports `${eventName}` and all standard SDMA field variables. Multiple entries are concatenated with newlines. If omitted, defaults to `"{resourceName} — {eventName}"`. |
|  `triggers[].steps`  | Yes | Array with one entry: `[{"stepType": "notification"}]`. |
|  `triggers[].resources`  | Yes | Resource types that activate this rule: `"asset"`, `"project"`, or `"file"`. |
|  `triggers[].events`  | Yes | Lifecycle events that activate this rule. See [Connector configuration](connector-configuration.md) for supported event types. |
|  `triggers[].filter`  | No | Optional filter. Use `stateFilter` to restrict delivery to specific asset states (for example, `["ERROR", "FAILED"]`). |
