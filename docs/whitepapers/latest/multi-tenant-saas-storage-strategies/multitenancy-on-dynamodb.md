---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multitenancy-on-dynamodb.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Multitenancy on DynamoDB
<a name="multitenancy-on-dynamodb"></a>

 The nature of how data is scoped and managed by DynamoDB adds some new twists to how you approach multitenancy. Although some storage services align nicely with the traditional data partitioning strategies, DynamoDB has a slightly less direct mapping to the silo, bridge, and pool models. With DynamoDB, you have to consider some additional factors when selecting your multitenant strategy.

 The sections that follow explore the AWS mechanisms that are commonly used to realize each of the multitenant partitioning schemes on DynamoDB.

## Silo model
<a name="silo-model-1"></a>

 Before looking at how you might implement the silo model on DynamoDB, you must first consider how the service scopes and controls access to data. Unlike Amazon RDS, DynamoDB has no notion of a database instance. Instead, all tables created in DynamoDB are global to an account within a region. That means every table name in that region must be unique for a given account.

![A diagrm depciting the silo model with DynamoDB tables .](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/silo-with-dynamodb.png)

 If you implement a silo model on DynamoDB, you have to find some way to create a grouping of one or more tables that are associated with a specific tenant. The approach must also create a secure, controlled view of these tables to satisfy the security requirements of silo customers, preventing any possibility of cross-tenant data access.

The preceding figure shows one example of how you might achieve this tenant-scoped grouping of tables. Notice that two tables are created for each tenant (Account and Customer). These tables also have a tenant identifier that is prepended to the table names. This addresses DynamoDB’s table naming requirements and creates the necessary binding between the tables and their associated tenants.

 Access to these tables is also achieved through the introduction of IAM policies. Your provisioning process needs to automate the creation of a policy for each tenant and apply that policy to the tables owned by a given tenant.

 This approach achieves the fundamental isolation goals of the silo model, defining clear boundaries between each tenant’s data. It also allows for tuning and optimization on a tenant-by-tenant basis. You can tune two specific areas:
+  [Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) can be captured at the table level, simplifying the aggregation of tenant metrics for storage activity.
+  Table write and read capacity, measured as input and output per second (IOPS), are applied at the table level, allowing you to create distinct scaling policies for each tenant.

 The disadvantages of this model tend to be more on the operational and management side. Clearly, with this approach, your operational views of a tenant require some awareness of the tenant table naming scheme to filter and present information in a tenant-centric context. The approach also adds a layer of indirection for any code that needs to interact with these tables. Each interaction with a DynamoDB table requires you to insert the tenant context to map each request to the appropriate tenant table.

 SaaS providers that adopt a microservice-based architecture also have another layer of considerations. With microservices, teams typically distribute storage responsibilities to individual services. Each service is given the freedom to determine how it stores and manages data. This can complicate your isolation story on DynamoDB, requiring you to expand your population of tables to accommodate the needs of each service. It also adds another dimension of scoping, where each table for each service identifies its binding to a service.

 To offset some of these challenges and better align with DynamoDB best practices, consider having a single table for *all* of your tenant data. This approach offers several efficiencies and simplifies the provisioning, management, and migration profile of your solution.

 In most cases, using separate DynamoDB tables and IAM policies to isolate your tenant data addresses the needs of your silo model. Your only other option is to consider the [Linked Account silo model](linked-account-silo-model.md), described earlier. However, as outlined previously, the Linked Account isolation model comes with additional limitations and considerations.

## Bridge model
<a name="bridge-model-1"></a>

 For DynamoDB, the line between the bridge model and silo model is very blurry. Essentially, if your goal using the bridge model is to have a single account with one-off schema variation for each client, you can see how that can be achieved with the silo model described earlier.

 For bridge, the only question would be whether you might relax some of the isolation requirements described with the silo model. You can achieve this by eliminating the introduction of any table-level IAM policies. Assuming your tenants aren’t requiring full isolation, you could argue that removing the IAM policies could simplify your provisioning scheme. However, even in bridge, there are merits to the isolation. So, although dropping the IAM isolation might be appealing, it’s still a good SaaS practice to leverage constructs and policies that can constrain cross-tenant access.

## Pool model
<a name="pool-model-1"></a>

 Implementing the pool model on DynamoDB requires you to step back and consider how the service manages data. As data is stored in DynamoDB, the service must continually assess and partition the data to achieve scale. And, if the profile of your data is evenly distributed, you could simply rely on this underlying partitioning scheme to optimize the performance and cost profile of your SaaS tenants.

 The challenge here is that data in a multitenant SaaS environment doesn’t typically have a uniform distribution. SaaS tenants come in all shapes and sizes and, as such, their data is anything but uniform. It’s very common for SaaS vendors to end up with a handful of tenants that consume the largest portion of their data footprint.

 Knowing this, you can see how it creates problems for implementing the pool model on top of DynamoDB. If you simply map tenant identifiers to a DynamoDB partition key, you’ll quickly discover that you also create partition “hot spots”. Imagine having one very large tenant who would undermine how DynamoDB effectively partitions your data. These hot spots can impact the cost and performance of your solution. With the suboptimal distribution of your keys, you need to increase IOPS to offset the impact of your hot partitions. This need for higher IOPS translates directly into higher costs for your solution.

 To solve this problem, you have to introduce some mechanism to better control the distribution of your tenant data. You’ll need an approach that doesn’t rely on a single tenant identifier to partition your data. These factors all lead down a single path—you must create a secondary sharding model to associate each tenant with multiple partition keys.

 Let’s look at one example of how you might bring such a solution to life. First, you need a separate table, which we’ll call the “tenant lookup table”, to capture and manage the mapping of tenants to their corresponding DynamoDB partition keys. The following figure represents an example of how you might structure your tenant lookup table.

