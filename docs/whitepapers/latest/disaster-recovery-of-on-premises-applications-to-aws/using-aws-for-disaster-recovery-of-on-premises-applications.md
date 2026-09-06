---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/using-aws-for-disaster-recovery-of-on-premises-applications.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using AWS for disaster recovery of on-premises applications
<a name="using-aws-for-disaster-recovery-of-on-premises-applications"></a>

 The following section outlines the benefits of using AWS for disaster recovery, explores various AWS disaster recovery solutions, and explains how to assess and implement a disaster recovery solution.

## Benefits of using AWS for disaster recovery
<a name="benefits-of-using-aws-for-disaster-recovery"></a>

 Using AWS for disaster recovery offers services that have the following benefits:
+  **Elasticity** – Disaster recovery-related AWS services are normally billed per usage. This provides the flexibility to utilize AWS as a disaster recovery site by paying only for the resources used, rather than committing to a long-term contract or set number of servers.
+  **TCO** – AWS offers a lower TCO than traditional, non-cloud solutions. AWS-based disaster recovery uses minimal resources in customers’ AWS accounts – primarily low-cost storage for replicating data. Customers are billed only for fully provisioned servers when launched at the time of recovery or drill.
+  **RTO and RPO** – Ability to achieve RTOs of minutes by launching the disaster recovery site on demand and RPOs of seconds using continuous data replication.
+  **Source infrastructure support** – Supports most applications running on x86 architecture (including physical and virtual).
+  **Hypervisor support** – Supports any hypervisor (including physical servers, when there is no hypervisor at all).
+  **Wide OS support** – AWS supports a [large variety](https://aws.amazon.com/ec2/faqs/) of Linux distributions and Windows versions.
+  **Environment isolation** – Ability to create the disaster recovery site in an isolated environment so that drills do not impact the source site.
+  **Application** **support** – Atomicity, consistency, isolation, durability (ACID)-compliant applications are supported, including any ACID-compliant database, such as Microsoft SQL Server, Oracle Database, and SAP HANA.
+  **Automation** – Ability to fully automate all of the disaster recovery-related operations.
+  **Ease of use** – Ability to add the disaster recovery capabilities to working applications with no need for redesign or re-architecture work.
