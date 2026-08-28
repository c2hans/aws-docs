---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.html
---

# Supported Regions and Aurora DB engines for IAM database authentication
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth"></a>

With IAM database authentication in Aurora, you can authenticate to your DB cluster using AWS Identity and Access Management (IAM) database authentication. With this authentication method, you don't need to use a password when you connect to a DB cluster. Instead, you use an authentication token. For more information, see [IAM database authentication ](UsingWithRDS.IAMDBAuth.md).

**Topics**
+ [IAM database authentication with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.amy)
+ [IAM database authentication with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.apg)

## IAM database authentication with Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.amy"></a>

IAM database authentication with Aurora MySQL is available in all Regions for the following versions:
+ Aurora MySQL 8.4 – All available versions
+ Aurora MySQL 3 – All available versions
+ Aurora MySQL 2 – All available versions

## IAM database authentication with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.apg"></a>

IAM database authentication with Aurora PostgreSQL is available in all Regions for the following engine versions:
+ Aurora PostgreSQL 17 – All available versions
+ Aurora PostgreSQL 16 – All available versions
+ Aurora PostgreSQL 15 – All available versions
+ Aurora PostgreSQL 14 – All available versions
+ Aurora PostgreSQL 13 – All available versions
+ Aurora PostgreSQL 12 – All available versions
+ Aurora PostgreSQL 11 – All available versions

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
