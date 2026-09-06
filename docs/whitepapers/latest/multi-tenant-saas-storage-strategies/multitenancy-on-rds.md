---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multitenancy-on-rds.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Multitenancy on Amazon RDS
<a name="multitenancy-on-rds"></a>

 With so many early SaaS systems delivered on relational databases, the developer community has established some common patterns for address multitenancy in these environments. In fact, Amazon RDS has a more natural mapping to the silo, bridge, and pool models.

 The construct and representation of data in Amazon RDS is very much an extension of non-managed relational environments. The basic mechanisms that are available in MySQL, for example, are also available to you in RDS. This makes the realization of multitenancy on all of the Amazon RDS flavors relatively straightforward.

 The following sections outline the various strategies that are commonly employed to realize the partitioning models on Amazon RDS.

## Silo model
<a name="silo-model-2"></a>

 You can achieve the silo pattern on AWS in multiple ways. However, the most common and simplest approach for achieving isolation is to create separate database instances for each tenant. Through instances, you can achieve a level of separation that typically satisfies the compliance needs of customers without the overhead of provisioning entirely separate accounts.

![A diagram depicting Amazon RDS instances as silos.](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/rds-as-silos.png)

 The preceding figure shows a basic silo model as it could be realized on top of Amazon RDS. Here, two separate instances are provisioned for each tenant.

 The diagram depicts a master database and two read replicas for each tenant instance. This is an optional concept to highlight how you can use this approach to set up and configure an optimized, highly available strategy for each tenant.

## Bridge model
<a name="bridge-model-2"></a>

 Achieving the bridge model on Amazon RDS fits the same themes we see across all the storage models. The basic approach is to leverage a single instance for all tenants while creating separate representations for each tenant within that database. This introduces the need to have provisioning and runtime table resolution to map each table to a given tenant.

 The bridge model offers you the opportunity to have tenants with different schemas and some flexibility when migrating tenant data. You could, for example, have different tenants running different versions of the product at a given moment in time and gradually migrate schema changes on a tenant-by-tenant basis.

 The following figure provides an example of one way you can implement the bridge model on Amazon RDS. In this diagram, you have a single Amazon RDS database instance that contains separate customer tables for Tenant1 and Tenant2.

![A diagram depicting an example of a bridge model on Amazon RDS.](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/bridge-model-rds.png)

 This example highlights the ability to have schema variation at the tenant level. Tenant1’s schema has a Status column, while that column is removed and replaced by the Gender column used by Tenant2.

 Another option here would be to introduce the notion of separate databases for each tenant within an instance. The terminology varies for each flavor of Amazon RDS. Some Amazon RDS storage containers refer to this as a database; others label it as a schema.

![A document depicting an Amazon RDS bridge with separate tables/schemas.](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/rds-bridge.png)

The preceding figure provides an illustration of this alternate bridge model. Notice that we created databases for each of the tenants, and the tenants then have their own collection of tables. For some SaaS organizations, this scopes the management of their tenant data more naturally, avoiding the need to propagate the naming to individual tables.

 This model is appealing, but it may not be the best fit for all flavors of Amazon RDS. Some Amazon RDS containers limit the number of databases/schemas that you can create for an instance.

 Although the bridge model allows for variation from tenant to tenant, it’s important to know that, typically, you should still adopt policies that try to limit schema changes. Each time you introduce a schema change, you can take on the challenge of successfully migrating your SaaS tenants to the new model without absorbing any downtime. So, although this model simplifies those migrations, it doesn’t promote one-off tenant schemas or regular changes to the representation of your tenant’s data.

## Pool model
<a name="pool-model-2"></a>

 The pool model for Amazon RDS relies on traditional relational indexing schemes to partition tenant data. As part of moving all the tenant data into a shared infrastructure model, you store the tenant data in a single Amazon RDS instance and the tenants share common tables. These tables are indexed with a unique tenant identifier that is used to access and manage each tenant’s data.

![A diagram depicting an Amazon RDS pool model with shared schema .](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/rds-pool-model.png)

 The preceding figure provides an example of the pool model in action. Here a single Amazon RDS instance with *one* Customer table holds data for all of the application’s tenants. Amazon RDS is an RDBMS, so all tenants must use the same schema version. Amazon RDS is not like DynamoDB, which has a flexible schema that allows each tenant to have a unique schema within a single table.

## Factoring in single instance limits
<a name="factoring-in-single-instance-limits"></a>

 Many of the models we described concentrate heavily on storing data in a single instance and partitioning data within that instance. Depending on the size and performance needs of your SaaS environment, using a single instance might not fit the profile of your tenant data. Amazon RDS has limits on the amount of data that can be stored in a single instance. The following is a breakdown of the limits:
+ Aurora – **128 TB**
+ MariaDB – **64 TB**
+ Microsoft SQL Server – **16 TB**
+ MySQL – **64 TB**
+ Oracle – **64 TB**
+ PostgreSQL – **64 TB**

 In addition, a single instance introduces resource contention issues (CPU, memory, I/O).

 In scenarios where a single instance is impractical, the natural extension is to introduce a sharding scheme where your tenant data is distributed across multiple instances. With this approach, you start with a small collection of sharded instances. Then, continually observe the profile of your tenant data and expand the number of instances to ensure that no single instance reaches limits or becomes a bottleneck.

## Weighing the tradeoffs
<a name="weighing-the-tradeoffs-1"></a>

 The tradeoffs of using Amazon RDS are fairly straightforward. The primary theme is often more about trading management and provisioning complexity for agility. Overall, the pain points of provisioning automation are likely lower with the silo model on Amazon RDS. However, the cost and management efficiency associated with the pool model is often compelling. This is especially significant as you think about how these models will align with your continuous delivery environment.
