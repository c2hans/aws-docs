---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/hybrid-migration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid Migration
<a name="hybrid-migration"></a>

 Hybrid migration refers to migrating virtual machines between two different vSphere installations: one that's in your on-premises data center and another that's in your VMware Cloud on AWS SDDC. Because these two vSphere installations might have different versions, configurations, or both, hybrid migration use cases typically carry additional prerequisites and configuration that ensure both compatibility of the virtual machines and appropriate network bandwidth and latency. VMware Cloud on AWS supports a variety of tools and methods for hybrid migration.
+ [Hybrid Migration With VMware HCX](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-E8671FC6-F64B-4D41-8F01-B6120B0E3675.html) VMware HCX, a multi-cloud app mobility solution, is provided free to all SDDCs and facilitates migration of workload VMs from your on-premises data center to your SDDC.
+ [Hybrid Migration with vMotion](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-DC377E35-B44A-444F-96ED-E7B6B3601DBB.html) Migration with vMotion, also known as hot migration or live migration, moves a powered-on VM from one host or datastore to another. Migration with vMotion is the best option for migrating small numbers of VMs without incurring any downtime.
+ [Hybrid Cold Migration](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-9ED97515-4714-4619-9C06-67744EDE2261.html) Cold migration moves powered-off VMs from one host or datastore to another. Cold migration is a good option when you can tolerate some VM downtime during the migration process.

## Migrate using VMware HCX
<a name="migrate-using-vmware-hcx"></a>

 This pattern describes the use of VMware Hybrid Cloud Extension (HCX) to migrate your on-premises virtual machines (VMs) and applications to VMware Cloud on Amazon Web Services (AWS). The migration uses VMware enterprise-class software-defined data center (SDDC) software on the AWS Cloud to provide optimized access to AWS services.

 VMware Cloud on AWS integrates compute, storage, and network virtualization products (vSphere, vSAN, and VMware NSX) with VMware vCenter server management, which is optimized to run on dedicated, elastic, bare-metal AWS infrastructure. The resulting infrastructure is low-maintenance, simplified, and hyper-converged. With this service, IT teams can manage their cloud-based resources with familiar VMware tools. For more information, see [VMware Cloud on AWS](https://cloud.vmware.com/vmc-aws) on the VMware website.

 VMware HCX supports three types of cloud migrations:
+  **Hybridity (data center extension):** Extending an existing, on-premises VMware SDDC to AWS to provide footprint expansion, on-demand capacity, a testing/development environment, and virtual desktops.
+  **Cloud evacuation (data center-wide infrastructure refresh):** Consolidating data centers and moving completely to the AWS Cloud (including handling data center co-location or end of lease).
+  **Application-specific:** Moving individual applications to the AWS Cloud to meet specific business needs.

 Following is the deployment architecture for migrating Oracle VMs from on-premises data centers to VMware Cloud on AWS. This migration is done without making any changes to the operating system, Oracle applications, or the databases.

 In this setup, the on-premises data center can be connected to the VMware Cloud on AWS environment using DX or IPsec VPN and the actual migrations are performed using VMware HCX

![Reference architecture diagram showing Oracle E-Business Suite Migration on VMWare Cloud on AWS](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/vmware-hcx-migration.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
