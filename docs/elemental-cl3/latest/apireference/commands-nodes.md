---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-nodes.html
---

# Nodes
<a name="commands-nodes"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Node | POST | /nodes | Add a node to the cluster. |
| GET Node List | GET | /nodes | Get the list of the nodes in the cluster. |
| GET Node | GET | /nodes/<ID of node> | Get the attributes on the specified node. |
| GET Node Status | GET | /nodes/<ID of node>/system\_status | Get the status of the specified node. |
| DELETE Node | DELETE  | /nodes/<ID of node> | Remove the specified node from the cluster. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
