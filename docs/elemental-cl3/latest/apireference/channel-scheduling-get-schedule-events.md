---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-schedule-events.html
---

# GET: Get Schedule Events
<a name="channel-scheduling-get-schedule-events"></a>

Within the system, active repeating schedules result in “schedule events”. A schedule event is an individual instance of the schedule and represents one time on the calendar when the channel will run. When new schedules are created or updated, and every hour after that, the system generates schedule events to bring the total queued schedule events to 24.

## HTTP Request and Response
<a name="channel-scheduling-get-schedule-events-http-request-response"></a>

### Request URL
<a name="channel-scheduling-get-schedule-events-http-request-response-url"></a>

To get all schedule events in the cluster:

```
GET http://<Conductor IP Address>/events
```

To get all schedule events from a single schedule:

```
GET http://<Conductor IP Address>/channels/<channel ID>/schedules/<schedule ID>/events
```

### Call Header
<a name="channel-scheduling-get-schedule-events-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="channel-scheduling-get-schedule-events-http-request-response-response"></a>

The response contains XML content consisting of one `schedule_events` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `schedule_event` elements, one for each schedule event found. Each element contains several elements, as follows.

| Element | Value Type | Description |
| --- | --- | --- |
| id | Integer | The ID for this schedule event, assigned by the system when the schedule event was generated. |
| start\_at | Datetime | The date and time that the channel will start, in ISO 8601 format, including the UTC offset. |
| stop\_at | Integer | The date and time that the channel will stop, in ISO 8601 format, including the UTC offset.  |
| state | String | An indication of the current state or progress of scheduling. Possible values are: queued, pending, started, stopped, and failed. |
| message | String | System messages about any unexpected errors which appear here. |
| schedule\_id | Integer | The ID for the schedule that spawned this schedule event. |
