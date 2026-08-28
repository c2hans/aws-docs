---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/GET_MOUNTED_ROLE.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# GET\_MOUNTED\_ROLE
<a name="GET_MOUNTED_ROLE"></a>

 When invoked as part of a multi-dialect AWS Glue view, it allows returning the IAM role used to mount the Lake Formation schema or database. Multi-dialect means that the SQL is supported across multiple query engines, such as Amazon EMR and Redshift. For more information about multi-dialect Glue views, see [Creating views in the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html).

## Syntax
<a name="GET_MOUNTED_ROLE-synopsis"></a>

```
get_mounted_role()
```

## Return type
<a name="GET_MOUNTED_ROLE-return-type"></a>

Returns a VARCHAR string or a null value.

## Usage notes
<a name="GET_MOUNTED_ROLE-usage"></a>

This function returns null for any use case outside of an external Lake Formation view.

## Example
<a name="GET_MOUNTED_ROLE-example"></a>

The following query returns the identity to mount the Lake Formation resource.

```
CREATE EXTERNAL PROTECTED VIEW external_schema.remote_view AS
SELECT mycol, get_mounted_role() FROM external_schema.remote_table;

mycol | get_mounted_role
----------------------------
1       arn:aws:iam::123456789012:role/salesrole
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
