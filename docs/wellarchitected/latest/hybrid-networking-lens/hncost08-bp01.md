---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost08-bp01.html
---

# HNCOST08-BP01 Regular cost analysis
<a name="hncost08-bp01"></a>

 Review cost dashboards to identify underutilized resources, anomalous spikes, and opportunities to switch connectivity types.

 **Desired outcome:** Data-driven cost reduction through continuous refinement.

 **Level of risk exposed if this best practice is not established:** Low

 **Benefits of establishing this best practice:**
+  Visibility into cost drivers
+  Identification of legacy resources for decommissioning
+  Support for budget forecasting

## Implementation guidance
<a name="implementation-guidance-59"></a>
+  Identified data transfer changes in cost data, such as by filtering Cost and Usage data by line\_item\_usage\_type for DataTransfer-Out-Bytes.
+  Use cost dashboards to review usage patterns. For example, you can achieve this by using Amazon Athena and Amazon Quick Suite.
+  Share findings in regular, weekly or monthly and FinOps reviews.

 **Resources:**
+  [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/data-transfer-cost-analysis.html)
+  [AWS Well-Architected Cost & Usage Report Library](https://catalog.workshops.aws/cur-query-library/en-US/queries/networking-and-content-delivery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
