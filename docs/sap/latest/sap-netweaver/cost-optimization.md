---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/cost-optimization.html
---

# Cost Optimization
<a name="cost-optimization"></a>

Resources (CPU, Memory, additional application servers, system copies for different tests/validations, and so on) require SAP landscape changes over time. AWS recommends that you monitor system utilization and the need for existing systems on a regular basis and take actions to reduce cost. In case of a database like SQL Server, the only opportunity to right-size the database server is by scaling up/down or shutting it down, if not required. Here are few suggestions that you can consider for cost optimization:
+ Consider Reserved instances over On-Demand instances if the requirement is to run your instances 24x7 365 days per year. Reserved instances provide up to a 75% discount over On-Demand instances. See [EC2 pricing](https://aws.amazon.com/ec2/pricing/) for details.
+ Consider running occasionally required systems like training, sandbox, and so on, on-demand for the duration required.
+ Monitor CPU and memory utilization over time for other non-production systems like Dev/QA and right-size them when possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
