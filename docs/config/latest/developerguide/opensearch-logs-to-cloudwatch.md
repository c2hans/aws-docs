---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-logs-to-cloudwatch.html
---

# opensearch-logs-to-cloudwatch
<a name="opensearch-logs-to-cloudwatch"></a>

Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs. The rule is NON\_COMPLIANT if logging is not configured.

**Note**
The rule does not evaluate Elasticsearch domains.

**Identifier:** OPENSEARCH\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

logTypes (Optional)Type: CSV
Comma-separated list of logs that are enabled. Valid values are 'search', 'index', 'error'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1203c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
