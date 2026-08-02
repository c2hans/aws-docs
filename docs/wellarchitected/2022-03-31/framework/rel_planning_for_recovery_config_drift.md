---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_planning_for_recovery_config_drift.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL13-BP04 Manage configuration drift at the DR site or Region
<a name="rel_planning_for_recovery_config_drift"></a>

 Ensure that the infrastructure, data, and configuration are as needed at the DR site or Region. For example, check that AMIs and service quotas are up to date.

 AWS Config continuously monitors and records your AWS resource configurations. It can detect drift and trigger [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to fix it and raise alarms. AWS CloudFormation can additionally detect drift in stacks you have deployed.

 **Common anti-patterns:**
+  Failing to make updates in your recovery locations, when you make configuration or infrastructure changes in your primary locations.
+  Not considering potential limitations (like service differences) in your primary and recovery locations.

 **Benefits of establishing this best practice:** Ensuring that your DR environment is consistent with your existing environment guarantees complete recovery.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Ensure that your delivery pipelines deliver to both your primary and backup sites. Delivery pipelines for deploying applications into production must distribute to all the specified disaster recovery strategy locations, including dev and test environments.
+  Enable AWS Config to track potential drift locations. Use AWS Config rules to create systems that enforce your disaster recovery strategies and generate alerts when they detect drift.
  +  [Remediating Noncompliant AWS Resources by AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)
  +  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+  Use AWS CloudFormation to deploy your infrastructure. AWS CloudFormation can detect drift between what your CloudFormation templates specify and what is actually deployed.
  +  [AWS CloudFormation: Detect Drift on an Entire CloudFormation Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help with disaster recovery](https://aws.amazon.com/partners/find/results/?keyword=Disaster+Recovery)
+  [AWS Architecture Blog: Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/)
+  [AWS CloudFormation: Detect Drift on an Entire CloudFormation Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/detect-drift-stack.html)
+  [AWS Marketplace: products that can be used for disaster recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery)
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud (AWS Whitepaper)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
+  [How do I implement an Infrastructure Configuration Management solution on AWS?](https://aws.amazon.com/answers/configuration-management/aws-infrastructure-configuration-management/?ref=wellarchitected)
+  [Remediating Noncompliant AWS Resources by AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)

 **Related videos:**
+  [AWS re:Invent 2018: Architecture Patterns for Multi-Region Active-Active Applications (ARC209-R2)](https://youtu.be/2e29I3dA8o4)
