---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-list-of-task-reports.html
---

# Monitoring Bulk Tasks: GET List of Task Reports
<a name="performing-bulk-tasks-get-list-of-task-reports"></a>

Get the list of bulk tasks. Each time one of the following commands is performed, a task\_report is created:
+ POST Start Channel
+ POST Stop Channel

A task report shows information about the bulk task. The bulk task is made up of individual task items. For example, a POST Start Channel is a bulk task that is made up of one or more task, each to start a different channel.

## HTTP Request and Response
<a name="performing-bulk-tasks-get-list-of-task-reports-http-request-response"></a>

### Request URL
<a name="performing-bulk-tasks-get-list-of-task-reports-http-request-response-url"></a>

```
GET http://<Conductor IP address>/task_reports
```

### Call Header
<a name="performing-bulk-tasks-get-list-of-task-reports-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="performing-bulk-tasks-get-list-of-task-reports-http-request-response-response"></a>

The response contains XML content consisting of one `task_reports` element

with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `task_reports` elements, one for each bulk task that is in progress or is completed. Each element contains several elements as listed.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The unique ID for this task\_report. |
| created\_at | String | The time this bulk task was created (the POST Start or Stop was received by the system). Time is in ISO 8601 format, with the timezone designator indicated as an offset from UTC. For example, 2015-08-17T11:59:35-07:00 is the time in the timezone that is 7 hours behind UTC. |
| updated\_at | String | The time the most recent change was made to this task report. In other words, the last time one or more of the count elements was updated.  |
| description | String | “Channel Start” or “Channel Stop”.”. |
| complete | Boolean | True means the bulk task has completed, with successes and/or failures.<br />False means not all the individual task items have completed yet. |
| task\_count | Integer | The total number of task items in the bulk task. For example, if there are three “start channel” commands, this element specifies 3. |
| failed\_count | Integer | The number of actions that have failed. |
| successful\_count | Integer | The number of actions that have succeeded. |
| tasks | Array | One or more task elements. Each task represents an individual task within the bulk task. See below. |

**Recommended Procedure**

1. Send a GET task\_reports as soon as a bulk task is POSTed.

1. Parse the response for the desired <id> and store that ID for later use. This ID is the ID of the individual bulk task.

1. Parse the response for the complete Boolean .

1. Before that final resolution, you may want to check on the status of individual task items: send a [GET task\_reports/<task ID>](performing-bulk-tasks-get-one-task-report.md), passing in the ID you saved earlier. Parse the <tasks> array of the response for tasks that are not successful or failed. If necessary for a status of a channel, check the ID within the individual <task> for the channel.
