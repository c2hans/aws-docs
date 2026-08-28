---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-source-repo-url-check.html
---

# codebuild-project-source-repo-url-check
<a name="codebuild-project-source-repo-url-check"></a>

Checks if the Bitbucket source repository URL contains sign-in credentials or not. The rule is NON\_COMPLIANT if the URL contains any sign-in information and COMPLIANT if it doesn't.

**Identifier:** CODEBUILD\_PROJECT\_SOURCE\_REPO\_URL\_CHECK

**Resource Types:** AWS::CodeBuild::Project

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d383c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
