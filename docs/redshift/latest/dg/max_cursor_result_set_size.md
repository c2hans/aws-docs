---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/max_cursor_result_set_size.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# max\_cursor\_result\_set\_size
<a name="max_cursor_result_set_size"></a>

## Values (default in bold)
<a name="max_cursor_result_set_size-values"></a>

 **0 (defaults to maximum)** - 14400000 MB

## Description
<a name="max_cursor_result_set_size-description"></a>

The `max_cursor_result_set_size` parameter is no longer used. For more information about cursor result set size, see [Cursor constraints](declare.md#declare-constraints).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
