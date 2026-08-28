---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-primary-node-fault-tolerance.html
---

# opensearch-primary-node-fault-tolerance
<a name="opensearch-primary-node-fault-tolerance"></a>

Checks if Amazon OpenSearch Service domains are configured with at least three dedicated primary nodes. The rule is NON\_COMPLIANT for an OpenSearch Service domain if 'DedicatedMasterEnabled' is set to 'false', or 'DedicatedMasterCount' is less than 3.

**Identifier:** OPENSEARCH\_PRIMARY\_NODE\_FAULT\_TOLERANCE

**Resource Types:** AWS::OpenSearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1207c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
