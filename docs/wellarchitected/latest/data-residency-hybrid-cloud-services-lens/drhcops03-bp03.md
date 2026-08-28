---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops03-bp03.html
---

# DRHCOPS03-BP03 Build redundant network connectivity
<a name="drhcops03-bp03"></a>

 Create redundant network connections to avoid connectivity loss to the Region and your workloads.

 **Desired outcome:** Redundant network connectivity improves your availability posture and supports your business continuity needs along with data residency requirements

 **Benefits of establishing this best practice:** Deploying redundant network connectivity using Outposts and Local Zones helps organizations maintain high availability, minimize latency, and keep data within specified geographic boundaries, addressing performance, resilience, and regulatory needs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-5"></a>
+  Establish redundant network connections between Outposts and AWS Regions using AWS Direct Connect or VPN connections.
+  Implement failover mechanisms to automatically switch over to a secondary network connection in case of a failure, reducing downtime and meeting RTO targets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
