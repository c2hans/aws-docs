---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/partitioning-models.html
---

# Multi-tenant SaaS partitioning models for PostgreSQL
<a name="partitioning-models"></a>

The best method for accomplishing multi-tenancy depends on the requirements for your SaaS application. The following sections demonstrate partitioning models for successfully implementing multi-tenancy in PostgreSQL.

**Note**
    The models discussed in this section are applicable to both Amazon RDS for PostgreSQL and Aurora PostgreSQL-Compatible. References to *PostgreSQL* in this section apply to both services.

There are three high-level models that you can use in PostgreSQL for SaaS partitioning: silo, bridge, and pool. The following image summarizes the trade-offs between the silo and pool models. The bridge model is a hybrid of the silo and pool models.

|
|
| Partitioning model | Advantages | Disadvantages |
| --- |--- |--- |
| **Silo** | Compliance alignment | Compromised agility |
| No cross-tenant impact | No centralized management |
| Tenant-level tuning | Deployment complexity |
| Tenant-level availability | Cost |
| **Pool** | Agility | Cross-tenant impact |
| Cost optimization | Compliance challenges |
| Centralized management | All or nothing availability |
| Simplified deployment |   |
| **Bridge** | Some compliance alignment | Some compliance challenges |
| Agility | All or nothing availability (mostly) |
| Cost optimization | Cross-tenant impact |
| Centralized management | Deployment complexity |

The following sections discuss each model in more detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
