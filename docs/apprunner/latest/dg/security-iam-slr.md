---
source_url: https://docs.aws.amazon.com/apprunner/latest/dg/security-iam-slr.html
---

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Using service-linked roles for App Runner
<a name="security-iam-slr"></a>

AWS App Runner uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to App Runner. Service-linked roles are predefined by App Runner and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using roles for management](using-service-linked-roles-management.md)
+ [Using roles for networking](using-service-linked-roles-networking.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
