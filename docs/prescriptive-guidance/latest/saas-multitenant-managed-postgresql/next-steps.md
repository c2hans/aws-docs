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
