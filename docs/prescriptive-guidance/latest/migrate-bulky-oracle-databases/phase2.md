---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase2.html
---

# Phase 2: Roll-forward phase
<a name="phase2"></a>

You can repeat the roll-forward phase as many times as necessary to catch the destination data file up to the source database.

The roll-forward phase consists of the following steps.

1. Create an incremental backup from the source database.

1. Transfer the backup to the destination system.

1. Convert the backup to the destination system endian format.

1. Apply the backup to the converted destination data file copies to roll them forward.

Each successive incremental backup takes less time and brings the destination data file copies closer to the current state of the source database.

## Step 1: Take incremental backups in parallel
<a name="step-1--take-incremental-backups-in-parallel.48c9c77f-c847-5d7e-ab69-cb91031fadab"></a>

Take incremental backups of the tablespace groups being transported on the source system in parallel.

This step creates incremental backups for all tablespaces that are listed in the xtt.properties file.

If you activate the **BLOCK CHANGE TRACKING** feature on the source system, you can reduce the time that the incremental backup takes.

The following command recognizes the next SCN after the full backup automatically.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl --backup --debug 3
```

## Step 2: Transfer the incremental backups and res.txt file to the destination system
<a name="step-2--transfer-the-incremental-backups-and-res.txt-file-to-the-destination-system.b6868802-45cd-564f-9917-2207a2011a82"></a>

If you have enough bandwidth, you can reduce the transfer time by using Direct Connect.

Transfer the incremental backups between *src\_scratch\_location* and *dest\_scratch\_location*. Transfer the res.txt file between $TMPDIR on the source system and $TMPDIR on the destination system.

If you take multiple incremental backups, you must copy the res.txt file after the last incremental backup and before you apply it on the destination system.

```
[source]$ scp $TMPDIR/res.txt oracle@[dest]:/u01/oracle/expimp/out/out<nn>
[source]$ scp <src_scratch_location>/* oracle@[dest]:<dest_scratch_location>
```

## Step 3: Convert and apply incremental backups
<a name="step-3--convert-and-apply-incremental-backups.ca01b748-83c4-5119-9a88-28685f7ef5a8"></a>

Convert incremental backups to the destination system endian format and apply incremental backups to the destination data file copies on the destination system.

This guide assumes that you have four tablespace groups. Run the xttdriver.pl command with the --restore option for each tablespace group.

In this step, the Oracle XTTS utility restarts the target database. To run the command in parallel, make the following customization in the xttdriver.pl Perl script.

1. Comment out the following lines:
   + Line 4867:      my $outputstart =  `sqlplus -L -s \\"/ as sysdba\\" \\@xttstartupnomount.sql`;
   + Line 4868:      checkError ("Error in executing xttstartupnomount.sql", $outputstart);
   + Line 4992:      my $outputstart =  `sqlplus -L -s \\"/ as sysdba\\" \\@xttdbopen.sql`;\\

1. Set the target database to NOMOUNT status.

   ```
   sqlplus / as sysdba @xttstartupnomount.sql
   ```

1. Perform a roll forward of the incremental backups in parallel.

   ```
   cd /u01/oracle/expimp/xtt<nn>
   export TMPDIR=/u01/oracle/expimp/out/out<nn>
   $ORACLE_HOME/perl/bin/perl xttdriver.pl --restore --debug 3
   ```

1. After you roll forward all incremental backups, set the target database to OPEN status.

   ```
   sqlplus / as sysdba @xttdbopen.sql
   ```

At this point, you can repeat phase 2 until the SCNs on the source and destination databases are close enough. Decide whether to proceed to phase 3 or repeat phase 2, depending on your target downtime.

To reduce the downtime during phase 3 (the transport phase), you can export and import the metadata of nonsegment-based objects, such as USER, PACKAGE, PROCEDURE, and FUNCTION, before you set the source database as READ ONLY.

If the source database contains a very large number of objects (hundreds of thousands), exporting and importing the metadata can take several hours. In this case, export and import the metadata of nonsegment-based objects before you set the source database to READ ONLY.

Run the export of nonsegment-based objects while the source system is in read/write mode. Then import the objects to the destination system before you set the source system to READ ONLY. During this time, keep the source database objects, such as PACKAGE, PROCEDURE, and FUNCTION, unchanged.

The following example shows a parameter file that you use to export metadata of nonsegment-based objects, including USER, PACKAGE\_SPEC, PACKAGE\_BODY, PROCEDURE, and FUNCTION.

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

The following example shows a parameter file that you use to import metadata of nonsegment-based objects.

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

At this point, the destination system has no tablespaces except SYSTEM, SYSAUX, UNDO, and TEMP. Therefore, you must remap all objects that you import to the SYSTEM tablespace.

Use the following command to import metadata.

```
SQL> create directory dmpdir as <location>;
impdp system/<system password> parfile=<parameter file>
```

Now you can see the created objects on the destination database.

```
SQL> select object_type, count(*) from dba_objects group by object_type order by count(*) desc;
OBJECT_TYPE                  COUNT(*)
------------------------------- ----------
SYNONYM                          89327
PACKAGE                           55670
PACKAGE BODY                  54447
VIEW                                 41378
JAVA CLASS                        31978
SEQUENCE                         12766
…..
```

The import creates the USER object with USERS as the default tablespace. During phase 3, you create the transportable tablespaces, and then you alter the USER objects to use the original default tablespaces.
