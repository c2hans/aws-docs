---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/faq-cohesion-and-coupling.html
---

# FAQs about analyzing cohesion and coupling
<a name="faq-cohesion-and-coupling"></a>

Understanding and effectively analyzing database coupling and cohesion is fundamental to successful database decomposition. Coupling and cohesion are discussed in the [Analyzing cohesion and coupling for database decomposition](cohesion-coupling.md) section of this guide. This FAQ section addresses key questions about identifying appropriate levels of granularity, selecting the right analysis tools, documenting findings, and prioritizing coupling issues.

## How do I identify the right level of granularity when analyzing coupling?
<a name="how-do-i-identify-the-right-level-of-granularity-when-analyzing-coupling"></a>

Start with a broad analysis of database relationships, then systematically drill down to identify natural separation points. Use database analysis tools to map table-level relationships, schema dependencies, and transaction boundaries. For example, examine join patterns in SQL queries to understand data access dependencies. You can also analyze transaction logs to identify business process boundaries.

Focus on areas where coupling is naturally minimal. These often align with business domain boundaries and represent optimal decomposition points. When determining appropriate service boundaries, consider both technical coupling (such as shared tables and foreign keys) and business coupling (such as process flows and reporting needs).

## What tools can I use to analyze database coupling and cohesion?
<a name="what-tools-can-i-use-to-analyze-database-coupling-and-cohesion"></a>

You can use a combination of automated tools and manual analysis to assess database coupling and cohesion. The following tools can help you with this assessment:
+ **Schema visualization tools** – You can use tools like [SchemaSpy](https://schemaspy.org/) or [pgAdmin](https://www.pgadmin.org/) to generate ER diagrams. These diagrams reveal table relationships and potential coupling points.
+ **Query analysis tools** – You can use [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) or [SQL Server Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store) to identify frequently joined tables and access patterns.
+ **Database profiling tools** – Tools such as [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/) or [MySQL Workbench](https://www.mysql.com/products/workbench/) provide insights into query performance and data dependencies.
+ **Dependency mapping tools** – The [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) can help you visualize schema relationships and identify tightly coupled components. [vFunction](https://vfunction.com/) can help you identify domain boundaries by analyzing the application's functional and domain boundaries.
+ **Transaction monitoring tools** – You can use database-specific tools, such as [Oracle Enterprise Manager](https://www.oracle.com/enterprise-manager/) or [SQL Server Extended Events](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?view=sql-server-ver17), to analyze transaction boundaries.
+ **Business logic migration tools** – You can use [Ispirer](https://aws.amazon.com/marketplace/seller-profile?id=seller-6w64f4cwyhmiw)** **or generative AI tools, such as [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) or [Kiro](https://kiro.dev/), to convert database business logic for the application layer, such as conversion to Java.

Combine these automated analyses with manual review of business processes and domain knowledge to fully understand system coupling. This multi-faceted approach makes sure that both technical and business perspectives are considered in your decomposition strategy.

## What's the best way to document coupling and cohesion findings?
<a name="whats-the-best-way-to-document-coupling-and-cohesion-findings"></a>

Create comprehensive documentation that visualizes database relationships and usage patterns. The following are the types of assets that you can use to record your findings:
+ **Dependency matrices** – Map table dependencies and highlight high-coupling areas.
+ **Relationship diagrams** – Use ER diagrams to show schema connections and foreign key relationships.
+ **Table usage heat maps** – Visualize query frequency and data access patterns across tables.
+ **Transaction flow diagrams** – Document multi-table transactions and their boundaries.
+ **Domain boundary maps** – Outline potential service boundaries based on business domains.

Combine these artifacts in a document, and regularly update it as the decomposition progresses. For diagrams, you can use tools such as [draw.io](https://drawio-app.com/) or [Lucidchart](https://www.lucidchart.com/pages). Consider implementing a wiki for easy team access and collaboration. This multi-faceted documentation approach provides a clear, shared understanding of system coupling and cohesion.

## How do I prioritize which coupling issues to address first?
<a name="how-do-i-prioritize-which-coupling-issues-to-address-first"></a>

Prioritize coupling issues based on a balanced assessment of business and technical factors. Evaluate each issue against business impact (such as revenue and customer experience), technical risk (such as system stability and data integrity), implementation effort, and team capabilities. Create a prioritization matrix that scores each issue from 1-5 across these dimensions. This matrix helps you identify the most valuable opportunities with manageable risks.

Start with high-impact, low-risk changes that align with existing team expertise. This helps you build organizational confidence and momentum for more complex changes. This approach promotes realistic execution and maximizes business value. Regularly review and adjust the priorities to help maintain alignment with changing business needs and team capacity.

## How do I handle transactions that span multiple operations?
<a name="how-do-i-handle-transactions-that-span-multiple-operations"></a>

Handle multi-operation transactions through carefully designed service-level coordination. Implement saga patterns for complex distributed transactions. Break them into smaller, reversible steps that can be managed independently. For example, an order processing flow might be split into separate steps for inventory check, payment processing, and order creation, each with its own compensation mechanism.

Where possible, redesign operations to be more atomic, which reduces the need for distributed transactions. When distributed transactions are unavoidable, implement robust tracking and compensation mechanisms to promote data consistency. Monitor transaction completion rates and implement clear error recovery procedures to maintain system reliability.
