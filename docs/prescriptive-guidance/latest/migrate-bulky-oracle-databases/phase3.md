---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase3.html
---

# Phase 3: Transport phase

During this phase, the source system becomes read-only. You make the data files on the destination system consistent with the source system by applying a final incremental backup. Then, export the object metadata from the source system and import it into the destination system.

## Step 1: Make the tablespaces in the source database read only
<a name="step-1--make-the-tablespaces-in-the-source-database-read-only.6dcc34d4-2b33-5385-9df1-b89eea077b98"></a>

As SYSDBA, make all tablespaces being transferred READ ONLY on the source system.

To reduce downtime, you can run the following two steps simultaneously.

## Step 2: Create the final incremental backup
<a name="step-2--create-the-final-incremental-backup.4073a9a5-9822-5bf2-bfbe-42a8e1ade448"></a>

On the source system, create the final incremental backup of the tablespaces being transferred.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl --backup --debug 3
```

This step returns an expected error, such as "ORA-20001: TABLESPACE(S) IS READONLY". You can ignore this error.

## Step 3: Export the metadata
<a name="step-3--export-the-metadata.4c0fd916-542b-5e79-9bbb-2d89a2921f4d"></a>

Export the metadata of the transportable tablespaces from the source database.

This is an example of the parameter file for exporting the metadata of the transportable tablespaces.

```
directory=dmpdir
metrics=y
dumpfile=xttsmeta%U.dmp
filesize=1048576000
logfile=expxtts.log
transport_tablespaces=
APPS_TS_ARCHIVE,
APPS_TS_INTERFACE,
APPS_TS_MEDIA,
APPS_TS_NOLOGGING,
….
exclude=table_statistics,index_statistics
```

In addition, if the source system has many tables and indexes, you can save time during exporting by excluding their statistics. After you import the transportable tablespace, import the statistics to the destination system.

Before you run expdp, create a database directory where dump files are stored on the source system.

```
SQL> create directory dmpdir as <location>;
expdp system/<system password> parfile=<parameter file>
```

The following two steps are the final steps for cross-platform transportable tablespace with RMAN incremental backups. Perform these steps sequentially.

## Step 4: Transfer the files and apply the final incremental backup
<a name="step-4--transfer-the-files-and-apply-the-final-incremental-backup.847c0540-03fb-5a3b-bbe3-141a963720bc"></a>

Transfer the final incremental backup and export dump files to the destination system, convert, and apply the final incremental backup.

Use Direct Connect to transfer the final incremental backup copies and res.txt file to the destination. You can use a VPN connection instead, but Direct Connect can help reduce downtime if it has enough bandwidth.

To restore the final incremental backup, on the destination system, run the following command, using the --restore option, for each tablespace group.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl --restore --debug 3
```

## Step 5: Import the object metadata
<a name="step-5--import-the-object-metadata.3d711943-ba3c-56ae-aa7f-7a1bd0064022"></a>

Import the object metadata into the destination system by using Oracle Data Pump. Run the following command to get the list of data files for the transport\_datafiles= parameter on the destination system.

```
cd /u01/oracle/expimp/xtt<nn>
export TMPDIR=/u01/oracle/expimp/out/out<nn>
$ORACLE_HOME/perl/bin/perl xttdriver.pl -e
```

Whenever you run the previous command, you get the xttplugin.txt file, which has the transport\_datafiles= parameter. Merge transport\_datafiles= in a single line from all the xttplugin.txt files, and put the data file lists into the transport\_datafiles argument of the parameter file for the import metadata.

The following code snippet shows the parameter file for importing the transportable tablespace on the destination system.

```
directory=dmpdir
metrics=y
dumpfile=xttsmeta%U.dmp
logfile=impxtts.log
exclude=TYPE
transport_datafiles= '+EBSDATA/APPS_TS_TX_DATA_2.dbf','+EBSDATA/APPS_TS_TX_DATA_11.dbf','+EBSDATA/APPS_TS_TX_DATA_22.dbf','+EBSDATA/APPS_TS_TX_DATA_183.dbf','+EBSDATA/APPS_TS_TX_DATA_204.dbf','+EBSDATA/APPS_TS_TX_DATA_219.dbf','+EBSDATA/APPS_TS_TX_DATA_227.dbf'…..
```

Before running impdp, create a database directory pointing to the location of the export dump files.

```
SQL> create directory dmpdir as <location>;
impdp system/<system password> parfile=<parameter file>
```
