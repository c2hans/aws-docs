---
source_url: https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html
---

# DisconnectUser (Publish)
<a name="actions-disconnectuser-publish"></a>

Disconnects another viewer from the Chat room. Use this in conjunction with the CreateChatToken flow to implement time-based or permanent user bans. For example, to permanently ban a user (viewer), precede this operation with a call to your application service, to prevent the application service from creating another token to the same room. To lift the ban (time- or logic-based), simply resume calling CreateChatToken.

## Required Capability
<a name="disconnectuser-required"></a>

`DISCONNECT_USER`

## Format
<a name="disconnectuser-format"></a>

```
{
  "Action": "DISCONNECT_USER",
  "RequestId": "string",
  "Reason": "string",
  "UserId": "string"
}
```

## Fields
<a name="disconnectuser-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
| `Action` | Yes | `DISCONNECT_USER` |
| `RequestId` | No | An identifier optionally specified by your application for tracking purposes. If specified, this appears in corresponding subscribe operations. |
| `Reason` | No | Reason for disconnecting the user. |
| `UserId` | Yes | User ID of the user(s) to disconnect from the room. If multiple connections share this ID, all are disconnected. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
