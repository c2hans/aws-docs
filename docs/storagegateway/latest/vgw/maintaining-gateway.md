---
source_url: https://docs.aws.amazon.com/storagegateway/latest/vgw/maintaining-gateway.html
---

# Maintaining Your Gateway
<a name="maintaining-gateway"></a>

Maintaining your Volume Gateway includes tasks such as sizing and configuring local disks for cache storage and upload buffer space, managing updates and setting an update schedule, managing bandwidth usage, and shutting down or deleting you gateway and associated resources if necessary. These tasks are common to all gateway types. If you haven't created a gateway, see [Creating your gateway](creating-your-gateway.md).

**Topics**
+ [Managing local disks for your Storage Gateway](ManagingLocalStorage-common.md) - Learn how to assess disk size requirements, add cache capacity, and manage the local disks that you allocate to your Volume Gateway for buffering and storage.
+ [Managing Bandwidth for Your Volume Gateway](MaintenanceUpdateBandwidth-common.md) - Learn how to limit the upload throughput from your gateway to AWS to control the amount of network bandwidth the gateway uses.
+ [Managing gateway updates](MaintenanceManagingUpdate-common.md) - Learn how to turn maintenance updates on or off, and modify the maintenance window schedule for your Volume Gateway.
+ [Shutting Down Your Gateway VM](MaintenanceShutDown-common.md) - Learn about what to do if you need to shutdown or reboot your gateway virtual machine for maintenance, such as when applying a patch to your hypervisor.
+ [Deleting your gateway and removing associated resources](deleting-gateway-common.md) - Learn how to delete your gateway using the AWS Storage Gateway console and clean up associated resources to avoid being charged for their continued use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
