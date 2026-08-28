---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appmesh-virtual-gateway-listeners-health-check-enabled.html
---

# appmesh-virtual-gateway-listeners-health-check-enabled
<a name="appmesh-virtual-gateway-listeners-health-check-enabled"></a>

Checks if listeners for AWS App Mesh virtual gateways have health check enabled. The rule is NON\_COMPLIANT if configuration.Spec.Listeners[].HealthCheck does not exist in one or more listeners.

**Identifier:** APPMESH\_VIRTUAL\_GATEWAY\_LISTENERS\_HEALTH\_CHECK\_ENABLED

**Resource Types:** AWS::AppMesh::VirtualGateway

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d139c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
