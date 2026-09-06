---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/select-and-prioritize-workloads-to-move-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Select and prioritize workloads to move to AWS
<a name="select-and-prioritize-workloads-to-move-to-aws"></a>

You will need to select and prioritize the workloads that you want to migrate to AWS. You may want to migrate a low-risk workflow first to use as a POC. After a successful POC, workloads that are time-sensitive or are constrained by the lack of adequate, on-premises compute resources are good candidates. Frequent data synchronization can be challenging and costly, so AWS suggests starting with workloads that have minimal runtime dependencies on on-premises data.

You may want to prioritize migrating workloads that use on-premises resources that are required for other purposes. AWS has customers that move both front-end and back-end workloads. Some customers run sign-off on AWS because it is critical to their schedule, and they lack the on-premises infrastructure needed to satisfy the resource requirements of these workloads. You might require only one workload to move to AWS, such as a bursty scale-out workload like IP characterization.

Another consideration is the data shared between workloads. You may benefit from keeping workloads that share data in the same location, either on-premises or in AWS.
