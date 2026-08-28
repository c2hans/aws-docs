---
source_url: https://docs.aws.amazon.com/guidance/latest/migrating-vmware-virtual-machines-to-nutanix-cloud-clusters-on-aws/nutanix-move-architecture-overview.html
---

# Nutanix Move architecture overview
<a name="nutanix-move-architecture-overview"></a>

Nutanix Move is delivered as a virtual machine (VM) appliance, which is typically hosted on the target Nutanix AHV cluster running on AWS. The Nutanix Move tool is composed of several software services that can be categorized into the following major software components:

1. The management server

1. Virtual move appliances for both the source and target environments

1. Disk readers and writers

The architecture of Nutanix Move for VMware ESXi environments utilizes the vCenter platform for inventory collection, and uses the vSphere Storage APIs for Data Protection (VADP), the Virtual Disk Development Kit (VDDK), and Changed Block Tracking (CBT) functionality to facilitate the data migration process.

An architecture diagram for the Nutanix Move solution is provided:

![Depicts Nutanix Move components](http://docs.aws.amazon.com/guidance/latest/migrating-vmware-virtual-machines-to-nutanix-cloud-clusters-on-aws/images/nutanix-move-architecture.jpeg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Migrating VMWare Virtual Machines to Nutanix Cloud Clusters on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
