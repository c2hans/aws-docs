---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus02-bp02.html
---

# HNSUS02-BP02 Perform lifecycle assessments for sustainability trade-offs
<a name="hnsus02-bp02"></a>

 Evaluate the environmental impact of architectural decisions (for example, regional placement, instance types, storage classes). Compare trade-offs between performance, cost, and sustainability.

 **Desired outcome:** Informed decisions that balance business needs with environmental responsibility.

 **Level of risk exposed if this best practice is not established:** Low

 **Benefits of establishing this best practice:**
+  Identifies opportunities to reduce carbon footprint without compromising functionality
+  Supports ESG reporting and transparency

## Implementation guidance
<a name="implementation-guidance-62"></a>
+  Use tools, such as the [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/blogs/aws/new-customer-carbon-footprint-tool/), to measure emissions
+  Prefer regions powered by renewable energy
+  Consider more efficient resources, such as Graviton-based instances

## Resources
<a name="resources-51"></a>
+  [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/sustainability/tools/aws-customer-carbon-footprint-tool/)[AWS Graviton Processor](https://aws.amazon.com/pm/ec2-graviton/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
