---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/continuous-monitoring-and-validation.html
---

# Continuous monitoring and validation
<a name="continuous-monitoring-and-validation"></a>

Achieving CMMC Level 2 certification is not the finish line. Certification is valid for three years, but the DoD expects you to maintain your security posture continuously. You must submit an annual affirmation of continued conformance to SPRS. Compliance drift between assessments can result in findings during spot checks or contract performance reviews.

## Monitoring framework
<a name="monitoring-framework"></a>

|
|
| Monitoring activity | Frequency | AWS service | Action on finding |
| --- |--- |--- |--- |
| Compliance posture | Continuous | Security Hub \+ AWS Config conformance pack | Automated alerts via Amazon SNS for score drops. Weekly summary to CISO. |
| Vulnerability scanning | Continuous | Amazon Inspector | Critical findings trigger Amazon SNS notification. SLA: Critical 48hrs, High 7 days. |
| Threat detection | Continuous | GuardDuty | High-severity findings trigger EventBridge and Lambda automated response. |
| Configuration drift | On change | AWS Config | Non-compliant changes trigger remediation or Amazon SNS alert. |
| Access review | Monthly | IAM Access Analyzer \+ credential reports | Unused credentials disabled. Over-permissive policies remediated. |
| Patch compliance | Weekly | Systems Manager Patch Manager | Non-compliant instances flagged. Patching windows enforced. |
| SPRS score | Weekly | Athena \+ Security Hub | Score drops below threshold trigger immediate investigation. |

## Proactive security controls
<a name="proactive-security-controls"></a>

In addition to continuous monitoring, you should have proactive security controls in place to help prevent unauthorized modification of segmentation and security controls. Design the preventive and detective controls so that in case of a deviation, respective stakeholders are notified immediately, and remediation steps can be taken. As your security posture matures, you should automate most responses so that deviations can be remediated without human intervention on a near real-time basis.

These are ways you can monitor your CUI boundary:
+ Periodically validate security group rules against the planned CUI scope
+ Manage security group and network configurations with a change control process
+ Manage security groups centrally from Firewall Manager
+ Monitor and alert on security group rule changes in the CUI Workload accounts
+ Monitor Amazon VPC peering connections to the CUI Workload accounts
+ Monitor configuration changes to in-scope APIs or AWS services that allow data in or out of the CUI boundary
+ Implement data loss prevention controls on connected systems to help prevent CUI leakage and validate scope boundary

You can automate responses by using AWS Config custom rules to monitor changes to security groups, Amazon VPC peering connections, and other resources that enforce segmentation boundaries. Attach AWS Config rules to Lambda responders to evaluate deviations and initiate automatic remediation when a change deviates from the defined CMMC segmentation boundaries.
