---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible.html
---

# Set up Oracle UTL\_FILE functionality on Aurora PostgreSQL-Compatible
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible"></a>

*Rakesh Raghav and anuradha chintha, Amazon Web Services*

## Summary
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-summary"></a>

As part of your migration journey from Oracle to Amazon Aurora PostgreSQL-Compatible Edition on the Amazon Web Services (AWS) Cloud, you might encounter multiple challenges. For example, migrating code that relies on the Oracle `UTL_FILE` utility is always a challenge. In Oracle PL/SQL, the `UTL_FILE` package is used for file operations, such as read and write, in conjunction with the underlying operating system. The `UTL_FILE` utility works for both server and client machine systems.

Amazon Aurora PostgreSQL-Compatible is a managed database offering. Because of this, it isn't possible to access files on the database server. This pattern walks you through the integration of Amazon Simple Storage Service (Amazon S3) and Amazon Aurora PostgreSQL-Compatible to achieve a subset of `UTL_FILE` functionality. Using this integration, we can create and consume files without using third-party extract, transform, and load (ETL) tools or services.

Optionally, you can set up Amazon CloudWatch monitoring and Amazon SNS notifications.

We recommend thoroughly testing this solution before implementing it in a production environment.

## Prerequisites and limitations
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ AWS Database Migration Service (AWS DMS) expertise
+ Expertise in PL/pgSQL coding
+ An Amazon Aurora PostgreSQL-Compatible cluster
+ An S3 bucket

**Limitations **

This pattern doesn't provide the functionality to act as a replacement for the Oracle `UTL_FILE` utility. However, the steps and sample code can be enhanced further to achieve your database modernization goals.

**Product versions**
+ Amazon Aurora PostgreSQL-Compatible Edition 11.9

## Architecture
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-architecture"></a>

**Target technology stack**
+ Amazon Aurora PostgreSQL-Compatible
+ Amazon CloudWatch
+ Amazon Simple Notification Service (Amazon SNS)
+ Amazon S3

**Target architecture **

The following diagram shows a high-level representation of the solution.

![Data files are uploaded to an S3 bucket, processed using the aws_s3 extension, and sent to the Aurora instance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3aeecd46-1f87-41f9-a9cd-f8181f92e83f/images/4a6c5f5c-58fb-4355-b243-d09a15c1cec6.png)

1. Files are uploaded from the application into the S3 bucket.

1. The `aws_s3` extension accesses the data, using PL/pgSQL, and uploads the data to Aurora PostgreSQL-Compatible.

