---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-redundancy-group-members.html
---

# Members of a Redundancy Group
<a name="commands-redundancy-group-members"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Member | POST | /redundancy\_groups/<ID of redundancy group>/members | Add a new node to the specified redundancy group. |
| PUT Member | PUT | /redundancy\_groups/<ID of redundancy group>/members/<ID of member node> | Modify the attributes of the specified node in the specified redundancy group. |
| GET Member List | GET | /redundancy\_groups/<ID of redundancy group>/members | Get the list of the nodes in the specified redundancy group. |
| GET Member | GET | /redundancy\_groups/<ID of redundancy group>/members/<ID of member node> | Get the attributes of the specified node in the specified redundancy group. |
| DELETE Member | DELETE  | /redundancy\_groups/<ID of redundancy group>/members/<ID of member node> | Delete the node with the specified ID from the specified redundancy group. |
| POST Initiate Failover | POST | /nodes/<ID of node>/redundancy | Test redundancy set up by initiating failover of the specified node. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
