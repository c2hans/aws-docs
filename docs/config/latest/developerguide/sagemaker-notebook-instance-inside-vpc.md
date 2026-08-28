---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-inside-vpc.html
---

# sagemaker-notebook-instance-inside-vpc
<a name="sagemaker-notebook-instance-inside-vpc"></a>

Checks if an Amazon SageMaker notebook instance is launched within a VPC or within a list of approved subnets. The rule is NON\_COMPLIANT if a notebook instance is not launched within a VPC or if its subnet ID is not included in the parameter list.

**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_INSIDE\_VPC

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

SubnetIds (Optional)Type: CSV
Comma-separated list of subnet IDs that notebook instances can be launched in.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1493c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
