---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-standalone-acc.html
---

# Configuring EKS Runtime Monitoring for a standalone account (API)
<a name="eks-runtime-monitoring-configuration-standalone-acc"></a>

A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of invitation, this section doesn't apply to your account. For more information, see [Configuring EKS Runtime Monitoring for multiple-account environments (API)](eks-runtime-monitoring-configuration-multiple-accounts.md).

After you enable Runtime Monitoring, ensure to install GuardDuty security agent through automated configuration or manual deployment. As a part of completing all the steps listed in the following procedure, make sure to install the security agent.

Based on the [Approaches to manage GuardDuty security agent in Amazon EKS clusters](how-runtime-monitoring-works-eks.md#eksrunmon-approach-to-monitor-eks-clusters), you can choose a preferred approach and follow the steps as mentioned in the following table.

|  **Preferred approach to manage GuardDuty security agent**  | **Steps** |
| --- | --- |
| Manage security agent through GuardDuty (Monitor all EKS clusters) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-standalone-acc.html)  |
| Monitor all EKS clusters but exclude some of them (using exclusion tag) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-standalone-acc.html)  |
| Monitor selective EKS clusters (using inclusion tag) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-standalone-acc.html)  |
| Manage the security agent manually |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-configuration-standalone-acc.html)  |
