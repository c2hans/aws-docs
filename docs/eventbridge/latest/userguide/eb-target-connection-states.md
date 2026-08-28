---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-states.html
---

# Connection states in EventBridge
<a name="eb-target-connection-states"></a>

Below are the connection statuses returned by EventBridge when creating or re-authorizing a connection.

For successful connections to public APIs, EventBridge returns a status of `AUTHORIZED`. For successful connections to private APIs, EventBridge returns a status of `ACTIVE`.

*Connectivity failures* refer to errors involving the network connectivity of the connection. Connectivity errors result in a connection status of `FAILED_CONNECTIVITY`. *Authorization failures* refer to errors involving the permissions specified for the connection. Authorization failures result in a status of `DEAUTHORIZED`.

For information on how to have EventBridge re-authorize the connection once you have updated it to address authorization or connectivity issues, see [Updating connections](eb-target-connection-edit.md).

EventBridge emits events when the state of a connection changes. For more information, see [Connection events](event-reference.md#event-reference-connections).

**Public APIs**

| Authorization method | Success | Connectivity failure | Authorization failure |
| --- | --- | --- | --- |
| Basic or API Key | `AUTHORIZED` | n/a | `DEAUTHORIZED` |
| OAuth (public endpoint) | `AUTHORIZED` | n/a | `DEAUTHORIZED` |
| OAuth (private endpoint) | `AUTHORIZED` | `FAILED_CONNECTIVITY` | `DEAUTHORIZED` |

**Private APIs**

| Authorization method | Success | Connectivity failure | Authorization failure |
| --- | --- | --- | --- |
| Basic or API Key | `ACTIVE` | `FAILED_CONNECTIVITY` | `DEAUTHORIZED` |
| OAuth (public endpoint) | `ACTIVE` | `FAILED_CONNECTIVITY` | `DEAUTHORIZED` |
| OAuth (private endpoint) | `ACTIVE` | `FAILED_CONNECTIVITY` | `DEAUTHORIZED` |

When you create a connection to a private API, there can be a delay of up to several minutes from when the connection is successfully created to when you can successfully make HTTPS calls to the private API. During this period:
+ Private OAuth connection will be in `AUTHORIZING` state, and will transition to `AUTHORIZED` when OAuth token exchange is successfully completed.
+ The connection will update to `ACTIVE` status, and EventBridge will retry any invocations from event buses or pipes.

If you are using the connection in an HTTP task within a Step Functions workflow, you can configure retries on `httpTimeoutExceptions` to retry any calls to the private API that happen during this period.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
