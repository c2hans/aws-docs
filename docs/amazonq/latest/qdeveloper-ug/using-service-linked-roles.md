---
source_url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/using-service-linked-roles.html
---

# Using service-linked roles for Amazon Q Developer and User Subscriptions
<a name="using-service-linked-roles"></a>

Amazon Q Developer uses AWS Identity and Access Management (IAM) [ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon Q Developer. Service-linked roles are predefined by Amazon Q Developer and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using service-linked roles for Amazon Q Developer](using-service-linked-roles-qdev.md)
+ [Using service-linked-roles for User Subscriptions](using-service-linked-roles-user-subs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
