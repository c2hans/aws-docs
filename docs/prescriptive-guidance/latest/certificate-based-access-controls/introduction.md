---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/introduction.html
---

# Strengthening security in IAM Roles Anywhere by using certificate-based access controls
<a name="introduction"></a>

*Alberto Sagrado Amador, Amazon Web Services*

As organizations expand their cloud footprints and embrace automation, it's increasingly critical to manage secure access for non-human identities, such as applications, servers, and containers. Traditional approaches use long-term credentials or hard-coded secrets, but these approaches can create security risks and operational overhead. [AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) addresses these challenges by allowing workloads outside of the AWS Cloud to access AWS resources securely through digital certificates, including traditional [X.509 certificates](https://en.wikipedia.org/wiki/X.509) (Wikipedia) and [quantum-resistant ML-DSA (FIPS 204) certificates](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.204.pdf) (NIST), instead of long-term credentials.

Organizations commonly struggle with the proliferation of access keys, complex credential rotation, and limited ability to enforce fine-grained access controls. Modern security frameworks emphasize [Zero Trust principles](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/zero-trust-principles.html), just-in-time access, and the principle of least privilege—all of which can be achieved through proper implementation of certificate-based authentication.

This guide demonstrates how to enhance security in IAM Roles Anywhere by effectively managing certificate attributes and [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) role trust relationships. It uses a practical architectural example to demonstrate how to implement fine-grained access controls and enforce the principle of least privilege in IAM Roles Anywhere sessions.

The architecture uses IAM Roles Anywhere and [AWS Private Certificate Authority (AWS Private CA)](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html). AWS Private CA acts as a trust anchor, and [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) manages the certificates. This foundation reflects real-world security configurations and their implications.

Without proper policy configurations for IAM roles, any certificate issued by AWS Private CA could potentially be used to assume roles. This can create significant security vulnerabilities, including unauthorized role assumption, data breaches, and credential compromise. This guide shows how to help mitigate these risks through proper configuration of policies and management of certificate attributes.

The following diagram shows the workflow of how an application can request access through IAM Roles Anywhere and then perform the permitted actions in the target AWS account.

![Using certificate-based authentication to gain temporary access credentials for AWS resources.](https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/images/guide-img/e306828d-cb6f-41be-b1da-12c08a777c76/images/fa80f90e-e9b5-493a-a98c-397bfa12de0b.png)

The diagram shows the following workflow:

1. The application requests temporary security credentials from IAM Roles Anywhere and provides its certificate for authentication.

1. IAM Roles Anywhere uses a trust relationship to authenticate the application with AWS Private CA.

1. IAM Roles Anywhere generates a JSON file that contains the temporary security credentials and returns it to the application.

1. Using the temporary security credentials, the application assumes an IAM role in the AWS account.

The application performs the actions allowed by the policies attached to the IAM role and in the account. For example, it might access an Amazon Simple Storage Service (Amazon S3) bucket.

## Intended audience
<a name="introduction-audience"></a>

This guide is intended for cloud architects, security engineers, and DevOps engineers who are implementing access controls for hybrid cloud environments or automating permissions management for non-human identities. This guide can also help you comply with regulations or meet security best practices. To understand the concepts and recommendations in this guide, you should be familiar with the following:
+ IAM fundamentals
+ Public key infrastructure (PKI) and digital certificate management (X.509 and ML-DSA post-quantum certificates)
+ Principles of Zero Trust security and least-privilege access
+ AWS services for certificate-based authentication, such as IAM Roles Anywhere and AWS Private CA

## Objectives
<a name="introduction-objectives"></a>

Using IAM Roles Anywhere and digital certificates (X.509 or ML-DSA) for authentication can deliver the following key business outcomes:
+ **Enhanced security** – Eliminates risks associated with use of long-term credentials and provides quantum-resistant authentication options
+ **Reduced operational overhead** – Automates credential management and rotation
+ **Improved compliance **– Provides detailed audit trails and enforces least-privilege access
+ **Scalable management** – Centralizes access control across hybrid environments
+ **Future-proof cryptography** – Helps protect against emerging quantum computing threats through ML-DSA support
+ **Cost efficiency** – Reduces costs associated with security incident response efforts and management complexity

## Choosing between X.509 and ML-DSA certificates
<a name="choosing-between-x-509-and-ml-dsa-certificates"></a>

IAM Roles Anywhere supports two types of digital certificates:
+ *X.509 certificates* are traditional PKI certificates that are suitable for most current use cases and are widely supported across systems and tools.
+ *ML-DSA certificates (FIPS 204)* are post-quantum cryptographic certificates that help protect against potential future quantum computing threats

Consider using ML-DSA in the following situations:
+ If your organization has long-term data protection requirements, such as over 10 years
+ If your industry has stringent compliance requirements and you anticipate post-quantum standards
+ If certificate compromise by quantum computers poses significant risk to your environment
+ If your organization is proactively preparing for a post-quantum cryptography migration

X.509 remains appropriate in the following circumstances:
+ For standard enterprise workloads with typical security requirements
+ For environments that require broad compatibility with existing tools
+ For short-to-medium term credential lifecycles

Both certificate types work identically within IAM Roles Anywhere and can coexist in the same environment. This helps organizations to adopt ML-DSA gradually, based on their specific risk profile and compliance requirements.
