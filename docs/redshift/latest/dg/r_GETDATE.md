---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_GETDATE.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# GETDATE function
<a name="r_GETDATE"></a>

GETDATE returns the current date and time in the current session time zone (UTC by default). It returns the start date or time of the current statement, even when it is within a transaction block.

## Syntax
<a name="r_GETDATE-synopsis"></a>

```
GETDATE()
```

The parentheses are required.

## Return type
<a name="r_GETDATE-return-type"></a>

TIMESTAMP

## Examples
<a name="r_GETDATE-examples"></a>

The following example uses the GETDATE function to return the full timestamp for the current date.

```
select getdate();

timestamp
---------------------
2008-12-04 16:10:43
```

The following example uses the GETDATE function inside the TRUNC function to return the current date without the time.

```
select trunc(getdate());

trunc
------------
2008-12-04
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
