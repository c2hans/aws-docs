---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/considerations-for-running-oracle-ebs-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Considerations for running Oracle E-Business Suite on AWS
<a name="considerations-for-running-oracle-ebs-on-aws"></a>

There are a number of considerations for running Oracle E-Business Suite on AWS.

## Sizing
<a name="sizing"></a>

 It is important to right size the Oracle E-Business Suite environment while migrating to AWS, because it can save on infrastructure costs and licensing. Right sizing also gives your business users adequate performance from Oracle E-Business Suite on the cloud.

 Migration to the cloud is also an opportunity to fix long-term outstanding issues that you might be having in your current Oracle E-Business Suite environment. Following are a few questions that you should ask your IT team when sizing Oracle E-Business Suite on AWS.
+  When are the peak periods of usage? (such as period close, batch data load, and so on.)
+  What is the pattern of load and spikes on the system? Is it due to transactional or batch load?
+  What is the number of named and concurrent users in the source system and their usage profile?
+  How much business data has to be retained in the system online?
+  What is the percentage of storage growth year-over-year?
+  How many reporting jobs are there? Can those be offloaded to a read-only standby database created using Oracle Active Data Guard?
+  What is the response time requirement from the system?
+  What are the workload requirements from a storage perspective, in terms of peak an average IOPS and throughput?
+  Are there any outliers in terms of jobs/concurrent programs – especially customizations that are causing unnecessary high peaks, and are candidates for tuning?

 Getting answers to these questions will help you right size your Oracle E-Business Suite instance, and allow selection of the right deployment topology.

## Throughput requirements
<a name="throughput-requirements"></a>

 Throughput is another important factor when selecting the compute for the database-tier instance. Throughput determines how much data can be read or written to the disk per second by the compute OS. Consider measuring throughput during events such as period end close while multiple concurrent batch jobs are performing intensive read and write operations.

 For Oracle RAC workloads, you will have to combine the throughput from all RAC instances when moving to non-RAC based deployment on AWS. Customers can select from a variety of compute instance and storage types that provide highly optimized levels of IOPS and throughput.

## Integrations with on-premises services
<a name="integrations-with-on-premises-services"></a>

 When migrating Oracle E-Business Suite on AWS, you may have the following integration services:
+  Single sign-on
  +  Enterprise-wide single sign-on with Microsoft Active Directory
  +  Integration with [Okta](https://www.okta.com/)
+  Microsoft SharePoint
+  Oracle E-Business Suite B2B integration using file-based transfers, such as FTP and HTTP.
+  Integrating with CRM/ERP systems such as Salesforce and SAP.
+  Message queue-based integration using [Apache Kafka](https://kafka.apache.org/), [IBM MQ](https://www.ibm.com/products/mq), and so on with Oracle E-Business Suite.

 Consider the effort involved in services integration, and follow relevant support articles from [MyOracleSupport](https://support.oracle.com/) to integrate with these applications and third-party services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
