---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/oracle-sqlloader.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle SQL\*Loader
<a name="oracle-sqlloader"></a>

 Oracle SQL\*Loader is well suited for small to moderate databases under 10 GB that contain a limited number of objects. Because the process involved in exporting from a source database and loading to a destination database is specific to a schema, you should use this process for one schema at a time. If the database contains multiple schemas, you need to repeat the process for each schema. This method can be a good choice even if the total database size is large, because you can do the import in multiple phases (one schema at a time).

 You can use this method for Oracle Database on either Amazon RDS or Amazon EC2, and you can choose between the following two options:

## Option 1
<a name="option-1"></a>

1.  Extract data from the source database, such as into flat files with column and row delimiters.

1.  Create tables in the destination database exactly like the source (use a generated script).

1.  Using SQL\*Loader, connect to the destination database from the source machine and import the data.

## Option 2
<a name="option-2"></a>

1.  Extract data from the source database, such as into flat files with column and row delimiters.

1.  Compress and encrypt the files.

1.  Launch an Amazon EC2 instance, and install the full Oracle client on it (for SQL\*Loader). For the database on Amazon EC2, this can be the same instance where the destination database is located. For Amazon RDS, this is a temporary instance.

1.  Transport the files to the Amazon EC2 instance.

1.  Decompress and unencrypt files in the Amazon EC2 instance.

1.  Create tables in the destination database exactly like the source (use a generated script).

1.  Using SQL\*Loader, connect to the destination database from the temporary Amazon EC2 instance and import the data.

 Use the first option if your database size is small, if you have direct SQL\*Net access to the destination database in AWS, and if data security is not a concern. Otherwise, use the second option, because you can use encryption and compression during the transportation phase. Compression substantially reduces the size of the files, making data transportation much faster.

 You can use either [SQL\*Plus](https://docs.oracle.com/cd/B19306_01/server.102/b14357/qstart.htm) or [SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) to perform data extraction, which is the first step in both options. For SQL\*Plus, use a query in a SQL script file and send the output directly to a text file, as shown in the following example:

```
set pagesize 0
set head off
set feed off
set line 200

SELECT col1|| '|' ||col2|| '|' ||col3|| '|' ||col4|| '|'
||col5 from SCHEMA.TABLE;
exit;
```

 To create encrypted and compressed output in the second option (see step 2 of the preceding Option 2 procedure), you can directly pipe the output to a zip utility.

 You can also extract data by using Oracle SQL Developer:

1.  In the **Connections** pane, select the tables you want to extract data from.

1.  From the **Tools** menu, choose the **Database Export** command, as shown in the following screenshot.
![Screen capture showing the Database export command](http://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/images/database-export.png)

1.  On the **Source/Destination** page of the **Export Wizard** (see the next screenshot), select the **Export DDL** option to generate the script for creating the table, which will simplify the entire process.

1.  In the **Format** drop-down on the same page, choose **loader**.

1.  In the **Save As** box on the same page, choose **Separate Files**.
![Screen capture showing the Export Wizard options on the Source/Destination page](http://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/images/export-wizard-src-dest-page.png)

 Continue to follow the Export Wizard steps to complete the export. The Export Wizard helps you create the data file, control file, and table creation script in one step for multiple tables in a schema, making it easier than using Oracle SQL\*Plus to do the same tasks.

 If you use Option 1 as specified, you can run Oracle SQL\*Loader from the source environment using the extracted data and control files to import data into the destination database. To do this, use the following command:

```
sqlldr userid=userID/password@$service control=control.ctl
        log=load.log bad=load.bad discard=load.dsc data=load.dat direct=y
        skip_index_maintenance=true errors=0
```

 If you use Option 2, then you need an Amazon EC2 instance with the full Oracle client installed. Additionally, you need to upload the data files to that Amazon EC2 instance. For the database on Amazon EC2, this could be the same Amazon EC2 instance where the destination database is located. For Amazon RDS, this will be a temporary Amazon EC2 instance.

 Before you do the upload, we recommend that you compress and encrypt your files. To do this, you can use a combination of [TAR](https://www.gnu.org/software/tar/) and ZIP/GZIP in Linux or a third-party utility such as WinZip or 7-Zip. After the Amazon EC2 instance is up and running and the files are compressed and encrypted, upload the files to the Amazon EC2 instance using Secure File Transfer Protocol (SFTP).

 From the Amazon EC2 instance, connect to the destination database using Oracle SQL\*Plus to ensure you can establish the connection. Run the `sqlldr` command shown in the preceding example for each control file that you have from the extract. You can also create a shell/bat script that will run `sqlldr` for all control files, one after the other.

**Note**
Enabling `skip_index_maintenance=true` significantly increases data-load performance. However, table indexes are not updated, so you will need to rebuild all indexes after the data load is complete.
