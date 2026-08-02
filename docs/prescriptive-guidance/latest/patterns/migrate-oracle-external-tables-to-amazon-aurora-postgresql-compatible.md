---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible.html
---

# Migrate Oracle external tables to Amazon Aurora PostgreSQL-Compatible
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible"></a>

*anuradha chintha and Rakesh Raghav, Amazon Web Services*

## Summary
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-summary"></a>

External tables give Oracle the ability to query data that is stored outside the database in flat files. You can use the ORACLE\_LOADER driver to access any data stored in any format that can be loaded by the SQL\*Loader utility. You can't use Data Manipulation Language (DML) on external tables, but you can use external tables for query, join, and sort operations.

Amazon Aurora PostgreSQL-Compatible Edition doesn't provide functionality similar to external tables in Oracle. Instead, you must use modernization to develop a scalable solution that meets functional requirements and is frugal.

This pattern provides steps for migrating different types of Oracle external tables to Aurora PostgreSQL-Compatible Edition on the Amazon Web Services (AWS) Cloud by using the `aws_s3` extension.

We recommend thoroughly testing this solution before implementing it in a production environment.

## Prerequisites and limitations
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Command Line Interface (AWS CLI)
+ An available Aurora PostgreSQL-Compatible database instance.
+ An on-premises Oracle database with an external table
+ pg.Client API
+ Data files

**Limitations **
+ This pattern doesn't provide the functionality to act as a replacement for Oracle external tables. However, the steps and sample code can be enhanced further to achieve your database modernization goals.
+ Files should not contain the character that is passing as a delimiter in `aws_s3` export and import functions.

**Product versions**
+ To import from Amazon S3 into RDS for PostgreSQL the database must be running PostgreSQL version 10.7 or later.

## Architecture
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-architecture"></a>

**Source technology stack  **
+ Oracle

**Source architecture **

![Diagram of data files going to a directory and table in the on-premises Oracle database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/555e69af-36fc-4ff5-b66c-af22b4cf262a/images/3fbc507d-b0fa-4e05-b999-043dc7327ed7.png)

**Target technology stack **
+ Amazon Aurora PostgreSQL-Compatible
+ Amazon CloudWatch
+ AWS Lambda
+ AWS Secrets Manager
+ Amazon Simple Notification Service (Amazon SNS)
+ Amazon Simple Storage Service (Amazon S3)

**Target architecture **

The following diagram shows a high-level representation of the solution.

![The description is after the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/555e69af-36fc-4ff5-b66c-af22b4cf262a/images/5421540e-d2e3-4361-89cc-d8415fcb21fd.png)

1. Files are uploaded to the S3 bucket.

1. The Lambda function is initiated.

1. The Lambda function initiates the DB function call.

1. Secrets Manager provides the credentials for database access.

1. Depending on the DB function, an SNS alarm is created.

**Automation and scale**

Any additions or changes to the external tables can be handled with metadata maintenance.

