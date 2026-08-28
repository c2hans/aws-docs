---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-explainability-job-network-isolation.html
---

# sagemaker-model-explainability-job-network-isolation
<a name="sagemaker-model-explainability-job-network-isolation"></a>

Checks whether an Amazon SageMaker model explainability job definition has network isolation enabled. The rule is NON\_COMPLIANT if NetworkConfig.EnableNetworkIsolation is not set to true.

**Identifier:** SAGEMAKER\_MODEL\_EXPLAINABILITY\_JOB\_NETWORK\_ISOLATION

**Resource Types:** AWS::SageMaker::ModelExplainabilityJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1475c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
