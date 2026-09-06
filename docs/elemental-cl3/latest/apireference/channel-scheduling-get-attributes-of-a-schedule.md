---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-attributes-of-a-schedule.html
---

# GET: Get the Attributes of a Schedule
<a name="channel-scheduling-get-attributes-of-a-schedule"></a>

Get the details of a specific schedule.

## HTTP Request and Response
<a name="channel-scheduling-get-attributes-of-a-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-get-attributes-of-a-schedule-http-request-response-url"></a>

```
GET http://<Conductor IP Address>/channels/<channel ID>/schedules/<schedule ID>
```

### Call Header
<a name="channel-scheduling-get-attributes-of-a-schedule-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="channel-scheduling-get-attributes-of-a-schedule-http-request-response-response"></a>

XML content consisting of one `schedule` element containing the same elements as the response for GET List of All Channel Schedules above.