## Tools
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-tools"></a>
+ [Amazon Aurora PostgreSQL-Compatible](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) – Amazon Aurora PostgreSQL-Compatible Edition is a fully managed, PostgreSQL-compatible, and ACID-compliant relational database engine that combines the speed and reliability of high-end commercial databases with the cost-effectiveness of open-source databases.
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) – AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With only one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) – Amazon CloudWatch monitors Amazon S3 resources and utilization.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a serverless compute service that supports running code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. In this pattern, Lambda runs the database function whenever a file is uploaded to Amazon S3.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) – AWS Secrets Manager is a service for credential storage and retrieval. Using Secrets Manager, you can replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) provides a storage layer to receive and store files for consumption and transmission to and from the Aurora PostgreSQL-Compatible cluster.
+ [aws\_s3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.html#aws_s3.table_import_from_s3) – The `aws_s3` extension integrates Amazon S3 and Aurora PostgreSQL-Compatible.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) coordinates and manages the delivery or sending of messages between publishers and clients. In this pattern, Amazon SNS is used to send notifications.

**Code **

Whenever a file is placed in the S3 bucket, a DB function must be created and called from the processing application or the Lambda function. For details, see the code (attached).

## Epics
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-epics"></a>

### Create an external file
<a name="create-an-external-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add an external file to the source database. | Create an external file, and move it to the `oracle` directory. | DBA |

### Configure the target (Aurora PostgreSQL-Compatible)
<a name="configure-the-target-aurora-postgresql-compatible"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Aurora PostgreSQL database. | Create a DB instance in your Amazon Aurora PostgreSQL-Compatible cluster. | DBA |
| Create a schema, aws\_s3 extension, and tables. | Use the code under `ext_tbl_scripts` in the *Additional information* section. The tables include actual tables, staging tables, error and log tables, and a metatable. | DBA, Developer |
| Create the DB function. | To create the DB function, use the code under  `load_external_table_latest` function in the *Additional information* section. | DBA, Developer |

### Create and configure the Lambda function
<a name="create-and-configure-the-lambda-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a role. | Create a role with permissions to access Amazon S3 and Amazon Relational Database Service (Amazon RDS). This role will be assigned to Lambda for running the pattern. | DBA |
| Create the Lambda function. | Create a Lambda function that reads the file name from Amazon S3 (for example, `file_key = info.get('object', {}).get('key')`) and calls the DB function (for example, `curs.callproc("load_external_tables", [file_key])`) with the file name as the input parameter.<br />Depending on the function call result, an SNS notification will be initiated (for example, `client.publish(TopicArn='arn:',Message='fileloadsuccess',Subject='fileloadsuccess')`).<br />Based on your business needs, you can create a Lambda function with extra code if required. For more information, see the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). | DBA |
| Configure an S3 bucket event trigger. | Configure a mechanism to call the Lambda function for all object creation events in the S3 bucket. | DBA |
| Create a secret. | Create a secret name for the database credentials by using Secrets Manager. Pass the secret in the Lambda function. | DBA |
| Upload the Lambda supporting files. | Upload a .zip file that contains the Lambda support packages and the attached Python script for connecting to Aurora PostgreSQL-Compatible. The Python code calls the function that you created in the database. | DBA |
| Create an SNS topic. | Create an SNS topic to send mail for the success or failure of the data load. | DBA |

### Add integration with Amazon S3
<a name="add-integration-with-amazon-s3"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | On the Amazon S3 console, create an S3 bucket with a unique name that does not contain leading slashes. An S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. | DBA |
| Create IAM policies. | To create the AWS Identity and Access Management (IAM) policies, use the code under `s3bucketpolicy_for_import` in the *Additional information* section. | DBA |
| Create roles. | Create two roles for Aurora PostgreSQL-Compatible, one role for Import and one role for Export. Assign the corresponding policies to the roles. | DBA |
| Attach the roles to the Aurora PostgreSQL-Compatible cluster. | Under **Manage roles**, attach the Import and Export roles to the Aurora PostgreSQL cluster. | DBA |
| Create supporting objects for Aurora PostgreSQL-Compatible. | For the table scripts, use the code under `ext_tbl_scripts` in the *Additional information* section.<br />For the custom function, use the code under `load_external_Table_latest` in the *Additional information* section. | DBA |

### Process a test file
<a name="process-a-test-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload a file into the S3 bucket. | To upload a test file into the S3 bucket, use the console or the following command in AWS CLI. <pre>aws s3 cp /Users/Desktop/ukpost/exttbl/"testing files"/aps s3://s3importtest/inputext/aps</pre><br />As soon as the file is uploaded, a bucket event initiates the Lambda function, which runs the Aurora PostgreSQL-Compatible function. | DBA |
| Check the data and the log and error files. | The Aurora PostgreSQL-Compatible function loads the files into the main table, and it creates `.log` and `.bad` files in the S3 bucket. | DBA |
| Monitor the solution. | In the Amazon CloudWatch console, monitor the Lambda function. | DBA |

