---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.TempDB.Modifying.html
---

# Modifying tempdb database options
<a name="SQLServer.TempDB.Modifying"></a>

You can modify the database options on the `tempdb` database on your Amazon RDS DB instances. For more information about which options can be modified, see [tempdb database](https://msdn.microsoft.com/en-us/library/ms190768%28v=sql.120%29.aspx) in the Microsoft documentation.

Database options such as the maximum file size options are persistent after you restart your DB instance. You can modify the database options to optimize performance when importing data, and to prevent running out of storage.

## Optimizing performance when importing data
<a name="SQLServer.TempDB.Modifying.Import"></a>

To optimize performance when importing large amounts of data into your DB instance, set the `SIZE` and `FILEGROWTH` properties of the tempdb database to large numbers. For more information about how to optimize `tempdb`, see [Optimizing tempdb performance](https://technet.microsoft.com/en-us/library/ms175527%28v=sql.120%29.aspx) in the Microsoft documentation.

The following example demonstrates setting the size to 100 GB and file growth to 10 percent.

```
1. alter database[tempdb] modify file (NAME = N'{{templog}}', SIZE={{100GB}}, FILEGROWTH = {{10%}})
```

## Preventing storage problems
<a name="SQLServer.TempDB.Modifying.Full"></a>

To prevent the `tempdb` database from using all available disk space, set the `MAXSIZE` property. The following example demonstrates setting the property to 2048 MB.

```
1. alter database [tempdb] modify file (NAME = N'{{templog}}', MAXSIZE = {{2048MB}})
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
