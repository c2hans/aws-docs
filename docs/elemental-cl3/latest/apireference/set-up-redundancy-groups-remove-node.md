---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-remove-node.html
---

# DELETE: Remove a Node from a Redundancy Group
<a name="set-up-redundancy-groups-remove-node"></a>

Remove the node with the specified member ID from the specified redundancy group.

```
DELETE http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>/members/<ID of member node>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
