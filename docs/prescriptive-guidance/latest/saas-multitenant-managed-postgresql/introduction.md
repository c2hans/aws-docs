---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/introduction.html
---

# Implementing managed PostgreSQL for multi-tenant SaaS applications on AWS
<a name="introduction"></a>

*Tabby Ward and Thomas Davis, Amazon Web Services*

When you select a database to store operational data, it is crucial to consider how the data should be structured, which queries it will answer, how fast it will provide answers, and the resiliency of the data platform itself. In addition to these general considerations are software as a service (SaaS) implications for operational data, such as performance isolation, tenant security, and unique characteristics and design patterns that are typical of data for multi-tenant SaaS applications. This guide discusses how these factors apply to using a PostgreSQL database on Amazon Web Services (AWS)  as the primary operational data store for a multi-tenant SaaS application. Specifically, the guide focuses on two AWS managed PostgreSQL options: Amazon Aurora PostgreSQL-Compatible Edition and Amazon Relational Database Service (Amazon RDS) for PostgreSQL.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guidance provides a detailed analysis of best practices for multi-tenant SaaS applications using Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL. We recommend that you use the design patterns and concepts provided in this guide to inform and standardize your implementation of Aurora PostgreSQL-Compatible or Amazon RDS for PostgreSQL for your multi-tenant SaaS applications.

This prescriptive guidance helps achieve the following business outcomes:
+ **Choosing the most optimal AWS managed PostgreSQL option for your use case **-- This guidance compares relational and non-relational options for database usage with SaaS applications. It also discusses which use cases are most optimal for Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL. This information will assist in selecting the best option for your SaaS application.
+ **Enforcement of SaaS best practices through the adoption of a SaaS partitioning model **– This guide discusses and compares three broad SaaS partitioning models that are applicable to a PostgreSQL database management system (DBMS): pool, bridged, and silo models, and their variations. These approaches capture SaaS best practices and provide flexibility when designing a SaaS application. The enforcement of a SaaS partitioning model is a crucial part of preserving best practices.
+ **Effective use of RLS in pool SaaS partitioning models **–** **Row-level security (RLS) supports the enforcement of tenant data isolation within a single PostgreSQL table by restricting the rows that can be viewed based on the user or a context variable. When you use the pool partitioning model, RLS is required to prevent cross-tenant access.
