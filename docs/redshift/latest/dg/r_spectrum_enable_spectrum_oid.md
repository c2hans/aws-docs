---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_spectrum_enable_spectrum_oid.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# enable\_spectrum\_oid
<a name="r_spectrum_enable_spectrum_oid"></a>

## Values (default in bold)
<a name="r_spectrum_enable_spectrum_oid-values"></a>

**true**, false

## Description
<a name="r_spectrum_enable_spectrum_oid-description"></a>

You can also disable only the `$spectrum_oid` pseudocolumn by setting the `enable_spectrum_oid` configuration parameter to `false`.

## Example
<a name="r_spectrum_enable_spectrum_oid-example"></a>

The following command disables the `$spectrum_oid` pseudocolumn by setting the `enable_spectrum_oid` configuration parameter to `false`.

```
set enable_spectrum_oid to false;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
