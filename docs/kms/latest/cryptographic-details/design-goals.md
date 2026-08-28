---
source_url: https://docs.aws.amazon.com/kms/latest/cryptographic-details/design-goals.html
---

# AWS KMS design goals
<a name="design-goals"></a>

AWS KMS is designed to meet the following requirements.

**Durability**
The durability of cryptographic keys is designed to equal that of the highest durability services in AWS. A single cryptographic key can encrypt large volumes of your data that has accumulated over a long time.

**Trustworthy**
Use of keys is protected by access control policies that you define and manage. There is no mechanism to export plaintext KMS keys. The confidentiality of your cryptographic keys is crucial. Multiple Amazon employees with role-specific access to quorum-based access controls are required to perform administrative actions on the HSMs.

**Low-latency and high throughput**
AWS KMS provides cryptographic operations at latency and throughput levels suitable for use by other services in AWS.

**Independent Regions**
AWS provides independent Regions for customers who need to restrict data access in different Regions. Key usage can be isolated within an AWS Region.

**Secure source of random numbers**
Because strong cryptography depends on truly unpredictable random number generation, AWS KMS provides a high-quality and validated source of random numbers.

**Audit**
AWS KMS records the use and management of cryptographic keys in AWS CloudTrail logs. You can use AWS CloudTrail logs to inspect use of your cryptographic keys, including the use of keys by AWS services on your behalf.

To achieve these goals, the AWS KMS system includes a set of AWS KMS operators and service host operators (collectively, “operators”) that administer “domains.” A domain is a Regionally defined set of AWS KMS servers, HSMs, and operators. Each AWS KMS operator has a hardware token that contains a private and public key pair that is used to authenticate its actions. The HSMs have an additional private and public key pair to establish encryption keys that protect HSM state synchronization.

This paper illustrates how AWS KMS protects your keys and other data that you want to encrypt. Throughout this document, encryption keys or data that you want to encrypt are referred to as “secrets” or “secret material.”

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
