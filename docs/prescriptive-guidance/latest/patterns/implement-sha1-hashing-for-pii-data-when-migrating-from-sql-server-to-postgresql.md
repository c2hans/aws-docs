---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql.html
---

# Implement SHA1 hashing for PII data when migrating from SQL Server to PostgreSQL
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql"></a>

*Rajkumar Raghuwanshi and Jagadish Kantubugata, Amazon Web Services*

## Summary
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-summary"></a>

This pattern describes how to implement Secure Hash Algorithm 1 (SHA1) hashing for email addresses when migrating from SQL Server to either Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL-Compatible. An email address is an example of *personally identifiable information* (PII). PII is information that, when viewed directly or paired with other related data, can be used to reasonably infer the identity of an individual.

This pattern covers the challenges of maintaining consistent hash values across different database collations and character encodings, and provides a solution using PostgreSQL functions and triggers. Although this pattern focuses on SHA1 hashing, it can be adapted for other hashing algorithms supported by PostgreSQL's `pgcrypto` module. Always consider the security implications of your hashing strategy and consult with security experts if handling sensitive data.

## Prerequisites and limitations
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Source SQL Server database
+ Target PostgreSQL database (Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible)
+ PL/pgSQL coding expertise

**Limitations**
+ This pattern requires database-level collation changes based on use cases.
+ The performance impact on large datasets has not been evaluated.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Microsoft SQL Server 2012 or later

## Architecture
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-architecture"></a>

**Source technology stack **
+ SQL Server
+ .NET Framework

**Target technology stack **
+ PostgreSQL
+ `pgcrypto` extension

**Automation and scale**
+ Consider implementing the hashing function as a stored procedure for easier maintenance.
+ For large datasets, evaluate performance and consider batch processing or indexing strategies.

## Tools
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service Amazon RDS for PostgreSQL ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)helps you set up, operate, and scale a PostgreSQL relational database in the AWS Cloud.
+ [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) supports heterogeneous database migrations by automatically converting the source database schema and a majority of the custom code to a format that’s compatible with the target database.

