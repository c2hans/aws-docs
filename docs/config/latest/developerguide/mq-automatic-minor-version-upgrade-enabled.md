---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/mq-automatic-minor-version-upgrade-enabled.html
---

# mq-automatic-minor-version-upgrade-enabled
<a name="mq-automatic-minor-version-upgrade-enabled"></a>

Checks if automatic minor version upgrades are enabled for Amazon MQ brokers. The rule is NON\_COMPLIANT if the 'AutoMinorVersionUpgrade' field is not enabled for an Amazon MQ broker.

**Identifier:** MQ\_AUTOMATIC\_MINOR\_VERSION\_UPGRADE\_ENABLED

**Resource Types:** AWS::AmazonMQ::Broker

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1109c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
