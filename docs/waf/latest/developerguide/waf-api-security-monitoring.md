---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-monitoring.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Monitoring and investigating AWS WAF API Security detections

After you deploy the API Security managed rule group, you monitor what it detects and investigate the findings that matter. This topic describes the surfaces available for both tasks, and what each surface can and can't tell you.

If you are still deciding which detections to enforce, see [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md) instead. That topic covers ranking detections and promoting rule actions from Count to Block.

## Choosing where to look
<a name="waf-api-security-monitoring-choosing"></a>

Each surface answers a different question. The most common mistake is taking a question to a surface that can't answer it.

**Monitoring surfaces and the questions they answer**

| Your question | Where to look |
| --- | --- |
| Is a detection firing, and how often? | The protection pack (web ACL) dashboard, or Amazon CloudWatch metrics |
| Which detections fire most on my traffic? | CloudWatch metrics, ranked by match rate |
| What did a detection match on? | Your protection pack (web ACL) logs, or the sampled requests view |
| How many clients are behind these matches? | Your logs, or events |
| What has one client been doing across my APIs? | Events, through an event actor |
| Is this activity one incident or many separate matches? | Events |

The distinction that matters most: metrics and the dashboard count requests and matches, not clients. A detection with a thousand matches might be one client a thousand times or a thousand clients once each. Those scenarios call for opposite responses. Use your logs or events to tell them apart.

## The protection pack (web ACL) dashboard
<a name="waf-api-security-monitoring-dashboard"></a>

The dashboard for your protection pack (web ACL) is built on the Amazon CloudWatch metrics that AWS WAF publishes. What it can show is bounded by what those metrics carry: request and match counts by rule, by label, and by resource, over time.

Use it to confirm the rule group is evaluating traffic, to see which detections are active, and to spot a change in volume. For the metric names and for guidance on reading a detection's rate and shape before you enforce it, see [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md).

## Events
<a name="waf-api-security-monitoring-events"></a>

An event is a correlated, deduplicated record of security-relevant activity against a protected resource. It isn't a record of a single rule match. The rule group labels every match and promotes a subset of that activity to an event, so one event can cover sustained activity that produced many labeled requests.

This is the difference between an event and a label. A label answers "what happened on this request." An event answers "what has been going on, and who has been doing it."

An event carries the following:
+ An identifier and a status
+ A category
+ Start, last-updated, and end times
+ The ARNs of the resource and the protection pack (web ACL)
+ An API Security detail that includes the label, the category, the confidence, the API patterns involved, and the actors seen

Confidence is `LOW`, `MEDIUM`, or `HIGH`, matching the rule group's confidence tiers, so an event traces back to the rule that produced it.

### Event status
<a name="waf-api-security-monitoring-event-status"></a>

Status moves through the values `EVENT_STARTED`, `EVENT_IN_PROGRESS`, `EVENT_COMPLETED`, and `EVENT_ENDED`. An event isn't a point in time. An event you fetch twice can differ if activity is ongoing.

### API patterns
<a name="waf-api-security-monitoring-api-patterns"></a>

An API pattern names the method, path pattern, port, and domains the activity touched. This is how you determine which of your endpoints an event concerns.

### Working with events through the API
<a name="waf-api-security-monitoring-events-api"></a>

**Note**
Events are available through the AWS WAF API and also through the API Portal Discovery dashboard.

**API Security event operations**

| Operation | What it returns | Required in the request |
| --- | --- | --- |
| [`ListEvents`](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListEvents.html) | Events in a time window, filtered and sorted | Scope |
| [`ListEventsByWebACL`](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListEventsByWebACL.html) | The same, scoped to one protection pack (web ACL) | Scope, WebAclArn |
| [`GetEvent`](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetEvent.html) | One event in full | Scope, EventId, WebAclArn |
| [`ListEventActors`](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListEventActors.html) | The actors seen in a time window | Scope, TimeWindow |
| [`GetEventActor`](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetEventActor.html) | One actor, its related events, and its change history | Scope, EventActorId |

