---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/faq-business-logic.html
---

# FAQs about migrating the business logic to the application layer
<a name="faq-business-logic"></a>

Migrating business logic from the database to the application layer is a critical and complex aspect of database modernization. This business logic migration is discussed in the [Migrating business logic from the database to the application layer](logic.md) section of this guide. This FAQ section addresses common questions about managing this transition effectively, from selecting initial candidates for migration to handling complex stored procedures and triggers.

## How do I identify which stored procedures to migrate first?
<a name="how-do-i-identify-which-stored-procedures-to-migrate-first"></a>

Start by identifying stored procedures that offer the best combination of low-risk and high-learning value. Focus on procedures that have minimal dependencies, clear functionality, and non-critical business impact. These make ideal candidates for initial migration because they help the team build confidence and establish patterns. For example, choose procedures that handle simple data operations over those that manage complex transactions or critical business logic.

Use database monitoring tools to analyze usage patterns and identify infrequently accessed procedures as early candidates. This approach minimizes business risk while providing valuable experience for tackling more complex migrations later. Score each procedure on complexity, business criticality, and dependency levels to create a prioritized migration sequence.

## What are the risks of moving logic to the application layer?
<a name="what-are-the-risks-of-moving-logic-to-the-application-layer"></a>

Moving database logic to the application layer introduces several key challenges. System performance can degrade due to increased network calls, especially for data-intensive operations that were previously handled within the database. Transaction management becomes more complex and requires careful coordination to maintain data integrity across distributed operations. Ensuring data consistency becomes challenging, particularly for operations that previously relied on database-level constraints.

Potential business disruption during the migration and the learning curve for developers are also significant concerns. Mitigate these risks through thorough planning, extensive testing in staged environments, and gradual migration that starts with less-critical components. Implement robust monitoring and rollback procedures to quickly identify and address issues in production.

## How do I maintain performance when moving logic away from the database?
<a name="how-do-i-maintain-performance-when-moving-logic-away-from-the-database"></a>

Implement appropriate caching mechanisms for frequently accessed data, optimize data access patterns to minimize network calls, and use batch processing for bulk operations. For non-time-critical operations, consider asynchronous processing to improve system responsiveness.

Monitor application performance metrics closely and tune them as needed. For example, you can replace multiple single-row operations with bulk processing, you can cache reference data that changes infrequently, and you can optimize query patterns to reduce data transfer. Regular performance testing and tuning helps the system maintain acceptable response times and improves maintainability and scalability.

## What should I do with complex stored procedures that involve multiple tables?
<a name="what-should-i-do-with-complex-stored-procedures-that-involve-multiple-tables"></a>

Approach complex, multi-table stored procedures through systematic decomposition. Start by breaking them into smaller, logically coherent components, and identify clear transaction boundaries and data dependencies. Create service interfaces for each logical component. This helps you gradually migrate without disrupting the existing functionality.

Implement a step-by-step migration, starting with the least coupled components. For highly intricate procedures, consider temporarily keeping them in the database while migrating simpler parts. This hybrid approach maintains system stability while you progress toward your architectural goals. Continuously monitor performance and functionality during the migration, and be prepared to adjust your strategy based on the results.

## How do I handle database triggers during migration?
<a name="how-do-i-handle-database-triggers-during-migration"></a>

Transform database triggers into application-level event handlers while maintaining system functionality. Replace synchronous triggers with event-driven patterns that message queues for asynchronous operations. Consider using [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) or [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) for the message queues. For audit requirements, implement application-level logging or use database change data capture (CDC) features.

Analyze each trigger's purpose and criticality. Some triggers might be better served by application logic, and others might require event-sourcing patterns to maintain data consistency. Start with simple triggers, such as audit logs, before tackling complex ones that manage business rules or data integrity. Monitor carefully during the migration to make sure that there is no loss of functionality or data consistency.

## What's the best way to test the migrated business logic?
<a name="whats-the-best-way-to-test-the-migrated-business-logic"></a>

Implement a multi-layered testing approach before you deploy the migrated business logic. Start with unit tests for new application code, then add integration tests that cover end-to-end business flows. Run old and new implementations in parallel, and then compare the results in order to validate functional equivalence. Conduct performance testing under various load conditions to verify that the system behavior matches or exceeds previous capabilities.

Use feature flags to control deployment so that you can quickly roll back if issues arise. Involve business users in the validation, particularly for critical workflows. Monitor key metrics during initial deployment, and gradually increase traffic to the new implementation. Throughout, maintain the ability to revert to the original database logic if needed.

## How do I manage the transition period when both database and application logic exist?
<a name="how-do-i-manage-the-transition-period-when-both-database-and-application-logic-exist"></a>

When the database and application logic are both in use, implement feature flags that control traffic flow and enable quick switching between old and new implementations. Maintain rigorous version control, and clearly document both implementations and their respective responsibilities. Set up comprehensive monitoring for both systems to quickly identify any discrepancies or performance issues.

Establish clear rollback procedures for each migrated component so that you can revert to the original logic if needed. Communicate regularly with all stakeholders about the transition status, potential impacts, and escalation procedures. This approach helps you gradually migrate while maintaining system stability and stakeholder confidence.

## How do I handle error scenarios in the application layer that were previously managed by the database?
<a name="how-do-i-handle-error-scenarios-in-the-application-layer-that-were-previously-managed-by-the-database"></a>

Replace database-level error handling with robust application-layer mechanisms. Implement circuit breakers and retry logic for transient failures. Use compensating transactions for maintaining data consistency across distributed operations. For example, if a payment update fails, the application should automatically retry within defined limits and initiate compensating actions if needed.

Set up comprehensive monitoring and alerting to quickly identify issues, and maintain detailed audit logs for troubleshooting. Design error handling to be as automated as possible, and define clear escalation paths for scenarios that require human intervention. This multi-layered approach provides system resilience while maintaining data integrity and business process continuity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
