---
source_url: https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-windows-storage-plan.html
---

# Storage
<a name="bobi-windows-storage-plan"></a>

See the [Sizing](bobi-windows-sizing.md) section for resources on SAP’s standard recommendations. If no storage performance requirements are available, AWS recommends General Purpose SSD (gp3) as the default EBS volume type for SAP workloads.

If the installation type is distributed or HA, fileshares for the global filesystem and transport directories will need to be used across all relevant EC2 instances. In this guide we will use standard Windows filesharing features to share these directories from the EC2 instance hosting the central services. The sapinst.exe installer will create these shares automatically if it is run as a user with appropriate permissions. Customers can also use NFS-based solutions (such as [Amazon FSx](https://aws.amazon.com/fsx), third-party solutions such as those available from the [AWS Marketplace](https://aws.amazon.com/marketplace/) or custom-built solutions), but that is beyond the scope of this guide. If using such a solution in the context of a high-availability installation, consider that the NFS solution could itself be a single point of failure without appropriate protection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
