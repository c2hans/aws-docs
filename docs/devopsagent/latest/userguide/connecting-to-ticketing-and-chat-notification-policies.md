---
source_url: https://docs.aws.amazon.com/devopsagent/latest/userguide/connecting-to-ticketing-and-chat-notification-policies.html
---

# Notification policies

AWS DevOps Agent posts investigation and mitigation updates, triage notices, and custom agent notifications to every Slack and Microsoft Teams channel connected to your Agent Space. When an investigation starts from a ServiceNow incident, PagerDuty incident, or Dynatrace problem, AWS DevOps Agent also writes its updates back to that incident or problem. These three integrations receive only their own investigations.

To control what an integration receives, set a *notification policy* on it. A notification policy on one of these five integrations has two parts:
+ The **Notifications** toggle turns its posts off or on.
+ A *filter* chooses which investigations post, by priority and source integration, and can leave out triage notices.

You can use a notification policy to do the following:
+ Turn off a noisy Slack channel without removing it.
+ Post Critical and High investigations to an on-call channel, and the rest to another channel.
+ Post investigations from PagerDuty, but not from ServiceNow, to a Microsoft Teams channel.

Each Slack or Microsoft Teams channel is a separate integration with its own policy. An integration without a notification policy receives every post. A notification policy doesn't stop any investigation or custom agent run.

A [code channel](connecting-to-ticketing-and-chat-using-slack-code-channels.md) keeps receiving the updates of its investigation or custom agent run, including its **Investigation** tab, whatever the policy of the channel it was opened from.

On the **Capabilities** tab, the **Notifications** column shows each integration's status: **Enabled**, **Disabled**, or **Custom** for a policy that the console can't show. To see an enabled integration's filter, choose **Enabled**.

![The Notifications column on the Capabilities tab, with the Notification filter popover open.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/notification-policy-column.png)

## Permissions
<a name="permissions"></a>

To set a notification policy, you need `aidevops:UpdateAssociation`, or `aidevops:AssociateService` when you connect the integration. The `AIDevOpsAgentFullAccess` managed policy includes both actions. `AIDevOpsOperatorAppAccessPolicy` includes neither. For more information, see [DevOps Agent IAM permissions](aws-devops-agent-security-devops-agent-iam-permissions.md).

## Turning off notifications for an integration
<a name="turning-off-notifications-for-an-integration"></a>

When notifications are off, AWS DevOps Agent doesn't post investigation updates, mitigation updates, custom agent notifications, or triage notices to the integration. Setup messages, such as the Microsoft Teams welcome message, still post.

Chat in a bidirectional Slack or Microsoft Teams channel keeps working, but an investigation that you start from chat follows the channel's policy and doesn't post there.

To turn off notifications in the console:

1. Open the Agent Space, and choose **Capabilities**.

1. Under **Communications** (Slack, Microsoft Teams, ServiceNow, or PagerDuty) or **Telemetry** (Dynatrace), choose the integration, and then choose **Edit**. For a channel, choose the row whose **Identifier** is the Slack channel ID or the Microsoft Teams channel name.

1. Turn **Notifications** off.

1. Submit the form: choose **Next** for a Slack channel, **Save** for ServiceNow or Dynatrace, **Submit** for Microsoft Teams, or **Associate service** for PagerDuty.

1. To confirm, choose **Turn off notifications**. For a Slack channel, then choose **Add**.

![The Turn off notifications dialog with the Cancel and Turn off notifications buttons.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/notification-policy-turn-off.png)

To turn notifications back on, turn **Notifications** on and submit the form. For a Slack channel, choose **Next** and then **Add**. You can also turn off **Notifications**, or set a filter, when you connect an integration.

If you remove a ServiceNow, PagerDuty, or Dynatrace integration instead, AWS DevOps Agent logs an error in your [vended logs](configuring-integrations-and-knowledge-vended-logs-and-metrics.md) for each update of its running investigations that it can't deliver.

## Choosing which investigations an integration receives
<a name="choosing-which-investigations-an-integration-receives"></a>

A filter applies only to investigations. Custom agent notifications post whenever notifications are on.

To set a filter in the console:

1. Open the integration's **Edit** page, as in steps 1 and 2 of the previous procedure.

1. With **Notifications** on, choose values in **Priority**, **Leave out triage notices**, and, for a Slack or Microsoft Teams channel, **Source integrations**. A field that you leave empty doesn't filter.

1. Submit the form, as in step 4 of the previous procedure. For a Slack channel, then choose **Add**.

