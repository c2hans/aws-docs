---
source_url: https://docs.aws.amazon.com/filegateway/latest/filefsxw/maintaining-gateway.html
---

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Maintaining your gateway
<a name="maintaining-gateway"></a>

Maintaining your Amazon FSx File Gateway involves doing general maintenance to optimize your gateway's performance. These tasks are common to all gateway types.

This section contains the following topics, which describe concepts and procedures related to maintaining your Amazon FSx File Gateway:

**Topics**
+ [Managing gateway updates](MaintenanceManagingUpdate-common.md) – Learn how to turn maintenance updates on or off, and modify the maintenance window schedule for your File Gateway.
+ [Performing maintenance tasks using the local console](manage-on-premises.md) – Learn how to perform maintenance tasks using the gateway local console.
+ [Shutting down your gateway VM](MaintenanceShutDown-common.md) – Learn about what to do if you need to shutdown or reboot your gateway virtual machine for maintenance, such as when applying a patch to your hypervisor.
+ [Replacing your existing FSx File Gateway with a new instance](migrate-data.md) – Learn how to replace your FSx File Gateway with a new instance when you want to improve performance or to respond to a notification to migrate the gateway.
+ [Deleting your gateway and removing associated resources](deleting-gateway-common.md) – Learn how to delete your gateway using the AWS Storage Gateway console and clean up associated resources to avoid being charged for their continued use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
