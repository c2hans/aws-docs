---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/operational-excellence.html
---

# Operational excellence
<a name="operational-excellence"></a>

 Operational excellence includes the ability to support development and run workloads effectively, gain insight into their operations, and to continuously improve supporting processes and procedures to deliver business value. This section provides an overview of design principles, questions, best practices, and guidance on implementation. For more information, see [Operational Excellence Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

## Definitions
<a name="definitions-ops"></a>

 This whitepaper covers operational excellence in the cloud, describing best practices in the following areas:
+  Organization
+  Prepare
+  Operate
+  Evolve

## Design principles
<a name="design-principles-ops"></a>
+  **Local Zones:** Operational design principles for Local Zones should focus on seamless integration with cloud-based monitoring and management tools, same as for deployments in an AWS Region. Implement robust incident response plans tailored to the specific metropolitan area, ensuring continuous service availability and [regulatory compliance](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/). For more information, see [Connectivity options for Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity.html).
+  **Outposts:** Operational design principles for Outposts should focus on automating deployment and configuration processes and aligning with existing on-premises operational procedures and governance frameworks. Implement centralized monitoring, logging, and incident response mechanisms to maintain consistent compliance, as AWS Outposts requires additional accountability within the shared responsibility model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
