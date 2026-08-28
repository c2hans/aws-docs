---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/alarms.html
---

# Managing alarms
<a name="alarms"></a>

When you run a resiliency assessment, as a part of operational recommendations, AWS Resilience Hub recommends setting up Amazon CloudWatch alarms to monitor your application resiliency. We recommend these alarms based on the resources and components of your current application configuration. If the resources and components in your application change, you should run a resiliency assessment to ensure you have the correct Amazon CloudWatch alarms for your updated application.

Additionally, AWS Resilience Hub now automatically detects and integrates any already configured Amazon CloudWatch alarms into its resilience assessments, providing a more comprehensive view of your application's resilience posture. This new capability combines AWS Resilience Hub recommendations with your current monitoring setup, streamlining alarm management and enhancing assessment accuracy. If you have implemented an Amazon CloudWatch alarm and AWS Resilience Hub doesn't automatically detect it, you can exclude the alarm and select the reason as **Already implemented**. For more information about excluding recommendation, see [Including or excluding operational recommendations](exclude-recommend.md).

AWS Resilience Hub provides a template file (`README.md`) that allows you to create alarms recommended by AWS Resilience Hub within AWS (such as Amazon CloudWatch) or outside AWS. The default values provided in the alarms are based on the best practices that are used for creating these alarms.

**Topics**
+ [Creating alarms from the operational recommendations](create-alarm.md)
+ [Viewing alarms](view-alarm.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
