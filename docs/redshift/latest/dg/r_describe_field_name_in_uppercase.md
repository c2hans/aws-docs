---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_describe_field_name_in_uppercase.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# describe\_field\_name\_in\_uppercase
<a name="r_describe_field_name_in_uppercase"></a>

## Values (default in bold)
<a name="r_describe_field_name_in_uppercase-values"></a>

**off (false)**, on (true)

## Description
<a name="description"></a>

Specifies whether column names returned by SELECT statements are uppercase or lowercase. If this parameter is on, column names are returned in uppercase. If this parameter is off, column names are returned in lowercase. Amazon Redshift stores column names in lowercase regardless of the setting for `describe_field_name_in_uppercase`.

## Example
<a name="example"></a>

```
set describe_field_name_in_uppercase to on;

show describe_field_name_in_uppercase;

DESCRIBE_FIELD_NAME_IN_UPPERCASE
--------------------------------
on
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
