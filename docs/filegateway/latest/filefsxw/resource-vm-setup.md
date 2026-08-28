---
source_url: https://docs.aws.amazon.com/filegateway/latest/filefsxw/resource-vm-setup.html
---

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Deploying and configuring the gateway VM host
<a name="resource-vm-setup"></a>

The following topics provide information about setting up the virtual machine host platform for your gateway.

**Topics**
+ [Deploy a default Amazon EC2 host for FSx File Gateway](ec2-quicklaunch-settings.md)
+ [Deploy a customized Amazon EC2 host for FSx File Gateway](ec2-gateway-file.md)
+ [Modify Amazon EC2 instance metadata options](modify-ec2-instance-metadata.md)
+ [Synchronize VM time with Hyper-V or Linux KVM host time](MaintenanceTimeSync-hyperv.md)
+ [Synchronize VM time with VMware host time](GettingStartedSyncVMTime-common.md)
+ [Configuring network adapters for your gateway](configure-multi-nic.md)
+ [Using VMware vSphere High Availability with Storage Gateway](vmware-ha.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