![A diagram introducing a tenant lookup table.](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/tenant-lookup-table.png)

 This table includes mappings for two tenants. The items associated with these tenants have attributes that contain sharding information for each table that is associated with a tenant. Here, our tenants both have sharding information for their Customer and Account tables. Also notice that for each tenant-table combination there are three pieces of information that represent the current sharding profile for a table. These are:
+  **ShardCount** — An indication of how many shards are currently associated with the table.
+  **ShardSize** — The current size of each of the shards
+  **ShardId** — A list of partition keys mapped to a tenant (for a table)

 With this mechanism in place, you can control how data is distributed for each table. The indirection of the lookup table gives you a way to dynamically adjust a tenant’s sharding scheme based on the amount of data it is storing. Tenants with a particularly large data footprint will be given more shards. Because the model configures sharding on a table-by-table basis, you have much more granular control over mapping a tenant’s data needs to a specific sharding configuration. This allows you to better align your partitioning with the natural variations that often show up in your tenant’s data profile.

 Although introducing a tenant lookup table provides you with a way to address tenant data distribution, it does not come without a cost. This model now introduces a level of indirection that you have to address in your solution’s data access layer. Instead of using a tenant identifier to directly access your data, first consult the shard mappings for that tenant and use the union of those identifiers to access your tenant data. The following sample Customer table shows how data would be represented in this model.

![A diagram depicting a customer table with shard IDs.](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/shard-id.png)

 In this example, the ShardID is a direct mapping from the *tenant lookup* table. That tenant lookup table included two separate lists of shard identifiers for the Customer table, one for Tenant1 and one for Tenant2. These shard identifiers correlate directly to the values you see in this sample customer table. Notice that the actual tenant identifier never appears in this Customer table.

## Managing shard distribution
<a name="managing-shard-distribution"></a>

 The mechanics of this model aren’t particularly complex. The problem gets more interesting when you think about how to implement a strategy that effectively distributes your data. How do you detect when a tenant requires additional shards? Which metrics and criteria can you collect to automate this process? How do the characteristics of your data and domain influence your data profile? There is no single approach that universally resolves these questions for every solution. Some SaaS organizations manually tune this, based on their customer insights. Others have more natural criteria that guide their approach.

 The approach outlined here is one way you might choose to handle the distribution of your data. Ultimately, you’ll likely find a hybrid of the principles we describe that best aligns with the needs of your environment. The key takeaway is that if you adopt the pool model, be aware of how DynamoDB partitions data. Moving in data blindly without considering how the data will be distributed will likely undermine the performance and cost profile of your SaaS solution.

## Dynamically optimizing IOPS
<a name="dynamically-optimizing-iops"></a>

 The IOPS needs of a SaaS environment can be challenging to manage. The load tenants place on your system can vary significantly. Setting the IOPS to some worst case, maximum level undermines the desire to optimize costs based on actual load.

 Instead, consider implementing a dynamic model where the IOPS of your tables are adjusted in real time based on the load profile of your application. [Dynamic DynamoDB](https://dynamic-dynamodb.readthedocs.io/en/latest/index.html) is one configurable open-source solution you can use to address this problem.

## Supporting multiple environments
<a name="supporting-multiple-environments"></a>

 As you think about the strategies outlined for DynamoDB, consider how each of these models will be realized in the presence of multiple environments (QA, development, production, etc.). The need for multiple environments impacts how you further partition your experience to separate out each of your storage strategies on AWS. With the bridge and pool models, for example, you can end up adding a qualifier to your table names to provide environment context. This adds a bit of misdirection that you must factor into your provisioning and runtime resolution of table names.

## Migration efficiencies
<a name="migration-efficiencies"></a>

 The schema-less nature of DynamoDB offers real advantages for SaaS providers, allowing you to apply updates to your application and migrate tenant data without introducing new tables or replication. DynamoDB simplifies the process of migrating tenants between your SaaS versions and allows you to simultaneously host agile tenants on the latest version of your SaaS solution, while allowing other tenants to continue using an earlier version.

## Weighing the tradeoffs
<a name="weighing-the-tradeoffs"></a>

 Each of the models has tradeoffs to consider as you determine which model best aligns with your business needs. The silo pattern may seem appealing, but the provisioning and management add a dimension of complexity that undermines the agility of your solution. Supporting separate environments and creating unique groups of tables will undoubtedly impact the complexity of your automated deployment. The bridge represents a slight variation of the silo model on DynamoDB. As such, it mirrors most of what we find with the silo model.

 The pool model on DynamoDB offers some significant advantages. The consolidated footprint of the data simplifies the provisioning, migration, and management and monitoring experiences. It also allows you to take a more multitenant approach to optimizing consumption and tenant experience by tuning the read and write IOPS on a cross-tenant basis. This allows you to react more broadly to performance issues and introduces opportunities to minimize cost. These factors tend to make the pool model very appealing to SaaS organizations.
