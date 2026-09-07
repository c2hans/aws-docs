---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible.html
---

# Load BLOB files into TEXT by using file encoding in Aurora PostgreSQL-Compatible
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible"></a>

*Bhanu Ganesh Gudivada and Jeevan Shetty, Amazon Web Services*

## Summary
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-summary"></a>

Often during migration, there are cases where you have to process unstructured and structured data that is loaded from files on a local file system. The data might also be in a character set that differs from the database character set.

These files hold the following types of data:
+ **Metadata** – This data describes the file structure.
+ **Semi-structured data** – These are textual strings in a specific format, such as JSON or XML. You might be able to make assertions about such data, such as "will always start with '<' " or "does not contain any newline characters."
+ **Full text** – This data usually contains all types of characters, including newline and quote characters. It might also consist of multibyte characters in UTF-8.
+ **Binary data** – This data might contain bytes or combinations of bytes including, nulls and end-of-file markers.

Loading a mixture of these types of data can be a challenge.

The pattern can be used with on-premises Oracle databases , Oracle databases that are on Amazon Elastic Compute Cloud (Amazon EC2) instances on the Amazon Web Services (AWS) Cloud, and Amazon Relational Database Service (Amazon RDS) for Oracle databases. As an example, this pattern is using Amazon Aurora PostgreSQL-Compatible Edition.

In Oracle Database, with the help of a `BFILE` (binary file) pointer, the `DBMS_LOB` package, and Oracle system functions, you can load from file and convert to CLOB with character encoding. Because PostgreSQL does not support the BLOB data type when migrating to an Amazon Aurora PostgreSQL-Compatible Edition database, these functions must be converted to PostgreSQL-compatible scripts.

This pattern provides two approaches for loading a file into a single database column in an Amazon Aurora PostgreSQL-Compatible database:
+ Approach 1 – You import data from your Amazon Simple Storage Service (Amazon S3) bucket by using the `table_import_from_s3` function of the `aws_s3` extension with the encode option.
+ Approach 2 – You encode to hexadecimal outside of the database, and then you decode to view `TEXT` inside the database.

We recommend using Approach 1 because Aurora PostgreSQL-Compatible has direct integration with the `aws_s3` extension.

This pattern uses the example of loading a flat file that contains an email template, which has multibyte characters and distinct formatting, into an Amazon Aurora PostgreSQL-Compatible database.

## Prerequisites and limitations
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Amazon RDS instance or an Aurora PostgreSQL-Compatible instance
+ A basic understanding of SQL and Relational Database Management System (RDBMS)
+ An Amazon Simple Storage Service (Amazon S3) bucket.
+ Knowledge of system functions in Oracle and PostgreSQL
+ RPM Package HexDump-XXD-0.1.1 (included with Amazon Linux 2)
**Note**
Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/).

**Limitations **
+ For the `TEXT` data type, the longest possible character string that can be stored is about 1 GB.

**Product versions**
+ Aurora supports the PostgreSQL versions listed in [Amazon Aurora PostgreSQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html).

## Architecture
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-architecture"></a>

**Target technology stack  **
+ Aurora PostgreSQL-Compatible

**Target architecture**

*Approach 1 – Using aws\_s3.table\_import\_from\_s3 *

From an on-premises server, a file containing an email template with multibyte characters and custom formatting is transferred to Amazon S3. The custom database function provided by this pattern uses the `aws_s3.table_import_from_s3` function with `file_encoding` to load files into the database and return query results  as the `TEXT` data type.

![Four-step process from the on-premises server to the TEXT output from the Aurora database.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cbf63cac-dcea-4e18-ab4f-c4f6296f60e7/images/9c46b385-e8a0-4e50-b856-d522c44d79e3.png)

1. Files are transferred to the staging S3 bucket.

1. Files are uploaded to the Amazon Aurora PostgreSQL-Compatible database.

1. Using the pgAdmin client, the custom function `load_file_into_clob` is deployed to the Aurora database.

1. The custom function internally uses `table_import_from_s3` with file\_encoding. The output from the function is obtained by using `array_to_string` and `array_agg` as `TEXT` output.

*Approach 2 – Encoding to hexadecimal outside of the database and decoding to view TEXT inside the database*

A file from an on-premises server or a local file system is converted into a hex dump. Then the file is imported into PostgreSQL as a `TEXT` field.

![Three-step process using Hex dump.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cbf63cac-dcea-4e18-ab4f-c4f6296f60e7/images/563038ca-f890-4874-85df-d0f82d99800a.png)

1. Convert the file to a hex dump in the command line by using the `xxd -p` option.

1. Upload the hex dump files into Aurora PostgreSQL-Compatible by using the `\copy` option, and then decode the hex dump files to binary.

1. Encode the binary data to return as `TEXT`.

## Tools
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.

