---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/next-steps.html
---

# Next steps
<a name="next-steps"></a>

AWS offers two options for operating managed PostgreSQL: Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL. We recommend that you evaluate the two services and choose the option that best supports your specific use case for your multi-tenant SaaS applications. Conforming to a SaaS partitioning model can ensure that a SaaS application that uses PostgreSQL adheres strictly to best practices to maintain tenancy. The SaaS silo, bridge, and pool partitioning models support many SaaS use cases. These models provide varying advantages among factors such as performance isolation, operational overhead, and tenant security.

**Next steps:**
+ [Evaluate Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL](db-selection.md#relational), and pick the best option for your SaaS application.
+ [Select a SaaS partitioning model](partitioning-models.md) that meets the requirements for your application: silo, bridge, or pool.
+ Implement PostgreSQL in accordance with your selected SaaS partitioning model.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
