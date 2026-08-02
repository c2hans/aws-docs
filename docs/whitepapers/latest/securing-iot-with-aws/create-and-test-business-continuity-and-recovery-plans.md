---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/create-and-test-business-continuity-and-recovery-plans.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 10. Create and test business continuity and recovery plans
<a name="create-and-test-business-continuity-and-recovery-plans"></a>

During an event, different IoT systems could behave in different ways. Before those events occur, you must define parameters relevant to your use case (should a system fail open or fail shut, does the system attempt recovery automatically or require human intervention, do you need to enable or disable manual controls) and then test those rigorously. Again, use the risk assessment and criticality assignments performed early in this process to ensure you apply the right amount of scrutiny and resources to this phase. Don’t forget about defining when to return to the baseline state in your recovery plans.
+  Define important parameters (such as overall availability) for your stakeholders.
+  Define the resilience requirements for the system and analyze failure modes to ensure adherence.
+  Test recovery plans periodically and adapt them according to lessons learned from tests and actual security incidents.
+  Perform threat and risk assessment of supporting IT systems and develop written procedures on how to return to the normal, well-defined, state of operation tailored to the assessment’s results.
+  Include third-party aspects (such as network communications, software, and support).
+  Use resiliency features at the edge to support data resiliency and backup needs.
+  Use cloud services for backup and business continuity.

## Supporting AWS resources
<a name="resources-10"></a>

 AWS provides the following assets and services to help you create and test business continuity and recovery plans:
+  [AWS IoT Lens for AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html) – A document that covers commonly encountered IoT use cases and identified key solution elements to ensure that your workload architecture uses established best practices.
+  [Resilience in AWS IoT Greengrass](https://docs.amazonaws.cn/en_us/greengrass/v1/developerguide/disaster-recovery-resiliency.html)
+  [Backup and Restore Use Cases with AWS](https://aws.amazon.com/backup-restore/use-cases/)
+  [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/)
+  [AWS Backup](https://aws.amazon.com/backup/)

 These general best practices apply across all IoT deployments, but as mentioned previously, different industries will have different threat and risk models. In the next section we will dive into examples across these industries and demonstrate prescriptive approaches that are more targeted.
