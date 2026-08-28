---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-one-time-schedule.html
---

# POST: Create a One-Time Schedule
<a name="channel-scheduling-create-a-one-time-schedule"></a>

Create a schedule that runs only once. Will only run if active. See also [POST: Create a Repeating Schedule](channel-scheduling-create-a-repeating-schedule.md).

## HTTP Request and Response
<a name="channel-scheduling-create-a-one-time-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-create-a-one-time-schedule-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels/<channel ID>/schedules
```

### Call Header
<a name="channel-scheduling-create-a-one-time-schedule-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="channel-scheduling-create-a-one-time-schedule-http-request-response-request-body"></a>

The request body contains XML content consisting of one schedule element, consisting of some or all of the following elements.

| Element | Value Type | Description |
| --- | --- | --- |
| name | String | [Required] A name you assign which must be unique in the channel. |
| active | Boolean | [Optional] If unspecified, defaults to false. A switch indicating whether the schedule will run. “True” for active schedules that run at the appointed time; “false” for inactive schedules that do not run but are saved in the system and can be activated later. |
| duration | Integer | [Optional] Length of time in seconds that the channel will run. If unspecified, defaults to nil="true", which results in a schedule that continues to run without stopping. |
| repeat | Boolean | [Required] The Boolean value for repeat which must be “false” for schedules that run only once. |
| run\_at | Datetime | [Required for one-time schedules] The date and time , in ISO 8601 format, that the schedule begins,including UTC offset. This is present only for schedules that run only once. |

### Response
<a name="channel-scheduling-create-a-one-time-schedule-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: element containing the newly assigned ID for the schedule.
+ Any elements not specified in the request body, with default values.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
