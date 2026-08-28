---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_CHECKSUM.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# CHECKSUM function
<a name="r_CHECKSUM"></a>

Computes a checksum value for building a hash index.

## Syntax
<a name="r_CHECKSUM-synopsis"></a>

```
CHECKSUM(expression)
```

## Argument
<a name="r_CHECKSUM-argument"></a>

 *expression*
The input expression must be a VARCHAR, INTEGER, or DECIMAL data type.

## Return type
<a name="r_CHECKSUM-return-type"></a>

The CHECKSUM function returns an integer.

## Example
<a name="r_CHECKSUM-example"></a>

The following example computes a checksum value for the COMMISSION column:

```
select checksum(commission)
from sales
order by salesid
limit 10;

checksum
----------
10920
1140
5250
2625
2310
5910
11820
2955
8865
975
(10 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
