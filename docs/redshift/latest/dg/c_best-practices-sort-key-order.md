---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key-order.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Load data in sort key order
<a name="c_best-practices-sort-key-order"></a>

Load your data in sort key order to avoid needing to vacuum.

If each batch of new data follows the existing rows in your table and the COPY operation is not large enough to trigger certain load optimizations, your data is properly stored in sort order, and you don't need to run a vacuum. You don't need to presort the rows in each load because COPY sorts each batch of incoming data as it loads.

For example, suppose that you load data every day based on the current day's activity. If your sort key is a timestamp column and the COPY operation is not large enough to trigger certain load optimizations, your data is stored in sort order. This order occurs because the current day's data is always appended at the end of the previous day's data. For more information, see [Load your data in sort key order](vacuum-managing-vacuum-times.md#vacuum-load-in-sort-key-order). For more information about vacuum operations, see [Vacuuming tables](https://docs.aws.amazon.com/redshift/latest/dg/t_Reclaiming_storage_space202.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
