---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_enable_result_cache_for_session.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# enable\_result\_cache\_for\_session
<a name="r_enable_result_cache_for_session"></a>

## Values (default in bold)
<a name="r_enable_result_cache_for_session-values"></a>

**on (true)**, off (false)

## Description
<a name="r_enable_result_cache_for_session-description"></a>

Specifies whether to use query results caching. If `enable_result_cache_for_session` is `on`, Amazon Redshift checks for a valid, cached copy of the query results when a query is submitted. If a match is found in the result cache, Amazon Redshift uses the cached results and doesn’t run the query. If `enable_result_cache_for_session` is `off`, Amazon Redshift ignores the results cache and runs all queries when they are submitted.

## Example
<a name="r_enable_result_cache_for_session-example"></a>

```
SET enable_result_cache_for_session TO off;
--Amazon Redshift now ignores the results cache
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
