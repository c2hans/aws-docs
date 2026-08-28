---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/api-reference.html
---

# API Reference
<a name="api-reference"></a>

All messages sent from the extensions to Amazon DCV are of a type of request. Messages from Amazon DCV to extensions can be of type response or event.

Requests from an extension will always receive a synchronous response from Amazon DCV of either success in a single with a stated status value or failure with a stated reason.

Extensions may specify in each request that an optional `request_id` will be replicated in the corresponding response.

Some requests require asynchronous processing where a successful response means that the request is being processed and the final outcome will be delivered with an event message.

Event messages are also used to deliver notifications of conditions originating in the local Amazon DCV client/server, the remote server/client, or the remote extension.

**Example**
An example of an event message would be `StreamingViewsChangedEvent`

**Topics**
+ [General API](general-api.md)
+ [Virtual Channel API](virtual-channel-api.md)
+ [Geometry API](geometry-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
