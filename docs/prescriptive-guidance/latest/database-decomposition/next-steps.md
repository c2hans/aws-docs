---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/next-steps.html
---

# Next steps for database decomposition on AWS
<a name="next-steps"></a>

After implementing initial database decomposition strategies through database wrapper services and moving business logic to the application layer, organizations must plan their next evolution. This section outlines key considerations for continuing your modernization journey.

**This section contains the following topics:**
+ [Incremental strategies for database decomposition](#next-steps-incremental-strategies)
+ [Technical considerations for distributed database environments](#next-steps-considerations)
+ [Organizational changes to support distributed architectures](#next-steps-organization)

## Incremental strategies for database decomposition
<a name="next-steps-incremental-strategies"></a>

Database decomposition follows a gradual evolution through three distinct phases. Teams first wrap the monolithic database with a database wrapper service to control access. They then begin splitting the data into service-specific databases, while maintaining the primary database for legacy needs. Finally, they complete migrate the business logic in order to transition to fully independent service databases.

Throughout this journey, teams must implement careful data synchronization patterns and continuously validate consistency across services. Performance monitoring becomes crucial to identify and address potential issues early. As services evolve independently, their schemas should be optimized based on actual usage patterns, and you should remove redundant structures that accumulated over time.

This incremental approach helps minimize risks while maintaining system stability throughout the transformation process.

## Technical considerations for distributed database environments
<a name="next-steps-considerations"></a>

In a distributed database environment, performance monitoring becomes essential to identify and address bottlenecks early. Teams must implement comprehensive monitoring systems and caching strategies to maintain performance levels. Read/write splitting can effectively balance loads across the system.

Data consistency requires careful orchestration across distributed services. Teams should implement eventual consistency patterns where appropriate and establish clear data ownership boundaries. Robust monitoring promotes data integrity across all services.

In addition, security must evolve to accommodate the distributed architecture. Each service needs fine-grained security controls, and your access patterns require regular review. Enhanced monitoring and auditing become critical in this distributed environment.

## Organizational changes to support distributed architectures
<a name="next-steps-organization"></a>

The team structure should align with service boundaries in order to define clear ownership and accountability. Organizations must establish new communication patterns and build additional technical capabilities within teams. This structure should support both maintenance of existing services and your continued architectural evolution.

You must update your operational processes to handle the distributed architecture. Teams must modify deployment procedures, adapt incident response processes, and evolve change management practices to coordinate across multiple services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
