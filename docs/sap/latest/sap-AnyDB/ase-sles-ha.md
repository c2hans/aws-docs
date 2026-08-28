---
source_url: https://docs.aws.amazon.com/sap/latest/sap-AnyDB/ase-sles-ha.html
---

# SAP ASE for SAP NetWeaver on AWS: high availability configuration for SUSE Linux Enterprise Server (SLES) for SAP applications
<a name="ase-sles-ha"></a>

This topic applies to SUSE Linux Enterprise Server (SLES) operating system for SAP NetWeaver running SAP Adaptive Server Enterprise (ASE) database on AWS cloud. It covers the instructions for configuration of a pacemaker cluster for SAP ASE database when deployed on Amazon EC2 instances in two different Availability Zones within an AWS Region and FSx for ONTAP as the storage layer.

This topic covers the implementation of high availability using the cold standby method. For more information, see [SAP Note 1650511 – SYB: High Availability Offerings with SAP Adaptive Server Enterprise](https://me.sap.com/notes/1650511/E) (requires SAP portal access).

**Topics**
+ [Planning](ase-sles-ha-planning.md)
+ [Architecture diagram](ase-sles-ha-diagrams.md)
+ [Deployment](ase-sles-ha-deployment.md)
+ [Operations](ase-sles-ha-operations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
