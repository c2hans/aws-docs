---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical.html
---

# Migrate from PostgreSQL on Amazon EC2 to Amazon RDS for PostgreSQL using pglogical
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical"></a>

*Rajesh Madiwale, Amazon Web Services*

## Summary
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical-summary"></a>

This pattern outlines steps for migrating a PostgreSQL database (version 9.5 and later) from Amazon Elastic Compute Cloud (Amazon EC2) to Amazon Relational Database Service (Amazon RDS) for PostgreSQL by using the PostgreSQL **pglogical **extension. Amazon RDS now supports the pglogical extension for PostgreSQL version 10.

## Prerequisites and limitations
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical-prereqs"></a>

**Prerequisites **
+ Choose the right type of Amazon RDS instance. For more information, see [Amazon RDS Instance Types](https://aws.amazon.com/rds/instance-types/).
+ Make sure that the source and target versions of PostgreSQL are the same.
+ Install and integrate the [**pglogical** extension with PostgreSQL](https://github.com/2ndQuadrant/pglogical) on Amazon EC2.

**Product versions**
+ PostgreSQL version 10 and later on Amazon RDS, with the features supported on Amazon RDS (see [PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts) in the AWS documentation). This pattern was tested by migrating PostgreSQL 9.5 to PostgreSQL version 10 on Amazon RDS, but it also applies to later versions of PostgreSQL on Amazon RDS.

## Architecture
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical-architecture"></a>

**Data migration architecture**

![Data migration architecture for PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/29af3931-48de-499f-9c4b-e10a98e4bba5/images/5f5b906f-dc1a-49a5-ae3f-3e10ae854784.png)

## Tools
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical-tools"></a>
+ [**pglogical**](https://github.com/2ndQuadrant/pglogical) extension
+ PostgreSQL native utilities: [**pg\_dump**](https://www.postgresql.org/docs/9.5/app-pgdump.html) and [**pg\_restore**](https://www.postgresql.org/docs/9.6/app-pgrestore.html)

## Epics
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical-epics"></a>

### Migrate data by using the pglogical extension
<a name="migrate-data-by-using-the-pglogical-extension"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon RDS PostgreSQL DB instance. | Set up a PostgreSQL DB instance in Amazon RDS. For instructions, see the [Amazon RDS for PostgreSQL documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html). | DBA |
| Obtain a schema dump from the source PostgreSQL database and restore it into the target PostgreSQL database. | 1. Use the [pg\_dump](https://www.postgresql.org/docs/11/backup-dump.html) utility  with the `-s` option to generate a schema file from the source database.<br />2. Use the [psql](https://www.postgresql.org/docs/11/app-psql.html) utility with the `-f` option to load the schema into the target database. | DBA |
| Turn on logical decoding. | In the Amazon RDS DB parameter group, set the `rds.logical_replication` static parameter to 1. For instructions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.FeatureSupport.LogicalDecoding). | DBA |
| Create the pglogical extension on the source and target databases. | 1. Create the `pglogical` extension on the source PostgreSQL database:<pre>psql -h <amazon-ec2-endpoint> -d target-dbname -U target-dbuser -c "create extension pglogical;"</pre><br />2. Create the `pglogical` extension on the target PostgreSQL database:<pre>psql -h <amazon-rds-endpoint> -d source-dbname -U source-dbuser -c "create extension pglogical;"</pre> | DBA |
| Create a publisher on the source PostgreSQL database. | To create a publisher, run:<pre>psql -d dbname -p 5432 <<EOF<br />SELECT pglogical.create_node( node_name := 'provider1', dsn := 'host=<ec2-endpoint> port=5432 dbname=source-dbname user=source-dbuser' );<br />EOF</pre> | DBA |
| Create a replication set, add tables and sequences. | To create a replication set on the source PostgreSQL database, and to add tables and sequences to the replication set, run:<pre>psql -d dbname -p 5432 <<EOF<br />SELECT pglogical.replication_set_add_all_tables('default', '{public}'::text[],synchronize_data := true);<br />EOF</pre> | DBA |
| Create a subscriber. | To create a subscriber on the target PostgreSQL database, run:<pre>psql -h <rds-endpoint> -d target-dbname -U target-dbuser  <<EOF<br />SELECT pglogical.create_node(<br />    node_name := 'subscriber1',<br />    dsn := 'host=<rds-endpoint> port=5432 dbname=target-dbname password=postgres user=target-dbuser'<br />);<br />EOF</pre> | DBA |
| Create a subscription. | To create a subscription on the target PostgreSQL database, run:<pre>psql -h <rds-endpoint> -d target -U postgres  <<EOF<br />SELECT pglogical.create_subscription(<br /> subscription_name := 'subscription1',<br /> replication_sets := array['default'],<br />    provider_dsn := 'host=<ec2-endpoint> port=5432 dbname=<source-dbname> password=<password> user=source-dbuser'<br />);</pre> | DBA |

### Validate your data
<a name="validate-your-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check source and target databases. | Check the source and target databases to confirm that data is being replicated successfully. You can perform basic validation by using `select count(1)` from the source and target tables. | DBA |

## Related resources
<a name="migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical-resources"></a>
+ [Amazon RDS](https://aws.amazon.com/rds/)
+ [Logical replication for PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication) (Amazon RDS documentation)
+ [pglogical](https://github.com/2ndQuadrant/pglogical) (GitHub repository)
+ [Limitations of pglogical](https://github.com/2ndQuadrant/pglogical#limitations-and-restrictions) (GitHub repository README file)
+ [Migrating PostgreSQL from on-premises or Amazon EC2 to Amazon RDS using logical replication](https://aws.amazon.com/blogs/database/migrating-postgresql-from-on-premises-or-amazon-ec2-to-amazon-rds-using-logical-replication/) (AWS Database blog)
