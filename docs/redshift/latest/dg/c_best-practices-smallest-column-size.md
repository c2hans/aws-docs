---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-smallest-column-size.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Use the smallest possible column size
<a name="c_best-practices-smallest-column-size"></a>

Don't make it a practice to use the maximum column size for convenience.

Instead, consider the largest values you are likely to store in your columns and size them accordingly. For instance, a CHAR column for storing U.S. state and territory abbreviations used by the post office only needs to be CHAR(2).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
