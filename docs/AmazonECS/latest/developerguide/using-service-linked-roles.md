---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html
---

# Using service-linked roles for Amazon ECS
<a name="using-service-linked-roles"></a>

Amazon Elastic Container Service uses AWS Identity and Access Management (IAM) [ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon ECS. Service-linked roles are predefined by Amazon ECS and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using roles to allow Amazon ECS to manage clusters](using-service-linked-roles-for-clusters.md)
+ [Using roles to manage Amazon ECS Managed Instances](using-service-linked-roles-instances.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
