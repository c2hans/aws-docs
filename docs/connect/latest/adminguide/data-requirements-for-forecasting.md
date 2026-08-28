---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/data-requirements-for-forecasting.html
---

# Data requirements for forecasting in Connect Customer
<a name="data-requirements-for-forecasting"></a>

Connect Customer generates forecasts using a machine-learning model tailored for contact center operations. The following are the historical input data requirements for both short-term and long-term forecasts.
+ **Historical data minimum requirement**: At least 1 forecast group should have a minimum of 1,000 contacts per month in the last 6 months.
+ **Historical data maximum duration**: Forecasting models use a maximum of 156 weeks of historical data.
+ For a queue channel to have non-zero forecasts, it needs at least 1 record in last 4 weeks or 28 days.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
