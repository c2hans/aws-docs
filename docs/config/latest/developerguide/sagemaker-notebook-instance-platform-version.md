---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-platform-version.html
---

# sagemaker-notebook-instance-platform-version
<a name="sagemaker-notebook-instance-platform-version"></a>

Checks if a Sagemaker Notebook Instance is configured to use a supported platform identifier version. The rule is NON\_COMPLIANT if a Notebook Instance is not using the specified supported platform identifier version as specified in the parameter.

**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_PLATFORM\_VERSION

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

supportedPlatformIdentifierVersionsType: CSV
Comma-separated list of the supported platform identifier version for the rule to check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1497c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
