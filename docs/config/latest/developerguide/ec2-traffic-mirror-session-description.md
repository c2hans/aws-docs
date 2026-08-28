---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-traffic-mirror-session-description.html
---

# ec2-traffic-mirror-session-description
<a name="ec2-traffic-mirror-session-description"></a>

Checks if Amazon EC2 traffic mirror sessions have a description. The rule is NON\_COMPLIANT if configuration.Description does not exist.

**Identifier:** EC2\_TRAFFIC\_MIRROR\_SESSION\_DESCRIPTION

**Resource Types:** AWS::EC2::TrafficMirrorSession

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d625c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
