---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/database-schema-changes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database schema changes
<a name="database-schema-changes"></a>

 It’s common for modern software to have a database layer. While we do not recommend the use of relational DBs for new projects due to scaling and other issues, many existing projects use relational database technology and would like to adopt CI/CD. When a relational database is used, it’s often necessary to modify the database in the continuous delivery process. Handling changes in a relational database requires special consideration, and it offers other challenges than the ones present when deploying application binaries. Usually, when you upgrade an application binary, you stop the application, upgrade it, and then start it again. You don't really bother about the application state, which is handled outside of the application.

 When upgrading databases, you do need to consider the state because a database contains much state but comparatively little logic and structure.

 The database schema before and after a change is applied should be considered as different versions of the database. You could use tools such as Liquibase and Flyway to manage the versions.

 In general, these tools employ some variant of the following methods:
+  Add a table to the database where a database version is stored.
+  Keep track of database change commands and bunch them together in versioned change sets. In the case of Liquibase, these changes are stored in XML files. Flyway employs a slightly different method where the change sets are handled as separate SQL files or occasionally as separate Java classes for more complex transitions.
+  When Liquibase is being asked to upgrade a database, it looks at the metadata table and determines which change sets to run in order to bring the database up-to-date with the latest version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
