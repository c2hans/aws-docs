---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/headnode-connect-v3.html
---

# Connect to a cluster
<a name="headnode-connect-v3"></a>

When you use AWS ParallelCluster, you can connect to the cluster head node to run jobs, view results, manage users, and monitor the cluster and job status. To connect to the cluster head node instance, use one of the following methods:
+ You can use `ssh` with a [key pair](install-v3.md#set-up-keypair) to log in. Specify the private key in [`HeadNode`](HeadNode-v3.md) / [`KeyName`](HeadNode-v3.md#yaml-HeadNode-Ssh-KeyName) in the cluster configuration. For more information, see [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) in the *Amazon EC2 User Guide for Linux Instances*.
+ You can use the `pcluster ssh` command line interface (CLI) command to log in. Specify the private key in the cluster configuration [`HeadNode`](HeadNode-v3.md) / [`KeyName`](HeadNode-v3.md#yaml-HeadNode-Ssh-KeyName). For more information, see [`pcluster ssh`](pcluster.ssh-v3.md).
+ You can use an SSM session to connect to the cluster head node. You must add the `AmazonSSMManagedInstanceCore` managed policy to [`HeadNode`](HeadNode-v3.md) / [`AdditionalIamPolicies`](HeadNode-v3.md#yaml-HeadNode-Iam-AdditionalIamPolicies) in the cluster configuration to connect by using an SSM session. For more information, see [SSM session manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) in the *SSM User Guide*.
+ You can use Amazon DCV to connect to the cluster head node. For more information, see [Connect to the head and login nodes through Amazon DCV](dcv-v3.md).
+ When you use the PCUI, you can also use an Amazon EC2 Connect command that the UI provides to connect to the cluster head node.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
