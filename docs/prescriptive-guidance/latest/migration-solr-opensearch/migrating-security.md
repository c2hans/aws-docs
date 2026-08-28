---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/migrating-security.html
---

# Migrating security features
<a name="migrating-security"></a>

The migration of security assets from Solr to OpenSearch involves extracting existing user credentials and permissions from the `security.json` file in Solr and recreating them in OpenSearch by using the OpenSearch Security API. This process maps Solr authentication and rule-based authorization to the OpenSearch role-based access control (RBAC) system. It ensures that all security policies and user access levels are maintained while taking advantage of the enhanced security features that OpenSearch provides.

The following table compares the security features supported in Solr and OpenSearch.

|
|
| Feature | Supported in Solr? | Supported in OpenSearch? |
| --- |--- |--- |
| Basic authentication | Yes | Yes |
| JWT authentication | Yes | Yes |
| Kerberos authentication | Yes | Yes (in self-managed OpenSearch) |
| Certificate authentication | Yes | Yes (in self-managed OpenSearch) |
| Hadoop authentication | Yes | No |
| Amazon Cognito authentication for dashboard access | No | Yes |
| SAML 2.0 standard authentication for OpenSearch Dashboards | No | Yes |
| AWS IAM Identity Center authentication and authorization | No | Yes |
| Native RBAC authorization | Yes (supports external role-based authorization) | Yes (built-in) |
| Domain access policy | No | Yes |
| Encryption at rest | Yes | Yes (default only in managed service) |
| Encryption at transit | Yes | Yes |
| Document and field-level security | No | Yes |
| Multi-tenancy for dashboard | No | Yes |

 Additional considerations:
+ ZooKeeper stores sensitive Solr security information, so protecting ZooKeeper nodes through multiple security measures is critical. This adds complexity to ensure that your Solr cluster remains secure and compliant.

  In contrast, OpenSearch doesn't use file-based storage for its security configuration, which eliminates these security complexities.
+ OpenSearch provides two methods for creating security assets: through its API or through the OpenSearch Dashboards user interface. Both approaches offer a straightforward implementation for security configuration management.

To create users and roles from OpenSearch Dashboards, see [Defining users and roles](https://docs.opensearch.org/latest/security/access-control/users-roles/) in the OpenSearch documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
