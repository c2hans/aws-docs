---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/oracle-export-and-import-utilities.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle Export and Import utilities
<a name="oracle-export-and-import-utilities"></a>

 Despite being replaced by Oracle Data Pump, the original Oracle Export and Import utilities are useful for migrations of databases with sizes less than 10 GB where the data lacks binary float and double data types. The import process creates the schema objects, so you do not need to run a script to create them beforehand. This makes the process well suited for databases with a large number of small tables. You can use this method for Amazon RDS for Oracle and Oracle Database on Amazon EC2.

 The first step is to export the tables from the source database by using the following command. Substitute the credentials as appropriate:

```
 exp userID/password@$service FILE=exp_file.dmp LOG=exp_file.log
```

 The export process creates a binary dump file that contains both the schema and data for the specified tables. You can import the schema and data into a destination database.

 Choose one of the following two options for the next steps:

## Option 1
<a name="option-1-1"></a>

1.  Export data from the source database into a binary dump file using `exp`.

1.  Import the data into the destination database by running `imp` directly from the source server.

## Option 2
<a name="option-2-1"></a>

1.  Export data from the source database into a binary dump file using `exp`.

1.  Compress and encrypt the files.

1.  Launch an Amazon EC2 instance and install the full Oracle client on it (for the `emp/imp` utility). For the database on Amazon EC2, this could be the same instance where the destination database is located. For Amazon RDS, this will be a temporary instance.

1.  Transport the files to the Amazon EC2 instance.

1.  Decompress and unencrypt the files in the Amazon EC2 instance.

1.  Import the data into the destination database by running `imp`.

 If your database size is larger than a gigabyte, use Option 2, because it includes compression and encryption. This method will also have better import performance.

 For both Option 1 and Option 2, use the following command to import into the destination database:

```
imp userID/password@$service FROMUSER=cust_schema
TOUSER=cust_schema FILE=exp_file.dmp LOG=imp_file.log
```

 There are many optional arguments that can be passed to the exp and imp commands based on your needs. For details, see the [Oracle documentation](https://docs.oracle.com/cd/E11882_01/server.112/e22490/original_import.htm#SUTIL1637).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