## Tools
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-tools"></a>
+ [Amazon Aurora PostgreSQL-Compatible](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) – Amazon Aurora PostgreSQL-Compatible Edition is a fully managed, PostgreSQL-compatible, and ACID-compliant relational database engine. It combines the speed and reliability of high-end commercial databases with the cost-effectiveness of open-source databases.
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) – The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With only one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) – Amazon CloudWatch monitors Amazon S3 resources and use.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet. In this pattern, Amazon S3 provides a storage layer to receive and store files for consumption and transmission to and from the Aurora PostgreSQL-Compatible cluster.
+ [aws\_s3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.html#aws_s3.table_import_from_s3) – The `aws_s3` extension integrates Amazon S3 and Aurora PostgreSQL-Compatible.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) coordinates and manages the delivery or sending of messages between publishers and clients. In this pattern, Amazon SNS is used to send notifications.
+ [pgAdmin](https://www.pgadmin.org/docs/) – pgAdmin is an open-source management tool for Postgres. pgAdmin 4 provides a graphical interface for creating, maintaining, and using database objects.

**Code**

To achieve the required functionality, the pattern creates multiple functions with naming similar to `UTL_FILE`. The *Additional information* section contains the code base for these functions.

In the code, replace `testaurorabucket` with the name of your test S3 bucket. Replace `us-east-1` with the AWS Region where your test S3 bucket is located.

## Epics
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-epics"></a>

### Integrate Amazon S3 and Aurora PostgreSQL-Compatible
<a name="integrate-amazon-s3-and-aurora-postgresql-compatible"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up IAM policies. | Create AWS Identity and Access Management (IAM) policies that grant access to the S3 bucket and objects in it. For the code, see the *Additional information* section. | AWS administrator, DBA |
| Add Amazon S3 access roles to Aurora PostgreSQL. | Create two IAM roles: one role for read and one role for write access to Amazon S3. Attach the two roles to the Aurora PostgreSQL-Compatible cluster: + One role for the S3Export feature<br />+ One role for the S3Import feature<br />For more information, see the Aurora PostgreSQL-Compatible documentation on [importing](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.html) and [exporting](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export.html) data to Amazon S3. | AWS administrator, DBA |

### Set up the extensions in Aurora PostgreSQL-Compatible
<a name="set-up-the-extensions-in-aurora-postgresql-compatible"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the aws\_commons extension. | The `aws_commons` extension is a dependency of the `aws_s3` extension. | DBA, Developer |
| Create the aws\_s3 extension. | The `aws_s3` extension interacts with Amazon S3. | DBA, Developer |

### Validate Amazon S3 and Aurora PostgreSQL-Compatible integration
<a name="validate-amazon-s3-and-aurora-postgresql-compatible-integration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test importing files from Amazon S3 into Aurora PostgreSQL. | To test importing files into Aurora PostgreSQL-Compatible, create a sample CSV file and upload it into the S3 bucket. Create a table definition based on the CSV file, and load the file into the table by using the `aws_s3.table_import_from_s3` function. | DBA, Developer |
| Test exporting files from Aurora PostgreSQL to Amazon S3. | To test exporting files from Aurora PostgreSQL-Compatible, create a test table, populate it with data, and then export the data by using the `aws_s3.query_export_to_s3` function. | DBA, Developer |

### To mimic the UTL\_FILE utility, create wrapper functions
<a name="to-mimic-the-utl_file-utility-create-wrapper-functions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the utl\_file\_utility schema. | The schema keeps the wrapper functions together. To create the schema, run the following command.<pre>CREATE SCHEMA utl_file_utility;</pre> | DBA, Developer |
| Create the file\_type type. | To create the `file_type` type, use the following code.<pre>CREATE TYPE utl_file_utility.file_type AS (<br />    p_path character varying(30),<br />    p_file_name character varying<br />);<br /><br /><br /></pre> | DBA/Developer |
| Create the init function. | The `init` function initializes common variable such as `bucket` or `region`. For the code, see the *Additional information* section. | DBA/Developer |
| Create the wrapper functions. | Create the wrapper functions `fopen`, `put_line`, and `fclose`. For code, see the *Additional information* section. | DBA, Developer |

### Test the wrapper functions
<a name="test-the-wrapper-functions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the wrapper functions in write mode. | To test the wrapper functions in write mode, use the code provided in the *Additional information* section. | DBA, Developer |
| Test the wrapper functions in append mode. | To test the wrapper functions in append mode, use the code provide in the *Additional information* section. | DBA, Developer |

## Related resources
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-resources"></a>
+ [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.html)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [Aurora](https://aws.amazon.com/rds/aurora/?nc2=h_ql_prod_db_aa&aurora-whats-new.sort-by=item.additionalFields.postDateTime&aurora-whats-new.sort-order=desc)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [Amazon SNS](https://aws.amazon.com/sns/?nc2=h_ql_prod_ap_sns&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)

## Additional information
<a name="set-up-oracle-utl_file-functionality-on-aurora-postgresql-compatible-additional"></a>

**Set up IAM policies**

Create the following policies.

|
|
| Policy name | JSON |
| --- |--- |
| S3IntRead | <pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "S3integrationtest",<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:GetObject",<br />                "s3:ListBucket"<br />            ],<br />            "Resource": [<br />         "arn:aws:s3:::testaurorabucket/*",<br />         "arn:aws:s3:::testaurorabucket"<br />            ]<br />        }<br />    ]<br />}</pre> |
| S3IntWrite | <pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "S3integrationtest",<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:PutObject",                <br />                "s3:ListBucket"<br />            ],<br />            "Resource": [                "arn:aws:s3:::testaurorabucket/*",                "arn:aws:s3:::testaurorabucket"<br />            ]<br />        }<br />    ]<br />}</pre> |

**Create the init function**

To initialize common variables, such as `bucket` or `region`, create the `init` function by using the following code.

```
CREATE OR REPLACE FUNCTION utl_file_utility.init(
    )
    RETURNS void
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
BEGIN
      perform set_config
      ( format( '%s.%s','UTL_FILE_UTILITY', 'region' )
      , 'us-east-1'::text
      , false );

      perform set_config
      ( format( '%s.%s','UTL_FILE_UTILITY', 's3bucket' )
      , 'testaurorabucket'::text
      , false );
END;
$BODY$;
```

**Create the wrapper functions**

Create the `fopen`, `put_line`, and `fclose` wrapper functions.

*fopen*

```
CREATE OR REPLACE FUNCTION utl_file_utility.fopen(
    p_file_name character varying,
    p_path character varying,
    p_mode character DEFAULT 'W'::bpchar,
    OUT p_file_type utl_file_utility.file_type)
    RETURNS utl_file_utility.file_type
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
declare
    v_sql character varying;
    v_cnt_stat integer;
    v_cnt integer;
    v_tabname character varying;
    v_filewithpath character varying;
    v_region character varying;
    v_bucket character varying;

BEGIN
    /*initialize common variable */
    PERFORM utl_file_utility.init();
    v_region := current_setting( format( '%s.%s', 'UTL_FILE_UTILITY', 'region' ) );
    v_bucket :=  current_setting( format( '%s.%s', 'UTL_FILE_UTILITY', 's3bucket' ) );

    /* set tabname*/
    v_tabname := substring(p_file_name,1,case when strpos(p_file_name,'.') = 0 then length(p_file_name) else strpos(p_file_name,'.') - 1 end );
    v_filewithpath := case when NULLif(p_path,'') is null then p_file_name else concat_ws('/',p_path,p_file_name) end ;
    raise notice 'v_bucket %, v_filewithpath % , v_region %', v_bucket,v_filewithpath, v_region;

    /* APPEND MODE HANDLING; RETURN EXISTING FILE DETAILS IF PRESENT ELSE CREATE AN EMPTY FILE */
    IF p_mode = 'A' THEN
        v_sql := concat_ws('','create temp table if not exists ', v_tabname,' (col1 text)');
        execute v_sql;

        begin
        PERFORM aws_s3.table_import_from_s3
            ( v_tabname,
            '',
            'DELIMITER AS ''#''',
            aws_commons.create_s3_uri
            (     v_bucket,
                v_filewithpath ,
                v_region)
            );
        exception
            when others then
             raise notice 'File load issue ,%',sqlerrm;
             raise;
        end;
        execute concat_ws('','select count(*) from ',v_tabname) into v_cnt;

        IF v_cnt > 0
        then
            p_file_type.p_path := p_path;
            p_file_type.p_file_name := p_file_name;
        else
            PERFORM aws_s3.query_export_to_s3('select ''''',
                            aws_commons.create_s3_uri(v_bucket, v_filewithpath, v_region)
                              );

            p_file_type.p_path := p_path;
            p_file_type.p_file_name := p_file_name;
        end if;
        v_sql := concat_ws('','drop table ', v_tabname);
        execute v_sql;
    ELSEIF p_mode = 'W' THEN
            PERFORM aws_s3.query_export_to_s3('select ''''',
                            aws_commons.create_s3_uri(v_bucket, v_filewithpath, v_region)
                              );
            p_file_type.p_path := p_path;
            p_file_type.p_file_name := p_file_name;
    END IF;

EXCEPTION
        when others then
            p_file_type.p_path := p_path;
            p_file_type.p_file_name := p_file_name;
            raise notice 'fopenerror,%',sqlerrm;
            raise;
END;
$BODY$;
```

*put\_line*

```
CREATE OR REPLACE FUNCTION utl_file_utility.put_line(
    p_file_name character varying,
    p_path character varying,
    p_line text,
    p_flag character DEFAULT 'W'::bpchar)
    RETURNS boolean
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
/**************************************************************************
* Write line, p_line in windows format to file, p_fp - with carriage return
* added before new line.
**************************************************************************/
declare
    v_sql varchar;
    v_ins_sql varchar;
    v_cnt INTEGER;
    v_filewithpath character varying;
    v_tabname  character varying;
    v_bucket character varying;
    v_region character varying;

BEGIN
 PERFORM utl_file_utility.init();

/* check if temp table already exist */

 v_tabname := substring(p_file_name,1,case when strpos(p_file_name,'.') = 0 then length(p_file_name) else strpos(p_file_name,'.') - 1 end );

 v_sql := concat_ws('','select count(1) FROM pg_catalog.pg_class c LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace where n.nspname like ''pg_temp_%'''
                         ,' AND pg_catalog.pg_table_is_visible(c.oid) AND Upper(relname) = Upper( '''
                         ,  v_tabname ,''' ) ');

 execute v_sql into v_cnt;

  IF v_cnt = 0 THEN
         v_sql := concat_ws('','create temp table ',v_tabname,' (col text)');
        execute v_sql;
        /* CHECK IF APPEND MODE */
        IF upper(p_flag) = 'A' THEN
            PERFORM utl_file_utility.init();
            v_region := current_setting( format( '%s.%s', 'UTL_FILE_UTILITY', 'region' ) );
            v_bucket :=  current_setting( format( '%s.%s', 'UTL_FILE_UTILITY', 's3bucket' ) );

            /* set tabname*/
            v_filewithpath := case when NULLif(p_path,'') is null then p_file_name else concat_ws('/',p_path,p_file_name) end ;

            begin
               PERFORM aws_s3.table_import_from_s3
                     ( v_tabname,
                          '',
                       'DELIMITER AS ''#''',
                        aws_commons.create_s3_uri
                           ( v_bucket,
                               v_filewithpath,
                               v_region    )
                    );
            exception
                when others then
                    raise notice  'Error Message : %',sqlerrm;
                    raise;
            end;
        END IF;
    END IF;
    /* INSERT INTO TEMP TABLE */
    v_ins_sql := concat_ws('','insert into ',v_tabname,' values(''',p_line,''')');
    execute v_ins_sql;
    RETURN TRUE;
    exception
            when others then
                raise notice  'Error Message : %',sqlerrm;
                raise;
END;
$BODY$;
```

*fclose*

```
CREATE OR REPLACE FUNCTION utl_file_utility.fclose(
    p_file_name character varying,
    p_path character varying)
    RETURNS boolean
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE
AS $BODY$
DECLARE
    v_filewithpath character varying;
    v_bucket character varying;
    v_region character varying;
    v_tabname character varying;
    v_sql character varying;
BEGIN
      PERFORM utl_file_utility.init();

    v_region := current_setting( format( '%s.%s', 'UTL_FILE_UTILITY', 'region' ) );
    v_bucket :=  current_setting( format( '%s.%s', 'UTL_FILE_UTILITY', 's3bucket' ) );

    v_tabname := substring(p_file_name,1,case when strpos(p_file_name,'.') = 0 then length(p_file_name) else strpos(p_file_name,'.') - 1 end );
    v_filewithpath := case when NULLif(p_path,'') is null then p_file_name else concat_ws('/',p_path,p_file_name) end ;

    raise notice 'v_bucket %, v_filewithpath % , v_region %', v_bucket,v_filewithpath, v_region ;

    /* exporting to s3 */
    perform aws_s3.query_export_to_s3
        (concat_ws('','select * from ',v_tabname,'  order by ctid asc'),
            aws_commons.create_s3_uri(v_bucket, v_filewithpath, v_region)
        );
    v_sql := concat_ws('','drop table ', v_tabname);
    execute v_sql;
    RETURN TRUE;
EXCEPTION
       when others then
     raise notice 'error fclose %',sqlerrm;
     RAISE;
END;
$BODY$;
```

**Test your setup and wrapper functions**

Use the following anonymous code blocks to test your setup.

*Test the write mode*

The following code writes a file named `s3inttest` in the S3 bucket.

```
do $$
declare
l_file_name varchar := 's3inttest' ;
l_path varchar := 'integration_test' ;
l_mode char(1) := 'W';
l_fs utl_file_utility.file_type ;
l_status boolean;

begin
select * from
utl_file_utility.fopen( l_file_name, l_path , l_mode ) into l_fs ;
raise notice 'fopen : l_fs : %', l_fs;

select * from
utl_file_utility.put_line( l_file_name, l_path ,'this is test file:in s3bucket: for test purpose', l_mode ) into l_status ;
raise notice 'put_line : l_status %', l_status;

select * from utl_file_utility.fclose( l_file_name , l_path ) into l_status ;
raise notice 'fclose : l_status %', l_status;

end;
$$
```

*Test the append mode*

The following code appends lines onto the `s3inttest` file that was created in the previous test.

```
do $$
declare
l_file_name varchar := 's3inttest' ;
l_path varchar := 'integration_test' ;
l_mode char(1) := 'A';
l_fs utl_file_utility.file_type ;
l_status boolean;

begin
select * from
utl_file_utility.fopen( l_file_name, l_path , l_mode ) into l_fs ;
raise notice 'fopen : l_fs : %', l_fs;

select * from
utl_file_utility.put_line( l_file_name, l_path ,'this is test file:in s3bucket: for test purpose : append 1', l_mode ) into l_status ;
raise notice 'put_line : l_status %', l_status;

select * from
utl_file_utility.put_line( l_file_name, l_path ,'this is test file:in s3bucket : for test purpose : append 2', l_mode ) into l_status ;
raise notice 'put_line : l_status %', l_status;

select * from utl_file_utility.fclose( l_file_name , l_path ) into l_status ;
raise notice 'fclose : l_status %', l_status;

end;
$$
```

**Amazon SNS notifications**

Optionally, you can set up Amazon CloudWatch monitoring and Amazon SNS notifications on the S3 bucket. For more information, see [Monitoring Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/monitoring-overview.html) and [Setting up Amazon SNS Notifications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
