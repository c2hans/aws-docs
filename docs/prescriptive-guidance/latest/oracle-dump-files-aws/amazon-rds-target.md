---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/amazon-rds-target.html
---

# Amazon RDS for Oracle as the target
<a name="amazon-rds-target"></a>

If your target database is an Amazon RDS for Oracle instance, make sure that it has sufficient access to read and write the files to and from Amazon S3. For more information about Amazon S3 integration with Amazon RDS for Oracle instances, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html).

To copy the Oracle Database dump files to Amazon RDS for Oracle, connect to the RDS for Oracle instance through a client tool such as [SQL Developer](https://www.oracle.com/in/database/sqldeveloper/) and run the following code.

```
SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
      p_bucket_name    =>  's3bucketname', -- provide the S3 bucket name where the dump files are located
      p_directory_name =>  'DATA_PUMP_DIR')
   AS TASK_ID FROM DUAL;
```

In a separate query window, check the progress and files in the `DATA_PUMP_DIR` in the Amazon RDS for Oracle instance by running the following code.

```
SELECT SID, SERIAL#, CONTEXT, SOFAR, TOTALWORK,opname,
       ROUND(SOFAR/TOTALWORK*100,2) "%_COMPLETE",units
FROM   V$SESSION_LONGOPS
where  OPNAME NOT LIKE '%aggregate%'
AND    TOTALWORK != 0
AND    SOFAR <> TOTALWORK;
select * from table(RDSADMIN.RDS_FILE_UTIL.LISTDIR('DATA_PUMP_DIR')) order by filename;
```

## Securing data at rest and data in transit in Amazon RDS
<a name="secure-data-amazon-rds"></a>

Amazon RDS follows the AWS shared responsibility model for data protection. According to this model, AWSS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).

We recommend that you secure your data in the following ways:
+ Encrypt Amazon RDS resources with AWS Key Management Service (AWS KMS). Amazon RDS encrypted DB instances provide an additional layer of data protection by securing your data from unauthorized access to the underlying storage. You can use Amazon RDS encryption to increase data protection of your applications deployed in the cloud, and to fulfill compliance requirements for encryption at rest. For information about how to encrypt your Amazon RDS instances, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.Enabling).
+ Encrypt connections to the databases. You can use SSL/TLS to encrypt a connection to a DB instance. For more information about encrypting connections to Amazon RDS for Oracle instances, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.SSL.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
