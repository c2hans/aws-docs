---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/introduction.html
---

# Optimizing PostgreSQL query performance
<a name="introduction"></a>

*Veeranjaneyulu Grandhi, Tirumala Dasari, Vamsikrishna Jammula, Srinivas Potlachervoo, and Naga Srinivas Reddy Ravulapati, Amazon Web Services*

PostgreSQL is an open source object-relational database system that is powerful, flexible, and reliable. There are many ways to optimize the performance of a PostgreSQL query. The process of optimizing the query depends on the use case. Knowing the current query plan can help you to identify and understand any issues and make the necessary changes. Sometimes, you might need to analyze the tables to keep the database statistics up to date. The PostgreSQL optimizer will use those statistics to run the query faster. This guide focuses on best practices for improving the performance of PostgreSQL queries.

This guide assumes that you have an existing Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon Aurora PostgreSQL-Compatible database instance.

## Use cases for query performance tuning
<a name="use-cases"></a>

This guide covers five use cases, with explanations and examples:
+ Collations
+ Data type mismatch
+ Function call in the `SELECT` statement
+ `IN` or `EXISTS`
+ Subqueries or Common Table Expressions (CTEs)

Each use case provides details of the initial run plan, how to analyze the plan to identify the problem, and a solution. Implementing these use cases typically results in faster response times for queries, reduced load on the server, and overall enhanced system efficiency. Those improvements can lead to a better user experience and increased system reliability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
