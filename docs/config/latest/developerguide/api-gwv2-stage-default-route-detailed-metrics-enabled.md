---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/api-gwv2-stage-default-route-detailed-metrics-enabled.html
---

# api-gwv2-stage-default-route-detailed-metrics-enabled
<a name="api-gwv2-stage-default-route-detailed-metrics-enabled"></a>

Checks if the default route settings for Amazon API Gateway V2 stages have detailed metrics enabled. The rule is NON\_COMPLIANT if configuration.defaultRouteSettings.detailedMetricsEnabled is false.

**Identifier:** API\_GWV2\_STAGE\_DEFAULT\_ROUTE\_DETAILED\_METRICS\_ENABLED

**Resource Types:** AWS::ApiGatewayV2::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7c71c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
