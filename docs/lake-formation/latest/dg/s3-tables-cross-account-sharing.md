---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/s3-tables-cross-account-sharing.html
---

# Accessing shared Amazon S3 tables
<a name="s3-tables-cross-account-sharing"></a>

 After you grant cross-account permissions on a database or table in the S3 tables catalog, to access the resources, you need to create resource links to the shared databases and tables.

1.  In the destination account (the account that receives the shared resources), create a database resource link. For detailed instructions, see [Creating a resource link to a shared Data Catalog database](create-resource-link-database.md).

   CLI example for creating a database resource link

   ```
   aws glue create-database
   --region us-east-1
   --catalog-id "111122223333"
   --database-input \
   '{
     "Name": "s3table_resourcelink",
     "TargetDatabase": {
       "CatalogId": "011426214932:s3tablescatalog/chmni-s3-table-bucket-011426214932",
       "DatabaseName": "s3_table_ns"
     },
     "CreateTableDefaultPermissions": []
   }'
   ```

1.  Grant cross account permission on the table.

   CLI example for cross-account permission grant

   ```
   aws lakeformation grant-permissions \
   --region us-east-1 \
   --cli-input-json \
   '{
       "Principal": {
           "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/S3TablesTestExecRole"
       },
       "Resource": {
           "Table": {
               "CatalogId": "011426214932:s3tablescatalog/chmni-s3-table-bucket-011426214932",
               "DatabaseName": "s3_table_ns",
               "Name": "test_s3_iceberg_table"
           }
       },
       "Permissions": [
           "ALL"
       ]
   }'
   ```

1.  Grant Lake Formation `DESCRIBE` permission on the resource link.

    CLI example for granting describe permission on the resource link.

   ```
   aws lakeformation grant-permissions \
       --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:role/S3TablesTestExecRole
       --resource Database='{CatalogId=111122223333;, Name=s3table_resourcelink}' \
       --permissions DESCRIBE
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
