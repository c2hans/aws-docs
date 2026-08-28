---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_enable_vacuum_boost.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# enable\_vacuum\_boost
<a name="r_enable_vacuum_boost"></a>

## Values (default in bold)
<a name="r_enable_vacuum_boost-values"></a>

**false**, true

## Description
<a name="description"></a>

Specifies whether to enable the vacuum boost option for all VACUUM commands run in a session. If `enable_vacuum_boost` is `true`, Amazon Redshift runs all VACUUM commands in the session with the BOOST option. If `enable_vacuum_boost` is `false`, Amazon Redshift doesn't run with the BOOST option by default. For more information about the BOOST option, see [VACUUM](r_VACUUM_command.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
