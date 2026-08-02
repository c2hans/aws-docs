---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/logic.html
---

# Migrating business logic from the database to the application layer
<a name="logic"></a>

Migrating business logic from database-stored procedures, triggers, and functions to application-layer services is a critical step in decomposing monolithic databases. This transformation improves service autonomy, simplifies maintenance, and enhances scalability. This section provides guidance on analyzing database logic, planning the migration strategy, and then implementing the transformation while maintaining business continuity. It also discusses establishing an effective rollback plan.

**This section contains the following topics:**
+ [Phase 1: Analyzing the business logic](#logic-analysis)
+ [Phase 2: Classifying the business logic](#logic-classification)
+ [Phase 3: Migrating the business logic](#logic-migration)
+ [Rollback strategy for business logic](#logic-rollback)

## Phase 1: Analyzing the business logic
<a name="logic-analysis"></a>

When modernizing monolithic databases, you must first conduct a comprehensive analysis of your existing database logic. This phase focuses on three primary categories:
+ *Stored procedures* often contain critical business operations, including data-manipulation logic, business rules, validation checks, and calculations. As core components of the application business logic, they require careful decomposition. For instance, a financial organization's stored procedures might handle interest calculations, account reconciliation, and compliance checks.
+ *Triggers* are key database components that handle audit trails, data validation, calculations, and cross-table consistency. For example, a retail organization might use triggers to manage inventory updates throughout their order processing system, which demonstrates the complexity of automated database operations.
+ *Functions* in databases primarily manage data transformations, calculations, and lookup operations. They are often embedded across multiple procedures and applications. For example, a healthcare organization might use functions to normalize patient data or look up medical codes.

Each category represents different aspects of business logic that is embedded within the database layer. You need to carefully evaluate and plan each in order migrate them to the application layer.

During this analysis phase, customers typically face three significant challenges. First, complex dependencies emerge through nested procedure calls, cross-schema references, and implicit data dependencies. Second, transaction management becomes critical, particularly when dealing with multi-step transactions and maintaining data consistency across distributed systems. Third, performance considerations must be carefully evaluated, especially for batch processing operations, bulk data updates, and real-time calculations that currently benefit from being close to the data.

To effectively address these challenges, you can use [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) for initial analysis and then use detailed dependency-mapping tools. This approach helps you understand the full scope of your database logic and create a comprehensive migration strategy that maintains business continuity during decomposition.

By thoroughly understanding these components and challenges, you can better plan your modernization journey and make informed decisions about which elements to prioritize during the migration to a microservices-based architecture.

When analyzing database code components, create comprehensive documentation for each stored procedure, trigger, and function. Start by clearly describing its purpose and core functionality, including business rules it implements. Detail all input and output parameters, and note their data types and valid ranges. Map out dependencies on other database objects, external systems, and downstream processes. Clearly define transaction boundaries and isolation requirements to maintain data integrity. Document any performance expectations, including response time requirements and resource utilization patterns. Finally, analyze usage patterns to understand peak loads, frequency of execution, and critical business periods.

## Phase 2: Classifying the business logic
<a name="logic-classification"></a>

Effective database decomposition requires systematic categorization of database logic across key dimensions: complexity, business impact, dependencies, usage patterns, and migration difficulty. This classification helps you identify high-risk components, determine testing requirements, and establish migration priorities. For example, complex stored procedures with high business impact and frequent usage require careful planning and extensive testing. However, simple, rarely used functions with minimal dependencies might be suitable for early migration phases.

This structured approach creates a balanced migration roadmap that minimizes business disruption while maintaining system stability. By understanding these interrelationships, you can improve the sequence of your decomposition efforts and allocate resources appropriately.

## Phase 3: Migrating the business logic
<a name="logic-migration"></a>

After you have analyzed and classified your business logic, it is time to migrate it. There are two approaches when migrating business logic out of a monolithic database: move the database logic to the application layer, or move the business logic to another database that is part of the microservice.

If you migrate the business logic to the application, then the database tables store only the data, and the database doesn't contain any business logic. This is the recommended approach. You can use [Ispirer](https://aws.amazon.com/marketplace/seller-profile?id=seller-6w64f4cwyhmiw)** **or generative AI tools, such as [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) or [Kiro](https://kiro.dev/), to convert database business logic for the application layer, such as conversion to Java. For more information, see [Migrate business logic from database to application for faster innovation and flexibility](https://aws.amazon.com/blogs/mt/migrate-business-logic-from-database-to-application-for-faster-innovation-and-flexibility/) (AWS blog post).

If you migrate the business logic to another database, you can use [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) to convert existing database schemas and code objects to your target database. It supports purpose-built AWS database services, such as [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html), and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html). By providing a comprehensive assessment report and automated conversion capabilities, AWS SCT helps streamline the transition process, allowing you to focus on optimizing your new database structure for improved performance and scalability. As you progress through your modernization project, AWS SCT can handle incremental conversions to support a phased approach, enabling you to validate and fine-tune each step of your database transformation.

## Rollback strategy for business logic
<a name="logic-rollback"></a>

Two critical aspects of any decomposition strategy are maintaining backward compatibility and implementing comprehensive rollback procedures. These elements work together to help protect operations during the transition period. This section describes how to manage compatibility during the decomposition process and establish effective emergency rollback capabilities that safeguard against potential issues.

### Maintain backward compatibility
<a name="maintain-backward-compatibility.39da9f3c-0892-5f61-aa68-0c24e849596b"></a>

During database decomposition, maintaining backward compatibility is essential for smooth transitions. Keep existing database procedures temporarily in place while gradually implementing new functionality. Use version control to track all changes and manage multiple database versions simultaneously. Plan for an extended coexistence period where both the source and target systems must operate reliably. This provides time to test and validate the new system before retiring legacy components. This approach minimizes business disruption and provides a safety net for rollback if needed.

### Emergency rollback plan
<a name="emergency-rollback-plan.1e75aee0-b113-5649-9a8d-ea5f87b91827"></a>

A comprehensive rollback strategy is essential for safe database decomposition. Implement feature flags in your code to control which version of business logic is active. This allows you to instantly switch between the new and original implementations without deployment changes. This approach provides fine-grained control over the transition and helps you roll back quickly if issues arise. Keep the original logic as a verified backup, and maintain detailed rollback procedures that specify triggers, responsibilities, and recovery steps.

Regularly test these rollback scenarios under various conditions to validate their effectiveness, and make sure that teams are familiar with emergency procedures. Feature flags also enable gradual rollouts by selectively enabling new functionality for specific user groups or transactions. This provides an additional layer of risk mitigation during the transition.
