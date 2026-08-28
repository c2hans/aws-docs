---
source_url: https://docs.aws.amazon.com/storagegateway/latest/tgw/resource-vm-setup.html
---

# Deploying and configuring the gateway VM host
<a name="resource-vm-setup"></a>

The topics in this section describe how to set up and manage the virtual machine host for your Storage Gateway appliance, including on-premises appliances running on VMware, Hyper-V, or Linux KVM, and appliances running on Amazon EC2 instances in the AWS cloud.

**Topics**
+ [Deploy a default Amazon EC2 host for Tape Gateway](ec2-quicklaunch-settings.md) - Learn about how to deploy and activate a Tape Gateway on an Amazon Elastic Compute Cloud (Amazon EC2) instance using the default specifications.
+ [Deploy a customized Amazon EC2 instance for Tape Gateway](ec2-gateway-common.md) - Learn about how to deploy and activate a Tape Gateway on an Amazon Elastic Compute Cloud (Amazon EC2) instance using customized settings.
+ [Modify Amazon EC2 instance metadata options](modify-ec2-instance-metadata.md) - Learn about how to configure your Amazon EC2 gateway instance to accept incoming metadata requests that use IMDS Version 1 (IMDSv1) or require that all metadata requests use IMDS Version 2 (IMDSv2).
+ [Synchronize VM time with Hyper-V or Linux KVM host time](MaintenanceTimeSync-hyperv.md) - Learn about how to view and synchronize the time of an on-premises Hyper-V or Linux KVM gateway virtual machine to a Network Time Protocol (NTP) server.
+ [Synchronize VM time with VMware host time](GettingStartedSyncVMTime-common.md) - Learn about how to check the host time for a VMware gateway virtual machine and, if needed, set the time and configure the host to synchronize its time automatically to a Network Time Protocol (NTP) server.
+ [Configuring paravirtualization on a VMware host](SetParaVirtualization-common.md) - Learn about how you can configure the VMware host platform for your Storage Gateway appliance to use paravirtual Internet Small Computer System Interface Protocol (iSCSI) controllers.
+ [Configuring network adapters for your gateway](NICConfiguring-common.md) - Learn about how you can reconfigure your gateway to use the VMXNET3 (10 GbE) network adapter, or to use more than one network adapter so that it can be accessed fron nultiple IP addresses.
+ [Using VMware vSphere High Availability with Storage Gateway](vmware-ha.md) - Learn about how to protect your storage workloads against hardware, hypervisor, or network failures by configuring Storage Gateway to work with VMware vSphere High Availability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
