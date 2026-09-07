---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/access-about-dbws.html
---

# Controlling access with the database wrapper service pattern
<a name="access-about-dbws"></a>

A *wrapper service* is a service layer that acts as a facade for the database. This approach is particularly valuable when you need to maintain existing functionality while preparing for future decomposition. This pattern follows a simple principle—when something is too messy, start by containing the mess. The wrapper service becomes the only authorized way to access the database, providing a controlled interface while hiding the underlying complexity.

Use this pattern when immediate database decomposition isn't feasible due to complex schemas or when multiple services require continuous data access. It's particularly valuable during transition periods because it provides time for careful refactoring while maintaining system stability. The pattern works well when consolidating data ownership to specific teams or when new applications need aggregated views across multiple tables.

For example, apply this pattern when:
+ Schema complexity prevents immediate separation
+ Multiple teams need ongoing data access
+ Gradual modernization is preferred
+ Team restructuring requires clear data ownership
+ New applications need consolidated data views

## Benefits and limitations of the database wrapper service pattern
<a name="access-about-dbws-benefits-limitations"></a>

The following are the benefits of the database wrapper pattern:
+ **Controlled growth** – The wrapper service prevents further uncontrolled additions to the database schema.
+ **Clear boundaries** – The implementation process helps you establish clear ownership and responsibility boundaries.
+ **Refactoring freedom** – A wrapper service lets you make internal changes without impacting consumers.
+ **Improved observability** – A wrapper service is a single point for monitoring and logging.
+ **Simplified testing** – A wrapper service makes it easier for consuming services to create simplified, mock versions for testing.

The following are the limitations of the database wrapper pattern.
+ **Technology coupling** – A wrapper service works best when it uses the same technology stack as the consuming services.
+ **Initial overhead** – The wrapper service requires additional infrastructure that might affect performance.
+ **Migration effort** – To implement the wrapper service, you must coordinate across teams to transition away from direct access.
+ **Performance** – If the wrapping service experiences high traffic, heavy usage, or frequent access, consuming services might experience poor performance. On top of the database, the wrapper service must handle pagination, cursors, and database connections. Depending it on your use case, it might not scale well, and it might be a poor fit for extract, transform, and load (ETL) workloads.

## Implementing the database wrapper service pattern
<a name="access-about-dbws-implementation"></a>

There are two phases to implement the database wrapper service pattern. First, you create the database wrapper service. Then, you direct all access through it and document the access patterns.

### Phase 1: Creating the database wrapper service
<a name="phase-1--creating-the-database-wrapper-service.8682d26a-fb00-50e1-b4f4-ab6caea388ca"></a>

Create a lightweight service layer that acts as a gatekeeper to your database. Initially, it should mirror all existing functionalities. This wrapper service becomes the mandatory access point for all database operations, which converts direct database dependencies into service-level dependencies. Implement detailed logging and monitoring at this layer to track usage patterns, performance metrics, and access frequencies. Maintain your existing stored procedures, but make sure that they're accessed only through this new service interface.

### Phase 2: Implementing access control
<a name="phase-2--implementing-access-control.44eff366-46c0-586f-88ef-9dd06197d035"></a>

Systematically redirect all database access through the wrapper service, and then revoke direct database permissions from external systems that access the database directly. Document each access pattern and dependency as services are migrated. This controlled access enables internal refactoring of database components without disrupting external consumers. For example, start with low-risk, read-only operations instead of complex transactional workflows.

### Phase 3: Monitor database performance
<a name="phase-3--monitor-database-performance.15cd368d-cf11-5489-815f-3c00d2e84b7d"></a>

Use the wrapper service as a centralized monitoring point for database performance. Track key metrics, including query response times, usage patterns, error rates, and resource utilization. Set up alerts for performance thresholds and unusual patterns. For example, monitor slow-running queries, connection pool utilization, and transaction throughput to proactively identify potential issues.

Use this consolidated view to optimize database performance through query tuning, resource allocation adjustments, and usage pattern analysis. The centralized nature of the wrapper service makes it easier to implement improvements and validate their impact across all consumers, while maintaining consistent performance standards.

### Best practices for implementing a database wrapper service
<a name="best-practices-for-implementing-a-database-wrapper-service.a5700673-e927-505f-8fc3-0cf1266aa405"></a>

The following best practices can help you implement a database wrapper service:
+ **Start small** – Begin with a minimal wrapper that simply proxies existing functionality
+ **Maintain stability** – Keep the service interface stable while making internal improvements
+ **Monitor usage** – Implement comprehensive monitoring to understand access patterns
+ **Clear ownership** – Assign a dedicated team to maintain both the wrapper and the underlying schema
+ **Encourage local storage** – Motivate teams to store their data in their own databases

## Scenario-based example
<a name="access-about-dbws-example"></a>

This section describes an example of how a fictitious company, named *AnyCompany Books*, could use the database wrapper pattern to control access to their monolithic database system. At AnyCompany Books, there are three critical services: Dispatch, Finance, and Order Processing. These services share access to a central database. Each service is maintained by a different team. Over time, they independently modify the database schema to meet their specific needs. This has led to a tangled web of dependencies and an increasingly complex database structure.

![Three applications sharing access to a central database with multiple, modified schemas.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/f6caaac6-d80b-4630-b9c9-23e649e59489.png)

The company's application or enterprise architect recognizes the need to decompose this monolithic database. Their goal is to give each service its own dedicated database to improve maintainability and reduce cross-team dependencies. However, they face a significant challenge—it's nearly impossible to decompose the database while all three teams continue to actively modify it for their ongoing projects. The constant schema changes and lack of coordination between teams make it extremely risky to attempt any significant restructuring.

The architect uses the database wrapper service pattern to start controlling access to the monolithic database. First, they set up the database wrapper service for a particular module, called the Order service. Then, they redirect the Order Processing service to access the wrapper service instead of directly accessing the database. The following image shows the modified infrastructure.

![Database access after implementing the wrapper service.](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/f88c0429-18a2-41f6-a897-f1a330fc1443.png)

Gradually, AnyCompany Books can move all of the other services to use their respective wrapper services. The end goal is for each service have its own database, without going through the wrapper service. But the database wrapper service is an important and necessary intermediate step. Subsequent sections of this guide help you decompose further.
