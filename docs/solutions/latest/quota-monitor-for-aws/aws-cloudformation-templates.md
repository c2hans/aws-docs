---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution includes the following CloudFormation templates, which you can download before deployment:

 [![View Template](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/view-template.png)](https://s3.amazonaws.com/solutions-reference/quota-monitor-for-aws/latest/quota-monitor-hub.template) **quota-monitor-hub.template** - Use this template to launch the Quota Monitor for AWS solution and all associated components in the monitoring account.

 [![View Template](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/view-template.png)](https://s3.amazonaws.com/solutions-reference/quota-monitor-for-aws/latest/quota-monitor-sq-spoke.template) **quota-monitor-sq-spoke.template** - Use this template to launch the Quota Monitor for AWS solution and all associated components in secondary accounts to support Service Quotas.

 [![View Template](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-sns-spoke.template) **quota-monitor-sns-spoke.template** - Use this template to launch notification resources in secondary accounts. This stack is optional and should be launched in only one Region within each secondary account.

 [![View Template](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-ta-spoke.template) **quota-monitor-ta-spoke.template** - Use this template to launch the Quota Monitor for AWS solution and all associated components in secondary accounts to support Trusted Advisor.

 [![View Template](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-prerequisite.template) **quota-monitor-prerequisite.template** - Use this supplemental template to fulfill the prerequisites needed for monitoring quotas across AWS Organizations. This template should be launched in the organization management account.

 [![View Template](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-hub-no-ou.template) **quota-monitor-hub-no-ou.template** - Use this supplemental template to launch the Quota Monitor for AWS and all associated components in the monitoring account, when you are not using AWS Organizations.

Refer to [Choose your deployment scenario](step-1.-choose-your-deployment-scenario.md) later in this guide to determine which templates you need to deploy to meet your needs. Refer to the [README.md](https://github.com/aws-solutions/quota-monitor-for-aws/blob/main/README.md) file in the GitHub repository for guidance to customize the template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
