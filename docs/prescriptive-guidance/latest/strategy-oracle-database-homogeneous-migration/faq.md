---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/faq.html
---

# FAQ
<a name="faq"></a>

## Q: Is it possible to migrate Oracle Database Enterprise Edition running on premises to Oracle Database Standard Edition 2 on Amazon RDS for Oracle or on Amazon EC2?
<a name="q--is-it-possible-to-migrate-oracle-database-enterprise-edition-running-on-premises-to-oracle-database-standard-edition-2-on-9999999999999999rdslongora--or-on-9999999999999999ec2--.e17716c8-ccd9-5239-9ca0-21c843f30a43"></a>

**A:** Yes. You must analyze the Enterprise Edition features that you're using, such as Transparent Data Encryption (TDE) or Advanced Compression, and determine whether you need those features on the target Oracle database. For information about other features, see the AWS Prescriptive Guidance guide [Evaluate downgrading Oracle databases to Standard Edition 2 on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/welcome.html).

## Q: Can we use a mixed approach such as AWS DMS and Oracle Data Pump together to migrate existing data?
<a name="q--can-we-use-a-mixed-approach-such-as-9999999999999999dms--and-oracle-data-pump-together-to-migrate-existing-data-.0260cb5a-4b25-516f-947d-7aea372a4a14"></a>

**A:** Yes. We recommend that you use AWS DMS for large object (LOB) column migration and Oracle Data Pump for non-LOB column tables.

## Q: Can we use AWS DMS and Oracle Data Pump together for near zero downtime migration?
<a name="q--can-we-use-9999999999999999dms--and-oracle-data-pump-together-for-near-zero-downtime-migration-.a9ef5998-547d-5cc5-84cd-6dd96d3ce35f"></a>

**A:** Yes, you can use Oracle Data Pump to migrate an existing database, and then use AWS DMS to replicate only ongoing changes, starting from a specific system change number (SCN) that was recorded before using Oracle Data Pump.

## Q: How can we use Oracle GoldenGate to enable active-active database replication and disaster recovery?
<a name="q--how-can-we-use-oracle-goldengate-to-enable-active-active-database-replication-and-disaster-recovery-.6604dc6f-3a12-5bb9-8fec-40b81524ae38"></a>

**A:** Use an additional GoldenGate hub, either on premises or on the EC2 instance. The GoldenGate hub moves transaction information from the source database to the target database.

## Q: How can we determine whether Amazon RDS for Oracle will be suitable as the target database?
<a name="q--how-can-we-determine-whether-9999999999999999rdslongora--will-be-suitable-as-the-target-database-.8a55560c-9b98-51c2-b738-3c754cde0a16"></a>

**A:** Make sure that all required features are supported on the target Amazon RDS for Oracle database. For more information, see [RDS for Oracle features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.FeatureSupport.html) in the Amazon RDS documentation.

## Q: How can I get common DBA operations such as the alter command to work in the target Amazon RDS for Oracle database?
<a name="q--how-can-i-get-common-dba-operations-such-as-the-alter-command-to-work-in-the-target-9999999999999999rdslongora--database-.d85d28f6-c2df-5e7f-b201-19d799e9a8e8"></a>

**A:** To administer the database, see the [list of commands that work differently](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html) in Amazon RDS for Oracle.

## Q: Can I use Oracle Data Guard to migrate ongoing replication changes to Amazon RDS for Oracle?
<a name="q--can-i-use-oracle-data-guard-to-migrate-ongoing-replication-changes-to-9999999999999999rdslongora--.fac74735-a80c-59a2-a29a-382b1ed6bf3e"></a>

**A:** No. You can use Oracle Data Guard only for Oracle on Amazon EC2 or Amazon RDS Custom for Oracle targets.

## Q: Will AWS help me align the deployment of the AWS service with my existing Oracle agreements?
<a name="q--will-9999999999999999aws--help-me-align-the-deployment-of-the-9999999999999999aws-service--with-my-existing-oracle-agreements-.1a2303ee-be93-5bbe-9649-2191e72d766b"></a>

**A:** No. An [AWS Partner](https://aws.amazon.com/partners/work-with-partners/) can help you address Oracle to AWS license deployment questions. For more information, see the AWS blog post [Understanding Your Options for Deploying and Licensing Oracle on AWS](https://aws.amazon.com/blogs/apn/understanding-your-options-for-deploying-and-licensing-oracle-on-aws/).

## Q: What will happen to my target Amazon RDS for Oracle instance if Oracle ends Extended Support for the database version? (For example, Oracle Database version 19c Extended Support ends on December 31, 2032.)
<a name="q--what-will-happen-to-my-target-9999999999999999rdslongora--instance-if-oracle-ends-extended-support-for-the-database-version---for-example--oracle-database-version-19c-extended-support-ends-on-december-31--2032.-.a461d720-5b97-5e59-80a0-860aa8a4872a"></a>

**A:** Using the same example, starting on January 1, 2033, all instances that are running on Oracle Database version 19c will be automatically upgraded to 21c. Also, you won't be able to create Amazon RDS for Oracle instances with Oracle Database version 19c.

## Q: Can I use Oracle Exadata features such as SmartScan in Amazon RDS for Oracle?
<a name="q--can-i-use-oracle-exadata-features-such-as-smartscan-in-9999999999999999rdslongora--.22dd04b7-71ad-57db-9c61-b13ff181b411"></a>

**A:** Amazon RDS for Oracle doesn't support the SmartScan feature. In your on-premises database, you need to identify the queries that use SmartScan and convert them to use database indexes instead.

## Q: How can I analyze my workload to determine the IOPs, throughput, CPU, and memory that is actively being used by the source Oracle database?
<a name="q--how-can-i-analyze-my-workload-to-determine-the-iops--throughput--cpu--and-memory-that-is-actively-being-used-by-the-source-oracle-database-.270b9414-9868-5bb7-bc56-31c5cc6cdaa0"></a>

**A:** Generate an [Automatic Workload Repository (AWR)](https://www.oracle.com/technetwork/database/manageability/diag-pack-ow09-133950.pdf) report from your source database or run a [Database Current State Investigation (CSI)](https://dbcsi.d29q8g3b9hzyur.amplifyapp.com/) script to get this information.
