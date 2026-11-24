---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-recipients.html
---

# Recipients

Recipients determine who receives in-app and email notifications. For Slack, the webhook URL is the destination — the recipients list is not used for routing.

Recipients are resolved at delivery time. You can specify users, groups, or project roles:

| Recipient type | Description |
| --- | --- |
| User | A specific portal user, identified by their account ID. |
| Group | A user group. Members are resolved dynamically at send time. |
| Role | A project role (`OWNER`, `MANAGER`, `CONTRIBUTOR`, or `VIEWER`). All users with that role in the asset’s project receive the notification. |

Recipients are validated as resource members at rule creation time and re-checked at delivery time. Non-members are silently skipped.

## Send Email to Addresses You List
<a name="notification-center-email-addresses"></a>

An email channel can also send to addresses that are not user accounts, such as a team alias or a shared mailbox. List them in `emailAddresses`. In the following example, replace `site-surveys@example.com` with your own address:

```json
"channels": [
  {
    "type": "email",
    "emailAddresses": ["site-surveys@example.com"]
  }
]
```
+ SDMA sends one email to each address. An address that is also a recipient’s address receives one email, not two.
+ To send only to the listed addresses, set `includeRecipientEmails` to `false`. SDMA then skips recipient resolution and the user lookups. `emailAddresses` is required when `includeRecipientEmails` is `false`.
+  `emailAddresses` and `includeRecipientEmails` are valid on email channels only.
