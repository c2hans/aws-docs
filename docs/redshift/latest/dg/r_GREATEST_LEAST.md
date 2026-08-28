---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_GREATEST_LEAST.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# GREATEST and LEAST functions
<a name="r_GREATEST_LEAST"></a>

Returns the largest or smallest value from a list of any number of expressions.

## Syntax
<a name="r_GREATEST_LEAST-synopsis"></a>

```
GREATEST (value [, ...])
LEAST (value [, ...])
```

## Parameters
<a name="r_GREATEST_LEAST-arguments"></a>

*expression\_list*
A comma-separated list of expressions, such as column names. The expressions must all be convertible to a common data type. NULL values in the list are ignored. If all of the expressions evaluate to NULL, the result is NULL.

## Returns
<a name="r_GREATEST_LEAST-returns"></a>

Returns the greatest (for GREATEST) or least (for LEAST) value from the provided list of expressions.

## Example
<a name="r_GREATEST_LEAST-examples"></a>

The following example returns the highest value alphabetically for `firstname` or `lastname`.

```
select firstname, lastname, greatest(firstname,lastname) from users
where userid < 10
order by 3;

 firstname | lastname  | greatest
-----------+-----------+-----------
 Lars      | Ratliff   | Ratliff
 Reagan    | Hodge     | Reagan
 Colton    | Roy       | Roy
 Barry     | Roy       | Roy
 Tamekah   | Juarez    | Tamekah
 Rafael    | Taylor    | Taylor
 Victor    | Hernandez | Victor
 Vladimir  | Humphrey  | Vladimir
 Mufutau   | Watkins   | Watkins
(9 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
