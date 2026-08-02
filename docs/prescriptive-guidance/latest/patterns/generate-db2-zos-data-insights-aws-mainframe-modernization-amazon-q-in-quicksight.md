---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html
---

# Generate Db2 z/OS data insights by using AWS Mainframe Modernization and Amazon Q in Quick Sight
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight"></a>

*Shubham Roy, Roshna Razack, and Santosh Kumar Singh, Amazon Web Services*

## Summary
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-summary"></a>

Note: AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

If your organization is hosting business-critical data in an IBM Db2 mainframe environment, gaining insights from that data is crucial for driving growth and innovation. By unlocking mainframe data, you can build faster, secure, and scalable business intelligence to accelerate data-driven decision-making, growth, and innovation in the Amazon Web Services (AWS) Cloud.

This pattern presents a solution for generating business insights and creating sharable narratives from mainframe data in IBM Db2 for z/OS tables. Mainframe data changes are streamed to [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) topic using [AWS Mainframe Modernization Data Replication with Precisely](https://docs.aws.amazon.com/m2/latest/userguide/precisely.html). Using [Amazon Redshift streaming ingestion](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html), Amazon MSK topic data is stored in [Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html) data warehouse tables for analytics in Amazon Quick Sight.

After the data is available in Quick Sight, you can use natural language prompts with [Amazon Q in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-gen-bi.html) to create summaries of the data, ask questions, and generate data stories. You don't have to write SQL queries or learn a business intelligence (BI) tool.

**Business context**

This pattern presents a solution for mainframe data analytics and data insights use cases. Using the pattern, you build a visual dashboard for your company's data. To demonstrate the solution, this pattern uses a health care company that provides medical, dental, and vision plans to its members in the US. In this example, member demographics and plan information are stored in the IBM Db2 for z/OS data tables. The visual dashboard shows the following:
+ Member distribution by region
+ Member distribution by gender
+ Member distribution by age
+ Member distribution by plan type
+ Members who have not completed preventive immunization

For examples of member distribution by region and members who have not completed preventive immunization, see the Additional information section.

After you create the dashboard, you generate a data story that explains the insights from the previous analysis. The data story provides recommendations for increasing the number of members who have completed preventive immunizations.

## Prerequisites and limitations
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-prereqs"></a>

**Prerequisites**
+ An active AWS account. This solution was built and tested on Amazon Linux 2 on Amazon Elastic Compute Cloud (Amazon EC2).
+ An virtual private cloud (VPC) with a subnet that can be accessed by your mainframe system.
+ A mainframe database with business data. For the example data used to build and test this solution, see the *Attachments* section.
+ Change data capture (CDC) enabled on the Db2 z/OS tables. To enable CDC on Db2 z/OS, see the [IBM documentation](https://www.ibm.com/docs/en/daafz/7.5?topic=cdc-enabling-data-capture-changes).
+ Precisely Connect CDC for z/OS installed on the z/OS system that's hosting the source databases. The Precisely Connect CDC for z/OS image is provided as a zip file within the [AWS Mainframe Modernization - Data Replication for IBM z/OS](https://aws.amazon.com/marketplace/pp/prodview-doe2lroefogia?applicationId=AWSMPContessa&ref_=beagle&sr=0-1) Amazon Machine Image (AMI). To install Precisely Connect CDC for z/OS on the mainframe, see the [Precisely installation documentation](https://help.precisely.com/r/AWS-Mainframe-Modernization/Latest/en-US/AWS-Mainframe-Modernization-Data-Replication-for-IBM-z/OS/Install-Precisely-Connect-CDC-z/OS).

**Limitations**
+ Your mainframe Db2 data should be in a data type that's supported by Precisely Connect CDC. For a list of supported data types, see the [Precisely Connect CDC documentation](https://help.precisely.com/r/AWS-Mainframe-Modernization/Latest/en-US/AWS-Mainframe-Modernization-Data-Replication-for-IBM-z/OS/Data-replication-overview/Supported-source-data-types).
+ Your data at Amazon MSK should be in a data type that's supported by Amazon Redshift. For a list of supported data types, see the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html).
+ Amazon Redshift has different behaviors and size limits for different data types. For more information, see the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html#materialized-view-streaming-ingestion-limitations).
+ The near real-time data in Quick Sight depends on the refresh interval set for the Amazon Redshift database.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). Amazon Q in Quick Sight is currently not available in every Region that supports Quick Sight. For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ AWS Mainframe Modernization Data Replication with Precisely version 4.1.44
+ Python version 3.6 or later
+ Apache Kafka version** **3.5.1

## Architecture
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-architecture"></a>

**Target architecture**

The following diagram shows an architecture for generating business insights from mainframe data by using [AWS Mainframe Modernization Data Replication with Precisely](https://aws.amazon.com/mainframe-modernization/capabilities/data-replication/) and Amazon Q in Quick Sight.

![Seven-step process from z/OS mainframe to Amazon QuickSight.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/cddb6d20-14ae-4276-90d8-14df435db824.png)

The diagram shows the following workflow:

1. The Precisely Log Reader Agent reads data from Db2 logs and writes the data into transient storage on an OMVS file system on the mainframe.

1. The Publisher Agent reads the raw Db2 logs from transient storage.

1. The on-premises controller daemon authenticates, authorizes, monitors, and manages operations.

1. The Apply Agent is deployed on Amazon EC2 by using the preconfigured AMI. It connects with the Publisher Agent through the controller daemon by using TCP/IP. The Apply Agent pushes data to Amazon MSK using multiple workers for high-throughput.

1. The workers write the data to the Amazon MSK topic in JSON format. As the intermediate target for the replicated messages, Amazon MSK provides the highly available and automated failover capabilities.

1. Amazon Redshift streaming ingestion provides low-latency, high-speed data ingestion from Amazon MSK to an Amazon Redshift Serverless database. A stored procedure in Amazon Redshift performs the mainframe change data (insert/update/deletes) reconciliation into Amazon Redshift tables. These Amazon Redshift tables serves as the data analytics source for Quick Sight.

1. Users access the data in Quick Sight for analytics and insights. You can use Amazon Q in Quick Sight to interact with the data by using natural language prompts.

## Tools
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them out or in.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) is a fully managed service that helps you build and run applications that use Apache Kafka to process streaming data.
+ [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data in a single dashboard. This pattern uses the generative BI capabilities of Amazon Q in Quick Sight.
+ [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/) is a serverless option of Amazon Redshift that makes it more efficient to run and scale analytics in seconds without the need to set up and manage data warehouse infrastructure.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.

**Other tools**
+ [Precisely Connect CDC](https://support.precisely.com/products/connect-cdc-formerly-sqdata/) collects and integrates data from legacy systems into cloud and data platforms.

**Code repository**

The code for this pattern is available in the GitHub [Mainframe\_DataInsights\_change\_data\_reconciliation](https://github.com/aws-samples/Mainframe_DataInsights_change_data_reconcilition) repository. The code is a stored procedure in Amazon Redshift. This stored procedure reconciles mainframe data changes (inserts, updates, and deletes) from Amazon MSK into the Amazon Redshift tables. These Amazon Redshift tables serve as the data analytics source for Quick Sight.

## Best practices
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-best-practices"></a>
+ Follow [best practices](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html) while setting up your Amazon MSK cluster.
+ Follow Amazon Redshift [data parsing best practices](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html#materialized-view-streaming-recommendations) for improving performance.
+ When you create the AWS Identity and Access Management (IAM) roles for the Precisely setup, follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-epics"></a>

### Set up AWS Mainframe Modernization Data Replication with Precisely on Amazon EC2
<a name="set-up-m2long-data-replication-with-precisely-on-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a security group. | To connect to the controller daemon and the Amazon MSK cluster, [create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/creating-security-groups.html) for the EC2 instance. Add the following inbound and outbound rules:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html)<br />Note the name of the security group. You will need to reference the name when you launch the EC2 instance and configure the Amazon MSK cluster. | DevOps engineer, AWS DevOps |
| Create an IAM policy and an IAM role. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | DevOps engineer, AWS systems administrator |
| Provision an EC2 instance. | To provision an EC2 instance to run Precisely CDC and connect to Amazon MSK, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | AWS administrator, DevOps engineer |

### Set up Amazon MSK
<a name="set-up-msk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Amazon MSK cluster. | To create an Amazon MSK cluster, do the following :[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html)<br />A typical provisioned cluster takes up to 15 minutes to create. After the cluster is created, its status changes from **Creating** to **Active**. | AWS DevOps, Cloud administrator |
| Set up SASL/SCRAM authentication. | To set up SASL/SCRAM authentication for an Amazon MSK cluster, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Cloud architect |
| Create the Amazon MSK topic. | To create the Amazon MSK topic, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Cloud administrator |

### Configure the Precisely Apply Engine on Amazon EC2
<a name="configure-the-precisely-apply-engine-on-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the Precisely scripts to replicate data changes. | To set up the Precisely Connect CDC scripts to replicate changed data from the mainframe to the Amazon MSK topic, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html)<br />For example .ddl files, see the [Additional information](#generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-additional) section. | App developer, Cloud architect |
| Generate the network ACL key. | To generate the network access control list (network ACL) key, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Cloud architect, AWS DevOps |

### Prepare the mainframe source environment
<a name="prepare-the-mainframe-source-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure defaults in the ISPF screen. | To configure default settings in the Interactive System Productivity Facility (ISPF), follow the instructions in the [Precisely documentation](https://help.precisely.com/r/AWS-Mainframe-Modernization/Latest/en-US/AWS-Mainframe-Modernization-Data-Replication-for-IBM-z/OS/Install-Precisely-Connect-CDC-z/OS/Start-ISPF-Panel-Interface). | Mainframe system administrator |
| Configure the controller daemon. | To configure the controller daemon, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Mainframe system administrator |
| Configure the publisher. | To configure the publisher, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Mainframe system administrator |
| Update the daemon configuration file. | To update the publisher details in the controller daemon configuration file, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Mainframe system administrator |
| Create the job to start the controller daemon. | To create the job, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Mainframe system administrator |
| Generate the capture publisher JCL file. | To generation the capture publisher JCL file, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Mainframe system administrator |
| Check and update CDC. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Mainframe system administrator |
| Submit the JCL files. | Submit the following JCL files that you configured in the previous steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html)<br />After you submit the JCL files, you can start the Apply Engine in Precisely on the EC2 instance. | Mainframe system administrator |

### Run and validate CDC
<a name="run-and-validate-cdc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the Apply Engine and validate the CDC. | To start the Apply Engine on the EC2 instance and validate the CDC, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Cloud architect, App developer |
| Validate the records on the Amazon MSK topic. | To read the message from the Kafka topic, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | App developer, Cloud architect |

### Store mainframe change data in an Amazon Redshift Serverless data warehouse
<a name="store-mainframe-change-data-in-an-rsslong-data-warehouse"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Amazon Redshift Serverless. | To create an Amazon Redshift Serverless data warehouse, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html).<br />On the Amazon Redshift Serverless dashboard, validate that the namespace and workgroup were created and are available. For this example pattern, the process might take 2‒5 minutes. | Data engineer |
| Set up the IAM role and trust policy required for streaming ingestion. | To set up Amazon Redshift Serverless streaming ingestion from Amazon MSK, do following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Data engineer |
| Connect Amazon Redshift Serverless to Amazon MSK. | To connect to the Amazon MSK topic, create an external schema in Amazon Redshift Serverless. In Amazon Redshift query editor v2, run the following SQL command, replacing `'iam_role_arn'` with the role that you created previously and replacing `'MSK_cluster_arn`' with the ARN for your cluster.<pre>CREATE EXTERNAL SCHEMA member_schema<br />FROM MSK<br />IAM_ROLE 'iam_role_arn'<br />AUTHENTICATION iam<br />URI 'MSK_cluster_arn';</pre> | Migration engineer |
| Create a materialized view. | To consume the data from the Amazon MSK topic in Amazon Redshift Serverless, create a materialized view. In Amazon Redshift query editor v2, run the following SQL commands, replacing `<MSK_Topic_name>` with the name of your Amazon MSK topic.<pre>CREATE MATERIALIZED VIEW member_view<br />AUTO REFRESH YES<br />AS SELECT<br />kafka_partition, <br />kafka_offset, <br />refresh_time, <br />json_parse(kafka_value) AS Data<br />FROM member_schema.<MSK_Topic_name><br />WHERE CAN_JSON_PARSE(kafka_value); <br /></pre> | Migration engineer |
| Create target tables in Amazon Redshift. | Amazon Redshift tables provide the input for Quick Sight. This pattern uses the tables `member_dtls` and `member_plans`, which match the source Db2 tables on the mainframe.<br />To create the two tables in Amazon Redshift, run the following SQL commands in Amazon Redshift query editor v2:<pre>-- Table 1: members_dtls<br />CREATE TABLE members_dtls (<br /> memberid INT ENCODE AZ64,<br /> member_name VARCHAR(100) ENCODE ZSTD,<br /> member_type VARCHAR(50) ENCODE ZSTD,<br /> age INT ENCODE AZ64,<br /> gender CHAR(1) ENCODE BYTEDICT,<br /> email VARCHAR(100) ENCODE ZSTD,<br /> region VARCHAR(50) ENCODE ZSTD<br />) DISTSTYLE AUTO;<br /><br />-- Table 2: member_plans<br />CREATE TABLE member_plans (<br /> memberid INT ENCODE AZ64,<br /> medical_plan CHAR(1) ENCODE BYTEDICT,<br /> dental_plan CHAR(1) ENCODE BYTEDICT,<br /> vision_plan CHAR(1) ENCODE BYTEDICT,<br /> preventive_immunization VARCHAR(50) ENCODE ZSTD<br />) DISTSTYLE AUTO;</pre> | Migration engineer |
| Create a stored procedure in Amazon Redshift. | This pattern uses a stored procedure to sync-up change data (`INSERT`, `UPDATE`, `DELETE`) from the source mainframe to the target Amazon Redshift data warehouse table for analytics in Quick Sight.<br />To create the stored procedure in Amazon Redshift, use query editor v2 to run the stored procedure code that's in the GitHub repository. | Migration engineer |
| Read from the streaming materialized view and load to the target tables. | The stored procedure reads data change from the streaming materialized view and loads the data changes to the target tables. To run the stored procedure, use the following command:<pre>call SP_Members_Load();</pre><br />You can use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to schedule the jobs in your Amazon Redshift data warehouse to call this stored procedure based on your data latency requirements. EventBridge runs jobs at fixed intervals. To monitor whether the previous call to the procedure completed, you might need to use a mechanism such as an [AWS Step Functions](https://aws.amazon.com/step-functions/) state machine. For more information, see the following resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html)<br />Another option is to use Amazon Redshift query editor v2 to schedule the refresh. For more information, see [Scheduling a query with query editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-schedule-query.html). | Migration engineer |

### Connect Quick Sight to data in Amazon Redshift
<a name="connect-quick-sight-to-data-in-rs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Quick Sight. | To set up Quick Sight, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/setting-up.html). | Migration engineer |
| Set up a secure connection between Quick Sight and Amazon Redshift. | To set up secure a connection between Quick Sight and Amazon Redshift, do the following[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Migration engineer |
| Create a dataset for Quick Sight. | To create a dataset for Quick Sight from Amazon Redshift, do following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Migration engineer |
| Join the dataset. | To create analytics in Quick Sight, join the two tables by following the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/joining-data.html#create-a-join).<br />In the **Join Configuration** pane, choose **Left** for **Join type**. Under **Join clauses**, use `memberid from member_plans = memberid from members_details`. | Migration engineer |

### Get business insights from the mainframe data by using Amazon Q in Quick Sight
<a name="get-business-insights-from-the-mainframe-data-by-using-qdev-in-quick-sight"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Amazon Q in Quick Sight. | To set up the Amazon Q in Quick Sight generative BI capability, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html). | Migration engineer |
| Analyze mainframe data and build a visual dashboard. | To analyze and visualize your data in Quick Sight, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html)<br />When you're finished, you can publish your dashboard to share with others in your organization. For examples, see *Mainframe visual dashboard* in the [Additional information](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight.html#generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-additional) section. | Migration engineer |

### Create a data story with Amazon Q in Quick Sight from mainframe data
<a name="create-a-data-story-with-qdev-in-quick-sight-from-mainframe-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a data story. | Create a data story to explain insights from the previous analysis, and generate a recommendation to increase preventive immunization for members:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Migration engineer |
| View the generated data story. | To view the generated data story, choose that story on the **Data stories** page. | Migration engineer |
| Edit a generated data story. | To change the formatting, layout, or visuals in a data story, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-stories-edit.html). | Migration engineer |
| Share a data story. | To share a data story, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-stories-share.html). | Migration engineer |

## Troubleshooting
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| For Quick Sight to Amazon Redshift dataset creation, `Validate Connection` has faled. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) |
| Trying to start the Apply engine on the EC2 instance returns the following error:<br />`-bash: sqdeng: command not found` | Export the `sqdata` installation path by running following command:<pre>export PATH=$PATH:/usr/sbin:/opt/precisely/di/sqdata/bin</pre> |
| Trying to start the Apply Engine returns one of the following connection errors:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight.html) | Check the mainframe spool to make sure that the controller daemon jobs are running. |

