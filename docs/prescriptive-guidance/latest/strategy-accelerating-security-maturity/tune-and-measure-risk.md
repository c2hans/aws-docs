---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/tune-and-measure-risk.html
---

# Risk
<a name="tune-and-measure-risk"></a>

During the mature phase of the walk stage, you can use AWS Security Hub CSPM to continually tune and measure security risk. Security Hub CSPM continually assesses an organization's security posture and takes actions to remediate identified issues. Security Hub CSPM centralizes and prioritizes security findings from across AWS accounts, services, and supported third-party partners. This helps you analyze security trends and identify the high priority security issues.

Security Hub CSPM performs hundreds of security checks and classifies them based on risk to your AWS environment. You can view your score against security controls in a unified dashboard in the Security Hub CSPM console. For more information, see [Determining security scores](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-security-score.html) in the Security Hub CSPM documentation. Through this dashboard, the DevSecOps function can quickly identify any checks that have failed, the severity of the security issue, and which AWS Region and resource is affected. Once identified, the DevSecOps team can prioritize and remediate the issue. As issues are remediated, Security Hub CSPM automatically updates the state.
