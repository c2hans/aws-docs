---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_CURRENT_DATABASE.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# CURRENT\_DATABASE
<a name="r_CURRENT_DATABASE"></a>

Returns the name of the database where you are currently connected.

## Syntax
<a name="r_CURRENT_DATABASE-synopsis"></a>

```
current_database()
```

## Return type
<a name="r_CURRENT_DATABASE-return-type"></a>

Returns a CHAR or VARCHAR string.

## Example
<a name="r_CURRENT_DATABASE-example"></a>

The following query returns the name of the current database.

```
select current_database();

current_database
------------------
tickit
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
