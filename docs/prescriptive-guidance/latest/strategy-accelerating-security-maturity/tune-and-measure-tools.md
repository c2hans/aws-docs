---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/tune-and-measure-tools.html
---

# Tools
<a name="tune-and-measure-tools"></a>

After you establish specialized teams for different security domains, align the teams with each other. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) can help you achieve this. Security Hub CSPM provides a centralized, unified dashboard to monitor progress against frameworks. It also integrates with AWS security services any many third-party tools.

The National Institute of Standards and Technology (NIST) [Cybersecurity Framework](https://www.nist.gov/cyberframework) on the NIST website is comprised of five functions: identify, protect, detect, respond, and recover. The following image shows how you can use different AWS services during each function and then configure those services to send their findings to Security Hub CSPM for consolidated reporting. If you choose to use other tools, you can use the Security Hub CSPM API, AWS Command Line Interface (AWS CLI), and AWS Security Finding Format (ASFF) to create custom integrations. For more information about Security Hub CSPM integrations with other services, see [Product integrations in AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-providers.html) in the Security Hub CSPM documentation.

![Security tools that integrate with AWS Security Hub](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/f7dfc681-575f-40c3-a007-4ba8e9dcf23b.png)

Security Hub CSPM integrates with all of these services and tools and provides the following:
+ Provides a unified dashboard that shows updates and helps teams to iterate in place
+ Automatically integrates with AWS security services, such as [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html), [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) , and [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html)
+ Supports integration with third-party tools, such as [Prowler](https://github.com/prowler-cloud/prowler) and [cfn\_nag](https://github.com/stelligent/cfn_nag)
+ Supports custom integrations with tools, such as Security Hub CSPM API, AWS CLI, and the AWS Security Finding Format (ASFF)
