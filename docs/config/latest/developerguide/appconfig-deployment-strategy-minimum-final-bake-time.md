---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appconfig-deployment-strategy-minimum-final-bake-time.html
---

# appconfig-deployment-strategy-minimum-final-bake-time
<a name="appconfig-deployment-strategy-minimum-final-bake-time"></a>

Checks if an AWS AppConfig deployment strategy requires the specified minimum bake time. The rule is NON\_COMPLIANT if the deployment strategy has a final bake time less than value specified in the rule parameter. The default value is 30 minutes.

**Identifier:** APPCONFIG\_DEPLOYMENT\_STRATEGY\_MINIMUM\_FINAL\_BAKE\_TIME

**Resource Types:** AWS::AppConfig::DeploymentStrategy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

minBakeTime (Optional)Type: intDefault: 30
The minimum bake time in minutes of the AWS AppConfig deployment strategy for the rule to check. The rule is NON\_COMPLIANT if the bake time is less than the value specified in this parameter. Valid values are 0 to 1440. The default value is 30.

## AWS CloudFormation template
<a name="w2aac20c16c17b7c99c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
