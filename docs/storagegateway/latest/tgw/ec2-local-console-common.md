---
source_url: https://docs.aws.amazon.com/storagegateway/latest/tgw/ec2-local-console-common.html
---

# Performing Tasks on the Amazon EC2 Local Console
<a name="ec2-local-console-common"></a>

Some Storage Gateway maintenance tasks require that you log in to the gateway local console for a gateway that you have deployed on an Amazon EC2 instance. You can access the gateway local console on your Amazon EC2 instance by using a Secure Shell (SSH) client. The topics in this section describes how to log in to the gateway local console and perform maintenance tasks.

**Topics**
+ [Logging In to Your Amazon EC2 Gateway Local Console](EC2_MaintenanceConsoleWindow-common.md) - Learn about how you can connect and log in to the gateway local console your Amazon EC2 instance by using a Secure Shell (SSH) client.
+ [Routing your gateway deployed on EC2 through an HTTP proxy](EC2_MaintenanceRoutingProxy-common.md) - Learn about how you can configure Storage Gateway to route all AWS enpoint traffic through a Socket Secure version 5 (SOCKS5) proxy server to your Amazon EC2 gateway instance.
+ [Testing gateway network connectivity](EC2_MaintenanceTestGatewayConnectivity-common.md) - Learn about how you can use the gateway local console to test network connectivity between your gateway and various network resources.
+ [Viewing your gateway system resource status](EC2_system-resource-check-common.md) - Learn about how you can use the gateway local console to check the virtual CPU cores, root volume size, and RAM that are available to your gateway appliance.
+ [Running Storage Gateway commands on the local console](EC2_MaintenanceGatewayConsole-common.md) - Learn about how you can run local console commands that allow you to perform additional tasks such as saving routing tables, connecting to Support, and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
