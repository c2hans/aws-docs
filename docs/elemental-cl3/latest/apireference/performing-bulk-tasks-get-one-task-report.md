---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-get-one-task-report.html
---

# Monitoring Bulk Tasks: GET One Task Report
<a name="performing-bulk-tasks-get-one-task-report"></a>

Get the specified task report related to one bulk task.

## HTTP Request and Response
<a name="performing-bulk-tasks-get-one-task-report-http-request-response"></a>

### Request URL
<a name="performing-bulk-tasks-get-one-task-report-http-request-response-url"></a>

```
GET http://<Conductor IP address>/task_reports/<ID of task_report>
```

where `<ID of task_report>` can be obtained from a GET Task Report List.

### Call Header
<a name="performing-bulk-tasks-get-one-task-report-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="performing-bulk-tasks-get-one-task-report-http-request-response-response"></a>

The response contains XML content consisting of one `task_report` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Several elements are shown in the table below.

| Element | Value | Description |
| --- | --- | --- |
| id<br />created\_at<br />updated\_at<br />description<br />complete<br />task\_count<br />failed\_count<br />successful\_count |   | The same elements as in the response to GET List of Tasks |
| tasks | Array | One or more task elements. Each task represents an individual action within the bulk task. See below. |

Task Elements

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this task. IDs are unique within the Tasks element.  |
| description | String | The type of bulk task for this task report: “Channel Start” or “Channel Stop.” |
| state | String | The state of this bulk task. When the state changes to "Success," the <successful\_count> increments; when the state changes to "Failure," then <failure\_count> increments.  |
| message | String | “Success” or “Failure.” |
