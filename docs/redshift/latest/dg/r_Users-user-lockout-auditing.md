---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_Users-user-lockout-auditing.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Auditing locked users
<a name="r_Users-user-lockout-auditing"></a>

To review which users are currently locked, see whether each lockout was automatic or manual, and review recent failed-login activity, a superuser can run the SHOW USER LOCKOUT command. For more information, see [SHOW USER LOCKOUT](r_SHOW_USER_LOCKOUT.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
