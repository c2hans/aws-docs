---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/faq.html
---

# FAQ
<a name="faq"></a>

**Q. **Why focus on the AWS Provider?

**A. **The AWS Provider is one of the most widely used and complex providers for provisioning infrastructure in Terraform. Following these best practices help users optimize their usage of the provider for the AWS environment.

**Q. **I'm new to Terraform. Can I use this guide?

**A. **The guide is for people who are new to Terraform as well as more advanced practitioners who want  to level up their skills. The practices improve workflows for users at any stage of learning.

**Q.** What are some key best practices covered?

**A.** Key best practices include [using IAM roles over access keys](security.md#iam-roles), [pinning versions](version.md#version-check), [incorporating automated testing](security.md#iac-code), [remote state locking](backend.md#amazon-s3), [credential rotation](security.md#continuous-monitoring), [contributing back to providers](version.md#contribute-providers), and [logically organizing code bases](structure.md).

**Q.** Where can I learn more about Terraform?

**A.** The [Resources](resources.md) section includes links to the official HashiCorp Terraform documentation and community forums. Use the links to learn more about advanced Terraform workflows.
