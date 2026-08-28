---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase1.html
---

# Phase 1: Prepare phase
<a name="phase1"></a>

During this phase, data files of the tablespace to be transported are backed up on the source system. Backup copies are transported to the destination system and restored by running the xttdriver.pl script.

## Step 1: Take full (level=0) tablespace backups on the source system
<a name="step-1--take-full--level-0--tablespace-backups-on-the-source-system.510a5845-048b-5303-9005-2406d0d4d4eb"></a>

To reduce the backup duration time, copy the xtt.properties and xttdriver.pl files to multiple directories. In each xtt.properties file under each directory, enter the name of the tablespace in the tablespaces parameter. Then, under each directory, run xttdriver.pl with the --backup option. This command transports all the tablespaces except for SYSTEM, SYSAUX, UNDO, and TEMP, which were created during installation of the target database.

For example, each xtt01\~xtt04 directory has all xtt scripts (xtt.properties and xttdriver.pl) with different values for the tablespaces= parameter in the xtt.properties file. When editing the tablespaces parameter in each xtt.properties file, consider dividing the tablespace groups so that the total size of the data files in each tablespace group is similar.

In this guide, the example supposes that there are four tablespace groups. If the source database is Oracle single instance, you create all xtt01\~04 directories. If the source database is Oracle RAC, you can create each xtt directory in each Oracle RAC server.

```
[oracle@erp expimp]$ ls
out  xtt01  xtt02  xtt03    xtt04
[oracle@erp out]$ ls
out01 out02 out03 out04
```

The following table shows examples of the tablespaces= parameter in the xtt.properties files.

|  |  |
| --- |--- |
| xtt01 | tablespaces=APPS\_TS\_TX\_DATA |
| xtt02 | tablespaces=APPS\_TS\_TX\_IDX |
| xtt03 | tablespaces=APPS\_TS\_SUMMARY |
| xtt04 | tablespaces=APPS\_CALCLIP, APPS\_OMO, APPS\_TS\_ARCHIVE, APPS\_TS\_DISCO, APPS\_TS\_DISCO\_OLAP,  APPS\_TS\_INTERFACE, APPS\_TS\_MEDIA, APPS\_TS\_NOLOGGING, APPS\_TS\_QUEUES, APPS\_TS\_SEED… |

To prevent any existing data file backup copies from being deleted while xttdriver.pl is running in parallel, comment out the following line in xttdriver.pl.

```
   if (@present)
   {
      ## Try deleting any existing copied datafiles
##Comment out it for executing rman command in parallel by AWS
##        system("\\rm -f $dfcopydir/*.tf");
      sleep 5;
   }
```

Use xttdriver.pl to make the RMAN backup of the source system.

If the source system is Oracle RAC, it can be run on each Oracle RAC instance simultaneously.

The output of xttdriver.pl is stored in the TMPDIR environment variable. Run each xttdriver.pl command with the --backup option, and use the --debug option to turn on debug mode.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl --backup --debug 3
```

In this example, <*nn*> represents the tablespace groups. If there are four tablespace groups, <*nn*> becomes 01, 02, 03, and 04.

## Step 2: Transfer full backup copies to the destination system
<a name="step-2--transfer-full-backup-copies-to-the-destination-system.1b7c256b-9e72-56a4-93b2-8f5f7282f7fe"></a>

### Option 1 - Using AWS Snowball Edge
<a name="option-1---using-aws-snowball-edge.5cf6f190-4d03-540a-a933-653f34f79bd3"></a>

**Path:** Source database -> source stage -> AWS Snowball Edge -> Amazon S3 -> Amazon FSx for Lustre

**Note**
AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The following diagram shows the transfer of a full backup using Snowball Edge.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/images/guide-img/c09fd9a4-3278-4711-9038-c55dfc694acd/images/fdf84cd7-cfc1-47f2-b71a-741ec515672d.png)

The Snowball Edge is a rugged physical storage and computing device that you can use to move large-scale data to AWS. Snowball Edge helps overcome challenges that you might encounter with large-scale data transfers, including long transfer times, a lack of usable bandwidth, and security concerns.

The entire data file backup copies are transferred into Amazon S3 by the Snowball Edge. If the source system size is over 100 TB, you must use multiple Snowball Edge devices to reduce the duration of the transfer.

Amazon FSx for Lustre is deeply integrated with Amazon S3. You can create an FSx for Lustre file system that is linked to your S3 bucket in minutes. When linked to the Amazon S3 data repository, FSx for Lustre file systems transparently present Amazon S3 objects as files. In the real environment, the performance of FSx for Lustre depends on its storage capacity, the size of each file, and how well files are distributed into the file system. When FSx for Lustre is used as target-stage storage, you don't need to restore tablespace backup copies into Amazon Elastic Block Store (Amazon EBS) or Amazon Elastic File System from Amazon S3.

1. Import the S3 bucket to Amazon FSx for Lustre.

   Use Snowball Edge to transfer and store the source stage area (for example, src\_backups) into an S3 bucket (for example, s3-src-backups).

   Create the FSx for Lustre file system (for example, dest\_backups) as the destination stage area for the data file backup copies.
![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/images/guide-img/c09fd9a4-3278-4711-9038-c55dfc694acd/images/68b11d6e-4107-4cda-9c55-1bf19eff272f.png)

   Install the open-source Lustre client on the destination system (Amazon EC2). For more information, see the [Amazon FSx for Lustre User Guide](https://docs.aws.amazon.com/fsx/latest/LustreGuide/install-lustre-client.html).

   After the Lustre client is installed, mount the FSx for Lustre file system to the destination system (Amazon EC2).

1. Transfer res.txt from $TMPDIR on the source to $TMPDIR on the destination.

### Option 2 -  Using AWS Direct Connect
<a name="option-2----using-aws-direct-connect.6d9fc6ef-5212-53c9-b7c6-70d859486446"></a>

**Path:** Source database -> source stage -> AWS Direct Connect -> Amazon FSx for Lustre

The following diagram shows the transfer of a full backup by using AWS Direct Connect.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/images/guide-img/c09fd9a4-3278-4711-9038-c55dfc694acd/images/330daa32-22c7-4070-98cb-82a080ef36b0.png)

Direct Connect gives you the ability to create private network connections between your data center, office, or colocation environment and AWS. These private network connections reduce network costs, increase throughput, and deliver a consistent experience.

You can directly transfer data file backup copies from the source system to the destination system (Amazon EC2) where the Amazon FSx for Lustre file system is mounted. This option is faster than the Snowball Edge option if you can accommodate the high bandwidth of Direct Connect.

After data file backup copies are transferred by Snowball or Direct Connect, you can see them in the FSx for Lustre file system in the target stage area.

## Step 3: Restore full backup copies and convert data files
<a name="step-3--restore-full-backup-copies-and-convert-data-files.77325278-d521-5ed0-a834-7bad7f9b7de2"></a>

Restore full backup copies and convert data files to destination system endian format. To reduce the restore and convert duration, run the xttdriver.pl command with the --restore option for each tablespace group.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl --restore --debug 3
```

After the step is complete, data files are placed in the defined *dest\_datafile\_location* in the xtt.properties file on the destination system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
