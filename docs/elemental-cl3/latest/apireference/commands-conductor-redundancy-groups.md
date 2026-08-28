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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
