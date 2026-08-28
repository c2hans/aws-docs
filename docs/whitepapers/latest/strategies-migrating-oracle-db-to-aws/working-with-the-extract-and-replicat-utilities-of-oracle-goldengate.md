---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/working-with-the-extract-and-replicat-utilities-of-oracle-goldengate.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Working with the Extract and Replicat utilities of Oracle GoldenGate
<a name="working-with-the-extract-and-replicat-utilities-of-oracle-goldengate"></a>

 The Oracle GoldenGate Extract and Replicat utilities work together to keep the source and destination databases synchronized by means of incremental transaction replication using trail files. All changes that occur on the source database are automatically detected by Extract, and then formatted and transferred to trail files on the GoldenGate Hub on-premises or on the Amazon EC2 instance. After the initial load is completed, the Replicat process reads the data from these files and replicates the data to the destination database nearly continuously.

## Running the Extract process of Oracle GoldenGate
<a name="running-the-extract-process-of-oracle-goldengate"></a>

 The Extract process of Oracle GoldenGate retrieves, converts, and outputs data from the source database to trail files. Extract queues transaction details to memory or to temporary disk storage. When the transaction is committed to the source database, Extract flushes all of the transaction details to a trail file for routing to the GoldenGate Hub on-premises or on the Amazon EC2 instance, and then to the destination database.

 The following process enables and starts the Extract process.

1.  First, configure the Extract parameter file on the GoldenGate Hub. The following example shows an Extract parameter file:

   ```
   EXTRACT EABC
   SETENV (ORACLE_SID=ORCL)
   SETENV (NLSLANG=AL32UTF8)

   USERID oggadm1@TEST, PASSWORD XXXXXX
   EXTTRAIL /path/to/goldengate/dirdat/ab IGNOREREPLICATES
   GETAPPLOPS
   TRANLOGOPTIONS EXCLUDEUSER OGGADM1 TABLE EXAMPLE.TABLE;
   ```

1.  On the GoldenGate Hub, launch the GoldenGate command line interface (`ggsci`). Log in to the source database. The following example shows the format for logging in:

   ```
   dblogin userid <user>@<db tnsname>
   ```

1.  Next, add a checkpoint table for the database:

   ```
   add checkpointtable

   Add transdata to turn on supplemental logging for the database table:

   add trandata <user>.<table>
   ```

    Alternatively, you can add `transdata` to turn on supplemental logging for all tables in the database:

   ```
   add trandata <user>.*
   ```

1.  Using the `ggsci` command line, use the following commands to enable the Extract process:

   ```
   add extract <extract name> tranlog, INTEGRATED tranlog,
   begin now

   add exttrail <path-to-trail-from-the param-file> extract

   <extractname-from-paramfile>, MEGABYTES Xm
   ```

1.  Register the Extract process with the database so that the archive logs are not deleted. This lets you recover old, uncommitted transactions if necessary. To register the Extract process with the database, use the following command:

   ```
   register EXTRACT <extract process name>, DATABASE
   ```

1.  To start the Extract process, use the following command:

   ```
   start <extract process name>
   ```

### Running the Replicat process of Oracle GoldenGate
<a name="running-the-replicat-process-of-oracle-goldengate"></a>

 The Replicat process of Oracle GoldenGate is used to push transaction information in the trail files to the destination database.

 The following process enables and starts the Replicat process.

1.  First, configure the Replicat parameter file on the GoldenGate Hub (on-premises or on an Amazon EC2 instance). The following listing shows an example Replicat parameter file:

   ```
   REPLICAT RABC

   SETENV (ORACLE_SID=ORCL)
   SETENV (NLSLANG=AL32UTF8)

   USERID oggadm1@TARGET, password XXXXXX
   ASSUMETARGETDEFS

   MAP EXAMPLE.TABLE, TARGET EXAMPLE.TABLE;
   ```

1.  Launch the Oracle GoldenGate command line interface (`ggsci`). Log in to the destination database. The following example shows the format for logging in:

   ```
   dblogin userid <user>@<db tnsname>
   ```

1.  Using the `ggsci` command line, add a checkpoint table. Note that *user* indicates the Oracle GoldenGate user account, not the owner of the destination table schema. The following example creates a checkpoint table named` gg_checkpoint`:

   ```
   add checkpointtable <user>.gg_checkpoint
   ```

1.  To enable the Replicat process, use the following command:

   ```
   add replicat <replicat name> EXTTRAIL <extract trail file>
   CHECKPOINTTABLE <user>.gg_checkpoint
   ```

1.  To start the Replicat process, use the following command:

   ```
   start <replicat name>
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
