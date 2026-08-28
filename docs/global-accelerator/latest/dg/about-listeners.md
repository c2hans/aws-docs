---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html
---

# Listeners for standard accelerators in AWS Global Accelerator
<a name="about-listeners"></a>

With AWS Global Accelerator, you add listeners that process inbound connections from clients based on the ports and protocols that you specify. Listeners support TCP and UDP protocols.

You define a standard listener when you create your standard accelerator, and you can add more listeners at any time. You associate each listener with one or more endpoint groups, and you associate each endpoint group with one AWS Region.

Optionally, you can configure *client affinity* for a listener. With client affinity, Global Accelerator directs all requests from a user at a specific source (client) IP address to the same endpoint resource. Choosing this option maintains client affinity for your users.

**Topics**
+ [Add a standard listener](about-listeners.creating-listeners.md)
+ [Edit a standard listener](about-listeners.creating-listeners-edit.md)
+ [Remove a standard listener](about-listeners.creating-listeners-remove.md)
+ [How client affinity works in Global Accelerator](about-listeners-client-affinity.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
