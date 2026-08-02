---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/faq.html
---

# FAQ for database decomposition
<a name="faq"></a>

This comprehensive FAQ section addresses the most common questions and challenges organizations face when undertaking database decomposition projects. From defining the initial scope and requirements to migrating stored procedures, these questions provide practical insights and strategic approaches to help teams successfully navigate their database modernization journey. Whether you're in the planning phase or already executing your decomposition strategy, these answers can help you avoid common pitfalls and implement best practices for optimal results.

**This section contains the following topics:**
+ [FAQs about defining scope and requirements](faq-scope.md)
+ [FAQs about controlling database access](faq-access.md)
+ [FAQs about analyzing cohesion and coupling](faq-cohesion-and-coupling.md)
+ [FAQs about migrating the business logic to the application layer](faq-business-logic.md)

## FAQs about migrating the business logic to the application layer
<a name="faq-business-logic2"></a>

Migrating business logic from the database to the application layer is a critical and complex aspect of database modernization. This business logic migration is discussed in the [Migrating business logic from the database to the application layer](logic.md) section of this guide. This FAQ section addresses common questions about managing this transition effectively, from selecting initial candidates for migration to handling complex stored procedures and triggers.

### How do I identify which stored procedures to migrate first?
<a name="how-do-i-identify-which-stored-procedures-to-migrate-first-.b2f0f081-e1e1-5ff6-b94c-3855431e988d"></a>

Start by identifying stored procedures that offer the best combination of low-risk and high-learning value. Focus on procedures that have minimal dependencies, clear functionality, and non-critical business impact. These make ideal candidates for initial migration because they help the team build confidence and establish patterns. For example, choose procedures that handle simple data operations over those that manage complex transactions or critical business logic.

Use database monitoring tools to analyze usage patterns and identify infrequently accessed procedures as early candidates. This approach minimizes business risk while providing valuable experience for tackling more complex migrations later. Score each procedure on complexity, business criticality, and dependency levels to create a prioritized migration sequence.

### What are the risks of moving logic to the application layer?
<a name="what-are-the-risks-of-moving-logic-to-the-application-layer-.74135e28-87af-5a77-8336-40067f7bd896"></a>

Moving database logic to the application layer introduces several key challenges. System performance can degrade due to increased network calls, especially for data-intensive operations that were previously handled within the database. Transaction management becomes more complex and requires careful coordination to maintain data integrity across distributed operations. Ensuring data consistency becomes challenging, particularly for operations that previously relied on database-level constraints.

Potential business disruption during the migration and the learning curve for developers are also significant concerns. Mitigate these risks through thorough planning, extensive testing in staged environments, and gradual migration that starts with less-critical components. Implement robust monitoring and rollback procedures to quickly identify and address issues in production.

### How do I maintain performance when moving logic away from the database?
<a name="how-do-i-maintain-performance-when-moving-logic-away-from-the-database-.d59d1de7-cb16-5166-9dd9-6c1944fa7a0c"></a>

Implement appropriate caching mechanisms for frequently accessed data, optimize data access patterns to minimize network calls, and use batch processing for bulk operations. For non-time-critical operations, consider asynchronous processing to improve system responsiveness.

Monitor application performance metrics closely and tune them as needed. For example, you can replace multiple single-row operations with bulk processing, you can cache reference data that changes infrequently, and you can optimize query patterns to reduce data transfer. Regular performance testing and tuning helps the system maintain acceptable response times and improves maintainability and scalability.

### What should I do with complex stored procedures that involve multiple tables?
<a name="what-should-i-do-with-complex-stored-procedures-that-involve-multiple-tables-.107e94e6-aa2b-5672-8faf-02dfb296c639"></a>

Approach complex, multi-table stored procedures through systematic decomposition. Start by breaking them into smaller, logically coherent components, and identify clear transaction boundaries and data dependencies. Create service interfaces for each logical component. This helps you gradually migrate without disrupting the existing functionality.

Implement a step-by-step migration, starting with the least coupled components. For highly intricate procedures, consider temporarily keeping them in the database while migrating simpler parts. This hybrid approach maintains system stability while you progress toward your architectural goals. Continuously monitor performance and functionality during the migration, and be prepared to adjust your strategy based on the results.

*How do I handle database triggers during migration?*

### What's the best way to test the migrated business logic?
<a name="what9999999999999999apos-s-the-best-way-to-test-the-migrated-business-logic-.a02f9785-b989-526c-9b74-ac20ba7d3ae2"></a>

Implement a multi-layered testing approach before you deploy the migrated business logic. Start with unit tests for new application code, then add integration tests that cover end-to-end business flows. Run old and new implementations in parallel, and then compare the results in order to validate functional equivalence. Conduct performance testing under various load conditions to verify that the system behavior matches or exceeds previous capabilities.

Use feature flags to control deployment so that you can quickly roll back if issues arise. Involve business users in the validation, particularly for critical workflows. Monitor key metrics during initial deployment, and gradually increase traffic to the new implementation. Throughout, maintain the ability to revert to the original database logic if needed.

### How do I manage the transition period when both database and application logic exist?
<a name="how-do-i-manage-the-transition-period-when-both-database-and-application-logic-exist-.c0d88c51-43bc-5a30-aad4-a9117c559adf"></a>

When the database and application logic are both in use, implement feature flags that control traffic flow and enable quick switching between old and new implementations. Maintain rigorous version control, and clearly document both implementations and their respective responsibilities. Set up comprehensive monitoring for both systems to quickly identify any discrepancies or performance issues.

Establish clear rollback procedures for each migrated component so that you can revert to the original logic if needed. Communicate regularly with all stakeholders about the transition status, potential impacts, and escalation procedures. This approach helps you gradually migrate while maintaining system stability and stakeholder confidence.

### How do I handle error scenarios in the application layer that were previously managed by the database?
<a name="how-do-i-handle-error-scenarios-in-the-application-layer-that-were-previously-managed-by-the-database-.b0cc3981-81f9-5a33-9b65-67925c204f59"></a>

Replace database-level error handling with robust application-layer mechanisms. Implement circuit breakers and retry logic for transient failures. Use compensating transactions for maintaining data consistency across distributed operations. For example, if a payment update fails, the application should automatically retry within defined limits and initiate compensating actions if needed.

Set up comprehensive monitoring and alerting to quickly identify issues, and maintain detailed audit logs for troubleshooting. Design error handling to be as automated as possible, and define clear escalation paths for scenarios that require human intervention. This multi-layered approach provides system resilience while maintaining data integrity and business process continuity.
