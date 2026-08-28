---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-features-activation-model.html
---

# Feature names for protection plans in GuardDuty API
<a name="guardduty-features-activation-model"></a>

When you enable Amazon GuardDuty for the first time, it starts processing [Foundational data sources](guardduty_data-sources.md) within your AWS environment. GuardDuty uses these data sources to process an independent stream of events such as VPC flow logs, DNS logs, and AWS CloudTrail management events. It then analyzes these events to identify potential security threats and generates findings in your account.

When one or more protection plans are enabled, then GuardDuty uses additional data from other AWS services in your AWS environment to monitor and analyze for potential security threats. These additional data sources are called features.

## Change from data sources to features
<a name="guardduty-features"></a>

When you add additional GuardDuty protections, such as S3 Protection, Runtime Monitoring, Lambda Protection, and others, you can configure the GuardDuty feature corresponding to the protection plan. Historically, GuardDuty protections were called `dataSources` in the APIs. However, after March 2023, new GuardDuty protection plans are now configured as `features` and not `dataSources`. GuardDuty still supports configuring protection plans launched before March 2023, as `dataSources` through the API, but new protection plans are only available as `features`. For information about which protection plans are impacted, see [GuardDuty API changes](guardduty-feature-object-api-changes-march2023.md).

If you manage GuardDuty configuration and protection plans through the console, you are not directly impacted by this change and don't need to take any action. This change affects the behavior of the APIs that are invoked to enable GuardDuty or protection plans within GuardDuty. If you use APIs or AWS CLI to enable or edit the configuration of a protection plan, you must use the associated feature name. For more information, see [Mapping `dataSources` to `features`](guardduty-feature-object-api-changes-march2023.md#guardduty-feature-enablement-datasource-relation).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
