---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_decomissioning_resources_decommission.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST04-BP03 Decommission resources
<a name="cost_decomissioning_resources_decommission"></a>

 Decommission resources triggered by events such as periodic audits, or changes in usage. Decommissioning is typically performed periodically, and is manual or automated.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The frequency and effort to search for unused resources should reflect the potential savings, so an account with a small cost should be analyzed less frequently than an account with larger costs. Searches and decommission events can be triggered by state changes in the workload, such as a product going end of life or being replaced. Searches and decommission events may also be triggered by external events, such as changes in market conditions or product termination.

**Implementation steps**
+  **Decommission resources: **Using the decommissioning process, decommission each of the resources that have been identified as orphaned.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
