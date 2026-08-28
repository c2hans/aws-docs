---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth-redis.html
---

# Authentication and Authorization
<a name="auth-redis"></a>

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. ElastiCache supports authenticating users using IAM and the Valkey and Redis OSS AUTH command, and authorizing user operations using Role-Based Access Control (RBAC).

**Topics**
+ [Role-Based Access Control (RBAC)](Clusters.RBAC.md)
+ [Authenticating with the Valkey and Redis OSS AUTH command](auth.md)
+ [Migrating from password-based authentication (AUTH) to IAM authentication](auth-to-iam-migration.md)
+ [Disabling access control on an ElastiCache Valkey or Redis OSS cache](in-transit-encryption-disable.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
