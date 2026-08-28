---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-security.html
---

# Security and the Spark operator with Amazon EMR on EKS
<a name="spark-operator-security"></a>

There are a couple ways to set up cluster-access permissions when you use the Spark operator. The first is to use role-based access control, Role-based access control (RBAC) restricts access based on a person's role within an organization. It has become a primary way to handle access. The second access method is to assume an AWS Identity and Access Management role, which provides resource access by means of specific assigned permissions.

**Topics**
+ [Setting up cluster access permissions with role-based access control (RBAC)](spark-operator-security-rbac.md)
+ [Setting up cluster access permissions with IAM roles for service accounts (IRSA)](spark-operator-security-irsa.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
