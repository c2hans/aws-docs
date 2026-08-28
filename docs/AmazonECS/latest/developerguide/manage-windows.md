---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/manage-windows.html
---

# Amazon ECS Windows container instance management
<a name="manage-windows"></a>

When you use EC2 instances for your Amazon ECS workloads, you are responsible for maintaining the instances.

Agent updates do not apply to Windows container instances. We recommend that you launch new container instances to update the agent version in your Windows clusters.

**Topics**
+ [Launching a container instance](launch_window-container_instance.md)
+ [Bootstrapping container instances](bootstrap_windows_container_instance.md)
+ [Using an HTTP proxy for Windows container instances](http_proxy_config-windows.md)
+ [Configuring container instances to receive Spot Instance notices](windows-spot-instance-draining-container.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
