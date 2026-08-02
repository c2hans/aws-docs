---
source_url: https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html
---

# DeleteMessage (Publish)
<a name="actions-deletemessage-publish"></a>

Instructs other clients to delete a message.

## Required Capability
<a name="deletemessage-required"></a>

`DELETE_MESSAGE`

## Format
<a name="deletemessage-format"></a>

```
{
  "Action": "DELETE_MESSAGE",
  "Id": "string",
  "Reason": "string",
  "RequestId": "string"
}
```

## Fields
<a name="deletemessage-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
| `Action` | Yes | `DELETE_MESSAGE` |
| `Id` | Yes | ID of the message to be deleted. This is the Id field in the received message (see [Message (Subscribe)](actions-message-subscribe.md)). |
|  `Reason`  | No | Reason for deleting the message. |
| `RequestId` | No | An optional identifier specified by your application for tracking purposes. If specified, this appears in corresponding subscribe operations. |