## Related resources
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-resources"></a>
+ [Generate insights by using AWS Mainframe Modernization and Amazon Q in Quick Sight](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight.html?did=pg_card&trk=pg_card) (pattern)
+ [Generate data insights by using AWS Mainframe Modernization and Amazon Q in Quick Sight](https://youtu.be/F8b7l79p6TM?si=gASuQtFbMVuEm7IJ) (demo)
+ [AWS Mainframe Modernization - Data Replication for IBM z/OS](https://aws.amazon.com/marketplace/pp/prodview-doe2lroefogia?sr=0-4&ref_=beagle&applicationId=AWSMPContessa)
+ [Amazon Redshift streaming ingestion to a materialized view](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html)

## Additional information
<a name="generate-db2-zos-data-insights-aws-mainframe-modernization-amazon-q-in-quicksight-additional"></a>

**Example .ddl files**

*members\_details.ddl*

```
CREATE TABLE MEMBER_DTLS (
memberid INTEGER NOT NULL,
member_name VARCHAR(50),
member_type VARCHAR(20),
age INTEGER,
gender CHAR(1),
email VARCHAR(100),
region VARCHAR(20)
);
```

*member\_plans.ddl*

```
CREATE TABLE MEMBER_PLANS (
memberid INTEGER NOT NULL,
medical_plan CHAR(1),
dental_plan CHAR(1),
vision_plan CHAR(1),
preventive_immunization VARCHAR(20)
);
```

**Example .sqd file**

Replace** **`<kafka topic name>` with your Amazon MSK topic name.

*script.sqd*

```
-- Name: DB2ZTOMSK: DB2z To MSK JOBNAME DB2ZTOMSK;REPORT EVERY 1;OPTIONS CDCOP('I','U','D');-- Source Descriptions
JOBNAME DB2ZTOMSK;
REPORT EVERY 1;
OPTIONS CDCOP('I','U','D');

-- Source Descriptions
BEGIN GROUP DB2_SOURCE;
DESCRIPTION DB2SQL /var/precisely/di/sqdata/apply/DB2ZTOMSK/ddl/mem_details.ddl AS MEMBER_DTLS;
DESCRIPTION DB2SQL /var/precisely/di/sqdata/apply/DB2ZTOMSK/ddl/mem_plans.ddl AS MEMBER_PLANS;
END GROUP;
-- Source Datastore
DATASTORE cdc://<zos_host_name>/DB2ZTOMSK/DB2ZTOMSK
OF UTSCDC
AS CDCIN
DESCRIBED BY GROUP DB2_SOURCE ;
-- Target Datastore(s)
DATASTORE 'kafka:///<kafka topic name>/key'
OF JSON
AS TARGET
DESCRIBED BY GROUP DB2_SOURCE;
PROCESS INTO TARGET
SELECT
{
REPLICATE(TARGET)
}
FROM CDCIN;
```

**Mainframe visual dashboard**

The following data visual was created by Amazon Q in Quick Sight for the analysis question `show member distribution by region`*.*

![Northeast and Southwest have 8 members, Southwest has 5 members, Midwest has 4 members.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/b40a784c-c1fc-444b-b6df-8bd1f7a6abaa.png)

The following data visual was created by Amazon Q in Quick Sight for the question `show member distribution by Region who have not completed preventive immunization, in pie chart`.

![Southeast shows 6, Southwest shows 5, and Midwest shows 4.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/8a95da3c-df4a-458b-9cfe-44e34f80a235.png)

**Data story output**

The following screenshots show sections of the data story created by Amazon Q in Quick Sight for the prompt `Build a data story about Region with most numbers of members. Also show the member distribution by age, member distribution by gender. Recommend how to motivate members to complete immunization. Include 4 points of supporting data for this pattern`.

In the introduction, the data story recommends choosing the region with the most members to gain the greatest impact from immunization efforts.

![Introduction screen for analysis based on geographic, demographic, and age of the member base.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/40f13957-2db4-42b7-b7a4-a0dd3dad6899.png)

The data story provides an analysis of member numbers for the four regions. The Northeast, Southwest, and Southeast regions have the most members.

![Northeast and Southwest regions have 8 members, Southeast has 6 members, and Midwest has 4 members.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/fc6ed0a0-b79c-4397-95ac-a2fc4c87482a.png)

The data story presents an analysis of members by age.

![Chart showing that the member base skews toward younger and middle-aged adults.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/8c56f1ec-3a2e-47a6-bbc4-3631782aa333.png)

The data story focuses on immunization efforts in the Midwest.

![Recommendation for personal outreach campaign and regional challenges.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/84a647e8-c7d5-4637-94f0-03a611f899b3.png)

![Continuation of data story analysis, with anticipated outcomes and conclusion.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/18e72bcb-1b9a-406a-8220-83aca7743ad2/images/fc9094fc-2a20-485d-b238-e5e4ec70f1d3.png)

## Attachments
<a name="attachments-18e72bcb-1b9a-406a-8220-83aca7743ad2"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/18e72bcb-1b9a-406a-8220-83aca7743ad2/attachments/attachment.zip)
