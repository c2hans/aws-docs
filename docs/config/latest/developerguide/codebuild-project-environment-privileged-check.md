---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-environment-privileged-check.html
---

# codebuild-project-environment-privileged-check
<a name="codebuild-project-environment-privileged-check"></a>

Checks if an AWS CodeBuild project environment has privileged mode enabled. The rule is NON\_COMPLIANT for a CodeBuild project if ‘privilegedMode’ is set to ‘true’.

**Identifier:** CODEBUILD\_PROJECT\_ENVIRONMENT\_PRIVILEGED\_CHECK

**Resource Types:** AWS::CodeBuild::Project

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

exemptedProjects (Optional)Type: CSV
Comma-separated list of CodeBuild project names that are allowed to have ‘privilegedMode’ with value ‘true’.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d375c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
