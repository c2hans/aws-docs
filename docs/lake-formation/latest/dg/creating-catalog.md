---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/creating-catalog.html
---

# Creating a catalog
<a name="creating-catalog"></a>

Catalogs represent the highest or top-most level in the three-level metadata hierarchy of the AWS Glue Data Catalog. You can use multiple methods to bring data into the Data Catalog and create multi-level catalogs.

 For more information on creating catalogs from external data sources, see [Bringing your data into the AWS Glue Data Catalog](bring-your-data-overview.md).

 To create a catalog using the Lake Formation console, you must be signed in as a data lake administrator or a *catalog creator*. A catalog creator is a principal who has been granted the Lake Formation `CREATE_CATALOG` permission. You can see a list of catalog creators on the **Administrative roles and tasks** page of the Lake Formation console. To view this list, you must have the `lakeformation:ListPermissions` IAM permission and be signed in as a data lake administrator or as a catalog creator with the grant option on the `CREATE_CATALOG` permission.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
