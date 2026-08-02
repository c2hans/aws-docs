---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/faq.html
---

# FAQ
<a name="faq"></a>

## How can I migrate from Oracle Database EE to Oracle Database SE2?
<a name="how-migrate"></a>

Migrating from Oracle Database EE to Oracle Database SE2 requires logical export of data from the Enterprise Edition database and import of the data into the Standard Edition 2 database instance. Use tools such as [Oracle Export/Import](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.ExportImport.html), [Oracle Data Pump](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.DataPump.html), or [Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.html) or [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) full load and change data capture (CDC) for reduced downtime.

## How can I downgrade my EE Oracle database to SE2 with minimum downtime?
<a name="how-downgrade"></a>

To reduce overall downtime, you can bulk load data into your SE2 database by using Oracle Export/Import. You can use logical replication tools such as AWS DMS or Oracle GoldenGate to synchronize your SE2 database.

## Can I have High Availability in my Amazon RDS for Oracle SE2 database?
<a name="ha"></a>

Amazon RDS currently uses synchronous replication technology and automatic failover functionality to provide [Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) deployments for Oracle DB instances. Multi-AZ deployments are available for all Oracle database editions supported by Amazon RDS.

## How can I monitor the performance of my Amazon RDS for Oracle SE2 database instance?
<a name="monitor"></a>

You can monitor your SE2 database instance using [Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/), [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html), and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html). You can also analyze database performance using Oracle Statspack in place of Oracle Automatic Workload Repository (AWR).

## Can I have encryption on my Amazon RDS for Oracle SE2 database instance?
<a name="encryption"></a>

Amazon RDS can [encrypt your Amazon RDS DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html). Data that is encrypted at rest includes the underlying storage for DB instances, its automated backups, read replicas, and snapshots. To turn on encryption in transit using [SSL encryption](https://docs.amazonaws.cn/en_us/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.html) for an Oracle DB instance, add the Oracle SSL option to the option group associated with the Oracle DB instance.

## What types of licensing options are available with Amazon RDS for Oracle?
<a name="license-types"></a>

There are two types of licensing options available for using Amazon RDS for Oracle:
+ **Bring Your Own License (BYOL)** – In this licensing model, you can use your existing Oracle Database licenses to run Oracle deployments on Amazon RDS. To run a DB instance under the BYOL model, you must have the appropriate Oracle Database license (with Software Update License and Support) for the DB instance class and Oracle Database edition that you want to run. You must also follow Oracle's [licensing policies](https://www.oracle.com/assets/cloud-licensing-070579.pdf) for Oracle Database software in the Amazon EC2 cloud computing environment. DB instances reside in the Amazon EC2 environment.
+ **License Included** – In the License Included service model, you do not need separately purchased Oracle licenses. The Oracle Database software has been licensed by AWS for your use subject to Section 10.3.1 of the [AWS Service Terms](https://aws.amazon.com/service-terms/). License Included pricing is inclusive of software, underlying hardware resources, and Amazon RDS management capabilities.

## Which Oracle Database editions are available with Amazon RDS for Oracle?
<a name="available-db"></a>

Amazon RDS currently supports the following Oracle Database editions under each of the licensing models:
+ **BYOL** – Enterprise Edition (EE), Standard Edition 2 (SE2)
+ **License Included** – Standard Edition 2 (SE2)

## What are the licensing policies for using Amazon RDS for Oracle?
<a name="license-policies"></a>
+ **BYOL** – To run a DB instance under the BYOL model, you must have the appropriate Oracle Database license (with Software Update License and Support) for the DB instance class and Oracle Database edition you want to run. You must also follow Oracle's [licensing policies](https://www.oracle.com/us/corporate/pricing/cloud-licensing-070579.pdf) for Oracle Database software in the Amazon EC2 cloud computing environment. DB instances reside in the Amazon EC2 environment.
+ **License Included** – In the License Included service model, you do not need separately purchased Oracle licenses. The Oracle Database software has been licensed by AWS for your use subject to Section 10.3.1 of the [AWS Service Terms](https://aws.amazon.com/service-terms/). License Included pricing is inclusive of software, underlying hardware resources, and Amazon RDS management capabilities.

## How is Amazon RDS for Oracle supported?
<a name="support"></a>
+ **BYOL** – Under this model, you continue to use your active Oracle support account and contact Oracle directly for Oracle Database specific service requests. If you have an active AWS Support account, you can contact AWS Support for Amazon RDS specific issues. Amazon Web Services and Oracle have a multiple-vendor support process for cases that require assistance from both organizations.
+ **License Included** – In this model, if you have an active AWS Support account, you should contact AWS Support for both Amazon RDS and Oracle Database specific service requests.

## How does the license option affect DB instance scaling?
<a name="scaling"></a>
+ **BYOL** – You can scale your DB instances in accordance with the terms of your Oracle licenses.
+ **License Included** – DB instances that are running Oracle can be scaled up and down at any point, subject to the prevailing hourly pricing for each DB instance class.

For more information on the scaling implications of Reserved DB instances, see [Reserved DB instances for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html).

## How does the license option affect version upgrades?
<a name="upgrades"></a>
+ **BYOL** – To use Amazon RDS for Oracle, you should have Software Update License and Support from Oracle.
+ **License Included** – The cost of the Software Update License is embedded in the hourly price, enabling access to Oracle Database software updates.

## Can I change the licensing option for my DB instance (for example, from BYOL to License Included)?
<a name="change-license"></a>

Yes, you can change your license options through the AWS Command Line Interface (AWS CLI) or through the AWS Management Console. On the Console, choose **Modify Instance**, and select the appropriate option in the **Licensing Model** dropdown list.
