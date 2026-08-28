---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-cleanup.html
---

# Cleaning up after the Neptune Blue/Green solution has completed
<a name="neptune-BG-cleanup"></a>

After you have promoted the staging (green) cluster to production, clean up the resources created by the Neptune Blue/Green solution:
+ Delete the Amazon EC2 instance that was created to run the solution.
+ Delete the CloudFormation templates for the [Neptune streams-based replication](streams-consumer-setup.md) that kept the green cluster in sync with the blue cluster. The main one has the stack name that you provided earlier, and one is composed of the deployment ID followd by "-replication": that is, `{{(DeploymentID)}}-replication`.

Deleting CloudFormation templates doesn't delete the clusters themselves. Once you have verified that the green cluster is working as expected, you can optionally take a snapshot before manually deleting the blue cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
