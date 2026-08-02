---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-update-a-schedule.html
---

# PUT: Update a Schedule
<a name="channel-scheduling-update-a-schedule"></a>

## HTTP Request and Response
<a name="channel-scheduling-update-a-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-update-a-schedule-http-request-response-url"></a>

```
PUT http://<Conductor IP Address>/channels/<channel ID>/schedules/<schedule ID>
```

### Call Header
<a name="channel-scheduling-update-a-schedule-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

 If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="channel-scheduling-update-a-schedule-http-request-response-request-body"></a>

One `schedule` element that contains the elements to be changed, enclosing the new value.

### Response
<a name="channel-scheduling-update-a-schedule-http-request-response-response"></a>

The system updates the schedule but does not return a response. To confirm that the schedule has been changed, run a GET on the schedule as described in [GET: Get the Attributes of a Schedule](channel-scheduling-get-attributes-of-a-schedule.md).
