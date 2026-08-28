---
source_url: https://docs.aws.amazon.com/sap/latest/sap-AnyDB/sap-ibm-pacemaker-overview.html
---

# Overview
<a name="sap-ibm-pacemaker-overview"></a>

Instructions in this document are based on recommendations provided by SAP and IBM on Db2 deployment on Linux via the SAP notes and KB articles listed in Table 1.

**Note**
When deploying IBM Db2 version 11.5 Mod Pack 6 (11.5.6) or higher, refer to the option recommended by IBM. For more information, see [Integrated solution using Pacemaker](https://www.ibm.com/docs/en/db2/11.5?topic=feature-integrated-solution-using-pacemaker).

 *Table 1 - SAP NetWeaver on IBM Db2 OSS Notes*

| SAP OSS Note | Description |
| --- | --- |
|  ** 1656099 **  | SAP Applications on AWS: Supported DB/OS and Amazon EC2 products |
|  **1656250 **  | SAP on AWS: Supported instance types |
|  **1612105 **  | DB6: FAQ on Db2 High Availability Disaster Recovery (HADR) |
|  **101809**  | DB6: Supported Db2 Versions and Fix Pack Levels |
|  **1168456 **  | SAP Db2 support info |
|  **1600156 **  | SAP Db2 support on AWS  |

 **What this guide doesn’t do**

This document doesn’t provide guidance on how to set up network and security constructs like Amazon Virtual Private Cloud (Amazon VPC), subnets, route tables, access control lists (ACLs), Network Address Translation (NAT) Gateway, AWS Identity and Access Management (IAM) Roles, or AWS Security Groups. It doesn’t cover the high availability (HA) setup for the SAP Application Server Central Services/Enqueue Replication Server (ASCS/ERS), and focuses only on the database (DB) layer when covering the single points of failure (SPOF) for the SAP applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
