---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/apprunner-service-observability-enabled.html
---

# apprunner-service-observability-enabled
<a name="apprunner-service-observability-enabled"></a>

Checks if AWS App Runner services have observability enabled. The rule is NON\_COMPLIANT if configuration.ObservabilityConfiguration.ObservabilityEnabled is false'.

**Identifier:** APPRUNNER\_SERVICE\_OBSERVABILITY\_ENABLED

**Resource Types:** AWS::AppRunner::Service

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d177c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
