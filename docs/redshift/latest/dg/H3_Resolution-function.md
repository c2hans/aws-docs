---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/H3_Resolution-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# H3\_Resolution
<a name="H3_Resolution-function"></a>

H3\_Resolution returns the resolution of an H3 cell ID from an input index. Resolution is an integer from 0 (coarsest) to 15 (finest). For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3).

## Syntax
<a name="H3_Resolution-function-syntax"></a>

```
H3_Resolution(index)
```

## Arguments
<a name="H3_Resolution-function-arguments"></a>

 *index*
A value of data type `BIGINT` or `VARCHAR` that represents the index of an H3 cell, or an expression that evaluates to one of these data types.

## Return type
<a name="H3_Resolution-function-return"></a>

`INTEGER` – represents the resolution of the input H3 cell ID.

If *index* is NULL, then NULL is returned.

If *index* is not valid, then an error is returned.

## Examples
<a name="H3_Resolution-function-examples"></a>

The following SQL inputs a VARCHAR that represents the index of an H3 cell, and returns an INTEGER that represents the resolution of the input H3 cell.

```
SELECT H3_Resolution('8025fffffffffff');
```

```
 h3_resolution
---------------
 0
```

The following SQL inputs a BIGINT that represents the index of an H3 cell, and returns an INTEGER that represents the resolution of the input H3 cell.

```
SELECT H3_Resolution(614553222213795839);
```

```
 h3_resolution
---------------
 8
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
