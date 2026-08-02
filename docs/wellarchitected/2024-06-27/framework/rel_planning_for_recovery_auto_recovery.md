---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_planning_for_recovery_auto_recovery.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL13-BP05 Automate recovery
<a name="rel_planning_for_recovery_auto_recovery"></a>

 Use AWS or third-party tools to automate system recovery and route traffic to the DR site or Region.

 Based on configured health checks, AWS services, such as Elastic Load Balancing and AWS Auto Scaling, can distribute load to healthy Availability Zones while services, such as Amazon Route 53 and AWS Global Accelerator, can route load to healthy AWS Regions. Amazon Application Recovery Controller helps you manage and coordinate failover using readiness check and routing control features. These features continually monitor your application’s ability to recover from failures, so you can control application recovery across multiple AWS Regions, Availability Zones, and on premises.

 For workloads on existing physical or virtual data centers or private clouds, [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) allows organizations to set up an automated disaster recovery strategy in AWS. Elastic Disaster Recovery also supports cross-Region and cross-Availability Zone disaster recovery in AWS.

 **Common anti-patterns:**
+  Implementing identical automated failover and failback can cause flapping when a failure occurs.

 **Benefits of establishing this best practice:** Automated recovery reduces your recovery time by eliminating the opportunity for manual errors.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate recovery paths. For short recovery times, follow your [disaster recovery plan](https://aws.amazon.com/disaster-recovery/faqs/#Core_concepts) to get your IT systems back online quickly in the case of a disruption.
  +  Use Elastic Disaster Recovery for automated Failover and Failback. Elastic Disaster Recovery continuously replicates your machines (including operating system, system state configuration, databases, applications, and files) into a low-cost staging area in your target AWS account and preferred Region. In the case of a disaster, after choosing to recover using Elastic Disaster Recovery, Elastic Disaster Recovery automates the conversion of your replicated servers into fully provisioned workloads in your recovery Region on AWS.
    +  [Using Elastic Disaster Recovery for Failover and Failback](https://docs.aws.amazon.com/drs/latest/userguide/failback.html)
    +  [AWS Elastic Disaster Recovery resources](https://aws.amazon.com/disaster-recovery/resources/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help with disaster recovery](https://aws.amazon.com/partners/find/results/?keyword=Disaster+Recovery)
+  [AWS Architecture Blog: Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/)
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery)
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+  [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/)
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud (AWS Whitepaper)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)

 **Related videos:**
+  [AWS re:Invent 2018: Architecture Patterns for Multi-Region Active-Active Applications (ARC209-R2)](https://youtu.be/2e29I3dA8o4)
