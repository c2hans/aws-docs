---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.prerequisites.html
---

# Prerequisites for migrating from Amazon RDS for Oracle to Amazon Redshift
<a name="chap-rdsoracle2redshift.prerequisites"></a>

The following prerequisites are also required to complete this walkthrough:
+ Familiarity with Amazon RDS, Amazon Redshift, the applicable database technologies, and SQL.
+ The custom scripts that include creating the tables to be migrated and SQL queries for confirming the migration, as listed following:
  +  `Oracle_Redshift_For_DMSDemo.template` — an AWS CloudFormation template.
  +  `Oraclesalesstarschema.sql` — SQL statements to build the **SH** schema.

    These scripts are available at the following link: ` [dms-sbs-RDSOracle2Redshift.zip](http://docs.aws.amazon.com/dms/latest/sbs/samples/dms-sbs-RDSOracle2Redshift.zip) `.

    Each step in the walkthrough also contains a link to download the file involved or includes the exact query in the step.
+ A user with AWS Identity and Access Management (IAM) credentials that allow you to launch Amazon RDS, AWS Database Migration Service (AWS DMS) instances, and Amazon Redshift clusters in your AWS Region. For information about IAM credentials, see [Setting up for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html#CHAP_SettingUp.IAM).
+ Basic knowledge of the Amazon Virtual Private Cloud (Amazon VPC) service and of security groups. For information about using Amazon VPC with Amazon RDS, see [Virtual Private Clouds (VPCs) and Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html). For information about Amazon RDS security groups, see [Amazon RDS Security Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html). For information about using Amazon Redshift in a VPC, see [Managing Clusters in an Amazon Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html).
+ An understanding of the supported features and limitations of AWS DMS. For information about AWS DMS, see https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html.
+ Knowledge of the supported data type conversion options for Oracle and Amazon Redshift. For information about data types for Oracle as a source, see [Using an Oracle database as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). For information about data types for Amazon Redshift as a target, see [Using an Amazon Redshift Database as a Target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html).

For more information about AWS DMS, see [Getting started with Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
