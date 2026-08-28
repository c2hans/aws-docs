---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/region-selection.html
---

# Region selection
<a name="region-selection"></a>

| CMSUS\_1: Are you selecting the Region to meet both your business requirements and sustainability goals?  |
| --- |
|   |

**CMSUS\_BP1.1: Choose a Region based on both your business requirements and sustainability goals**

Choose a Region to optimize your KPIs, including those related to performance, cost, and carbon footprint. For more details, see [SUS01-BP01](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_region_a2.html) in the *Sustainability Pillar whitepaper*.

**Prescriptive guidance:**
+  An edge device might be on the move and it should connect to the closest Region to meet cost, network latency, and sustainability requirements.
+  As per business and regulatory requirements, configure the critical part of the workload as active/active.
+  Avoid short lived connections from the edge to avoid connection overhead of establishing a new connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
