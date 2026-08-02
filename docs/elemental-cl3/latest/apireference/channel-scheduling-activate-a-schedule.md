---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-activate-a-schedule.html
---

# POST: Activate a Schedule
<a name="channel-scheduling-activate-a-schedule"></a>

Inactive schedules can be activated as follows.

## HTTP Request and Response
<a name="channel-scheduling-activate-a-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-activate-a-schedule-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels/<channel ID>/schedules/<schedule ID>/active
```

### Call Header
<a name="channel-scheduling-activate-a-schedule-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="channel-scheduling-activate-a-schedule-http-request-response-response"></a>

The response shows the `schedule` element with <active> set to “true” and other elements as described in [POST: Create a One-Time Schedule](channel-scheduling-create-a-one-time-schedule.md) and [POST: Create a Repeating Schedule](channel-scheduling-create-a-repeating-schedule.md). The response also includes the following elements, which are used internally by the system: <args>, <schedulable\_type>, and <schedulable\_id>. The response is otherwise identical to the response to a GET Schedule. For an example response, see [GET List Example](channel-scheduling-get-list-of-all-channel-schedules-example.md).
