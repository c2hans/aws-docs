---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution includes the following CloudFormation templates, which you can download before deployment:

 [https://s3.amazonaws.com/solutions-reference/quota-monitor-for-aws/latest/quota-monitor-hub.template](https://s3.amazonaws.com/solutions-reference/quota-monitor-for-aws/latest/quota-monitor-hub.template) **quota-monitor-hub.template** - Use this template to launch the Quota Monitor for AWS solution and all associated components in the monitoring account.

 [https://s3.amazonaws.com/solutions-reference/quota-monitor-for-aws/latest/quota-monitor-sq-spoke.template](https://s3.amazonaws.com/solutions-reference/quota-monitor-for-aws/latest/quota-monitor-sq-spoke.template) **quota-monitor-sq-spoke.template** - Use this template to launch the Quota Monitor for AWS solution and all associated components in secondary accounts to support Service Quotas.

 [https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-sns-spoke.template](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-sns-spoke.template) **quota-monitor-sns-spoke.template** - Use this template to launch notification resources in secondary accounts. This stack is optional and should be launched in only one Region within each secondary account.

 [https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-ta-spoke.template](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-ta-spoke.template) **quota-monitor-ta-spoke.template** - Use this template to launch the Quota Monitor for AWS solution and all associated components in secondary accounts to support Trusted Advisor.

 [https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-prerequisite.template](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-prerequisite.template) **quota-monitor-prerequisite.template** - Use this supplemental template to fulfill the prerequisites needed for monitoring quotas across AWS Organizations. This template should be launched in the organization management account.

 [https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-hub-no-ou.template](https://solutions-reference.s3.amazonaws.com/quota-monitor-for-aws/latest/quota-monitor-hub-no-ou.template) **quota-monitor-hub-no-ou.template** - Use this supplemental template to launch the Quota Monitor for AWS and all associated components in the monitoring account, when you are not using AWS Organizations.

Refer to [Choose your deployment scenario](step-1.-choose-your-deployment-scenario.md) later in this guide to determine which templates you need to deploy to meet your needs. Refer to the [README.md](https://github.com/aws-solutions/quota-monitor-for-aws/blob/main/README.md) file in the GitHub repository for guidance to customize the template.
