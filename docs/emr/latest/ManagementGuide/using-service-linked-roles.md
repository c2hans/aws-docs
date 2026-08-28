---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/using-service-linked-roles.html
---

# Using service-linked roles for Amazon EMR
<a name="using-service-linked-roles"></a>

Amazon EMR uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon EMR. Service-linked roles are predefined by Amazon EMR and include all the permissions that the service requires to call other AWS services on your behalf.

**Topics**
+ [Using service-linked roles for Amazon EMR for cleanup](using-service-linked-roles-cleanup.md)
+ [Using service-linked roles with Amazon EMR for write-ahead logging](using-service-linked-roles-wal.md)

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
