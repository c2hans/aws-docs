---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/best-practices.html
---

# Best practices
<a name="best-practices"></a>

This section lists some of the high-level takeaways from this guide. For detailed discussions on each point, follow the links to the corresponding sections.

## Compare AWS options for managed PostgreSQL
<a name="compare-aws-options-for-managed-postgresql.d9567711-43ff-5669-b860-bfed661a253e"></a>

AWS offers two primary ways to run PostgreSQL in a managed environment. (In this context, *managed* means that the PostgreSQL infrastructure and DBMS are partially or completely supported by an AWS service.) Managed PostgreSQL options on AWS have the benefit of automating backups, failover, optimization, and some administration of PostgreSQL. As managed options, AWS offers Amazon Aurora PostgreSQL-Compatible Edition and Amazon Relational Database Service (Amazon RDS) for PostgreSQL. You can select the best choice from these two models by analyzing your PostgreSQL use case. For more information, see the section [Choosing between Amazon RDS and Aurora](db-selection.md#relational) in this guide.

## Select a multi-tenant SaaS partitioning model
<a name="select-a-multi-tenant-saas-partitioning-model.2303588e-3cb4-591f-97e1-eec3ea9a085b"></a>

You can choose from three SaaS partitioning models that are applicable to PostgreSQL: silo, bridge, and pool. Each model has advantages and disadvantages, and you should choose the most optimal model depending on your use case. Amazon RDS for PostgreSQL and Aurora PostgreSQL-Compatible support all three models. Choosing a model is critical to maintaining tenant data isolation in your SaaS applications. For a detailed discussion of these models, see the section [Multi-tenant SaaS partitioning models for PostgreSQL](partitioning-models.md) in this guide.

## Use row-level security for pool SaaS partitioning models
<a name="use-row-level-security-for-pool-saas-partitioning-models.80e59ce8-584b-5282-91f0-bbd9745e99db"></a>

Row-level security (RLS) is required to maintain tenant data isolation in a pool model with PostgreSQL. This is because there is no logical separation between infrastructure, PostgreSQL databases, or schemas on a per-tenant basis in a pool model. RLS centralizes the enforcement of isolation policies at the database level and removes the burden of maintaining this isolation from software developers. You can use RLS to limit database operations to a specific tenant. For more information and an example, see the section [Row-level security recommendations](rls.md) in this guide.
