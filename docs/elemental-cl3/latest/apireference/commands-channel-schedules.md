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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
