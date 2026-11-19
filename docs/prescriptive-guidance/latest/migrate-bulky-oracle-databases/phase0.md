---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/phase0.html
---

# Phase 0: Setup phase

1. Install Oracle Database 12.1.0.2 or later on the target [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instance.

1. Verify the target database.

   You must verify that the target database instance has the same time zone and character set as the source database. If they differ, this migration approach fails.

   To check that the time zone version is the same in the source and target databases, run the following command.

   ```
   SQL> select * from v$timezone_file;
   FILENAME            VERSION    CON_ID
   -----------------------   -------------   ----------
   timezlrg_14.dat        14               0
   ```

   To check that both the DB character set and the national character set are the same in the source and target, run the following command.

   ```
   SQL> select * from nls_database_parameters
            where parameter in ('NLS_CHARACTERSET','NLS_NCHAR_CHARACTERSET');
   PARAMETER                                  VALUE
   --------------------------------------------   --------------------
   NLS_NCHAR_CHARACTERSET         UTF8
   NLS_CHARACTERSET                    AL32UTF8
   ```

1. Set up the Oracle XTTS utility.

   On the source system, download and extract the script file [rman\_xttconvert\_VER4.zip](https://support.oracle.com/epmos/main/downloadattachmentprocessor?attachid=2471245.1%3ARMAN_XTTS_VER4&docType=REFERENCE&action=download) from Oracle document 2471245.1. Update the parameters in the xtt.properties file to match your environment configuration. Then copy the xtt.properties and xttdriver.pl scripts to the target system.
