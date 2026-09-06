---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/security-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security considerations
<a name="security-considerations"></a>

 Data security must be a top priority for SaaS providers. When adopting a multitenant strategy, your organization needs a robust security strategy to ensure that tenant data is effectively protected from unauthorized access. Protecting this data and conveying that your system has employed the appropriate security measures is essential to gaining the trust of your SaaS customers.

 The storage strategies you choose are likely to use common security patterns supported on AWS. Encrypting data at rest, for example is a horizontal strategy that can be applied universally across any of the models. This provides a foundational level of security which ensures that—even if there is unauthorized access to data—it would be useless without the keys needed to decrypt the information.

 Now, as you look at the security profiles of the silo, bridge, and pool models, you will notice additional variations in how security is realized with each one. You’ll discover that AWS Identity and Access Management (Amazon IAM), for example, has nuances in how it can scope and control access to tenant data. In general, the silo and bridge models have a more natural fit with IAM policies because they can be applied to limit access to entire databases or tables. Once you cross over to a pool model, you may not be in a position to leverage IAM to scope access to the data. Instead, more responsibility shifts to the authorization models of your application’s services. These services must use a user’s identity to resolve the scope and control they have over data in a shared representation.

## Isolation and security
<a name="isolation-and-security"></a>

 Supporting tenant isolation is fundamental for some organizations and domains. The notion that data is separated—even in a virtualized environment—can be seen as essential to SaaS providers that have specific regulatory or security requirements.

 As you consider each AWS storage solution, think about how isolation is achieved on each of the AWS storage services. As you will see, achieving isolation on RDS looks very different from how it does on DynamoDB. Consider these differences as you select your storage strategy and assess the security considerations of your customers.
