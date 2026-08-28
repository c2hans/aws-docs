---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_DB_COLLATION.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# DB\_COLLATION
<a name="r_DB_COLLATION"></a>

Returns the collation setting of the current database.

## Syntax
<a name="r_DB_COLLATION-synopsis"></a>

```
db_collation()
```

## Return type
<a name="r_DB_COLLATION-return-type"></a>

Returns a VARCHAR string representing the collation of the current database. Possible values are `case_sensitive` or `case_insensitive`.

## Example
<a name="r_DB_COLLATION-example"></a>

The following example returns the collation of the current database.

```
select db_collation();

db_collation
----------------
case_sensitive
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