The following details about these operations are easy to get wrong:
+ **`GetEvent` requires the protection pack (web ACL) ARN as well as the event identifier.** You can't fetch an event by its identifier alone. Keep the ARN alongside the identifier when you store or forward an event.
+ **`GetEventActor` doesn't take a protection pack (web ACL) ARN.** An actor isn't scoped to one protection pack (web ACL). This is what allows you to see a client that has been active against more than one of them.
+ **`ListEventActors` requires a time window; `ListEvents` does not.** Query for actors over a period. Query for events over a period, or leave out the time window to get the past year, which is also the longest window you can request.

### The reclassification timeline
<a name="waf-api-security-monitoring-timeline"></a>

The reclassification timeline is opt-in. The rule group can revise its assessment of ongoing activity, and an event keeps a timeline of those revisions. Each entry carries the time, the label, the confidence, and the API patterns as they stood at that point.

List operations don't return the timeline by default. Request it by setting `Include` to `TIMELINE`. The timeline is where you see a detection that started at low confidence and firmed up, which is a different story from one that was high from the first request.

## Investigating an actor
<a name="waf-api-security-monitoring-actor"></a>

An event actor is the client the rule group attributed activity to, and it is the primary surface for per-client investigation.

An actor carries the following attributes: its identifier, client IP address, TLS fingerprint, ASN and ASN organization, country, an auth fingerprint, and when it was first seen. Listing actors also returns the number of events each appears in. `EVENT_COUNT` is the only available sort order, so a list of actors is in effect a list of your noisiest clients.

`GetEventActor` adds the following to that summary:
+ **Related events** – All events attributed to this client, so you can see its full activity rather than working event by event.
+ **A change history** of the client's network attributes, with the time of each change. A client that moves address, ASN, or country stays one actor rather than appearing as several. This is the purpose of an actor: a behavioral detection is about a client over time, and a client that changes address mid-activity would otherwise appear as two clients doing half as much each.

The change history covers network attributes only. The auth fingerprint isn't tracked over time.

## Joining an event back to your logs
<a name="waf-api-security-monitoring-logs"></a>

An event tells you what the rule group concluded. Your logs tell you which requests led there. The auth fingerprint connects them: it is a hash that identifies the caller, so the same caller can be matched across events and your AWS WAF logs.

The following is the investigation path:

1. **Find the activity** with `ListEvents` or `ListEventsByWebACL`, or by starting from `ListEventActors` if you want to begin with the noisiest clients.

1. **Read the detail** with `GetEvent`. Note the label, the confidence, and the API patterns. Request the timeline if you want to see how the assessment developed.

1. **Identify the client** with `GetEventActor`. Note its auth fingerprint and its related events.

1. **Find the requests** by matching that auth fingerprint in your protection pack (web ACL) logs.

1. **Decide.** If the activity is unwanted, add your own rule. The identity labels the rule group adds are the mechanism for acting on a client across your endpoints rather than on one request. They are described in [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md). For worked examples, see [AWS WAF API Security examples](waf-api-security-examples.md).

If the activity turns out to be your own, see [Example scenarios of false positives with AWS WAF API Security](waf-api-security-false-positives.md), which covers the most common cases and what to do about each.

## Limits
<a name="waf-api-security-monitoring-limits"></a>
+ **Filtering** – You can filter events by event category and by resource ARN, and separately by API pattern. Event category has one value today, `API_SECURITY`, so filtering on it has no practical effect while API Security is the only feature producing events.
+ **Sorting** – Events sort by start time, end time, or confidence. Actors sort by event count only.
+ **Page sizes** – Events are returned up to 20 per page.
+ **Caps within a response** – An event names up to 20 API patterns and up to 20 actors, and keeps up to 32 timeline entries. An actor carries up to 20 related events and up to 20 change-history entries. A request accepts up to 8 filters with up to 10 values each.
