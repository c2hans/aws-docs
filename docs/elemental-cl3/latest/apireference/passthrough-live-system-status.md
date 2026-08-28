---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/passthrough-live-system-status.html
---

# Passthrough of Live System Status
<a name="passthrough-live-system-status"></a>

You can pass through a request for the status of an AWS Elemental Live system within the Conductor cluster as well. This passthrough command is structured slightly differently from a live\_event command.

## HTTP Request and Response
<a name="passthrough-live-system-status-http-request-response"></a>

### Request URL
<a name="passthrough-live-system-status-http-request-response-url"></a>

```
GET http://<Conductor IP address>/nodes/<ID of node>/system_status
```

where <ID of node> is the ID of the node as assigned by Conductor Live.

When the command is submitted, the Conductor Live API queries the appropriate AWS Elemental Live node and returns the system status as reported by that node.

### Call Header
<a name="passthrough-live-system-status-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="passthrough-live-system-status-http-request-response-body"></a>

There is no body in the system\_status command.

### Response
<a name="passthrough-live-system-status-http-request-response-response"></a>

The response repeats back the response received from the Live API, exactly as received from that API.

## Example
<a name="passthrough-live-system-status-example"></a>

```
GET http://198.51.100.0/nodes/13/system_status
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
