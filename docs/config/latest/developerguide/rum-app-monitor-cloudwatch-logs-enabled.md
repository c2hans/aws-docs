---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rum-app-monitor-cloudwatch-logs-enabled.html
---

# rum-app-monitor-cloudwatch-logs-enabled
<a name="rum-app-monitor-cloudwatch-logs-enabled"></a>

Checks if Amazon CloudWatch RUM app monitors have CloudWatch logs enabled. The rule is NON\_COMPLIANT if configuration.CwLogEnabled is false.

**Identifier:** RUM\_APP\_MONITOR\_CLOUDWATCH\_LOGS\_ENABLED

**Resource Types:** AWS::RUM::AppMonitor

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1371c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
