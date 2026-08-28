---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.html
---

# sagemaker-notebook-no-direct-internet-access
<a name="sagemaker-notebook-no-direct-internet-access"></a>

Checks if direct internet access is disabled for an Amazon SageMaker notebook instance. The rule is NON\_COMPLIANT if a SageMaker notebook instance is internet-enabled.

**Identifier:** SAGEMAKER\_NOTEBOOK\_NO\_DIRECT\_INTERNET\_ACCESS

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1503c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
