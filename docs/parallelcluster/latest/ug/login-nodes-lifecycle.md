---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/login-nodes-lifecycle.html
---

# Login Nodes lifecycle
<a name="login-nodes-lifecycle"></a>

Currently, there is no dedicated command to stop and start the login nodes in a pool. In order to stop the login nodes in a pool the cluster administrator has to update the cluster configuration specifying zero on the count of login nodes (`Count: 0` ) and then run an [`pcluster.update-cluster-v3`](pcluster.update-cluster-v3.md) command.

**Note**
Logged in users are notified about the termination of the specific instance and about the related gracetime period. During the gracetime period no new connections will be allowed except for the ones from the [cluster default user](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html). The message shown is customizable by the cluster administrator from the head node or from a login node editing the file  `/opt/parallelcluster/shared_login_nodes/loginmgtd_config.json`. This termination message is not visible when you are connected using the [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Session Manager.

 In order to start the login nodes pool the cluster administrator has to restore the previous `Count` value in the cluster configuration and then run an [`update-cluster`](pcluster.update-cluster-v3.md) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
