---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/best-practices-revisions.html
---

# Revision access rules in AWS Data Exchange
<a name="best-practices-revisions"></a>

Revision access rules specify which revisions subscribers can access when they subscribe to your product in AWS Data Exchange. You choose options for subscribers to get historical and future revisions.
+ *Historical revision options* – Historical revisions are revisions that you published prior to the subscription start date. You have three options for historical revisions:
  + **All pre-existing revisions published prior to subscription** – Give your subscribers access to all historical revisions.
  + **A fixed number of trailing revisions published prior to subscription** – You choose how many historical revisions your subscribers have access to (from 1 to 100).
  + **No historical revisions** – Your subscribers get no access to historical revisions. With this option, your subscribers will initially have no data available, until you publish your next revision after their subscription starts.
+ *Future revision options* – Future revisions are revisions that you publish after subscription start. You have two options for future revisions:
  + **All future revisions published during subscription duration** – Give your subscribers access to all revisions that you publish until their subscription expires.
  + **No future revisions** – Your subscribers get no access to future revisions.

**Note**
You can't choose both **No historical revisions** and **No future revisions**. That would create a product with no revisions and no data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
