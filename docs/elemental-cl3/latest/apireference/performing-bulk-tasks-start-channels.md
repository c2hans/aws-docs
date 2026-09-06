---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-start-channels.html
---

# POST Start: Start One or More Channels
<a name="performing-bulk-tasks-start-channels"></a>

Start one or more channels. If the specified channels are currently idle on their nodes, then they will start. If the channels are currently running, they simply continue running.

The channel must be in a state that allows it to be started. To check the status, use GET Channel. For information on the status, see [Channel Status Elements](monitoring-manage-channels.md#monitoring-manage-channels-status).

## HTTP Request and Response
<a name="performing-bulk-tasks-start-channels-http-request-response"></a>

### Request URL
<a name="performing-bulk-tasks-start-channels-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels/start
```

### Call Header
<a name="performing-bulk-tasks-start-channels-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="performing-bulk-tasks-start-channels-http-request-response-request-body"></a>

The request contains XML content consisting of one `channel_ids` element (of type “array”) with the following.
+ One or more `channel_id` elements, one for each channel to start.

### Response
<a name="performing-bulk-tasks-start-channels-http-request-response-response"></a>

The response contains XML content consisting of one `task_report` element, containing the same elements as the response for [GET One Task Report](performing-bulk-tasks-get-one-task-report.md). The failed count and success count may both specify 0. The entire element may be missing, indicating that no actions have been performed yet.
