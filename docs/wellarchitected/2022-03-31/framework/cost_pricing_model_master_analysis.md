---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_pricing_model_master_analysis.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST07-BP05 Perform pricing model analysis at the master account level
<a name="cost_pricing_model_master_analysis"></a>

 Use Cost Explorer Savings Plans and Reserved Instance recommendations to perform regular analysis at the management account level for commitment discounts.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Performing regular cost modeling ensures that opportunities to optimize across multiple workloads can be implemented. For example, if multiple workloads use On-Demand Instances, at an aggregate level, the risk of change is lower, and implementing a commitment-based discount will achieve a lower overall cost. It is recommended to perform analysis in regular cycles of two weeks to one month. This allows you to make small adjustment purchases, so the coverage of your pricing models continues to evolve with your changing workloads and their components.

Use the [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) recommendations tool to find opportunities for commitment discounts.

To find opportunities for Spot workloads, use an hourly view of your overall usage, and look for regular periods of changing usage or elasticity.

**Implementation steps**
+ ** Perform a commitment discount analysis: **Using Cost Explorer in your account review the Savings Plans and Reserved Instance recommendations. To verify you implement the correct recommendations with the required discounts and risk, follow the Well-Architected labs.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Accessing Reserved Instance recommendations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-recommendations.html)
+  [Instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

 **Related videos:**
+  [Save up to 90% and run production workloads on Spot](https://www.youtube.com/watch?v=BlNPZQh2wXs)

 **Related examples:**
+  [Well-Architected Lab: Pricing Models](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_3_Pricing_Models/README.html)
