---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/cluster-secret-rotation-troubleshooting.html
---

# Troubleshooting cluster secret rotation in AWS PCS
<a name="cluster-secret-rotation-troubleshooting"></a>

Cluster secret rotation fails if the environment isn't properly prepared. The most common cause is active instances in your cluster. To prevent failure:

1. Set all node groups to 0 capacity.

1. Wait for nodes to stop.

1. Verify your cluster isn't in these states: `CREATE_FAILED`, `DELETE_FAILED`, `RESUMING`, `SUSPENDING`, or `SUSPENDED`.

If rotation fails:
+ A RotationFailed CloudTrail event appears
+ The cluster secret remains unchanged
+ Check the RotationFailed event in CloudTrail for details
+ Complete all preparation steps for successful rotation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
