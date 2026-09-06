---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/understanding-migration-methods.html
---

# Understanding migration methods
<a name="understanding-migration-methods"></a>

You can choose from the following migration methods:
+ **Offline migration** – Your target database and corresponding application is offline for an extended period of time during an offline migration. During the database migration, users can't perform any transactions on the target database. Offline migration is ideal for development and testing in small, non-critical database environments.
+ **Online migration** – Your target database and corresponding application is offline for only a minimal time period during an online migration. During the database migration, users can perform transactions on the target database during a short window of time. Online migration is ideal for large, critical production databases.

For more information about offline and online migration methods, see [Choosing the right migration method](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-postgresql-planning/methods.html) in the *Migrating on-premises PostgreSQL databases to the AWS Cloud: pre-analysis and planning *guide.

**Note**
We recommend that you use the migration method that you shortlisted for production for at least one of your test databases. This can help you gain experience and troubleshoot issues in a test environment before you perform any operations on your production database.
