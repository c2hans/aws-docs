---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about implementing managed PostgreSQL in multi-tenant SaaS applications.

**Q. **Which managed PostgreSQL options does AWS offer?** **

**A. **AWS offers [Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) and [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html).  [AWS also has a broad catalog of managed database offerings](https://aws.amazon.com/products/databases/).

**Q. **Which service is optimal for SaaS applications?** **

**A. **You can use both Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL for SaaS applications and all the SaaS partitioning models discussed in this guide. These two services** **have differences in scalability, crash recovery, failover, storage options, high availability, disaster recovery, backup, and the instance classes available for each option. The optimal choice will depend on your specific use case. Use the [decision matrix](matrix.md) in this guide to choose the best option for your use case. ** **

**Q. **Which unique requirements should I consider if I decide to use a PostgreSQL database with a multi-tenant SaaS application?** **

**A. **As with any data store used with a SaaS application, the most important consideration is the method for maintaining tenant data isolation. As discussed in this guide, there are multiple ways you can achieve tenant data isolation with AWS managed PostgreSQL** **offerings. Additionally, you should consider performance isolation on a per-tenant basis for any PostgreSQL implementations.

**Q. **Which models can I use to maintain tenant data isolation with PostgreSQL?

**A. **You can use the silo, bridge, and pool models as SaaS partitioning strategies to maintain tenant data isolation. For a discussion of these models and how they can be applied to PostgreSQL, see the section [Multi-tenant SaaS partitioning models for PostgreSQL](partitioning-models.md) in this guide.

**Q. **How do I maintain tenant data isolation with a single PostgreSQL database that is shared across multiple tenants?

**A. **PostgreSQL supports a row-level security (RLS) feature that you can use to enforce tenant data isolation in a single PostgreSQL database or instance. Additionally, you can provision separate PostgreSQL databases per tenant in a single instance, or create schemas on a per-tenant basis to achieve this goal. For the advantages and disadvantages of these approaches, see the section [Row-level security recommendations](rls.md) in this guide.
