---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes.html
---

# AWS PCS login nodes
<a name="working-with_login-nodes"></a>

An AWS PCS cluster usually needs at least 1 login node to support interactive access and job management. A way to accomplish this is with a static AWS PCS compute node group configured for login node capability. You can also configure a standalone EC2 instance to act as a login node.

**Topics**
+ [Using an AWS PCS compute node group to provide login nodes](working-with_login-nodes_compute-node-group-for-login.md)
+ [Using standalone instances as AWS PCS login nodes](working-with_login-nodes_standalone.md)
+ [Connecting a standalone login node to multiple clusters in AWS PCS](multi-cluster-login-script.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
