---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-how-it-works.html
---

# How it works
<a name="notification-center-how-it-works"></a>

A notification rule is a connector of type `notification` associated to an asset template. When an asset event matches the rule’s trigger, SDMA delivers an alert to the configured recipients through the configured channel.

The governance model is the same as every other connector:

1. An administrator creates a notification rule at the library level, specifying recipients, channel, trigger events, and message templates.

1. The administrator associates the rule with one or more asset templates.

1. When an asset created from one of those templates fires a matching lifecycle event, SDMA delivers the notification.

1. Every delivery is tracked as a connector invocation — visible in the portal with status, timestamp, and result.
