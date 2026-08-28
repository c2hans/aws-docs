---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase2.html
---

# Phase 2: Roll-forward phase
<a name="phase2"></a>

You can repeat the roll-forward phase as many times as necessary to catch the destination data file up to source database.

The roll-forward phase consists of the following steps.

1. Create an incremental backup from the source database.

1. Transfer the backup to the destination system.

1. Convert the backup to the destination system endian format.

1. Apply the backup to the converted destination data file copies to roll them forward.

Each successive incremental backup should take less time and will bring the destination data file copies more current with the source database.

## Step 1: Take incremental backups in parallel
<a name="step-1--take-incremental-backups-in-parallel.0174b06b-14b6-5fa5-b0d8-66d606922acf"></a>

Take incremental backups of the tablespace groups being transported on the source system in parallel.

This step creates incremental backups for all tablespaces= that are listed in the xtt.properties file.

If you can activate the **BLOCK CHANGE TRACKING** feature on the source system, you can greatly reduce the time of the incremental backup.

The following command recognizes the next SCN after the full backup automatically.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl --backup --debug 3
```

## Step 2: Transfer the incremental backups and res.txt file to the destination system
<a name="step-2--transfer-the-incremental-backups-and-res.txt-file-to-the-destination-system.c5544a26-98c4-5b16-b9e5-4e7ef38cef08"></a>

If you have enough bandwidth, you can reduce the transferring duration by using Direct Connect.

Transfer the incremental backups between  *src\_scratch\_location* and *dest\_scratch\_location*. Transfer the res.txt file between $TMPDIR on the source system and $TMPDIR on the destination system.

If you take multiple incremental backups, the res.txt file must be copied after the last incremental backup before it can be applied on destination system.

```
[source]$ scp $TMPDIR/res.txt oracle@[dest]:/u01/oracle/expimp/out/out<nn>
[source]$ scp <src_scratch_location>/* oracle@[dest]:<dest_scratch_location>
```

## Step 3: Convert and apply incremental backups
<a name="step-3--convert-and-apply-incremental-backups.99034c45-599c-5f57-b1c5-0aef3e3b1b34"></a>

Convert incremental backups to the destination system endian format and apply incremental backups to the destination data file copies on the destination system.

In this guide, suppose that tablespace groups are four. Run each xttdriver.pl command with the --restore option for each tablespace group.

In this step, the Oracle XTTS utility takes the target database to be restarted. To run the command in parallel, you must use the following customization in the Perl script, xttdriver.pl.

1. Comment out the following lines:
   + Line 4867:      my $outputstart =  `sqlplus -L -s \\"/ as sysdba\\" \\@xttstartupnomount.sql`;
   + Line 4868:      checkError ("Error in executing xttstartupnomount.sql", $outputstart);
   + Line 4992:      my $outputstart =  `sqlplus -L -s \\"/ as sysdba\\" \\@xttdbopen.sql`;\\

1. Make the target DB in NOMOUNTstatus.

   ```
   sqlplus / as sysdba @xttstartupnomount.sql
   ```

1. Perform a roll forward of the incremental backups in parallel.

   ```
   cd /u01/oracle/expimp/xtt<nn>
   export TMPDIR=/u01/oracle/expimp/out/out<nn>
   $ORACLE_HOME/perl/bin/perl xttdriver.pl --restore --debug 3
   ```

1. After rolling forward all incremental backups, set the target DB in OPENstatus.

   ```
   sqlplus / as sysdba @xttdbopen.sql
   ```

At this point, you can repeat phase 2 until the SCNs on the source and destination databases get close enough. You must decide to whether go forward to phase 3 or repeat phase 2, depending on given target downtime.

To reduce the downtime during phase 3 (the transport phase), you can export and import the metadata of nonsegment-based objects, such as USER, PACKAGE, PROCEDURE, and FUNCTION, before you set the source database as READ ONLY.

If the number of database objects in the source database is extremely large (hundreds of thousands), exporting and importing the metadata will take several hours. In this case, consider exporting metadata.

Exporting nonsegment-based objects is run in read/write on the source system. Then you must import the objects to the destination system before the source system is set to READ ONLY. At this time, you must keep the database source objects such as PACKAGE, PROCEDURE, and FUNCTION unchanged.

This is an example of the dump parameter file that is used to export metadata of nonsegment-based objects, including USER, PACKAGE\_SPEC, PACKAGE\_BODY, PROCEDURE, and FUNCTION.

```
directory=dmpdir
dumpfile=xttsmsc%U.dmp
full=y
filesize=1048576000
logfile=expmsc.log
metrics=y
exclude=TABLE,INDEX,CONSTRAINT,COMMENT,
MATERIALIZED_VIEW,MATERIALIZED_VIEW_LOG,SCHEMA_CALLOUT
```

Use the following command to export metadata.

```
SQL> create directory dmpdir as <location>;
expdp system/<system password> parfile=<parameter file>
```

This is an example of the dump parameter file to import metadata of nonsegment objects.

```
directory=dmpdir
dumpfile=xttsmsc%U.dmp
full=y
logfile=impmsc1.log
EXCLUDE=TABLESPACE, PROCOBJ, RLS_CONTEXT, RLS_GROUP, RLS_POLICY, TABLESPACE_QUOTA
metrics=y
remap_tablespace=
APPS_TS_ARCHIVE:SYSTEM,
APPS_TS_INTERFACE:SYSTEM,
APPS_TS_SEED:SYSTEM,
APPS_TS_SUMMARY:SYSTEM,
…..
```

At this time, there are no tablespaces except SYSTEM, SYSAUX, UNDO, and TEMP on the destination system. So you must remap all objects to be imported to the SYSTEM tablespace.

Use the following command to import metadata.

```
SQL> create directory dmpdir as <location>;
impdp system/<system password> parfile=<parameter file>
```

Now you can see the created objects on the destination database.

```
SQL> select object_type, count(*) from dba_objects group by object_type order by count(*) desc;
OBJECT_TYPE                  COUNT(*)
------------------------------- ----------
SYNONYM                          89327
PACKAGE                           55670
PACKAGE BODY                  54447
VIEW                                 41378
JAVA CLASS                        31978
SEQUENCE                         12766
…..
```

There are no tablespaces except SYSTEM,/span>, SYSAUX, UNDO, and TEMP. The USER object is created with USERS as the default tablespace. During phase 3, the transportable tablespaces will be created, and then the USER objects will be altered with the original default tablespaces.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
