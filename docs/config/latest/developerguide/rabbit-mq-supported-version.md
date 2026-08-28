---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rabbit-mq-supported-version.html
---

# rabbit-mq-supported-version
<a name="rabbit-mq-supported-version"></a>

Checks if an Amazon MQ RabbitMQ broker is running on a specified minimum supported engine version. The rule is NON\_COMPLIANT if the RabbitMQ broker is not running on the minimum supported engine version that you specify.

**Identifier:** RABBIT\_MQ\_SUPPORTED\_VERSION

**Resource Types:** AWS::AmazonMQ::Broker

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

supportedEngineVersionType: String
String value for the rule to check the minimum supported engine version for the RabbitMQ broker. RabbitMQ brokers use semantic versioning specification: X.Y.Z. X denotes the major version, Y represents the minor version, and Z denotes the patch version.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1213c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
