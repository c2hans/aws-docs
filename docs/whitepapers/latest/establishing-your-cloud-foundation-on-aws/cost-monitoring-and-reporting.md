---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/cost-monitoring-and-reporting.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost monitoring and reporting
<a name="cost-monitoring-and-reporting"></a>

Visibility across your cloud environment is critical. Your cloud team and your finance teams will require visibility into the cloud spend, and stakeholders owning business units and workloads need the ability to generate and save custom reports. Doing so, will create a [cost-aware culture](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost-aware-culture.html) within your organization.

Specific reports generated for the different workloads in your environment will allow different stakeholders to create different views of the environment, based on groups of resources, environments, or stages of development, and will enable them to forecast the spend or detect anomalies in costs during a specific time frame.

The level of granularity and visibility in reports can be enabled at different levels for different dashboards, and is granted based on roles and groups for each of the workloads via federation. A few examples are:

1. In order to analyze and monitor your entire environment, your cloud team and/or your FinOps team will need access to the environment level billing. From here, they can set up budgets, analyze spend trends, and detect anomalies across the entire environment.

1. A business owner needs visibility across the different workloads and applications, access can be granted for the specific group of resources or custom dashboards to visualize the spend for each of the workloads.

1. A builder, a developer, or an individual user needs visibility, access can be granted to visualize the cost associated with the resources they are using, or within their sandbox environment.

Setting up the right monitoring tools for spend in your environment will allow you to evaluate different spend patterns. Evaluating your patterns weekly or monthly with these reports, can help you determine if any anomalies in spend patterns exist, and quickly identify and remediate the root cause.

Defining metrics that allow you to identify if your cost strategy is successful, for example `unit-cost`. This will feed into your overall finance strategy, allowing your technology and business stakeholders identify cost-saving opportunities and repurpose some of the savings to new initiatives or projects to enhance your cloud environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
