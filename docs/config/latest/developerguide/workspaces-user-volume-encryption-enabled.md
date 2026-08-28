---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/workspaces-user-volume-encryption-enabled.html
---

# workspaces-user-volume-encryption-enabled
<a name="workspaces-user-volume-encryption-enabled"></a>

Checks if an Amazon WorkSpace volume has the user volume encryption settings set to enabled. This rule is NON\_COMPLIANT if the encryption setting is not enabled for the user volume.

**Identifier:** WORKSPACES\_USER\_VOLUME\_ENCRYPTION\_ENABLED

**Resource Types:** AWS::WorkSpaces::Workspace

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Africa (Cape Town), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1641c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
