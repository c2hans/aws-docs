---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/faq.html
---

# FAQ about certificate-based access controls on AWS
<a name="faq"></a>

## What are certificate attributes, and why are they important for IAM Roles Anywhere?
<a name="faq-1"></a>

*Certificate attributes* are fields within digital certificates (X.509 or ML-DSA) that contain information about the certificate holder, such as common name, organization, or custom extensions. In AWS Identity and Access Management Roles Anywhere, these attributes can be used in role trust policies to implement fine-grained access control. This helps you make access decisions based on the certificate's characteristics rather than its validity.

## How do temporary credentials work with IAM Roles Anywhere?
<a name="faq-2"></a>

When a workload authenticates by using a certificate, IAM Roles Anywhere provides temporary security credentials that typically last between 15 minutes to 12 hours. When these credentials expire, they must be refreshed. This reduces the risk of credential compromise. The temporary nature of these credentials is a key security feature that helps maintain the principle of least privilege.

## What are the advantages of using IAM Roles Anywhere?
<a name="faq-3"></a>

Compared to using long-term access keys, IAM Roles Anywhere offers several advantages:
+ No need to manage or rotate access keys
+ Certificate-based authentication with built-in validation
+ Automatic credential expiration and renewal
+ Fine-grained access control through certificate attributes
+ Improved audit capabilities through certificate tracking
+ Reduced risk of credential exposure

## How does IAM Roles Anywhere integrate with existing certificate infrastructure?
<a name="faq-4"></a>

IAM Roles Anywhere can integrate with your existing public key infrastructure (PKI) by registering your certificate authority (CA) as a trust anchor. You can use either your existing CA or AWS Private Certificate Authority. When registered as a trust anchor, the CA issues certificates that can be used to authenticate workloads and obtain temporary AWS credentials.

## What are the best practices for implementing least privilege with IAM Roles Anywhere?
<a name="faq-5"></a>

Key best practices include:
+ Use certificate attributes to restrict role assumption to specific workloads
+ Implement specific trust relationships based on certificate characteristics
+ Monitor and log AWS Identity and Access Management (IAM) role assumptions
+ Implement strict role permissions based on workload requirements
+ Regularly audit trust policies for roles, [identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_id-based) for roles, and profile policies

## What is the difference between X.509 and ML-DSA certificates?
<a name="faq-6"></a>

Consider ML-DSA certificates in the following circumstances:
+ If your organization has long-term data protection requirements, such as over 10 years.
+ If you operate in an industry with stringent compliance requirements and anticipate post-quantum standards.
+ If certificate compromise by quantum computers poses significant risk to your operations.
+ If you're proactively preparing for post-quantum cryptography migration.

X.509 certificates remain appropriate for standard enterprise workloads with typical security requirements and short-to-medium term credential lifecycles.

## Are ML-DSA certificates available in all AWS Regions?
<a name="faq-7"></a>

Yes, ML-DSA certificate support is available in all AWS Regions where IAM Roles Anywhere is available, including AWS GovCloud (US) Regions, AWS European Sovereign Cloud (Germany) Region, and China Regions.

## Can I use both X.509 and ML-DSA certificates in the same environment?
<a name="faq-8"></a>

Yes, both certificate types can coexist in the same IAM Roles Anywhere environment. You can register trust anchors for both X.509 and ML-DSA certificate authorities. This can help you adopt ML-DSA gradually, based on your specific risk profile and compliance requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
