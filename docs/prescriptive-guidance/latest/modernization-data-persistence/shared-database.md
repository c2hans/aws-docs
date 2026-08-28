---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/shared-database.html
---

# Shared-database-per-service pattern
<a name="shared-database"></a>

In the shared-database-per-service pattern, the same database is shared by several microservices. You need to carefully assess the application architecture before adopting this pattern, and make sure that you avoid hot tables (single tables that multiple microservices write to). All your database changes must also be backward-compatible; for example, developers can drop columns or tables only if objects are not referenced by the current and previous versions of all microservices.

In the following illustration, an insurance database is shared by all the microservices and an IAM policy provides access to the database. This creates development time coupling; for example, a change in the "Sales" microservice needs to coordinate schema changes with the "Customer" microservice. This pattern does not reduce dependencies between development teams, and introduces runtime coupling because all microservices share the same database. For example, long-running "Sales" transactions can lock the "Customer" table and this blocks the "Customer" transactions.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/e134ff57-1cc8-4902-8ba9-b58c0dc1b6d6.png)

You should consider using this pattern if:
+ You don't want too much refactoring of your existing code base.
+ You enforce data consistency by using transactions that provide atomicity, consistency, isolation, and durability (ACID).
+ You want to maintain and operate only one database.
+ Implementing the database-per-service pattern is difficult because of interdependencies among your existing microservices.
+ You don't want to completely redesign your existing data layer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