**Other tools**
+ [pgAdmin](https://www.pgadmin.org/) is an open source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.
+ [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms) is an integrated environment for managing any SQL infrastructure.

## Best practices
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-best-practices"></a>
+ Use appropriate collation settings for handling special characters on the target database side.
+ Test thoroughly with a variety of email addresses, including addresses with non-ASCII characters.
+ Maintain consistency in uppercase and lowercase handling between the application and database layers.
+ Benchmark performance of queries using the hashed values.

## Epics
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-epics"></a>

### Analyze source hashing implementation
<a name="analyze-source-hashing-implementation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review SQL Server code. | To review SQL Server code that generates SHA1 hashes, do the following:+ Analyze the existing SQL Server implementation of SHA1 hashing.<br />+ Identify the exact methods used for hash generation.<br />+ Document the input parameters and output format.<br />+ Review any data type conversions or transformations.<br />+ Examine collation settings and their impact. | Data engineer, DBA, App developer |
| Document the hashing algorithm and data transformations. | To document the exact hashing algorithm and data transformations, do the following:+ Create detailed technical documentation of the hashing process.<br />+ Document the step-by-step transformation logic.<br />+ Specify input and output formats and data types.<br />+ Include edge cases and special character handling. | App developer, Data engineer, DBA |

### Create PostgreSQL hashing function
<a name="create-postgresql-hashing-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create `pgcrypto` extension. | To create the `pgcrypto` extension, use `pgAdmin/psql` to run the following command:<pre>CREATE EXTENSION pgcrypto;</pre> | DBA, Data engineer |
| Implement a PostgreSQL function. | Implement the following PostgreSQL function to replicate the SQL Server hashing logic. At a high level, this function uses the following steps:1. Optionally converts the input to uppercase.<br />2. Creates an SHA1 hash of the input.<br />3. Takes the last 10 bytes (80 bits) of this hash.<br />4. Converts these bytes to a 64-bit integer.<pre>CREATE OR REPLACE FUNCTION utility.hex_to_bigint ( <br />     par_val character varying, <br />     par_upper character varying DEFAULT 'lower'::character varying) <br />RETURNS bigint <br />LANGUAGE 'plpgsql' <br />AS $BODY$ <br />DECLARE <br />    retnumber bigint; <br />    digest_bytes bytea;<br />BEGIN <br />    if lower(par_upper) = 'upper' <br />    then <br />        digest_bytes := digest(upper(par_val), 'sha1');<br />    else <br />        digest_bytes := digest((par_val), 'sha1');<br />    end if; <br />    retnumber := ('x' || encode(substring(digest_bytes, length(digest_bytes)-10+1), 'hex'))::bit(64)::bigint; <br />    RETURN retnumber; <br />END; <br />$BODY$;</pre> | Data engineer, DBA, App developer |
| Test the function. | To test the function, use sample data from SQL Server to verify matching hash values. Run the following command:<pre>select 'alejandro_rosalez@example.com' as Email, utility.hex_to_bigint('alejandro_rosalez@example.com','upper') as HashValue;<br /><br />--OUTPUT<br />/*<br />email 	        hashvalue<br />"alejandro_rosalez@example.com"	451397011176045063<br />*/<br /></pre> | App developer, DBA, Data engineer |

### Implement triggers for automatic hashing
<a name="implement-triggers-for-automatic-hashing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create triggers on relevant tables. | To create triggers on relevant tables to automatically generate hash values on insert or update, run the following command:<pre>CREATE OR REPLACE FUNCTION update_email_hash() <br />RETURNS TRIGGER <br />AS $$ <br />BEGIN <br />    NEW.email_hash = utility.hex_to_bigint(NEW.email, 'upper'); <br />    RETURN NEW; <br />END; <br />$$ LANGUAGE plpgsql;</pre><pre>CREATE TRIGGER email_hash_trigger BEFORE INSERT OR UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_email_hash();</pre> | App developer, Data engineer, DBA |

### Migrate existing data
<a name="migrate-existing-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Develop a migration script or use AWS DMS.  | Develop a migration script or use AWS DMS to populate hash values for existing data (including hash values stored as `BIGINT` in the source system.) Complete the following tasks:+ Create migration scripts for data transfer with hash values.<br />+ Configure AWS DMS tasks with appropriate transformation rules.<br />+ Set up source and target endpoints in AWS DMS.<br />+ Implement error handling and logging mechanisms.<br />+ Design a batch processing strategy for large datasets.<br />+ Create validation queries for data verification. | Data engineer, App developer, DBA |
| Use the new PostgreSQL hashing function. | To use the new PostgreSQL hashing function to ensure consistency, do the following:+ Implement validation procedures to verify hash consistency.<br />+ Create comparison scripts between the source and target systems.<br />+ Set up automated testing for hash value verification.<br />+ Document any discrepancies and resolution steps. | App developer, DBA, DevOps engineer |

### Update application queries
<a name="update-application-queries"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify application queries. | To identify application queries that use hashed values, do the following:+ Analyze the application codebase for queries using hash values.<br />+ Review stored procedures and functions that reference hash operations.<br />+ Document query performance metrics and execution plans.<br />+ Identify dependencies on hash-based lookups.<br />+ Map out affected application components. | App developer, DBA, Data engineer |
| Modify queries. | If necessary, modify queries to use the new PostgreSQL hashing function. Do the following:+ Refactor existing queries to use the PostgreSQL hashing function.<br />+ Update stored procedures and functions.<br />+ Implement and test new query patterns.<br />+ Optimize modified queries for performance. | App developer, DBA, Data engineer |

### Test and validate
<a name="test-and-validate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform testing. | To perform thorough testing with a subset of production data, do the following:+ Create a test plan for data subset validation.<br />+ Extract representative sample of production data.<br />+ Set up a test environment with proper configurations.<br />+ Execute data loading and transformation tests.<br />+ Perform volume and stress testing. | App developer, Data engineer, DBA |
| Validate that hash values match. | To validate that hash values match between SQL Server and PostgreSQL, do the following:+ Develop comparison scripts for hash values.<br />+ Create validation reports for hash matching.<br />+ Implement automated verification procedures.<br />+ Document any discrepancies found.<br />+ Analyze and resolve hash mismatches. | App developer, Data engineer, DBA |
| Verify application functionality. | To verify application functionality by using the migrated data and the new hashing implementation, do the following:+ Execute end-to-end application testing.<br />+ Validate all application features using hashed data.<br />+ Test application performance with the new implementation.<br />+ Verify API integrations and dependencies. | App developer, DBA, Data engineer |

## Troubleshooting
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Hash values don’t match. | Verify character encodings and collations between source and target. For more information, see [Manage collation changes in PostgreSQL on Amazon Aurora and Amazon RDS](https://aws.amazon.com/blogs/database/manage-collation-changes-in-postgresql-on-amazon-aurora-and-amazon-rds/) (AWS Blog). |

## Related resources
<a name="implement-sha1-hashing-for-pii-data-when-migrating-from-sql-server-to-postgresql-resources"></a>

**AWS Blogs**
+ [Manage collation changes in PostgreSQL on Amazon Aurora and Amazon RDS](https://aws.amazon.com/blogs/database/manage-collation-changes-in-postgresql-on-amazon-aurora-and-amazon-rds/)
+ [Migrate SQL Server to Amazon Aurora PostgreSQL using best practices and lessons learned from the field](https://aws.amazon.com/blogs/database/migrate-sql-server-to-amazon-aurora-postgresql-using-best-practices-and-lessons-learned-from-the-field/)

**Other resources**
+ [PostgreSQL pgcrypto module](https://www.postgresql.org/docs/current/pgcrypto.html) (PostgreSQL documentation)
+ [PostgreSQL trigger functions](https://www.postgresql.org/docs/current/plpgsql-trigger.html) (PostgreSQL documentation)
+ [SQL Server HASHBYTES function](https://docs.microsoft.com/en-us/sql/t-sql/functions/hashbytes-transact-sql) (Microsoft documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
