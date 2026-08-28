---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/apprunner-service-max-unhealthy-threshold.html
---

# apprunner-service-max-unhealthy-threshold
<a name="apprunner-service-max-unhealthy-threshold"></a>

Checks if an AWS App Runner service is configured to have an unhealthy threshold less than or equal to the specified value. The rule is NON\_COMPLIANT if the unhealthy threshold is greater than the value specified in the required rule parameter.

**Identifier:** APPRUNNER\_SERVICE\_MAX\_UNHEALTHY\_THRESHOLD

**Resource Types:** AWS::AppRunner::Service

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

maxUnhealthyThresholdType: int
The maximum unhealthy threshold value for the rule to check. The rule is NON\_COMPLIANT if an AWS App Runner service is configured with an unhealthy threshold greater than this value. Valid values are 1 to 20

## AWS CloudFormation template
<a name="w2aac20c16c17b7d173c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
