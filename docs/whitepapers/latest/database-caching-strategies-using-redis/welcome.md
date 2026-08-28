---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/welcome.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database Caching Strategies Using Redis
<a name="welcome"></a>

Publication date: **March 8, 2021** ([Document Revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 In-memory data caching can be one of the most effective strategies for improving your overall application performance and reducing your database costs.

 You can apply caching to any type of database, including relational databases (such as [*Amazon Relational Database Service*](https://aws.amazon.com/rds/) (Amazon RDS)) or NoSQL databases (such as [*Amazon DynamoDB*](https://aws.amazon.com/dynamodb/), [Amazon DocumentDB](https://aws.amazon.com/documentdb/) (with MongoDB compatibility), and [Amazon Keyspaces](https://aws.amazon.com/keyspaces/) (for Apache Cassandra)).

 One of the benefits of caching is that it’s an easier option to implement, and it dramatically improves the speed and scalability of your application. Caching can also apply to objects (for instance, objects stored in [Amazon Simple Storage Service](https://aws.amazon.com/s3/)), as this paper will explore.

 This whitepaper describes some of the caching strategies and implementation approaches that address the limitations and challenges associated with disk-based databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
