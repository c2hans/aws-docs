---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase4.html
---

# Phase 4: Validate
<a name="phase4"></a>

## Step 1: Check tablespaces for corruption
<a name="step-1--check-tablespaces-for-corruption.45075a61-7f65-5923-816f-186548ec485f"></a>

In this step, the transported tablespaces are read only in the destination database. You can validate whether the tablespaces are valid or not by running the RMAN command as follows.

```
sqlplus / as sysdba;
set feedback off
set pagesize 0
set heading off
spool tbs_val.sql;
select 'validate tablespace '||tablespace_name||' check logical;' from dba_tablespaces where tablespace_name not in ('SYSTEM','SYSAUX','TEMP','USERS','UNDOTBS1','UNDOTBS2','UNDOTBS3','UNDOTBS3','UNDOTBS4');
spool off;
exit;

--Remove the first and last line in the spool file, tbs_val.sql
rman target /
RMAN> @tbs_val.sql
```

In addition, you can check the count of the objects, such as the table, index, synonym, view, and package objects.

## Step 2. Make all transported tablespaces in the destination database read/write
<a name="step-2.-make-all-transported-tablespaces-in-the-destination-database-read-write.07d52143-b0e3-579d-b55a-b94ae01d9e92"></a>

```
sqlplus / as sysdba;
set feedback off
set pagesize 0
set heading off
spool tbs_rw.sql
select 'alter tablespace '||tablespace_name||' read write;' from dba_tablespaces where status='READ ONLY';
spool off;
exit;
--Remove the first and last line in the spool file, tbs_rw.sql
sqlplus / as sysdba;
SQL> @tbs_rw.sql
```
