---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions when defining your encryption standards or when creating your encryption infrastructure in the implementation phase.

## When do I need symmetric encryption?
<a name="faq-symmetric-encryption"></a>

You might use symmetric encryption when:
+ Speed, cost, and lower computational overhead are a priority.
+ You need to encrypt a large amount of data.
+ The encrypted data isn't leaving the boundaries of the organization's network.

## When do I need asymmetric encryption?
<a name="faq-asymmetric-encryption"></a>

You might use asymmetric encryption when:
+ You need to share the data outside of the organization.
+ Regulations or governance prohibit sharing the key.
+ Nonrepudiation is required. (*Nonrepudiation* prevents a user from denying prior commitments or actions.)
+ You need to strictly segregate access to encryption keys based on organization roles.

## When do I need envelope encryption?
<a name="faq-envelope-encryption"></a>

You need to support and implement envelope encryption if your encryption policy requires key rotation. Some governance and compliance regimes require key rotation, or your policy might mandate it to meet a business need.

## When do I need to use a hardware security module (HSM)?
<a name="faq-hsm"></a>

You might need an HSM if your policy specifies compliance with:
+ The Federal Information Processing Standards (FIPS) 140-2 level 3 encryption standard. For more information, see [FIPS validation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/fips-validation.html) (AWS CloudHSM documentation).
+ Industry-standard APIs, such as PKCS\#11, Java Cryptography Extension (JCE), or Microsoft Cryptography API: Next Generation (CNG)

## Why should I centrally manage encryption keys?
<a name="faq-central-management"></a>

The following are common benefits of centralized key management:
+ Because keys are used and administered in different locations, you can reuse keys, which can reduce costs.
+ You have more control over access to the encryption keys.
+ Storing keys in a single location makes it easier to view, audit, and update keys in the event of a standards change.

## Do I need to use a purpose-built encryption infrastructure for data at rest?
<a name="faq-infrastructure"></a>

Your enterprise needs an encryption infrastructure if any one of the following is true:
+ Your enterprise handles and stores data of any classification other than public.
+ Your enterprise captures and stores data about employees or customers.
+ Your enterprise handles PII data.
+ Your enterprise must be compliant with regulatory or governance regimes that require data to be encrypted.
+ Your enterprise executive leadership has mandated encryption of all data at rest.

## How can AWS KMS help my organization meet its encryption objectives for data at rest?
<a name="faq-aws-kms"></a>

In addition to many other features, AWS Key Management Service can help you:
+ Use envelope encryption.
+ Control encryption key access, such as separating key administration from key usage.
+ Share keys across multiple AWS Regions and AWS accounts.
+ Centralize key administration.
+ Automate and mandate key rotation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
