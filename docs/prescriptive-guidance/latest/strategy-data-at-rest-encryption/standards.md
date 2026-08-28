---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/standards.html
---

# Standards
<a name="standards"></a>

Standards are derived from your policy. These are narrower in scope and help define the framework and architecture for implementation. For example, if your organization's policy is to encrypt your data at rest, then a standard would define what type of encryption is required and provide general direction about how to adhere to the policy.

Encryption standards commonly specify the following:
+ The types of encryption that should be used
+ Minimum specifications for encryption keys
+ Who has access to encryption keys
+ Where encryption keys should be stored
+ Criteria for picking an appropriate key strength when choosing encryption or hashing techniques
+ Key rotation frequency

Whereas you rarely need to update an encryption policy, encryption standards are subject to change. The cybersecurity industry constantly evolves to meet the ever-changing threat landscape. As such, your standards should change to adopt the latest technologies and best practices in order to provide the best possible protection for your enterprise data.

In an enterprise organization, vice presidents, directors, or data stewards typically define encryption standards, and a compliance officer typically reviews and approves them.

Consider the following categories of factors when defining and maintaining encryption standards in your organization:
+ [Cost and performance considerations](#cost-performance)
+ [Key access control](#access-control)
+ [Encryption types](#encryption-types)
+ [Encryption key specifications](#encryption-key-specifications)
+ [Key storage location](#key-storage-location)

## Cost and performance considerations
<a name="cost-performance"></a>

Consider the following operational factors when determining encryption standards for data at rest:
+ The available hardware resources must be able to support your standards at scale.
+ The cost of encryption varies based on the length of the key, the amount of data, and the time required to perform the encryption. For example, when compared to symmetric encryption, asymmetric encryption uses longer keys and takes more time.
+ Consider the performance requirements of your enterprise applications. If your application requires low latency and high throughput, then you might want to use symmetric encryption.

## Key access control
<a name="access-control"></a>

Identify access control policies for your encryption keys based on the principle of least privilege. *Least privilege* is the security best practice of granting users the minimum access they need to perform their job functions. In your standards, define an access control policy that:
+ Identifies the roles that manage the key-encryption keys and data keys.
+ Defines and maps key permissions to roles. For example, it defines who has key admin privileges and who has and key user privileges. Key admins can create or modify key-encryption keys, and key users can encrypt and decrypt data and generate data keys.

## Encryption types
<a name="encryption-types"></a>

In your standards, define which encryption types and features are suitable for your organization:
+ Document when to use symmetric and asymmetric encryption algorithms. For more information, see *When do I need symmetric encryption?* and *When do I need asymmetric encryption?* in the [FAQ](faq.md) section.
+ Decide whether you should use envelope encryption, and define the circumstances. For more information, see *When do I need envelope encryption?* in the [FAQ](faq.md) section.
+ Define criteria for when to use encryption alternatives, such as tokenization and hashing.

## Encryption key specifications
<a name="encryption-key-specifications"></a>

Define required specifications for your encryption keys, such as key strength and algorithms. These specifications must comply with the regulatory and compliance regimes defined in the policy. Consider defining the following specifications:
+ Define the minimum key strength and algorithms for both symmetric and asymmetric encryption types. The factors of key strength include the length, randomness, and uniqueness.
+ Define when you want to implement new versions of encryption algorithms. For example, your standards might state *Implement the latest version of the algorithm within 30 days of release* or *Always use one version older than the latest release*.
+ Define the interval for rotating your encryption keys.

## Key storage location
<a name="key-storage-location"></a>

In your standards, consider the following when deciding where to store your encryption keys:
+ Compliance and regulatory requirements might dictate where your encryption keys can be stored.
+ Decide whether you want to store keys in a centralized location or with their corresponding data. For more information, see *Why should I centrally manage encryption keys?* in the [FAQ](faq.md) section.
+ If you choose centralized storage, decide whether to store keys in an enterprise-managed infrastructure, such as a hardware security module (HSM), or a managed service provider, such as AWS KMS. For more information, see *When do I need to use a hardware security module (HSM)?* in the [FAQ](faq.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
