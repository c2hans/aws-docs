---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/apigatewayv2-integration-private-https-enabled.html
---

# apigatewayv2-integration-private-https-enabled
<a name="apigatewayv2-integration-private-https-enabled"></a>

Checks if Amazon API Gateway V2 private integration traffic for HTTP APIs uses the HTTPS protocol. The rule is NON\_COMPLIANT if configuration.TlsConfig does not exist.

**Identifier:** APIGATEWAYV2\_INTEGRATION\_PRIVATE\_HTTPS\_ENABLED

**Resource Types:** AWS::ApiGatewayV2::Integration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7c57c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
