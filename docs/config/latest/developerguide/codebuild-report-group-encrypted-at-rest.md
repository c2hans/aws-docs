---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-report-group-encrypted-at-rest.html
---

# codebuild-report-group-encrypted-at-rest
<a name="codebuild-report-group-encrypted-at-rest"></a>

Checks if an AWS CodeBuild report group has encryption at rest setting enabled. The rule is NON\_COMPLIANT if 'EncryptionDisabled' is 'true'.

**Identifier:** CODEBUILD\_REPORT\_GROUP\_ENCRYPTED\_AT\_REST

**Resource Types:** AWS::CodeBuild::ReportGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d387c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
