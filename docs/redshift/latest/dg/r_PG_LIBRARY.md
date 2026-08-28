---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_PG_LIBRARY.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# PG\_LIBRARY
<a name="r_PG_LIBRARY"></a>

Stores information about user-defined libraries.

PG\_LIBRARY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_PG_LIBRARY-table-columns2"></a>

| Column name  | Data type  | Description  |
| --- | --- | --- |
| name | name | Library name. |
| language\_oid | oid  | Reserved for system use. |
| file\_store\_id | integer | Reserved for system use. |
| owner | integer | User ID of the library owner. |

## Example
<a name="r_PG_LIBRARY-example"></a>

The following example returns information for user-installed libraries.

```
select * from pg_library;

name       | language_oid | file_store_id | owner
-----------+--------------+---------------+------
f_urlparse |       108254 |          2000 |   100
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
