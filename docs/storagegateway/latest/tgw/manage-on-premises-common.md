---
source_url: https://docs.aws.amazon.com/storagegateway/latest/tgw/manage-on-premises-common.html
---

# Performing Tasks on the VM Local Console
<a name="manage-on-premises-common"></a>

For a Tape Gateway that you deploy on-premises, you can perform the following maintenance tasks using the gateway local console that you access from your virtual machine host platform. These tasks are common to VMware, Microsoft Hyper-V, and Linux Kernel-based Virtual Machine (KVM) hypervisors.

**Topics**
+ [Logging in to the Tape Gateway local console](LocalConsole-login-common.md) - Learn about how to log in to the gateway local console where you can configure gateway network settings and change the default password.
+ [Configuring a SOCKS5 proxy for your on-premises gateway](MaintenanceRoutingProxy-common.md) - Learn about how you can configure Storage Gateway to route all AWS endpoint traffic through a Socket Secure version 5 (SOCKS5) proxy server.
+ [Configuring Your Gateway Network](MaintenanceConfiguringStaticIP-common.md) - Learn about how you can configure your gateway to use DHCP or assign a static IP address.
+ [Testing your gateway connection to the internet](MaintenanceTestGatewayConnectivity-common.md) - Learn about how you can use the gateway local console to test the connection between the gateway and the internet.
+ [Running storage gateway commands in the local console for an on-premises gateway](MaintenanceGatewayConsole-common.md) - Learn about how to run local console commands that allow you to perform additional tasks such as saving routing tables, connecting to Support, and more.
+ [Viewing your gateway system resource status](system-resource-check-common.md) - Learn about how to check the virtual CPU cores, root volume size, and RAM that are available to your gateway appliance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
