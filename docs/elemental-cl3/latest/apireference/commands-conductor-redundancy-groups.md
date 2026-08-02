---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-conductor-redundancy-groups.html
---

# Conductor Redundancy Groups
<a name="commands-conductor-redundancy-groups"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Group | POST | /conductor\_redundancy\_groups | Create a new Conductor redundancy group. |
| PUT Group | PUT | /conductor\_redundancy\_groups/<ID of group> | Modify the specified Conductor redundancy group. |
| GET Group List | GET | /conductor\_redundancy\_groups | Get the list of Conductor redundancy groups. |
| GET Group | GET | /conductor\_redundancy\_groups/<ID of group> | Get the attributes of the specified Conductor redundancy group. |
| DELETE Group | DELETE | /conductor\_redundancy\_groups/<ID of group> | Delete the Conductor redundancy group that has the specified ID. |
| POST Enable Group | POST | conductor\_ redundancy\_groups/<ID of group>/enable | Enable redundancy on the two Conductor nodes in the Conductor redundancy group. |
| DELETE Disable Group | DELETE | conductor\_ redundancy\_groups/<ID of group>/disable | Disable redundancy on the Conductor redundancy group. |
