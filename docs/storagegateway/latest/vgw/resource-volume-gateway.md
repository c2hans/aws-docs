---
source_url: https://docs.aws.amazon.com/storagegateway/latest/vgw/resource-volume-gateway.html
---

# Working with Volume Gateway storage resources
<a name="resource-volume-gateway"></a>

The topics in this section describe how you can manage the storage resources that are associated with your Volume Gateway appliance and its virtual host platform. This includes resources such as the physical disks attached to a gateway's hypervisor host platform, with specific procedures for removing disks from VMware vSphere ESXi, Microsoft Hyper-V, or Linux Kernel-based Virtual Machine (KVM) virtualization hosts. This also includes managing the Amazon EBS volumes attached to a gateway's Amazon EC2 instance for gateways hosted on Amazon EC2 in the AWS cloud.

**Topics**
+ [Removing Disks from Your Gateway](add-remove-disks.md) - Learn about what to do if you need to remove a disk from the VMware vSphere ESXi, Microsoft Hyper-V, or Linux Kernel-based Virtual Machine (KVM) virtualization host platform for your gateway, for example if you have a physical disk failure.
+ [Managing Amazon EBS volumes on Amazon EC2 gateways](GatewayInstanceStorage-common.md) - Learn about how you can increase or reduce the quanity of Amazon EBS volumes that are allocated for use as upload buffer or cache storage for a gateway that is hosted on an Amazon EC2 instance, for example, if your application storage needs increase or decrease over time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
