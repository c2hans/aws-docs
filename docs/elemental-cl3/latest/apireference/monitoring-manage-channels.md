---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-manage-channels.html
---

# Managing Channels
<a name="monitoring-manage-channels"></a>

## Channel Status Elements
<a name="monitoring-manage-channels-status"></a>

The `status` element of a channel provides information about the current status of the channel. The status imposes rules about the ability to modify (PUT), delete (DELETE), or start or stop (POST Start Channel and POST Stop Channel) a channel.

You can obtain the status of a channel using [GET Channel List](get-list-of-channels.md) or [GET Channel](get-attributes-of-a-channel.md).

| Status | Modify | Delete | Start | Stop |
| --- | --- | --- | --- | --- |
| Active | Not allowed | Not allowed | Not allowed | Allowed |
| Complete | Allowed | Allowed | Allowed | Not applicable |
| Error | Allowed. Status will change to idle. | Allowed | Not allowed | Not applicable |
| Idle | Allowed | Allowed | Allowed | Not applicable |
| Pending | Not allowed | Not allowed | Not allowed | Not allowed |
| Postprocessing | Not allowed | Not allowed | Not allowed | Allowed |
| Preprocessing | Not allowed | Not allowed | Not allowed | Allowed |
| Running | Not allowed | Not allowed | Not allowed | Allowed |
| Started | Not allowed | Not allowed | Not allowed | Allowed |
| Starting | Not allowed | Not allowed | Not allowed | Allowed |
| Stopping | Not allowed | Not allowed | Not allowed | Not applicable |
| Suspended | Not allowed | Not allowed | Not allowed | Allowed |
| Unknown | Not allowed | Not allowed | Not allowed | Not allowed |
| Unreachable | Not allowed | Not allowed | Not allowed | Not allowed |

## POST Channel Revert: Resetting the Channel
<a name="monitoring-manage-channels-reset"></a>

If a channel is in one of the following statuses, you can make it revert to the Idle state:
+ Complete
+ Error
+ Unknown

If you try to revert to `Idle` from another status, the system ignores the command.

### Call Header
<a name="monitoring-manage-channels-reset-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request URL
<a name="monitoring-manage-channels-reset-request-url"></a>

```
POST http://<Conductor IP address>/channels/<ID of channel>/revert
```
