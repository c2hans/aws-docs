---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html
---

# Business Continuity Plan (BCP)
<a name="business-continuity-plan-bcp"></a>

 Your disaster recovery plan should be a subset of your organization’s *business continuity plan* (BCP), it should not be a standalone document. There is no point in maintaining aggressive disaster recovery targets for restoring a workload if that workload’s business objectives cannot be achieved because of the disaster’s impact on elements of your business *other* than your workload. For example an earthquake might prevent you from transporting products purchased on your eCommerce application – even if effective DR keeps your workload functioning, your BCP needs to accommodate transportation needs. Your DR strategy should be based on business requirements, priorities, and context.

## Business impact analysis and risk assessment
<a name="business-impact-analysis-and-risk-assessment"></a>

 A *business impact analysis* should quantify the business impact of a disruption to your workloads. It should identify the impact on internal and external customers of not being able to use your workloads and the effect that has on your business. The analysis should help to determine how quickly the workload needs to be made available and how much data loss can be tolerated. However, it is important to note that recovery objectives should not be made in isolation; the probability of disruption and cost of recovery are key factors that help to inform the business value of providing disaster recovery for a workload.

 Business impact may be time dependent. You may want to consider factoring this in to your disaster recovery planning. For example, disruption to your payroll system is likely to have a very high impact to the business just before everyone gets paid, but it may have a low impact just after everyone has already been paid.

 A *risk assessment* of the type of disaster and geographical impact along with an overview of the technical implementation of your workload will determine the probability of disruption occurring for each type of disaster.

 For highly critical workloads, you might consider deploying infrastructure across multiple Regions with data replication and continuous backups in place to minimize business impact. For less critical workloads, a valid strategy may be not to have any disaster recovery in place at all. And for some disaster scenarios, it is also valid not to have any disaster recovery strategy in place as an informed decision based on a low probability of the disaster occurring. Remember that Availability Zones within an AWS Region are already designed with meaningful distance between them, and careful planning of location, such that most common disasters should only impact one zone and not the others. Therefore, a multi-AZ architecture within an AWS Region may already meet much of your risk mitigation needs.

 The cost of the disaster recovery options should be evaluated to ensure that the disaster recovery strategy provides the correct level of business value considering the business impact and risk.

 With all of this information, you can document the threat, risk, impact and cost of different disaster scenarios and the associated recovery options. This information should be used to determine your recovery objectives for each of your workloads.

## Recovery objectives (RTO and RPO)
<a name="recovery-objectives-rto-and-rpo"></a>

 When creating a Disaster Recovery (DR) strategy, organizations most commonly plan for the Recovery Time Objective (RTO) and Recovery Point Objective (RPO).

![Image showing relationship of recovery objectives.](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/recovery-objectives.png)

*Figure 3 - Recovery objectives*

 **Recovery Time Objective (RTO)** is the maximum acceptable delay between the interruption of service and restoration of service. This objective determines what is considered an acceptable time window when service is unavailable and is defined by the organization.

 There are broadly four DR strategies discussed in this paper: backup and restore, pilot light, warm standby, and multi-site active/active (see [Disaster Recovery Options in the Cloud](disaster-recovery-options-in-the-cloud.md)). In the following diagram, the business has determined their maximum permissible RTO as well as the limit of what they can spend on their service restoration strategy. Given the business’ objectives, the DR strategies Pilot Light or Warm Standby will satisfy both the RTO and the cost criteria.

![Graph showing recovery time objective as a relationship of costs and complexity versus length of service interruption.](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/recovery-time-objective.png)

*Figure 4 - Recovery time objective*

 **Recovery Point Objective (RPO)** is the maximum acceptable amount of time since the last data recovery point. This objective determines what is considered an acceptable loss of data between the last recovery point and the interruption of service and is defined by the organization.

 In the following diagram, the business has determined their maximum permissible RPO as well as the limit of what they can spend on their data recovery strategy. Of the four DR strategies, either Pilot Light or Warm Standby DR strategy meet both criteria for RPO and cost.

![Graph showing recovery point objective as a relationship of costs and complexity versus data loss before service interruption.](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/recovery-point-objective.png)

*Figure 5 - Recovery point objective*

**Note**
If the cost of the recovery strategy is higher than the cost of the failure or loss, the recovery option should not be put in place unless there is a secondary driver such as regulatory requirements. Consider recovery strategies of varying cost when making this assessment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
