---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/security.html
---

# Security and Compliance in Amazon Linux 2023
<a name="security"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AL2023, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations.

**Topics**
+ [Amazon Linux Security advisories for AL2023](alas.md)
+ [Listing applicable Advisories](listing-applicable-advisories.md)
+ [Applying security updates in-place](security-inplace-update.md)
+ [Setting SELinux modes for AL2023](selinux-modes.md)
+ [Enable Post-Quantum Cryptography (PQC) on AL2023](crypto-policies-pq.md)
+ [Enable FIPS Mode on AL2023](fips-mode.md)
+ [Enable FIPS Mode in an AL2023 Container](fips-mode-container.md)
+ [Swap OpenSSL FIPS providers on AL2023](fips-openssl-swap-provider.md)
+ [AL2023 Kernel Hardening](kernel-hardening.md)
+ [Repository metadata signing in AL2023](repo-metadata-signing.md)
+ [UEFI Secure Boot on AL2023](uefi-secure-boot.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
