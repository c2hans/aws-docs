---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-placement-group.html
---

# (Optional) Create a placement group
<a name="working-with_networking_efa_create-placement-group"></a>

We recommended you launch all instances that use EFA in a cluster placement group to minimize the physical distance between them. Create a placement group for each compute node group where you plan to use EFA. See [Placement groups for EC2 instances in AWS PCS](working-with_networking_placement-groups.md) to create a placement group for your compute node group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
