---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/login-nodes-security.html
---

# Security for login nodes
<a name="login-nodes-security"></a>

Login nodes inherit the  `AllowedIPs` settings [`AllowedIps`](HeadNode-v3.md#yaml-HeadNode-Ssh-AllowedIps) from the head node, unless AllowedIps is specified for the [login node pool](LoginNodes-v3.md#LoginNodes-v3-Pools). In this manner, cluster administrators can restrict the security posture of the cluster by specifying the source CIDR or a prefix list from where SSH connections are allowed on either the head node or a pool of login nodes.

 In the present implementation the access to the head node is not automatically restricted when enabling login nodes. If needed, a cluster administrator can restrict this access updating the head nodes ssh configuration using standard Linux commands. This can be also be accomplished by specifying custom Security Groups on the head node by using the   `AdditionalSecurityGroups` setting in the head node section of the ParallelCluster YAML file to deny connections from unauthorized users.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
