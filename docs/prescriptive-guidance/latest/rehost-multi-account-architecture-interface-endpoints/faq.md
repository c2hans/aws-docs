---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/faq.html
---

# FAQ
<a name="faq"></a>

**Q: Who can I share resources with?**

A: You can share resources with any AWS account. If you are part of an organization in AWS Organizations and sharing within your organization is enabled, you can also share resources with organizational units (OUs) or with your entire organization. For supported resource types, you can also share resources with AWS Identity and Access Management (IAM) roles and IAM users. If you share resources with accounts that are outside your organization, those accounts receive an invitation to join the resource share. After they accept the invitation, they can start using the shared resources.

**Q: Will I incur any charges for sharing my resources with other AWS accounts?**

A: No. You can share resources at no additional cost.

**Q: Can I stop sharing a resource?**

A: Yes. To stop sharing a resource, remove it from the resource share or delete the resource share.

**Q: How can I ensure security in AWS RAM?**

A: Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud. For more information, see [Security in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security.html) in the AWS RAM documentation.
