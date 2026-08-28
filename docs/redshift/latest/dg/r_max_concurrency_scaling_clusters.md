---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_max_concurrency_scaling_clusters.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# max\_concurrency\_scaling\_clusters
<a name="r_max_concurrency_scaling_clusters"></a>

## Values (default in bold)
<a name="r_max_concurrency_scaling_clusters-values"></a>

 **1**, 0 to 10

## Description
<a name="r_max_concurrency_scaling_clusters-description"></a>

Sets the maximum number of concurrency scaling clusters allowed when concurrency scaling is enabled. Increase this value if more concurrency scaling is required. Decrease this value to reduce the usage of concurrency scaling clusters and the resulting billing charges.

The maximum number of concurrency scaling clusters is an adjustable quota. For more information, see [Amazon Redshift quotas](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html#amazon-redshift-limits-quota) in the *Amazon Redshift Management Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
