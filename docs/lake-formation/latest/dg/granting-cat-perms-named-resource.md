---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/granting-cat-perms-named-resource.html
---

# Granting data permissions using the named resource method
<a name="granting-cat-perms-named-resource"></a>

The named Data Catalog resource method is a way of granting permissions to AWS Glue Data Catalog objects, such as catalogs, databases, tables, columns, and views, using a centralized approach. It allows you to define resource-based policies that control access to specific resources within your data lake.

When you use the named resource method to grant permissions, you can specify the resource type and the permissions that you want to grant or revoke for that resource. You can also revoke the permission later if needed, thereby removing the permissions from the associated resources.

You can grant permissions by using the AWS Lake Formation console, APIs, or the AWS Command Line Interface (AWS CLI).

**Topics**
+ [Granting catalog permissions using the named resource method](granting-multi-catalog-permissions.md)
+ [Granting database permissions using the named resource method](granting-database-permissions.md)
+ [Granting table permissions using the named resource method](granting-table-permissions.md)
+ [Granting permissions on views using the named resource method](granting-view-permissions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
