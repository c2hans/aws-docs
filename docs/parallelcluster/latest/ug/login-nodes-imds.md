---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/login-nodes-imds.html
---

# Imds properties for login nodes
<a name="login-nodes-imds"></a>

Access to the login node's IMDS (and the instance profile credentials) is restricted to root user, cluster administrative user (`pc-cluster-admin` by default) and operating system specific default user (`ec2-user` on Amazon Linux 2023 and Red Hat, and `ubuntu` on Ubuntu 22.04 and Ubuntu 24.04)

To restrict IMDS access, AWS ParallelCluster manages a chain of `iptables`.

**Note**
Any customization of `iptables` or `ip6tables` rules can interfere with the mechanism used to restrict IMDS access on the login node.See also [`Imds property setting`](HeadNode-v3.md#HeadNode-v3-Imds).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
