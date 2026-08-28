---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-conductor-redundancy-group-members.html
---

# Members of a Conductor Redundancy Group
<a name="commands-conductor-redundancy-group-members"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Member | POST | /conductor\_redundancy\_groups/<br /><ID of group>/members | Add a new node to the specified Conductor redundancy group. |
| GET Member List | GET | /conductor\_redundancy\_groups/<br /><ID of group>/members | Get the list of the nodes in the specified Conductor redundancy group. |
| GET Member | GET | /conductor\_redundancy\_groups/<br /><ID of group>/members/<ID of member node> | Get the attributes of the specified node in the specified Conductor redundancy group. |
| DELETE Member | DELETE  | /conductor\_redundancy\_groups/<br /><ID of group>/members/<ID of member node> | Delete the node with the specified ID from the specified Conductor redundancy group. |
| GET Alerts | GET | /alerts | Get a list of the alerts that have occurred. |
| GET Messages | GET | /messages | Get a list of the messages that have occurred. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
