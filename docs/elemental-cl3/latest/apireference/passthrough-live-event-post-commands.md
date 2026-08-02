---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/passthrough-live-event-post-commands.html
---

# Passthrough of Live Event POST Commands
<a name="passthrough-live-event-post-commands"></a>

## HTTP Request and Response
<a name="passthrough-live-event-post-commands-http-request-response"></a>

### Request URL
<a name="passthrough-live-event-post-commands-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels/<ID of channel>/live_events/<action>
```

where:
+ ID of channel is the ID of a channel known to the Conductor Live API.
+ /live\_events/<action> is the command from the AWS Elemental Live API. See the table below for a complete list of commands.

When the command is submitted, the Conductor Live API determines the Live event that corresponds to the Conductor Live channel and then submits the appropriately formed command to the Live API.

| Action | Signature in AWS Elemental Live | Signature in Conductor Live |
| --- | --- | --- |
| POST | /live\_events/<id>/activate\_input | /channels/<ID of channel>/live\_events/activate\_input |
| POST | /live\_events/<id>/adjust\_audio\_gain | /channels/<ID of channel>/live\_events/adjust\_audio\_gain |
| POST | /live\_events/<id>/avail\_image | /channels/<ID of channel>/live\_events/avail\_image |
| POST | /live\_events/<id>/blackout\_image | /channels/<ID of channel>/live\_events/blackout\_image |
| POST | /live\_events/<id>/bulk\_metadata | /channels/<ID of channel>/live\_events/bulk\_metadata |
| POST | /live\_events/<id>/cue\_point | /channels/<ID of channel>/live\_events/cue\_point |
| POST | /live\_events/<id>/motion\_image\_inserter | /channels/<ID of channel>/live\_events/motion\_image\_inserter |
| POST | /live\_events/<id>/mute\_audio | /channels/<ID of channel>/live\_events/mute\_audio |
| POST | /live\_events/<id>/unmute\_audio | /channels/<ID of channel>/live\_events/unmute\_audio |
| POST | /live\_events/<id>/pause\_output | /channels/<ID of channel>/live\_events/pause\_output |
| POST | /live\_events/<id>/unpause\_output | /channels/<ID of channel>/live\_events/unpause\_output |
| POST | /live\_events/<id>/pause\_output\_group | /channels/<ID of channel>/live\_events/pause\_output\_group |
| POST | /live\_events/<id>/unpause\_output\_group | /channels/<ID of channel>/live\_events/unpause\_output\_group |
| POST | /live\_events/<id>/private\_metadata | /channels/<ID of channel>/live\_events/private\_metadata |
| POST | /live\_events/<id>/reset\_video\_buffer\_stats | /channels/<ID of channel>/live\_events/reset\_video\_buffer\_stats |
| POST | /live\_events/<id>/rollover\_output | /channels/<ID of channel>/live\_events/rollover\_output |
| POST | /live\_events/<id>/start\_output | /channels/<ID of channel>/live\_events/start\_output |
| POST | /live\_events/<id>/start\_output\_group | /channels/<ID of channel>/live\_events/start\_output\_group |
| POST | /live\_events/<id>/stop\_output | /channels/<ID of channel>/live\_events/stop\_output |
| POST | /live\_events/<id>/stop\_output\_group | /channels/<ID of channel>/live\_events/stop\_output\_group |
| POST | /live\_events/<id>/time\_signal | /channels/<ID of channel>/live\_events/time\_signal |
| POST | /live\_events/<id>/timed\_metadata | /channels/<ID of channel>/live\_events/timed\_metadata |
| POST | /live\_events/<id>/image\_inserter | /channels/<ID of channel>/live\_events/image\_inserter |
| POST | /live\_events/<id>/image\_inserter/input | /channels/<ID of channel>/live\_events/image\_inserter/input |
| POST | /live\_events/<id>/prepare\_input | /channels/<ID of channel>/live\_events/prepare\_input |

### Call Header
<a name="passthrough-live-event-post-commands-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="passthrough-live-event-post-commands-http-request-response-body"></a>

Include a request body only if the original AWS Elemental Live command includes a body.Format the body in exactly the same way.

### Response
<a name="passthrough-live-event-post-commands-http-request-response-response"></a>

The response repeats back the response received from the Live API, exactly as received from that API.

## Example
<a name="passthrough-live-event-post-commands-example"></a>

AWS Elemental Live REST call:

```
POST http://<Live IP address>/live_events/<ID of event>/mute_audio
```

Conductor Live passthrough of this call:

```
POST http://<Conductor IP address>/channels/3/live_events/mute_audio
```
