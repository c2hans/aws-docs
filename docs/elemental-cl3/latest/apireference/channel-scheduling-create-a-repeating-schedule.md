---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-repeating-schedule.html
---

# POST: Create a Repeating Schedule
<a name="channel-scheduling-create-a-repeating-schedule"></a>

Create a schedule that repeats regularly. Will only run if active. (See also [POST: Create a One-Time Schedule](channel-scheduling-create-a-one-time-schedule.md).

## HTTP Request and Response
<a name="channel-scheduling-create-a-repeating-schedule-http-request-response"></a>

### Request URL
<a name="channel-scheduling-create-a-repeating-schedule-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels/<channel ID>/schedules
```

### Call Header
<a name="channel-scheduling-create-a-repeating-schedule-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="channel-scheduling-create-a-repeating-schedule-http-request-response-request-body"></a>

XML content consisting of one `schedule` element, consisting of some or all of the following elements:

| Element | Value Type | Description |
| --- | --- | --- |
| name | String | [Required] A name you assign which must be unique in the channel. |
| active | Boolean | [Optional] If unspecified, defaults to false. A switch indicating whether the schedule will run. “True” for active schedules that run at the appointed time and false for inactive schedules that do not run but are saved in the system and can be activated later. |
| duration | Integer | [Required for repeating schedules] The length of time in seconds that the channel will run. If unspecified, defaults to nil="true", which results in a schedule that continues to run without stopping. |
| repeat | Boolean | [Required] The Boolean value for repeat which must be “true” for repeating schedules. |
| cron | CRON expression | [Required for repeating schedules] The expression which specifies the schedule according to the cron standard, as summarized in [CRON Syntax Summary](channel-scheduling-cron-syntax-summary.md). |

### Response
<a name="channel-scheduling-create-a-repeating-schedule-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: element containing the newly assigned ID for the schedule.
+ If not specified in the request, the active element, defaulted to “false.”

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
