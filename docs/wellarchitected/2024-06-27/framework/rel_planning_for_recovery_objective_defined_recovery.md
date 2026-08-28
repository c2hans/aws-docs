---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_planning_for_recovery_objective_defined_recovery.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL13-BP01 Define recovery objectives for downtime and data loss
<a name="rel_planning_for_recovery_objective_defined_recovery"></a>

 The workload has a recovery time objective (RTO) and recovery point objective (RPO).

 *Recovery Time Objective (RTO)* is the maximum acceptable delay between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable.

 *Recovery Point Objective (RPO)*  is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable loss of data between the last recovery point and the interruption of service.

 RTO and RPO values are important considerations when selecting an appropriate Disaster Recovery (DR) strategy for your workload. These objectives are determined by the business, and then used by technical teams to select and implement a DR strategy.

 **Desired Outcome:**

 Every workload has an assigned RTO and RPO, defined based on business impact. The workload is assigned to a predefined tier, defining service availability and acceptable loss of data, with an associated RTO and RPO. If such tiering is not possible then this can be assigned bespoke per workload, with the intent to create tiers later. RTO and RPO are used as one of the primary considerations for selection of a disaster recovery strategy implementation for the workload. Additional considerations in picking a DR strategy are cost constraints, workload dependencies, and operational requirements.

 For RTO, understand impact based on duration of an outage. Is it linear, or are there nonlinear implications? (for example. after four hours, you shut down a manufacturing line until the start of the next shift).

 A disaster recovery matrix, like the following, can help you understand how workload criticality relates to recovery objectives. (Note that the actual values for the X and Y axes should be customized to your organization needs).

