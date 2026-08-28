---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/efs-access-point-enforce-user-identity.html
---

# efs-access-point-enforce-user-identity
<a name="efs-access-point-enforce-user-identity"></a>

Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a user identity. The rule is NON\_COMPLIANT if 'PosixUser' is not defined or if parameters are provided and there is no match in the corresponding parameter.

**Identifier:** EFS\_ACCESS\_POINT\_ENFORCE\_USER\_IDENTITY

**Resource Types:** AWS::EFS::AccessPoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), Israel (Tel Aviv), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedUids (Optional)Type: CSV
Comma-separated list of POSIX user ID that are approved for EFS access point user enforcement.

approvedGids (Optional)Type: CSV
Comma-separated list of POSIX group IDs that are approved for EFS access point user enforcement.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d693c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
