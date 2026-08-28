---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-fc-v3-delete-cluster.html
---

# Trying to delete a cluster
<a name="troubleshooting-fc-v3-delete-cluster"></a>

If you get an error while trying to delete a cluster, the following sections provide troubleshooting tips for the common scenarios.

## The `pcluster delete-cluster` command fails to run locally
<a name="delete-cluster-failure-cli-v3"></a>

Check the `~/.parallelcluster/pcluster-cli.log` file in your local file system.

## The cluster stack fails to delete
<a name="delete-cluster-failure-v3"></a>

If the cluster stack fails to delete, check the CloudFormation stack events message.

Check if your issue is mentioned in [GitHub Known Issues](https://github.com/aws/aws-parallelcluster/wiki) at AWS ParallelCluster on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
