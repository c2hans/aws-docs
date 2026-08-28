---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_pricing_model_analysis.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST07-BP01 Perform pricing model analysis
<a name="cost_pricing_model_analysis"></a>

 Analyze each component of the workload. Determine if the component and resources will be running for extended periods (for commitment discounts), or dynamic and short-running (for Spot or On-Demand Instances). Perform an analysis on the workload using the Recommendations feature in AWS Cost Explorer.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

AWS has multiple [pricing models](https://aws.amazon.com/pricing/) that allow you to pay for your resources in the most cost-effective way that suits your organization’s needs.

**Implementation steps**
+ ** Perform a commitment discount analysis:** Using Cost Explorer in your account, review the Savings Plans and Reserved Instance recommendations. To verify that you implement the correct recommendations with the required discounts and risk, follow the [Well-Architected labs](https://wellarchitectedlabs.com/cost/costeffectiveresources/).
+  **Analyze workload elasticity: **Using the hourly granularity in Cost Explorer, or a custom dashboard. Analyze the workload elasticity. Look for regular changes in the number of instances that are running. Short duration instances are candidates for Spot Instances or Spot Fleet.
  +  [Well-Architected Lab: Cost Explorer](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/Lab_Guide.html#Elasticity)
  +  [Well-Architected Lab: Cost Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_5_Cost_Visualization/README.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Accessing Reserved Instance recommendations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-recommendations.html)
+  [Instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

 **Related videos:**
+  [Save up to 90% and run production workloads on Spot](https://www.youtube.com/watch?v=BlNPZQh2wXs)

 **Related examples:**
+  [Well-Architected Lab: Cost Explorer](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_5_Cost_Visualization/Lab_Guide.html#Elasticity)
+  [Well-Architected Lab: Cost Visualization](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_5_Cost_Visualization/README.html)
+  [Well-Architected Lab: Pricing Models](https://wellarchitectedlabs.com/Cost/CostEffectiveResources.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
