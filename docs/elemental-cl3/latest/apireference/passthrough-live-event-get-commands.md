---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/passthrough-live-event-get-commands.html
---

# Passthrough of Live Event GET Commands
<a name="passthrough-live-event-get-commands"></a>

## HTTP Request and Response
<a name="passthrough-live-event-get-commands-http-request-response"></a>

### Request URL
<a name="passthrough-live-event-get-commands-http-request-response-url"></a>

```
GET http://<Conductor IP address> /channels/<ID of channel>/live_events/<action>
```

where:
+ ID of channel is the ID of a channel known to the Conductor Live API.
+ /live\_events/<action> is the command from the AWS Elemental Live API. See below for a list.

When the command is submitted, the Conductor Live API determines the Live event that corresponds to the Conductor Live channel, then submits the appropriately formed command to the Live API.

| Action | Signature in AWS Elemental Live | Signature in Conductor Live |
| --- | --- | --- |
| GET | /live\_events/<id>/inputs | /channels/<ID of channel>/live\_events/inputs |

### Call Header
<a name="passthrough-live-event-get-commands-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="passthrough-live-event-get-commands-http-request-response-body"></a>

Include a body only if the original AWS Elemental Live command includes a body. Format the body in exactly the same way.

### Response
<a name="passthrough-live-event-get-commands-http-request-response-response"></a>

The response repeats back the response received from the Live API, exactly as received from that API.

## Example
<a name="passthrough-live-event-get-commands-example"></a>

AWS Elemental Live REST call:

```
GET http:/live_events/13/inputs
```

Conductor Live passthrough of this call:

```
GET http://192.0.2.16/channels/13/live_events/inputs
```
