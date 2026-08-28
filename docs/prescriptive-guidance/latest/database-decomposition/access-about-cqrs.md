---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/access-about-cqrs.html
---

# Controlling access with the CQRS pattern
<a name="access-about-cqrs"></a>

Another pattern that you can use to isolate external systems that connect to this central database is *command query responsibility segregation (CQRS)*. If some of the external systems are connecting to your central database primarily for reads, such as analytics, reporting, or other read-intensive operations, you can create separate read-optimized data stores.

This pattern effectively isolates these external systems from the impacts of database decomposition and schema changes. By maintaining dedicated read replicas or purpose-built data stores for specific query patterns, teams can continue their operations without being affected by changes in the primary database structure. For example, while you decompose your monolithic database, reporting systems can continue to work with their existing data views, and analytical workloads can maintain their current query patterns through dedicated analytical stores. This approach provides technical isolation and enables organizational autonomy because different teams can evolve their systems independently without tight coupling to the primary database's transformation journey.

![External system accessing a read replica instead of the monolithic database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/images/guide-img/6bdbec4e-98b8-4cd1-adda-f196258cf753/images/e7ceafc0-3563-4a3b-8cfe-c738a0ab3fa2.png)

For more information about this pattern and an example of its use to decouple table relationships, see [CQRS pattern](joins.md#joins-cqrs) later in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
