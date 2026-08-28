---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/efs-access-point-enforce-root-directory.html
---

# efs-access-point-enforce-root-directory
<a name="efs-access-point-enforce-root-directory"></a>

Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a root directory. The rule is NON\_COMPLIANT if the value of 'Path' is set to '/' (default root directory of the file system).

**Identifier:** EFS\_ACCESS\_POINT\_ENFORCE\_ROOT\_DIRECTORY

**Resource Types:** AWS::EFS::AccessPoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

approvedDirectories (Optional)Type: CSV
Comma-separated list of subdirectory paths that are approved for Amazon EFS access point root directory enforcement.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d691c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
