---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/cfn-cluster-ops.html
---

# Cluster operations
<a name="cfn-cluster-ops"></a>

When a cluster custom resource is added to a CloudFormation stack, CloudFormation can perform the following cluster operations:
+ CloudFormation creates a cluster in a new separate stack when it deploys a stack that includes the AWS ParallelCluster custom resource.
+ If you update the cluster configuration defined in the stack, according to configuration update policies, CloudFormation updates the cluster. The AWS ParallelCluster custom resource provider doesn't stop the compute fleet before updating the cluster. We recommend that you use the [`QueueUpdateStrategy`](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy) setting for cluster updates. This way, you can avoid making explicit `pcluster update-compute-fleet` calls before and after updates when using the AWS ParallelCluster custom resource.
+ If you delete the stack, the cluster is deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
