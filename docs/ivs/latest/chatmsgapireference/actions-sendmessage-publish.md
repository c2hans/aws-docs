---
source_url: https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-sendmessage-publish.html
---

# SendMessage (Publish)
<a name="actions-sendmessage-publish"></a>

Sends a message to participants of the room.

## Required Capability
<a name="sendmessage-required"></a>

`SEND_MESSAGE`

## Format
<a name="sendmessage-format"></a>

```
{
  "Action": "SEND_MESSAGE",
  "Attributes": {
    "user_id": "string",
    "display_name": "string"
  },
  "Content": "string",
  "RequestId": "string"
}
```

## Fields
<a name="sendmessage-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
| `Action` | Yes | `SEND_MESSAGE` |
| `Attributes` | No | Details of the event; e.g., `user_id`, `display_name`, and/or anything you want. |
| `Content` | Yes | Message to send. The character length of this field must be shorter than the room’s configured `maximumMessageLength`. Maximum: 500 unicode code points. |
| `RequestId` | No | An identifier optionally specified by your application for tracking purposes. If specified, this appears in corresponding subscribe operations. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
