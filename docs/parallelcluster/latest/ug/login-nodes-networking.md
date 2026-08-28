---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/login-nodes-networking.html
---

# Networking for login nodes
<a name="login-nodes-networking"></a>

Login nodes are provisioned with a single connection address to the network load balancer configured for the pool of login nodes. The connectivity settings of the address are based on the type of subnet specified in the Login nodes Pool configuration.
+ If the subnet is private, the address will be private and, in order to grant access to the login nodes, the cluster administrator must provision a bastion host.
+ If the subnet is public, the address will be public

All connection requests are managed by the Network Load Balancer using round-robin routing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