![Chart showing the disaster recovery matrix](http://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/images/disaster-recovery-matrix.png)

 **Common anti-patterns:**
+  No defined recovery objectives.
+  Selecting arbitrary recovery objectives.
+  Selecting recovery objectives that are too lenient and do not meet business objectives.
+  Not understanding of the impact of downtime and data loss.
+  Selecting unrealistic recovery objectives, such as zero time to recover and zero data loss, which may not be achievable for your workload configuration.
+  Selecting recovery objectives more stringent than actual business objectives. This forces DR implementations that are costlier and more complicated than what the workload needs.
+  Selecting recovery objectives incompatible with those of a dependent workload.
+  Your recovery objectives do not consider regulatory compliance requirements.
+  RTO and RPO defined for a workload, but never tested.

 **Benefits of establishing this best practice:** Your recovery objectives for time and data loss are necessary to guide your DR implementation.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 For the given workload, you must understand the impact of downtime and lost data on your business. The impact generally grows larger with greater downtime or data loss, but the shape of this growth can differ based on the workload type. For example, you may be able to tolerate downtime for up to an hour with little impact, but after that impact quickly rises. Impact to business manifests in many forms including monetary cost (such as lost revenue), customer trust (and impact to reputation), operational issues (such as missing payroll or decreased productivity), and regulatory risk. Use the following steps to understand these impacts, and set RTO and RPO for your workload.

 **Implementation Steps**

1.  Determine your business stakeholders for this workload, and engage with them to implement these steps. Recovery objectives for a workload are a business decision. Technical teams then work with business stakeholders to use these objectives to select a DR strategy.
**Note**
For steps 2 and 3, you can use the [Implementation worksheet](#implementation-worksheet).

1.  Gather the necessary information to make a decision by answering the questions below.

1.  Do you have categories or tiers of criticality for workload impact in your organization?

   1.  If yes, assign this workload to a category

   1.  If no, then establish these categories. Create five or fewer categories and refine the range of your recovery time objective for each one. Example categories include: critical, high, medium, low. To understand how workloads map to categories, consider whether the workload is mission critical, business important, or non-business driving.

   1.  Set workload RTO and RPO based on category. Always choose a category more strict (lower RTO and RPO) than the raw values calculated entering this step. If this results in an unsuitably large change in value, then consider creating a new category.

1.  Based on these answers, assign RTO and RPO values to the workload. This can be done directly, or by assigning the workload to a predefined tier of service.

1.  Document the disaster recovery plan (DRP) for this workload, which is a part of your organization’s [business continuity plan (BCP)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html), in a location accessible to the workload team and stakeholders

   1.  Record the RTO and RPO, and the information used to determine these values. Include the strategy used for evaluating workload impact to the business

   1.  Record other metrics besides RTO and RPO are you tracking or plan to track for disaster recovery objectives

   1.  You will add details of your DR strategy and runbook to this plan when you create these.

1.  By looking up the workload criticality in a matrix such as that in Figure 15, you can begin to establish predefined tiers of service defined for your organization.

1.  After you have implemented a DR strategy (or a proof of concept for a DR strategy) as per [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel_planning_for_recovery_disaster_recovery.md), test this strategy to determine workload actual RTC (Recovery Time Capability) and RPC (Recovery Point Capability). If these do not meet the target recovery objectives, then either work with your business stakeholders to adjust those objectives, or make changes to the DR strategy is possible to meet target objectives.

 **Primary questions**

1.  What is the maximum time the workload can be down before severe impact to the business is incurred

   1.  Determine the monetary cost (direct financial impact) to the business per minute if workload is disrupted.

   1.  Consider that impact is not always linear. Impact can be limited at first, and then increase rapidly past a critical point in time.

1.  What is the maximum amount of data that can be lost before severe impact to the business is incurred

   1.  Consider this value for your most critical data store. Identify the respective criticality for other data stores.

   1.  Can workload data be recreated if lost? If this is operationally easier than backup and restore, then choose RPO based on the criticality of the source data used to recreate the workload data.

1.  What are the recovery objectives and availability expectations of workloads that this one depends on (downstream), or workloads that depend on this one (upstream)?

   1.  Choose recovery objectives that allow this workload to meet the requirements of upstream dependencies

   1.  Choose recovery objectives that are achievable given the recovery capabilities of downstream dependencies. Non-critical downstream dependencies (ones you can “work around”) can be excluded. Or, work with critical downstream dependencies to improve their recovery capabilities where necessary.

 **Additional questions**

 Consider these questions, and how they may apply to this workload:

1.  Do you have different RTO and RPO depending on the type of outage (Region vs. AZ, etc.)?

1.  Is there a specific time (seasonality, sales events, product launches) when your RTO/RPO may change? If so, what is the different measurement and time boundary?

1.  How many customers will be impacted if workload is disrupted?

1.  What is the impact to reputation if workload is disrupted?

1.  What other operational impacts may occur if workload is disrupted? For example, impact to employee productivity if email systems are unavailable, or if Payroll systems are unable to submit transactions.

1.  How does workload RTO and RPO align with Line of Business and Organizational DR Strategy?

1.  Are there internal contractual obligations for providing a service? Are there penalties for not meeting them?

1.  What are the regulatory or compliance constraints with the data?

## Implementation worksheet
<a name="implementation-worksheet"></a>

 You can use this worksheet for implementation steps 2 and 3. You may adjust this worksheet to suit your specific needs, such as adding additional questions.

<a name="worksheet"></a>![Worksheet](http://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/images/worksheet.png)

 **Level of effort for the Implementation Plan: **Low

## Resources
<a name="resources"></a>

 **Related Best Practices:**
+  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel_backing_up_data_periodic_recovery_testing_data.md)
+ [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel_planning_for_recovery_disaster_recovery.md)
+ [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel_planning_for_recovery_dr_tested.md)

 **Related documents:**
+  [AWS Architecture Blog: Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/)
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud (AWS Whitepaper)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
+  [Managing resiliency policies with AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resiliency-policies.html)
+  [APN Partner: partners that can help with disaster recovery](https://aws.amazon.com/partners/find/results/?keyword=Disaster+Recovery)
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery)

 **Related videos:**
+  [AWS re:Invent 2018: Architecture Patterns for Multi-Region Active-Active Applications (ARC209-R2)](https://youtu.be/2e29I3dA8o4)
+  [Disaster Recovery of Workloads on AWS](https://www.youtube.com/watch?v=cJZw5mrxryA)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
