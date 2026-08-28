---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/view-fed-glue-connection-catalog.html
---

# Viewing catalog objects
<a name="view-fed-glue-connection-catalog"></a>

For each available data source, AWS Glue creates a corresponding catalog in the AWS Glue Data Catalog. After you create a catalog, you can view the databases and tables in the catalog using the Lake Formation console or AWS CLI. For

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Choose **Catalogs** under Data Catalog. The catalogs page shows the catalogs that you've permissions on.
![View catalogs.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/view-catalogs.png)

1. Choose a catalog from the list to view the databases and tables contained in the catalog. The list contains the databases in your account and resource links, which are links to shared databases and tables in external accounts, and are used for cross-account access to data in the data lake.
![View catalogs/databases.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/catalog-database-view.png)

1. Choose **Tables** option under **View** to view and manage the tables in the database.

****AWS CLI examples for viewing catalogs and databases****
The following example shows how to view a catalog using AWS CLI

```
aws glue get-catalog \
--catalog-id {{123456789012}}:{{dynamodbcatalog}}
```

The following example shows how to request all catalogs in the account.

```
aws glue get-catalogs \
 --recursive
```

The following example request shows how to get the databases in the catalog.

```
aws glue get-database \
--catalog-id 123456789012:{{dynamodbcatalog}}
--database-name {{database name}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
