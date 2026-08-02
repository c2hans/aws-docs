---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html
---

# Migrate and replicate VSAM files to Amazon RDS or Amazon MSK using Connect from Precisely
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely"></a>

*Prachi Khanna and Boopathy GOPALSAMY, Amazon Web Services*

## Summary
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-summary"></a>

This pattern shows you how to migrate and replicate Virtual Storage Access Method (VSAM) files from a mainframe to a target environment in the AWS Cloud by using [Connect](https://www.precisely.com/product/precisely-connect/connect) from Precisely. The target environments covered in this pattern include Amazon Relational Database Service (Amazon RDS) and Amazon Managed Streaming for Apache Kafka (Amazon MSK). Connect uses [change data capture (CDC)](https://www.precisely.com/resource-center/productsheets/change-data-capture-with-connect) to continuously monitor updates to your source VSAM files and then transfer these updates to one or more of your AWS target environments. You can use this pattern to meet your application modernization or data analytics goals. For example, you can use Connect to migrate your VSAM application files to the AWS Cloud with low latency, or migrate your VSAM data to an AWS data warehouse or data lake for analytics that can tolerate synchronization latencies that are higher than required for application modernization.

## Prerequisites and limitations
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-prereqs"></a>

**Prerequisites**
+ [IBM z/OS V2R1](https://www-40.ibm.com/servers/resourcelink/svc00100.nsf/pages/zosv2r1-pdf-download?OpenDocument) or later
+ [CICS Transaction Server for z/OS (CICS TS) V5.1](https://www.ibm.com/support/pages/cics-transaction-server-zos-51-detailed-system-requirements) or later (CICS/VSAM data capture)
+ [IBM MQ 8.0](https://www.ibm.com/support/pages/downloading-ibm-mq-80) or later
+ Compliance with [z/OS security requirements](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Installation/Install-Connect-CDC-SQData-on-zOS/Prerequisites-for-z/OS/Security-authorization-requirements-for-z/OS) (for example, APF authorization for SQData load libraries)
+ VSAM recovery logs turned on
+ (Optional) [CICS VSAM Recovery Version (CICS VR)](https://www.ibm.com/docs/en/cics-vr/5.1?topic=started-introducing-cics-vr) to automatically capture CDC logs
+ An active AWS account
+ An [Amazon Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html) with a subnet that’s reachable by your legacy platform
+ A VSAM Connect license from Precisely

**Limitations**
+ Connect doesn’t support automatic target table creation based on source VSAM schemas or copybooks. You must define the target table structure for the first time.
+ For non-streaming targets such as Amazon RDS, you must specify the conversion source to target mapping in the Apply Engine configuration script.
+ Logging, monitoring, and alerting functions are implemented through APIs and require external components (such as Amazon CloudWatch) to be fully operational.

**Product versions**
+ SQData 40134 for z/OS
+ SQData 4.0.43 for the Amazon Linux Amazon Machine Image (AMI) on Amazon Elastic Compute Cloud (Amazon EC2)

## Architecture
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-architecture"></a>

**Source technology stack**
+ Job Control Language (JCL)
+ z/OS Unix shell and Interactive System Productivity Facility (ISPF)
+ VSAM utilities (IDCAMS)

** Target technology stack**
+ Amazon EC2
+ Amazon MSK
+ Amazon RDS
+ Amazon VPC

**Target architecture**

*Migrating VSAM files to Amazon RDS*

The following diagram shows how to migrate VSAM files to a relational database, such as Amazon RDS, in real time or near real time by using the CDC agent/publisher in the source environment (on-premises mainframe) and the [Apply Engine](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Apply-engine) in the target environment (AWS Cloud).

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4ee183bd-1c0d-449d-8cdc-eb6e2c41a695/images/47cefbde-e0c8-4c36-ba48-cccc2c443074.png)

The diagram shows the following batch workflow:

1. Connect captures changes to a file by comparing VSAM files from backup files to identify changes and then sends the changes to the logstream.

1. The publisher consumes data from the system logstream.

1. The publisher communicates captured data changes to a target engine through TCP/IP. The Controller Daemon authenticates communication between the source and target environments.

1. The Apply Engine in the target environment receives the changes from the Publisher agent and applies them to a relational or non-relational database.

The diagram shows the following online workflow:

1. Connect captures changes in the online file by using a log replicate and then streams captured changes to a logstream.

1. The publisher consumes data from the system logstream.

1. The publisher communicates captured data changes to the target engine through TCP/IP. The Controller Daemon authenticates communication between the source and target environments.

1. The Apply Engine in the target environment receives the changes from the Publisher agent and then applies them to a relational or non-relational database.

*Migrating VSAM files to Amazon MSK*

The following diagram shows how to stream VSAM data structures from a mainframe to Amazon MSK in high-performance mode and automatically generate JSON or AVRO schema conversions that integrate with Amazon MSK.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4ee183bd-1c0d-449d-8cdc-eb6e2c41a695/images/13eb27ad-c0d2-489b-91e1-5b2a729fb8dd.png)

The diagram shows the following batch workflow:

1. Connect captures changes to a file by using CICS VR or by comparing VSAM files from backup files to identify changes. Captured changes are sent to the logstream.

1. The publisher consumes data from the system logstream.

1. The publisher communicates captured data changes to the target engine through TCP/IP. The Controller Daemon authenticates communication between the source and target environments.

1. The Replicator Engine that’s operating in parallel processing mode splits the data to a unit of work cache.

1. Worker threads capture the data from the cache.

1. Data is published to Amazon MSK topics from the worker threads.

1. Users apply changes from Amazon MSK to targets such as Amazon DynamoDB, Amazon Simple Storage Service (Amazon S3), or Amazon OpenSearch Service by using [connectors](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html).

The diagram shows the following online workflow:

1. Changes in the online file are captured by using a log replicate. Captured changes are streamed to the logstream.

1. The publisher consumes data from the system logstream.

1. The publisher communicates captured data changes to the target engine through TCP/IP. The Controller Daemon authenticates communication between the source and target environments.

1. The Replicator Engine that’s operating in parallel processing mode splits the data to a unit of work cache.

1. Worker threads capture the data from the cache.

1. Data is published to Amazon MSK topics from the worker threads.

1. Users apply changes from Amazon MSK to targets such as DynamoDB, Amazon S3, or OpenSearch Service by using [connectors](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html).

## Tools
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-tools"></a>
+ [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) is a fully managed service that helps you build and run applications that use Apache Kafka to process streaming data.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.

## Epics
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-epics"></a>

### Prepare the source environment (mainframe)
<a name="prepare-the-source-environment-mainframe"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Connect CDC 4.1. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | IBM Mainframe Developer/Admin |
| Set up the zFS directory. | To set up a zFS directory, follow the instructions from [zFS variable directories](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Installation/Install-Connect-CDC-SQData-on-zOS/Prerequisites-for-z/OS/Security-authorization-requirements-for-z/OS/zFS-variable-directories) in the Precisely documentation.Controller Daemon and Capture/Publisher agent configurations are stored in the z/OS UNIX Systems Services file system (referred to as zFS). The Controller Daemon, Capture, Storage, and Publisher agents require a predefined zFS directory structure for storing a small number of files. | IBM Mainframe Developer/Admin |
| Configure TCP/IP ports. | To configure TCP/IP ports, follow the instructions from [TCP/IP ports](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Installation/Install-Connect-CDC-SQData-on-UNIX/Prerequisites-for-UNIX/Security-authorization-requirements-for-UNIX/TCP/IP-ports) in the Precisely documentation.The Controller Daemon requires TCP/IP ports on source systems. The ports are referenced by the engines on the target systems (where captured change data is processed). | IBM Mainframe Developer/Admin |
| Create a z/OS logstream. | To create a [z/OS logstream](https://www.ibm.com/docs/en/was/8.5.5?topic=SSEQTP_8.5.5/com.ibm.websphere.installation.zseries.doc/ae/cins_logstrm.html), follow the instructions from [Create z/OS system logStreams](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-sources/IMS-z/OS/IMS-TM-EXIT-capture/Prepare-environment/Create-z/OS-system-logStreams?tocId=wy6243SXlIiEczwR8JE8WA) in the Precisely documentation.Connect uses the logstream to capture and stream data between your source environment and target environment during migration.<br />For an example JCL that creates a z/OS LogStream, see [Create z/OS system logStreams](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-sources/IMS-z/OS/IMS-TM-EXIT-capture/Prepare-environment/Create-z/OS-system-logStreams?tocId=wy6243SXlIiEczwR8JE8WA) in the Precisely documentation. | IBM Mainframe Developer |
| Identify and authorize IDs for zFS users and started tasks. | Use RACF to grant access to the OMVS zFS file system. For an example JCL, see [Identify and authorize zFS user and started task IDs](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-sources/IMS-z/OS/IMS-log-reader-capture/Prepare-environment/Identify-and-authorize-zFS-user-and-started-task-IDs?tocId=MrBXpFu~N0iAy~8VTrH0tQ) in the Precisely documentation. | IBM Mainframe Developer/Admin |
| Generate z/OS public/private keys and the authorized key file. | Run the JCL to generate the key pair. For an example, see *Key pair example* in the *Additional information* section of this pattern.<br />For instructions, see [Generate z/OS public and private keys and authorized key file](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-sources/Db2-z/OS/Prepare-the-environment/Generate-z/OS-public-and-private-keys-and-authorized-key-file?tocId=fceE77dWT8smZsSaE~FeMQ) in the Precisely documentation. | IBM Mainframe Developer/Admin |
| Activate the CICS VSAM Log Replicate and attach it to the logstream. | Run the following JCL script:<pre> //STEP1 EXEC PGM=IDCAMS<br /> //SYSPRINT DD SYSOUT=*<br /> //SYSIN DD *<br />   ALTER SQDATA.CICS.FILEA -<br />   LOGSTREAMID(SQDATA.VSAMCDC.LOG1) -<br />   LOGREPLICATE</pre> | IBM Mainframe Developer/Admin |
| Activate the VSAM File Recovery Log through an FCT. | Modify the File Control Table (FCT) to reflect the following parameter changes:<pre> Configure FCT Parms<br />   CEDA ALT FILE(name) GROUP(groupname)<br />   DSNAME(data set name)<br />   RECOVERY(NONE|BACKOUTONLY|ALL)<br />   FWDRECOVLOG(NO|1–99)<br />   BACKUPTYPE(STATIC|DYNAMIC)<br />   RECOVERY PARAMETERS<br />   RECOVery : None | Backoutonly | All<br />   Fwdrecovlog : No | 1-99<br />   BAckuptype : Static | Dynamic</pre> | IBM Mainframe Developer/Admin |
| Set up CDCzLog for the Publisher agent. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | IBM Mainframe Developer/Admin |
| Activate the Controller Daemon. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | IBM Mainframe Developer/Admin |
| Activate the publisher. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | IBM Mainframe Developer/Admin |
| Activate the logstream. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | IBM Mainframe Developer/Admin |

### Prepare the target environment (AWS)
<a name="prepare-the-target-environment-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Precisely on an EC2 instance. | To install Connect from Precisely on the Amazon Linux AMI for Amazon EC2, follow the instructions from [Install Connect CDC (SQData) on UNIX](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Installation/Install-Connect-CDC-SQData-on-UNIX) in the Precisely documentation. | General AWS |
| Open TCP/IP ports. | To modify the security group to include the Controller Daemon ports for inbound and outbound access, follow the instructions from [TCP/IP](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-sources/Change-data-capture/Transient-storage-and-publishing/TCP/IP) in the Precisely documentation. | General AWS |
| Create file directories. | To create file directories, follow the instructions from [Prepare target apply environment](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-targets/Kafka/Prepare-target-apply-environment) in the Precisely documentation. | General AWS |
| Create the Apply Engine configuration file. | Create the Apply Engine configuration file in the working directory of the Apply Engine. The following example configuration file shows Apache Kafka as the target:<pre>builtin.features=SASL_SCRAM<br />  security.protocol=SASL_SSL<br />  sasl.mechanism=SCRAM-SHA-512<br />  sasl.username=<br />  sasl.password=<br />  metadata.broker.list=</pre>For more information, see [Security](https://kafka.apache.org/documentation/#security) in the Apache Kafka documentation. | General AWS |
| Create scripts for Apply Engine processing. | Create the scripts for the Apply Engine to process source data and replicate source data to the target. For more information, see [Create an apply engine script](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Apply-engine/Apply-engine-script-development/Create-an-apply-engine-script) in the Precisely documentation. | General AWS |
| Run the scripts. | Use the `SQDPARSE` and `SQDENG` commands to run the script. For more information, see [Parse a script for zOS](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Apply-engine/Apply-engine-script-development/Parse-a-script/Parse-a-script-for-zOS) in the Precisely documentation. | General AWS |

### Validate the environment
<a name="validate-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the list of VSAM files and target tables for CDC processing. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | General AWS, Mainframe |
| Verify that the Connect CDC SQData product is linked. | Run a testing job and verify that the return code from this job is 0 (Successful).Connect CDC SQData Apply Engine status messages should show active connection messages. | General AWS, Mainframe |

### Run and validate test cases (Batch)
<a name="run-and-validate-test-cases-batch"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the batch job in the mainframe. | Run the batch application job using a modified JCL. Include steps in the modified JCL that do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | General AWS, Mainframe |
| Check the logstream. | Check the logstream to confirm that you can see the change data for the completed mainframe batch job. | General AWS, Mainframe |
| Validate the counts for the source delta changes and target table. | To confirm the records are tallied, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | General AWS, Mainframe |

### Run and validate test cases (Online)
<a name="run-and-validate-test-cases-online"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the online transaction in a CICS region. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely.html) | IBM Mainframe Developer |
| Check the logstream. | Confirm that the logstream is populated with specific record level changes. | AWS Mainframe Developer |
| Validate the count in the target database. | Monitor the Apply Engine for record level counts. | Precisely, Linux |
| Validate the record counts and data records in the target database. | Query the target database to validate the record counts and data records. | General AWS |

## Related resources
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-resources"></a>
+ [VSAM z/OS](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Setup-and-configure-sources/VSAM-z/OS) (Precisely documentation)
+ [Apply engine](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Apply-engine) (Precisely documentation)
+ [Replicator engine](https://help.precisely.com/r/Connect-CDC-SQData/4.1.43/en-US/Connect-CDC-SQData-Help/Source-and-Target-Configuration/Replicator-engine) (Precisely documentation)
+ [The log stream](https://www.ibm.com/docs/en/zos/2.3.0?topic=logger-log-stream) (IBM documentation)

## Additional information
<a name="migrate-and-replicate-vsam-files-to-amazon-rds-or-amazon-msk-using-connect-from-precisely-additional"></a>

**Configuration file example**

This is an example configuration file for a logstream where the source environment is a mainframe and the target environment is Amazon MSK:

```

  -- JOBNAME -- PASS THE SUBSCRIBER NAME
  -- REPORT  progress report will be produced after "n" (number) of Source records processed.

  JOBNAME VSMTOKFK;
  --REPORT EVERY 100;
  -- Change Op has been ‘I’ for insert, ‘D’ for delete , and ‘R’ for Replace. For RDS it is 'U' for update
  -- Character Encoding on z/OS is Code Page 1047, on Linux and UNIX it is Code Page 819 and on Windows, Code Page 1252
  OPTIONS
  CDCOP('I', 'U', 'D'),
  PSEUDO NULL = NO,
  USE AVRO COMPATIBLE NAMES,
  APPLICATION ENCODING SCHEME = 1208;

  --       SOURCE DESCRIPTIONS

  BEGIN GROUP VSAM_SRC;
  DESCRIPTION COBOL ../copybk/ACCOUNT AS account_file;
  END GROUP;

  --       TARGET DESCRIPTIONS

  BEGIN GROUP VSAM_TGT;
  DESCRIPTION COBOL ../copybk/ACCOUNT AS account_file;
  END GROUP;

  --       SOURCE DATASTORE (IP & Publisher name)

  DATASTORE cdc://10.81.148.4:2626/vsmcdct/VSMTOKFK
  OF VSAMCDC
  AS CDCIN
  DESCRIBED BY GROUP VSAM_SRC ACCEPT ALL;

  --       TARGET DATASTORE(s) - Kafka and topic name

  DATASTORE 'kafka:///MSKTutorialTopic/key'
  OF JSON
  AS CDCOUT
  DESCRIBED BY GROUP VSAM_TGT FOR INSERT;

  --       MAIN SECTION

  PROCESS INTO
  CDCOUT
  SELECT
  {
  SETURL(CDCOUT, 'kafka:///MSKTutorialTopic/key')
  REMAP(CDCIN, account_file, GET_RAW_RECORD(CDCIN, AFTER), GET_RAW_RECORD(CDCIN, BEFORE))
  REPLICATE(CDCOUT, account_file)
  }
  FROM CDCIN;
```

**Key pair example**

This an example of how to run the JCL to generate the key pair:

```
//SQDUTIL EXEC PGM=SQDUTIL //SQDPUBL DD DSN=&USER..NACL.PUBLIC, // DCB=(RECFM=FB,LRECL=80,BLKSIZE=21200), // DISP=(,CATLG,DELETE),UNIT=SYSDA, // SPACE=(TRK,(1,1)) //SQDPKEY DD DSN=&USER..NACL.PRIVATE, // DCB=(RECFM=FB,LRECL=80,BLKSIZE=21200), // DISP=(,CATLG,DELETE),UNIT=SYSDA, // SPACE=(TRK,(1,1)) //SQDPARMS DD  keygen //SYSPRINT DD SYSOUT= //SYSOUT DD SYSOUT=* //SQDLOG DD SYSOUT=* //*SQDLOG8 DD DUMMY
```