## Related resources
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-resources"></a>
+ [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [Working with Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
+ [Setting up Amazon SNS notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html)

## Additional information
<a name="migrate-oracle-external-tables-to-amazon-aurora-postgresql-compatible-additional"></a>

**ext\_table\_scripts**

```
CREATE EXTENSION aws_s3 CASCADE;
CREATE TABLE IF NOT EXISTS meta_EXTERNAL_TABLE
(
    table_name_stg character varying(100) ,
    table_name character varying(100)  ,
    col_list character varying(1000)  ,
    data_type character varying(100)  ,
    col_order numeric,
    start_pos numeric,
    end_pos numeric,
    no_position character varying(100)  ,
    date_mask character varying(100)  ,
    delimeter character(1)  ,
    directory character varying(100)  ,
    file_name character varying(100)  ,
    header_exist character varying(5)
);
CREATE TABLE IF NOT EXISTS ext_tbl_stg
(
    col1 text
);
CREATE TABLE IF NOT EXISTS error_table
(
    error_details text,
    file_name character varying(100),
    processed_time timestamp without time zone
);
CREATE TABLE IF NOT EXISTS log_table
(
    file_name character varying(50) COLLATE pg_catalog."default",
    processed_date timestamp without time zone,
    tot_rec_count numeric,
    proc_rec_count numeric,
    error_rec_count numeric
);
sample insert scripts of meta data:
INSERT INTO meta_EXTERNAL_TABLE (table_name_stg, table_name, col_list, data_type, col_order, start_pos, end_pos, no_position, date_mask, delimeter, directory, file_name, header_exist) VALUES ('F_EX_APS_TRANSACTIONS_STG', 'F_EX_APS_TRANSACTIONS', 'source_filename', 'character varying', 2, 8, 27, NULL, NULL, NULL, 'databasedev', 'externalinterface/loaddir/APS', 'NO');
INSERT INTO meta_EXTERNAL_TABLE (table_name_stg, table_name, col_list, data_type, col_order, start_pos, end_pos, no_position, date_mask, delimeter, directory, file_name, header_exist) VALUES ('F_EX_APS_TRANSACTIONS_STG', 'F_EX_APS_TRANSACTIONS', 'record_type_identifier', 'character varying', 3, 28, 30, NULL, NULL, NULL, 'databasedev', 'externalinterface/loaddir/APS', 'NO');
INSERT INTO meta_EXTERNAL_TABLE (table_name_stg, table_name, col_list, data_type, col_order, start_pos, end_pos, no_position, date_mask, delimeter, directory, file_name, header_exist) VALUES ('F_EX_APS_TRANSACTIONS_STG', 'F_EX_APS_TRANSACTIONS', 'fad_code', 'numeric', 4, 31, 36, NULL, NULL, NULL, 'databasedev', 'externalinterface/loaddir/APS', 'NO');
INSERT INTO meta_EXTERNAL_TABLE (table_name_stg, table_name, col_list, data_type, col_order, start_pos, end_pos, no_position, date_mask, delimeter, directory, file_name, header_exist) VALUES ('F_EX_APS_TRANSACTIONS_STG', 'F_EX_APS_TRANSACTIONS', 'session_sequence_number', 'numeric', 5, 37, 42, NULL, NULL, NULL, 'databasedev', 'externalinterface/loaddir/APS', 'NO');
INSERT INTO meta_EXTERNAL_TABLE (table_name_stg, table_name, col_list, data_type, col_order, start_pos, end_pos, no_position, date_mask, delimeter, directory, file_name, header_exist) VALUES ('F_EX_APS_TRANSACTIONS_STG', 'F_EX_APS_TRANSACTIONS', 'transaction_sequence_number', 'numeric', 6, 43, 48, NULL, NULL, NULL, 'databasedev', 'externalinterface/loaddir/APS', 'NO');
```

**s3bucketpolicy\_for import**

```
---Import role policy
--Create an IAM policy to allow, Get,  and list actions on S3 bucket
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "s3import",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::s3importtest",
                "arn:aws:s3:::s3importtest/*"
            ]
        }
    ]
}
--Export Role policy
--Create an IAM policy to allow, put,  and list actions on S3 bucket
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "s3export",
            "Action": [
                "S3:PutObject",
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::s3importtest/*"
            ]
        }
    ]
}
```

**Sample DB function load\_external\_tables\_latest**

```
CREATE OR REPLACE FUNCTION public.load_external_tables(pi_filename text)
 RETURNS character varying
 LANGUAGE plpgsql
AS $function$
/* Loading data from S3 bucket into a APG table */
DECLARE
 v_final_sql TEXT;
 pi_ext_table TEXT;
 r refCURSOR;
 v_sqlerrm text;
 v_chunk numeric;
 i integer;
 v_col_list TEXT;
 v_postion_list CHARACTER VARYING(1000);
 v_len  integer;
 v_delim varchar;
 v_file_name CHARACTER VARYING(1000);
 v_directory CHARACTER VARYING(1000);
 v_table_name_stg CHARACTER VARYING(1000);
 v_sql_col TEXT;
 v_sql TEXT;
 v_sql1 TEXT;
 v_sql2 TEXT;
 v_sql3 TEXT;
 v_cnt integer;
 v_sql_dynamic TEXT;
 v_sql_ins TEXT;
 proc_rec_COUNT integer;
 error_rec_COUNT integer;
 tot_rec_COUNT integer;
 v_rec_val integer;
 rec record;
 v_col_cnt integer;
 kv record;
 v_val text;
 v_header text;
 j integer;
 ERCODE VARCHAR(5);
 v_region text;
 cr CURSOR FOR
 SELECT distinct DELIMETER,
   FILE_NAME,
   DIRECTORY
 FROM  meta_EXTERNAL_TABLE
 WHERE table_name = pi_ext_table
   AND DELIMETER IS NOT NULL;

 cr1 CURSOR FOR
   SELECT   col_list,
   data_type,
   start_pos,
   END_pos,
   concat_ws('',' ',TABLE_NAME_STG) as TABLE_NAME_STG,
   no_position,date_mask
 FROM  meta_EXTERNAL_TABLE
 WHERE table_name = pi_ext_table
 order by col_order asc;
cr2 cursor FOR
SELECT  distinct table_name,table_name_stg
   FROM  meta_EXTERNAL_TABLE
   WHERE upper(file_name) = upper(pi_filename);

BEGIN
 -- PERFORM utl_file_utility.init();
   v_region := 'us-east-1';
   /* find tab details from file name */

   --DELETE FROM  ERROR_TABLE WHERE file_name= pi_filename;
  -- DELETE FROM  log_table WHERE file_name= pi_filename;

 BEGIN

   SELECT distinct table_name,table_name_stg INTO strict pi_ext_table,v_table_name_stg
   FROM  meta_EXTERNAL_TABLE
   WHERE upper(file_name) = upper(pi_filename);
 EXCEPTION
   WHEN NO_DATA_FOUND THEN
    raise notice 'error 1,%',sqlerrm;
    pi_ext_table := null;
    v_table_name_stg := null;
      RAISE USING errcode = 'NTFIP' ;
    when others then
        raise notice 'error others,%',sqlerrm;
 END;
 j :=1 ;

for rec in  cr2
 LOOP

  pi_ext_table     := rec.table_name;
  v_table_name_stg := rec.table_name_stg;
  v_col_list := null;

 IF pi_ext_table IS NOT NULL
  THEN
    --EXECUTE concat_ws('','truncate table  ' ,pi_ext_table) ;
   EXECUTE concat_ws('','truncate table  ' ,v_table_name_stg) ;

       SELECT distinct DELIMETER INTO STRICT v_delim
       FROM  meta_EXTERNAL_TABLE
       WHERE table_name = pi_ext_table;

       IF v_delim IS NOT NULL THEN
     SELECT distinct DELIMETER,
       FILE_NAME,
       DIRECTORY ,
       concat_ws('',' ',table_name_stg),
       case  header_exist when 'YES' then 'CSV HEADER' else 'CSV' end as header_exist
     INTO STRICT v_delim,v_file_name,v_directory,v_table_name_stg,v_header
     FROM  meta_EXTERNAL_TABLE
     WHERE table_name = pi_ext_table
       AND DELIMETER IS NOT NULL;

     IF    upper(v_delim) = 'CSV'
     THEN
       v_sql := concat_ws('','SELECT aws_s3.table_import_FROM_s3 ( ''',
       v_table_name_stg,''','''',
       ''DELIMITER '''','''' CSV HEADER QUOTE ''''"'''''', aws_commons.create_s3_uri ( ''',
       v_directory,''',''',v_file_name,''', ''',v_region,'''))');
       ELSE
       v_sql := concat_ws('','SELECT aws_s3.table_import_FROM_s3(''',
           v_table_name_stg, ''','''', ''DELIMITER AS ''''^''''',''',','
          aws_commons.create_s3_uri
           ( ''',v_directory, ''',''',
           v_file_name, ''',',
            '''',v_region,''')
          )');
          raise notice 'v_sql , %',v_sql;
       begin
        EXECUTE  v_sql;
       EXCEPTION
         WHEN OTHERS THEN
           raise notice 'error 1';
         RAISE USING errcode = 'S3IMP' ;
       END;

       select count(col_list) INTO v_col_cnt
       from  meta_EXTERNAL_TABLE where table_name = pi_ext_table;

        -- raise notice 'v_sql 2, %',concat_ws('','update ',v_table_name_stg, ' set col1 = col1||''',v_delim,'''');

       execute concat_ws('','update ',v_table_name_stg, ' set col1 = col1||''',v_delim,'''');

       i :=1;
       FOR rec in cr1
       loop
       v_sql1 := concat_ws('',v_sql1,'split_part(col1,''',v_delim,''',', i,')',' as ',rec.col_list,',');
       v_sql2 := concat_ws('',v_sql2,rec.col_list,',');
   --    v_sql3 := concat_ws('',v_sql3,'rec.',rec.col_list,'::',rec.data_type,',');

       case
         WHEN upper(rec.data_type) = 'NUMERIC'
         THEN v_sql3 := concat_ws('',v_sql3,' case WHEN length(trim(split_part(col1,''',v_delim,''',', i,'))) =0
                THEN null
                 ELSE
                 coalesce((trim(split_part(col1,''',v_delim,''',', i,')))::NUMERIC,0)::',rec.data_type,' END as ',rec.col_list,',') ;
         WHEN UPPER(rec.data_type) = 'TIMESTAMP WITHOUT TIME ZONE' AND rec.date_mask = 'YYYYMMDD'
         THEN v_sql3 := concat_ws('',v_sql3,' case WHEN length(trim(split_part(col1,''',v_delim,''',', i,'))) =0
                THEN null
                 ELSE
                 to_date(coalesce((trim(split_part(col1,''',v_delim,''',', i,'))),''99990101''),''YYYYMMDD'')::',rec.data_type,' END as ',rec.col_list,',');
         WHEN UPPER(rec.data_type) = 'TIMESTAMP WITHOUT TIME ZONE' AND rec.date_mask =  'MM/DD/YYYY hh24:mi:ss'
         THEN v_sql3 := concat_ws('',v_sql3,' case WHEN length(trim(split_part(col1,''',v_delim,''',', i,'))) =0
                THEN null
                 ELSE
                 to_date(coalesce((trim(split_part(col1,''',v_delim,''',', i,'))),''01/01/9999 0024:00:00''),''MM/DD/YYYY hh24:mi:ss'')::',rec.data_type,' END as ',rec.col_list,',');
          ELSE
        v_sql3 := concat_ws('',v_sql3,' case WHEN length(trim(split_part(col1,''',v_delim,''',', i,'))) =0
                THEN null
                 ELSE
                  coalesce((trim(split_part(col1,''',v_delim,''',', i,'))),'''')::',rec.data_type,' END as ',rec.col_list,',') ;
       END case;

       i :=i+1;
       end loop;

         -- raise notice 'v_sql 3, %',v_sql3;

       SELECT trim(trailing ' ' FROM v_sql1) INTO v_sql1;
       SELECT trim(trailing ',' FROM v_sql1) INTO v_sql1;

       SELECT trim(trailing ' ' FROM v_sql2) INTO v_sql2;
       SELECT trim(trailing ',' FROM v_sql2) INTO v_sql2;

       SELECT trim(trailing ' ' FROM v_sql3) INTO v_sql3;
       SELECT trim(trailing ',' FROM v_sql3) INTO v_sql3;

       END IF;
      raise notice 'v_delim , %',v_delim;

     EXECUTE concat_ws('','SELECT COUNT(*) FROM ',v_table_name_stg)  INTO v_cnt;

    raise notice 'stg cnt , %',v_cnt;

    /* if upper(v_delim) = 'CSV' then
       v_sql_ins := concat_ws('', ' SELECT * from ' ,v_table_name_stg );
     else
      -- v_sql_ins := concat_ws('',' SELECT ',v_sql1,'  from (select col1 from ' ,v_table_name_stg , ')sub ');
       v_sql_ins := concat_ws('',' SELECT ',v_sql3,'  from (select col1 from ' ,v_table_name_stg , ')sub ');
       END IF;*/

v_chunk := v_cnt/100;

for i in 1..101
loop
     BEGIN
    -- raise notice 'v_sql , %',v_sql;
       -- raise notice 'Chunk number , %',i;
       v_sql_ins := concat_ws('',' SELECT ',v_sql3,'  from (select col1 from ' ,v_table_name_stg , ' offset ',v_chunk*(i-1), ' limit ',v_chunk,') sub ');

     v_sql := concat_ws('','insert into  ', pi_ext_table ,' ', v_sql_ins);
     -- raise notice 'select statement , %',v_sql_ins;
          -- v_sql := null;
     -- EXECUTE concat_ws('','insert into  ', pi_ext_table ,' ', v_sql_ins, 'offset ',v_chunk*(i-1), ' limit ',v_chunk );
     --v_sql := concat_ws('','insert into  ', pi_ext_table ,' ', v_sql_ins );

     -- raise notice 'insert statement , %',v_sql;

    raise NOTICE 'CHUNK START %',v_chunk*(i-1);
   raise NOTICE 'CHUNK END %',v_chunk;

     EXECUTE v_sql;

  EXCEPTION
       WHEN OTHERS THEN
       -- v_sql_ins := concat_ws('',' SELECT ',v_sql1, '  from (select col1 from ' ,v_table_name_stg , ' )sub ');
         -- raise notice 'Chunk number for cursor , %',i;

    raise NOTICE 'Cursor - CHUNK START %',v_chunk*(i-1);
   raise NOTICE 'Cursor -  CHUNK END %',v_chunk;
         v_sql_ins := concat_ws('',' SELECT ',v_sql3, '  from (select col1 from ' ,v_table_name_stg , ' )sub ');

         v_final_sql := REPLACE (v_sql_ins, ''''::text, ''''''::text);
        -- raise notice 'v_final_sql %',v_final_sql;
         v_sql :=concat_ws('','do $a$ declare  r refcursor;v_sql text; i numeric;v_conname text;  v_typ  ',pi_ext_table,'[]; v_rec  ','record',';
           begin

           open r for execute ''select col1 from ',v_table_name_stg ,'  offset ',v_chunk*(i-1), ' limit ',v_chunk,''';
           loop
           begin
           fetch r into v_rec;
           EXIT WHEN NOT FOUND;

           v_sql := concat_ws('''',''insert into  ',pi_ext_table,' SELECT ',REPLACE (v_sql3, ''''::text, ''''''::text) , '  from ( select '''''',v_rec.col1,'''''' as col1) v'');
            execute v_sql;

           exception
            when others then
          v_sql := ''INSERT INTO  ERROR_TABLE VALUES (concat_ws('''''''',''''Error Name: '''',$$''||SQLERRM||''$$,''''Error State: '''',''''''||SQLSTATE||'''''',''''record : '''',$$''||v_rec.col1||''$$),'''''||pi_filename||''''',now())'';

               execute v_sql;
             continue;
           end ;
           end loop;
           close r;
           exception
           when others then
         raise;
           end ; $a$');
      -- raise notice ' inside excp v_sql %',v_sql;
          execute v_sql;
      --  raise notice 'v_sql %',v_sql;
       END;
  END LOOP;
     ELSE

     SELECT distinct DELIMETER,FILE_NAME,DIRECTORY ,concat_ws('',' ',table_name_stg),
       case  header_exist when 'YES' then 'CSV HEADER' else 'CSV' end as header_exist
       INTO STRICT v_delim,v_file_name,v_directory,v_table_name_stg,v_header
     FROM  meta_EXTERNAL_TABLE
     WHERE table_name = pi_ext_table                  ;
     v_sql := concat_ws('','SELECT aws_s3.table_import_FROM_s3(''',
       v_table_name_stg, ''','''', ''DELIMITER AS ''''#'''' ',v_header,' '',','
      aws_commons.create_s3_uri
       ( ''',v_directory, ''',''',
       v_file_name, ''',',
        '''',v_region,''')
      )');
         EXECUTE  v_sql;

     FOR rec in cr1
     LOOP

      IF rec.start_pos IS NULL AND rec.END_pos IS NULL AND rec.no_position = 'recnum'
      THEN
        v_rec_val := 1;
      ELSE

       case
         WHEN upper(rec.data_type) = 'NUMERIC'
         THEN v_sql1 := concat_ws('',' case WHEN length(trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))) =0
                THEN null
                 ELSE
                 coalesce((trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1)))::NUMERIC,0)::',rec.data_type,' END as ',rec.col_list,',') ;
         WHEN UPPER(rec.data_type) = 'TIMESTAMP WITHOUT TIME ZONE' AND rec.date_mask = 'YYYYMMDD'
         THEN v_sql1 := concat_ws('','case WHEN length(trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))) =0
                THEN null
                 ELSE
                 to_date(coalesce((trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))),''99990101''),''YYYYMMDD'')::',rec.data_type,' END as ',rec.col_list,',');
         WHEN UPPER(rec.data_type) = 'TIMESTAMP WITHOUT TIME ZONE' AND rec.date_mask = 'YYYYMMDDHH24MISS'
         THEN v_sql1 := concat_ws('','case WHEN length(trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))) =0
                THEN null
                 ELSE
                 to_date(coalesce((trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))),''9999010100240000''),''YYYYMMDDHH24MISS'')::',rec.data_type,' END as ',rec.col_list,',');
          ELSE
        v_sql1 := concat_ws('',' case WHEN length(trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))) =0
                THEN null
                 ELSE
                  coalesce((trim(substring(COL1, ',rec.start_pos ,',', rec.END_pos,'-',rec.start_pos ,'+1))),'''')::',rec.data_type,' END as ',rec.col_list,',') ;
       END case;

      END IF;
      v_col_list := concat_ws('',v_col_list ,v_sql1);
     END LOOP;

           SELECT trim(trailing ' ' FROM v_col_list) INTO v_col_list;
           SELECT trim(trailing ',' FROM v_col_list) INTO v_col_list;

           v_sql_col   :=  concat_ws('',trim(trailing ',' FROM v_col_list) , ' FROM  ',v_table_name_stg,' WHERE col1 IS NOT NULL AND length(col1)>0 ');

           v_sql_dynamic := v_sql_col;

           EXECUTE  concat_ws('','SELECT COUNT(*) FROM ',v_table_name_stg) INTO v_cnt;

         IF v_rec_val = 1 THEN
             v_sql_ins := concat_ws('',' select row_number() over(order by ctid) as line_number ,' ,v_sql_dynamic) ;

         ELSE
               v_sql_ins := concat_ws('',' SELECT' ,v_sql_dynamic) ;
           END IF;

     BEGIN
       EXECUTE concat_ws('','insert into  ', pi_ext_table ,' ', v_sql_ins);
           EXCEPTION
              WHEN OTHERS THEN
          IF v_rec_val = 1 THEN
                  v_final_sql := ' select row_number() over(order by ctid) as line_number ,col1 from ';
                ELSE
                 v_final_sql := ' SELECT col1 from';
               END IF;
       v_sql :=concat_ws('','do $a$ declare  r refcursor;v_rec_val numeric := ',coalesce(v_rec_val,0),';line_number numeric; col1 text; v_typ  ',pi_ext_table,'[]; v_rec  ',pi_ext_table,';
             begin
             open r for execute ''',v_final_sql, ' ',v_table_name_stg,' WHERE col1 IS NOT NULL AND length(col1)>0 '' ;
             loop
             begin
             if   v_rec_val = 1 then
             fetch r into line_number,col1;
             else
             fetch r into col1;
             end if;

             EXIT WHEN NOT FOUND;
              if v_rec_val = 1 then
              select line_number,',trim(trailing ',' FROM v_col_list) ,' into v_rec;
              else
                select ',trim(trailing ',' FROM v_col_list) ,' into v_rec;
              end if;

             insert into  ',pi_ext_table,' select v_rec.*;
              exception
              when others then
               INSERT INTO  ERROR_TABLE VALUES (concat_ws('''',''Error Name: '',SQLERRM,''Error State: '',SQLSTATE,''record : '',v_rec),''',pi_filename,''',now());
               continue;
              end ;
               end loop;
             close r;
              exception
              when others then
              raise;
              end ; $a$');
         execute v_sql;

     END;

         END IF;

   EXECUTE concat_ws('','SELECT COUNT(*) FROM  ' ,pi_ext_table)   INTO proc_rec_COUNT;

   EXECUTE concat_ws('','SELECT COUNT(*) FROM  error_table WHERE file_name =''',pi_filename,''' and processed_time::date = clock_timestamp()::date')  INTO error_rec_COUNT;

   EXECUTE concat_ws('','SELECT COUNT(*) FROM ',v_table_name_stg)   INTO tot_rec_COUNT;

   INSERT INTO  log_table values(pi_filename,now(),tot_rec_COUNT,proc_rec_COUNT, error_rec_COUNT);

   raise notice 'v_directory, %',v_directory;

   raise notice 'pi_filename, %',pi_filename;

   raise notice 'v_region, %',v_region;

  perform aws_s3.query_export_to_s3('SELECT replace(trim(substring(error_details,position(''('' in error_details)+1),'')''),'','','';''),file_name,processed_time FROM  error_table WHERE file_name = '''||pi_filename||'''',
   aws_commons.create_s3_uri(v_directory, pi_filename||'.bad', v_region),
   options :='FORmat csv, header, delimiter $$,$$'
   );

raise notice 'v_directory, %',v_directory;

   raise notice 'pi_filename, %',pi_filename;

   raise notice 'v_region, %',v_region;

  perform aws_s3.query_export_to_s3('SELECT * FROM  log_table WHERE file_name = '''||pi_filename||'''',
   aws_commons.create_s3_uri(v_directory, pi_filename||'.log', v_region),
   options :='FORmat csv, header, delimiter $$,$$'
   );

   END IF;
 j := j+1;
 END LOOP;

       RETURN 'OK';
EXCEPTION
    WHEN  OTHERS THEN
  raise notice 'error %',sqlerrm;
   ERCODE=SQLSTATE;
   IF ERCODE = 'NTFIP' THEN
     v_sqlerrm := concat_Ws('',sqlerrm,'No data for the filename');
   ELSIF ERCODE = 'S3IMP' THEN
    v_sqlerrm := concat_Ws('',sqlerrm,'Error While exporting the file from S3');
   ELSE
      v_sqlerrm := sqlerrm;
   END IF;

 select distinct directory into v_directory from  meta_EXTERNAL_TABLE;

 raise notice 'exc v_directory, %',v_directory;

   raise notice 'exc pi_filename, %',pi_filename;

   raise notice 'exc v_region, %',v_region;

  perform aws_s3.query_export_to_s3('SELECT * FROM  error_table WHERE file_name = '''||pi_filename||'''',
   aws_commons.create_s3_uri(v_directory, pi_filename||'.bad', v_region),
   options :='FORmat csv, header, delimiter $$,$$'
   );
    RETURN null;
END;
$function$
```
