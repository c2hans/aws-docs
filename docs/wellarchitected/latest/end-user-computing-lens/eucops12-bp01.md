---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp01.html
---

# EUCOPS12-BP01 Deploy alerting mechanisms that quickly identify anomalous metrics
<a name="eucops12-bp01"></a>

 AWS EUC services provide access to desktops and applications which can be highly variable in their resource requirements over time. Weekly, monthly, quarterly, and year-end activities can cause spikes in resource consumption that might result in unnecessary alerts and a degraded user experience.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-13"></a>

 The design and pilot phases of an AWS EUC project should identify resource requirements for each application set over a typical business cycle. Identify the peak activity levels to verify that the compute instance types selected for both Amazon WorkSpaces and WorkSpaces Applications can deliver performance that maintains a good user experience and improves productivity.

 Third party tools from vendors such as ControlUp, Nuvens, LiquidWare, Lakeside Software, and Aternity can be used to collect resource usage trends and build baselines for key applications. Some of these can be found on the AWS Marketplace.

 AWS and the AWS Partner Network offer many services and automation capabilities you can use to automatically and elastically scale backend application services or to provide increased compute capabilities during periods of heavy utilization**.**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
