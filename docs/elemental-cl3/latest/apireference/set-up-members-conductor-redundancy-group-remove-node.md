---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-remove-node.html
---

# DELETE: Remove a Node from the Conductor Redundancy Group
<a name="set-up-members-conductor-redundancy-group-remove-node"></a>

Remove the Conductor node with the specified member ID from the Conductor redundancy group. Conductor redundancy must be disabled; if it is currently enabled, disable it as described in [DELETE Disable: Disable Conductor Redundancy Group](set-up-conductor-redundancy-groups-disable.md).

```
DELETE http://<Conductor IP address>/conductor_redundancy_groups/<ID of Conductor redundancy group>/members/<ID of member node>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
