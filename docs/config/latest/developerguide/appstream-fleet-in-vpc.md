---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appstream-fleet-in-vpc.html
---

# appstream-fleet-in-vpc
<a name="appstream-fleet-in-vpc"></a>

Checks if Amazon AppStream 2.0 fleets use an Amazon Virtual Private Cloud (Amazon VPC). The rule is NON\_COMPLIANT if configuration.VpcConfig does not exist. The rule does not check Elastic fleets.

**Identifier:** APPSTREAM\_FLEET\_IN\_VPC

**Resource Types:** AWS::AppStream::Fleet

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d183c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
