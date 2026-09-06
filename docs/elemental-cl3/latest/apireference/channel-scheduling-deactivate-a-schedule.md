---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-deactivate-a-schedule.html
---

# DELETE: Deactivate a Schedule
<a name="channel-scheduling-deactivate-a-schedule"></a>

Active schedules can be deactivated as follows.

## HTTP Request and Response
<a name="channel-scheduling-deactivate-a-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-deactivate-a-schedule-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/channels/<channel ID>/schedules/<schedule ID>/active
```

### Call Header
<a name="channel-scheduling-deactivate-a-schedule-http-request-response-call-header"></a>
+ Accept: application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="channel-scheduling-deactivate-a-schedule-http-request-response-response"></a>

The system deactivates the schedule but does not return a response. To confirm that the schedule has been deactivated, run a GET on the schedule as described in [GET: Get the Attributes of a Schedule](channel-scheduling-get-attributes-of-a-schedule.md).
