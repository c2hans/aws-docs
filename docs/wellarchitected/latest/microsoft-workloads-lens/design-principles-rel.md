---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/design-principles-rel.html
---

# Design principles
<a name="design-principles-rel"></a>
+  **Use Microsoft high availability patterns:** Implement SQL Server Always On Availability Groups across multiple Availability Zones, deploy Active Directory domain controllers with proper site topology, and use Exchange Database Availability Groups to maintain Microsoft workload resilience while benefiting from AWS infrastructure reliability.
+  **Integrate with AWS managed services for Microsoft technologies:** Use Amazon RDS Multi-AZ for SQL Server, AWS Managed Microsoft AD for directory services, and Amazon FSx for Windows File Server to reduce operational overhead while maintaining Microsoft workload compatibility and using AWS managed reliability features.
+  **Design for cross-AZ resilience with Microsoft-aware configurations:** Configure SQL Server listener endpoints across Availability Zones, establish Active Directory sites aligned with Availability Zones, implement SharePoint farm topology with cross-AZ redundancy, and verify that .NET applications handle Availability Zone failures gracefully through stateless design and proper load balancing.

 For general reliability design principles that apply to all workloads, see [Design principles for reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
