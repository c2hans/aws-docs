---
source_url: https://docs.aws.amazon.com/kms/latest/developerguide/kms-internals.html
---

# AWS KMS internal operations
<a name="kms-internals"></a>

AWS Key Management Service (AWS KMS) provides cryptographic keys and operations secured by [FIPS 140-3 Security Level 3 validated hardware security modules (HSM)](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884) scaled for the cloud. AWS KMS keys and functionality are used by multiple AWS cloud services, and you can use them to protect data in your applications. This technical guide provides details on the cryptographic operations that are run within AWS when you use AWS KMS.

AWS KMS internals are required to scale and secure HSMs for a globally distributed key management service.

**Topics**
+ [Domains and domain state](domains-and-domain-state.md)
+ [Internal communication security](internal-communication-security.md)
+ [Replication process for multi-Region keys](replicate-key-details.md)
+ [Durability protection](durability-protection.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
