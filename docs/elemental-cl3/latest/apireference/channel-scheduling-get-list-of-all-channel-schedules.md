---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-list-of-all-channel-schedules.html
---

# GET List: Get List of All Channel Schedules
<a name="channel-scheduling-get-list-of-all-channel-schedules"></a>

Get a list of active and inactive schedules for a given channel.

## HTTP Request and Response
<a name="channel-scheduling-get-list-of-all-channel-schedules-http-request-response"></a>

### Request URL
<a name="channel-scheduling-get-list-of-all-channel-schedules-http-request-response-url"></a>

```
GET http://<Conductor IP Address>/channels/<channel ID>/schedules
```

### Call Header
<a name="channel-scheduling-get-list-of-all-channel-schedules-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="channel-scheduling-get-list-of-all-channel-schedules-http-request-response-response"></a>

The response contains XML content consisting of one `schedules` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `schedule` elements, one for each schedule found. Each element contains several elements, as follows.

| Element | Value Type | Description |
| --- | --- | --- |
| id | Integer | The ID for this schedule, assigned by the system when the schedule is created. |
| name | String | The name that you assigned to the schedule. |
| active | Boolean | A switch indicating whether the schedule will run. “True” for active schedules that run at the appointed time and “false” for inactive schedules that do not run but are saved in the system and can be activated later. |
| duration | Integer | The length of time, in seconds, that the channel will run. |
| repeat | Boolean | A switch indicating whether the schedule will run more than one time.“True” for repeating schedules and “false” for schedules that run only once. |
| run\_at | Datetime | The date and time that the schedule begins. This is present only for schedules that run only once. |
| cron | CRON expression | The expression which specifies the schedule according to the cron standard, as summarized in [CRON Syntax Summary](channel-scheduling-cron-syntax-summary.md). This is present only for repeating schedules. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
