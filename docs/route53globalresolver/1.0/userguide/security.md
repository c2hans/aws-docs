---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/security.html
---

# Security in Amazon Route 53 Global Resolver

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Route 53 Global Resolver, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

**Topics**
+ [Amazon Route 53 Global Resolver security features](#security-features)
+ [Data protection](data-protection.md)
+ [Identity and access management](security-iam.md)
+ [Compliance validation](compliance-validation.md)
+ [Resilience](disaster-recovery-resiliency.md)
+ [Infrastructure Security](infrastructure-security.md)

## Amazon Route 53 Global Resolver security features
<a name="security-features"></a>

Amazon Route 53 Global Resolver includes several built-in security features to protect your DNS infrastructure:

Encrypted DNS protocols
Amazon Route 53 Global Resolver supports DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) to encrypt DNS queries in transit, protecting against eavesdropping and tampering.

DNS filtering and threat protection
Comprehensive DNS filtering capabilities allow you to block access to malicious domains, leverage AWS managed threat intelligence, and create custom security policies. Advanced threat protection detects DNS tunneling and Domain Generation Algorithms (DGAs).

DNSSEC validation
When enabled, Amazon Route 53 Global Resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains, providing protection against DNS spoofing and cache poisoning attacks.

DDoS protection
Amazon Route 53 Global Resolver includes built-in DDoS protection using AWS Shield, along with custom dynamic protection using top talker metrics and rate limiting to quickly respond to high-volume attacks.

Access control
Multiple authentication mechanisms including IP ACLsAccess Sources and token-based authentication (JWT) provide flexible access control for different client types and protocols.

Comprehensive logging
Continuous query logging provides visibility into DNS activity for security monitoring, compliance auditing, and threat detection.
