---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/security.html
---

# Security and Compliance in AL2027
<a name="security"></a>

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Linux, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations.

AL2027 includes several security enhancements over AL2023, see: [Security updates and features](security-features.md)

**Topics**
+ [Amazon Linux Security advisories for AL2027](alas.md)
+ [Listing applicable advisories](security-dnf-updateinfo.md)
+ [Applying security updates in-place](security-update-advisory.md)
+ [Setting SELinux modes for AL2027](selinux-modes.md)
+ [Post-Quantum Cryptography (PQC) on AL2027](crypto-policies-pq.md)
+ [Enable FIPS Mode on AL2027](fips-mode.md)
+ [Enable FIPS Mode in an AL2027 Container](fips-mode-container.md)
+ [Swap OpenSSL FIPS providers on AL2027](fips-openssl-swap-provider.md)
+ [AL2027 kernel hardening](kernel-hardening.md)
+ [Repository metadata signing in AL2027](repo-metadata-signing.md)
+ [Security patching during preview](#security-patching-preview)
+ [UEFI Secure Boot on AL2027](uefi-secure-boot.md)

## Security patching during preview
<a name="security-patching-preview"></a>

During the preview period, there is no guarantee that open CVEs for AL2027 packages will be patched in preview artifacts. AL2027 preview artifacts may have unpatched CVEs.

All CVE patching mechanisms and fixes will be in place before any public release.
