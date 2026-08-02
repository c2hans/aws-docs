---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-channel-schedules.html
---

# Channel Schedules
<a name="commands-channel-schedules"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST | POST | /channels/<channel ID>/schedules | Create a repeating or one-time schedule. |
| POST Activate Schedule | POST | /channels/<channel ID>/schedules/<schedule ID>/active | Activate a schedule. |
| DELETE Deactivate Schedule | DELETE | /channels/<channel ID>/schedules/<schedule ID>/active | Deactivate a schedule. |
| PUT Update Schedule | PUT | /channels/<channel ID>/schedules/<schedule ID> | Modify the attributes of the specified schedule. |
| GET Schedule List | GET | /channels/<channel ID>/schedules | Get the list of all schedules for a channel. |
| GET Schedule | GET | /channels/<channel ID>/schedules/<schedule ID> | Get the attributes of the specified schedule. |
| GET Schedule Events (All) | GET | /events | Get all schedule events for the cluster. |
| GET Schedule Events <br />(One Schedule) | GET | /channels/<channel ID>/schedules/<schedule ID>/events | Get all schedule events generated from one schedule. |
| DELETE Delete Schedule | DELETE | /channels/<channel ID>/schedules/<schedule ID> | Delete the specified schedule. |