![The Notification policy section of a Slack channel's Edit page, with filters set.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/notification-policy-edit.png)

Turning off notifications on the **Edit** page keeps the saved filter for when you turn them back on.

The following table lists the filter fields and the integrations that each one applies to.

| Field | Values | Integrations |
| --- | --- | --- |
| Priority | Critical, High, Medium, Low, Minimal | All five |
| Leave out triage notices | Linked to another investigation, Skipped by triage | All five |
| Source integrations | Up to 25 integrations from the same Agent Space | Slack and Microsoft Teams |

A post goes to the integration only when it matches every field that you set:
+ **Priority**: the investigation or incident that the post is about has a chosen priority.
+ **Leave out triage notices**: the post isn't a triage notice about a chosen outcome.
+ **Source integrations**: the investigation or incident has a chosen source or no source.

### Priority
<a name="priority"></a>

The following table shows the priority that an investigation takes from the incident or problem that starts it.

| AWS DevOps Agent priority | ServiceNow | PagerDuty | Dynatrace event category |
| --- | --- | --- | --- |
| Critical | 1 - Critical | P1 | AVAILABILITY |
| High | 2 - High | P2, or high urgency | ERROR, SLOWDOWN, MONITORING\_UNAVAILABLE |
| Medium | 3 - Moderate | P3 | RESOURCE\_CONTENTION, CUSTOM\_ALERT |
| Low | 4 - Low | P4, or low urgency | INFO |
| Minimal | 5 - Planning | P5 | None |

The PagerDuty column shows PagerDuty's default priority names. AWS DevOps Agent maps a PagerDuty priority by its position in your account's priority list, so a renamed priority maps the same way. A PagerDuty incident that has no priority, or whose priority AWS DevOps Agent can't look up, uses its urgency.

An investigation's priority follows a PagerDuty incident's priority as it changes. It follows a ServiceNow incident's priority when your business rule runs on Update (see [Connecting ServiceNow](connecting-to-ticketing-and-chat-connecting-servicenow.md)). Dynatrace doesn't update an investigation's priority after the problem opens.

On a ServiceNow, PagerDuty, or Dynatrace integration, a priority filter chooses which incidents or problems get updates. For example, to write back only to 1 - Critical ServiceNow incidents, set **Priority** to **Critical** on the ServiceNow integration.

To split investigations between two Slack channels, set **Priority** to **Critical** and **High** on one channel, and to **Medium**, **Low**, and **Minimal** on the other.

### Triage notices
<a name="triage-notices"></a>

Triage can link an incident to an investigation of the same issue, or skip one that matches skip criteria that you define in a skill. AWS DevOps Agent then posts a triage notice instead of investigating. For more information, see [Autonomous incident response](production-operations-autonomous-incident-response.md).

Choosing an outcome in **Leave out triage notices** also leaves out the later notice when the incident is unlinked, unskipped, or canceled while it's linked or skipped.

A triage notice follows the priority and source filters by using the incident's own priority and source. Linking doesn't change which integrations receive an investigation. For example, a Medium investigation doesn't post to a channel filtered to Critical, even if triage links a Critical incident to it.

### Source integrations
<a name="source-integrations"></a>

An investigation's *source* is the integration that started it. A source filter applies only to investigations that have a source. An investigation that you start without one, such as from the AWS DevOps Agent web app or from chat, always matches.

For example, to post investigations from PagerDuty but not from ServiceNow to a Microsoft Teams channel, set **Source integrations** on the channel to the PagerDuty integration.

## When a change takes effect
<a name="when-a-change-takes-effect"></a>

A change to a notification policy, or to an investigation's priority, takes effect at the next update of each investigation or custom agent run, including runs in progress. An investigation that rises from Medium to Critical starts posting to a channel filtered to Critical at its next update. Posts queued before a change can still arrive shortly after it.

A change doesn't edit or resend earlier posts:
+ When you turn off notifications, or an investigation stops matching, the integration keeps what it already received. A Slack *card*, the investigation's top-level message, keeps its last status. AWS DevOps Agent doesn't comment on a ServiceNow or PagerDuty incident when the investigation finishes.
+ When you turn notifications back on, or an investigation starts matching, AWS DevOps Agent doesn't resend skipped updates. A Slack card catches up at the next status change or summary. A channel without the card gets a new one.

## Notes
<a name="notes"></a>

Notification policies don't apply to Amazon EventBridge events or AWS Support cases.

Notification policies also work in the following ways:
+ On a Slack channel, only **Skipped by triage** has an effect, because Slack doesn't post linked or unlinked notices.
+ **Leave out triage notices** doesn't stop the event that Dynatrace receives when AWS DevOps Agent creates an investigation, even for a problem that triage then links or skips.
+ If triage links an incident to a completed investigation, that investigation runs again and posts according to its own priority and source.
+ A channel that you connect during a run receives only the run's later posts, according to its own policy.
+ With a notification policy, every investigation comment on a ServiceNow or PagerDuty incident links to the investigation, so an incident that starts matching mid-run still gets the link.
+ A removed integration stays in **Source integrations**, shown by its association ID, and matches only the investigations that it started before you removed it.
