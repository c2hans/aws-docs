---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/pl-sql.html
---

# Step 2. Collect PL/SQL objects and sizing
<a name="pl-sql"></a>

In this step, you collect another attribute that is critical to identifying good candidates for database migrations: the number of PL/SQL objects and sizing (per schema). This data attribute is important because PL/SQL objects typically require manual code conversion, thus increasing the time and complexity of migration. Start with the top 10% of databases from [step 1](cmdb.md) (adjust this percentage to suit your needs). Query this list for PL/SQL object counts as well as database versions, database editions, and ports to validate data. We recommend that you automate this step by using a script, because you will run this process multiple times as you iterate through the full database candidate list.

The [appendix](appendix.md) to this guide provides sample queries for Oracle and SQL Server databases. You can wrap these queries in a script to collect the necessary data. To optimize, create a common user across all databases.

Continue iterating through the remaining list, and reprioritize the database candidates based on the object count and database size, in ascending order for both, to prioritize database candidates for [step 3](sct.md). Format the list as a comma-separated value (CSV) file in preparation for the next step.

![Criteria for filtering databases based on PL/SQL object counts](https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/images/guide-img/d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2/images/4bf9d277-b941-4be3-9ad3-571aeb904ff4.png)
