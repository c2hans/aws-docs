---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/data-migration-using-oracle-rman.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data migration using Oracle RMAN
<a name="data-migration-using-oracle-rman"></a>

 If you are planning to migrate the entire database and your destination database is self-managed on Amazon EC2, you can use Oracle RMAN to migrate data. Data migration by using Oracle Data Pump is faster and more flexible than data migration using Oracle RMAN; however, Oracle RMAN is a better option for the following cases:
+  You already have an RMAN backup available in Amazon S3 that can be used. If you are looking for options to migrate RMAN backups to Amazon S3, consider [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) or [AWS DataSync](https://aws.amazon.com/datasync/) services.
+  The database is very large (greater than 5 TB), and you are planning to use AWS Import/Export.
+  You need to make numerous incremental data changes before switching over to the database on AWS.

**Note**
This method is for Amazon EC2 and VMware Cloud on AWS. You cannot use this method if your destination database is Amazon RDS.

 To migrate data using Oracle RMAN:

1.  Create a full backup of the source database using RMAN.

1.  Encrypt and compress the files.

1.  Transport files to AWS using the most optimal method.

1.  Restore the RMAN backup to the destination database.

1.  Capture incremental backups from the source, and apply them to the destination database until switchover can be performed.

## Creating a full backup of the source database Using RMAN
<a name="creating-a-full-backup-of-the-source-database-using-rman"></a>

 Create a backup of the source database using RMAN:

```
$ rman target=/

RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON; RMAN> BACKUP DATABASE PLUS ARCHIVELOG
```

 If you have a license for the compression and encryption option, then you already have the RMAN backups created as encrypted and compressed files. Otherwise, after the backup files are created, encrypt and compress them using tools such as ZIP, 7-Zip, or GZIP. All subsequent actions occur on the server running the destination database.

## Transporting files to AWS
<a name="transporting-files-to-aws"></a>

 Depending on the size of the database and the time available for migration, you can choose the most optimal method for file transportation to AWS. For small files, consider AWS DataSync. For moderate to large databases between 100 GB to 5 TB, [Tsunami UDP](http://tsunami-udp.sourceforge.net/) is an option, as described in [Using Tsunami to upload files to EC2](data-migration-using-oracle-data-pump.md#using-tsunami-to-upload-files-to-amazon-ec2). You can achieve the same results using commercial third-party WAN acceleration tools. For very large databases over 5 TB, consider using AWS Storage Gateway or [AWS Snow Family](https://aws.amazon.com/snow/) devices for offline file transfer.

## Migrating data to Oracle Database on AWS
<a name="migrating-data-to-oracle-database-on-aws"></a>

 There are two ways to migrate data to a destination database. You can create a new database and restore from the RMAN backup, or you can create a duplicate database from the RMAN backup. Creating a duplicate database is easier to perform.

 To create a duplicate database, move the transported files to a location accessible to the Oracle Database instance on Amazon EC2. Start the target instance in `NOMOUNT` mode. Now use RMAN to connect to the destination database. For this example, we are not connecting to the source database or the RMAN catalog, so use the following command:

```
$ rman AUXILIARY /

DUPLICATE TARGET DATABASE TO DBONEC2
   SPFILE
   NOFILENAMECHECK;
```

 The duration of this process varies based on the size of the database and the type of Amazon EC2 instance. For better performance, use [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) General Purpose (SSD) [volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) for the RMAN backup files. For more information about SSD volume types, see [Introducing the Amazon EBS General Purpose (SSD) volume type](https://aws.amazon.com/about-aws/whats-new/2014/06/16/introducing-the-amazon-ebs-general-purpose-ssd-volume-type/).

 Once the process is finished, RMAN produces a completion message, and you now have your duplicate instance. After verification, you can delete the Amazon EBS volumes containing the RMAN backup files. We recommend that you take a snapshot of the volumes for later use before deleting them if needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
