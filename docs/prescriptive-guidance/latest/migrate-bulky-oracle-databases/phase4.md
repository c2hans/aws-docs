---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase4.html
---

# Phase 4: Validate

## Step 1: Check tablespaces for corruption
<a name="step-1--check-tablespaces-for-corruption.54856f81-03d4-5555-a587-2f048c06f914"></a>

In this step, the transported tablespaces are read-only in the destination database. You can validate the tablespaces by running the following Oracle Recovery Manager (RMAN) commands.

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

You can also check the number of objects, such as tables, indexes, synonyms, views, and packages.

## Step 2: Make all transported tablespaces in the destination database read/write
<a name="step-2--make-all-transported-tablespaces-in-the-destination-database-read-write.988b5542-938b-5b99-af03-e2aae320d173"></a>

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
