---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-multi-year-data.html
---

# Multi-year data at monthly granularity
<a name="ce-multi-year-data"></a>

While you can use the default 14-month historical data to perform cost analysis at quarterly or monthly level, you should enable multi-year data in Cost Explorer if you want to evaluate your year-over-year cost or identify long-term cost trends.

You can enable up to 38 months of multi-year data at monthly granularity for your entire organization. Using multi-year data to perform cost analysis over a longer duration, you can track changes in your AWS costs as your business or applications mature, or after implementing infrastructure optimizations.

Once enabled, multi-year data is available within 48 hours. Note that this data is only available in Cost Explorer, as Savings Plans and Reservations utilization and coverage reports don’t support this data.

To enable multi-year data in Cost Explorer, see [Configuring multi-year and granular data](ce-configuring-data.md).

**Note**
We will disable multi-year data for your organization if no one in the organization accesses it in three consecutive months. However, if you need the data, you can re-enable it in Cost Management preferences.
Multi-year data is only available for chargeable costs in Cost Explorer. If you're onboarded to AWS Billing Conductor, you won’t be able to use this feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
