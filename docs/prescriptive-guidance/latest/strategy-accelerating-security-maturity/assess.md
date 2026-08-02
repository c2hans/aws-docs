---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/assess.html
---

# Assess: Evaluating your current cloud security posture
<a name="assess"></a>

Before you deploy anything to the landing zone, assess your landing zone to make sure it meets your requirements and to establish a baseline. This practice is called a *cloud posture assessment*. It helps you identify and remediate risks across your cloud infrastructure. Assessing your cloud security posture provides visibility of the relevant security controls in the cloud environment.

The following are the benefits of a cloud posture assessment:
+ It helps you understand your current security posture and get recommendations to reduce your risk profile, remediate existing vulnerabilities, or correct misconfigurations.
+ It helps you identify security best practices so that you can avoid missteps and reduce business risks.
+ It provides metrics that help you track improvement and measure success.

This section reviews services and tools, AWS Security Hub CSPM and Prowler, that you can use to perform a cloud posture assessment in your environment.

## Prowler
<a name="prowler"></a>

[Prowler](https://github.com/prowler-cloud/prowler/#requirements-and-installation) is an open source command-line tool that helps you assess, audit, and monitor your accounts for adherence to AWS security best practices and other security frameworks and standards. It inspects your configuration and identifies security issues. You can use Prowler in multi-account environments, and third-party vendors can also use it to assess the security of your AWS environment.

The following are the benefits of** **Prowler:
+ It is free and open source.
+ It has flexible deployment options and is scalable.
+ It runs compliance checks, such as for [Center for Internet Security (CIS) Benchmark for AWS](https://www.cisecurity.org/benchmark/amazon_web_services), General Data Protection Regulation (GDPR), and HIPAA.
+ It helps you create snapshots and baselines.

## AWS Security Hub CSPM
<a name="as-hlong"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your environment against security industry standards and best practices. It is integrated with AWS Control Tower so that you can configure Security Hub CSPM detective controls through the AWS Control Tower service. The objective of accelerating security maturity is to mature the assessment process from a one-time snapshot to a continuous process for monitoring progress.

The following are the benefits of Security Hub CSPM:
+ It provides a unified dashboard that shows current status of the environment and helps you identify and remediate issues.
+ It performs continuous assessments with automated checks.