**Other tools**
+ [pgAdmin4](https://www.pgadmin.org/) is an open source administration and development platform for PostgreSQL. pgAdmin4 can be used on Linux, Unix, mac OS, and Windows to manage PostgreSQL.

## Epics
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-epics"></a>

### Approach 1: Import data from Amazon S3 to Aurora PostgreSQL-Compatible
<a name="approach-1-import-data-from-amazon-s3-to-aurora-postgresql-compatible"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch an EC2 instance. | For instructions on launching an instance, see [Launch your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html). | DBA |
| Install the PostgreSQL client pgAdmin tool. | Download and install [pgAdmin](https://www.pgadmin.org/download/). | DBA |
| Create an IAM policy. | Create an AWS Identity and Access Management (IAM) policy named `aurora-s3-access-pol` that grants access to the S3 bucket where the files will be stored. Use the following code, replacing `<bucket-name>` with the name of your S3 bucket.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:GetObject",<br />                "s3:AbortMultipartUpload",<br />                "s3:DeleteObject",<br />                "s3:ListMultipartUploadParts",<br />                "s3:PutObject",<br />                "s3:ListBucket"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::<bucket-name>/*",<br />                "arn:aws:s3:::<bucket-name>"<br />            ]<br />        }<br />    ]<br />}</pre> | DBA |
| Create an IAM role for object import from Amazon S3 to Aurora PostgreSQL-Compatible. | Use the following code to create an IAM role named `aurora-s3-import-role` with the [AssumeRole](https://docs.amazonaws.cn/en_us/STS/latest/APIReference/API_AssumeRole.html) trust relationship. `AssumeRole` allows Aurora to access other AWS services on your behalf.<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Effect": "Allow","Principal": {<br />        "Service": "rds.amazonaws.com"<br />      },"Action": "sts:AssumeRole"<br />    }<br />  ]<br />}<br /></pre> | DBA |
| Associate the IAM role to the cluster. | To associate the IAM role with the Aurora PostgreSQL-Compatible database cluster, run the following AWS CLI command. Change `<Account-ID>` to the ID of the AWS account that hosts the Aurora PostgreSQL-Compatible database. This enables the Aurora PostgreSQL-Compatible database to access the S3 bucket.<pre>aws rds add-role-to-db-cluster --db-cluster-identifier aurora-postgres-cl<br />--feature-name s3Import --role-arn arn:aws:iam::<Account-ID>:role/aurora-s3-import-role</pre> | DBA |
| Upload the example to Amazon S3. | 1. In the *Additional information* section of this pattern, copy the email template code into a file named `salary.event.notification.email.vm`.<br />2. Upload to the file to the S3 bucket. | DBA, App owner |
| Deploy the custom function. | 1. From the *Additional information* section, copy the custom function `load_file_into_clob` SQL file content into a temporary table.<br />2. Log in to the Aurora PostgreSQL-Compatible database and deploy it into the database schema by using the pgAdmin client. | App owner, DBA |
| Run the custom function for importing the data into the database. | Run the following SQL command, replacing the items in angle brackets with the appropriate values.<pre>select load_file_into_clob('aws-s3-import-test'::text,'us-west-1'::text,'employee.salary.event.notification.email.vm'::text);</pre><br />Replace the items in angle brackets with the appropriate values, as shown in the following example, before running the command.<pre>Select load_file_into_clob('aws-s3-import-test'::text,'us-west-1'::text,'employee.salary.event.notification.email.vm'::text);</pre><br />The command loads the file from Amazon S3 and returns the output as `TEXT`. | App owner, DBA |

### Approach 2: Convert the template file into a hex dump in a local Linux system
<a name="approach-2-convert-the-template-file-into-a-hex-dump-in-a-local-linux-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Convert the template file into a hex dump. | The Hexdump utility displays the contents of binary files in hexadecimal, decimal, octal, or ASCII. The `hexdump` command is part of the `util-linux` package and comes pre-installed in Linux distributions. The Hexdump RPM package is part of Amazon Linux 2 as well. (: Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/).)To convert the file contents into a hex dump, run the following shell command.<pre>xxd -p </path/file.vm> | tr -d '\n' > </path/file.hex></pre><br />Replace the path and file with the appropriate values, as shown in the following example.<pre>xxd -p employee.salary.event.notification.email.vm | tr -d '\n' > employee.salary.event.notification.email.vm.hex</pre> | DBA |
| Load the hexdump file into the database schema. | Use the following commands to load the hexdump file into the Aurora PostgreSQL-Compatible database.1. Log in to Aurora PostgreSQL database, and create a new table called `email_template_hex`.<pre>CREATE TABLE email_template_hex(hex_data TEXT);</pre><br />2. Load the files from the local file system into the DB schema by using the following command.<pre>\copy email_template_hex FROM '/path/file.hex';</pre><br />Replace the path with the location on your local file system.<pre>\copy email_template_hex FROM '/tmp/employee.salary.event.notification.email.vm.hex';</pre><br />3. Create one more table called `email_template_bytea`.<pre>CREATE TABLE email_template_bytea(hex_data bytea);</pre><br />4. Insert the data from `email_template_hex` into `email_template_bytea`.<pre>INSERT INTO email_template_bytea (hex_data)<br /><br />(SELECT decode(hex_data, 'hex') FROM email_template_hex limit 1);</pre><br />5. To return hex bytea code as `TEXT` data, run the following command.<pre>SELECT encode(hex_data::bytea, 'escape') FROM email_template_bytea;</pre> | DBA |

## Related resources
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-resources"></a>

**References**
+ [Using a PostgreSQL database as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html)
+ [Oracle Database 19c to Amazon Aurora with PostgreSQL Compatibility (12.4) Migration Playbook](https://d1.awsstatic.com/whitepapers/Migration/oracle-database-amazon-aurora-postgresql-migration-playbook-12.4.pdf)
+ [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html)
+ [Associating an IAM role with an Amazon Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.AddRoleToDBCluster.html)
+ [pgAdmin](https://www.pgadmin.org/)

**Tutorials**
+ [Getting Started with Amazon RDS](https://aws.amazon.com/rds/getting-started/)
+ [Migrate from Oracle to Amazon Aurora](https://aws.amazon.com/getting-started/projects/migrate-oracle-to-amazon-aurora/)

## Additional information
<a name="load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible-additional"></a>

**load\_file\_into\_clob custom function**

```
CREATE OR REPLACE FUNCTION load_file_into_clob(
    s3_bucket_name text,
    s3_bucket_region text,
    file_name text,
    file_delimiter character DEFAULT '&'::bpchar,
    file_encoding text DEFAULT 'UTF8'::text)
    RETURNS text
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
    blob_data BYTEA;
    clob_data TEXT;
    l_table_name CHARACTER VARYING(50) := 'file_upload_hex';
    l_column_name CHARACTER VARYING(50) := 'template';
    l_return_text TEXT;
    l_option_text CHARACTER VARYING(150);
    l_sql_stmt CHARACTER VARYING(500);

BEGIN

    EXECUTE format ('CREATE TEMPORARY TABLE %I (%I text, id_serial serial)', l_table_name, l_column_name);

    l_sql_stmt := 'select ''(format text, delimiter ''''' || file_delimiter || ''''', encoding ''''' || file_encoding ||  ''''')'' ';

    EXECUTE FORMAT(l_sql_stmt)
    INTO l_option_text;

    EXECUTE FORMAT('SELECT aws_s3.table_import_from_s3($1,$2,$6, aws_commons.create_s3_uri($3,$4,$5))')
    INTO l_return_text
    USING l_table_name, l_column_name, s3_bucket_name, file_name,s3_bucket_region,l_option_text;

    EXECUTE format('select array_to_string(array_agg(%I order by id_serial),E''\n'') from %I', l_column_name, l_table_name)
    INTO clob_data;

    drop table file_upload_hex;

    RETURN clob_data;
END;
$BODY$;
```

**Email template**

```
######################################################################################
##                                                                                    ##
##    johndoe Template Type: email                                                    ##
##    File: johndoe.salary.event.notification.email.vm                                ##
##    Author: Aimée Étienne    Date 1/10/2021                                                ##
##  Purpose: Email template used by EmplmanagerEJB to inform a johndoe they         ##
##        have been given access to a salary event                                    ##
##    Template Attributes:                                                             ##
##        invitedUser - PersonDetails object for the invited user                        ##
##        salaryEvent - OfferDetails object for the event the user was given access    ##
##        buyercollege - CompDetails object for the college owning the salary event    ##
##        salaryCoordinator - PersonDetails of the salary coordinator for the event    ##
##        idp - Identity Provider of the email recipient                                ##
##        httpWebRoot - HTTP address of the server                                    ##
##                                                                                    ##
######################################################################################

$!invitedUser.firstname $!invitedUser.lastname,

Ce courriel confirme que vous avez ete invite par $!salaryCoordinator.firstname $!salaryCoordinator.lastname de $buyercollege.collegeName a participer a l'evenement "$salaryEvent.offeringtitle" sur johndoeMaster Sourcing Intelligence.

Votre nom d'utilisateur est $!invitedUser.username

Veuillez suivre le lien ci-dessous pour acceder a l'evenement.

${httpWebRoot}/myDashboard.do?idp=$!{idp}

Si vous avez oublie votre mot de passe, utilisez le lien "Mot de passe oublie" situe sur l'ecran de connexion et entrez votre nom d'utilisateur ci-dessus.

Si vous avez des questions ou des preoccupations, nous vous invitons a communiquer avec le coordonnateur de l'evenement $!salaryCoordinator.firstname $!salaryCoordinator.lastname au ${salaryCoordinator.workphone}.

*******

johndoeMaster Sourcing Intelligence est une plateforme de soumission en ligne pour les equipements, les materiaux et les services.

Si vous avez des difficultes ou des questions, envoyez un courriel a support@johndoeMaster.com pour obtenir de l'aide.
```
