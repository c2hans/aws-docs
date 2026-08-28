---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-model-quality-job-encrypt-in-transit.html
---

# sagemaker-model-quality-job-encrypt-in-transit
<a name="sagemaker-model-quality-job-encrypt-in-transit"></a>

Checks if Amazon SageMaker model quality job definitions have inter-container traffic encryption enabled when the instance count is 2 or greater. The rule is NON\_COMPLIANT if configuration.NetworkConfig.EnableInterContainerTrafficEncryption is false.

**Identifier:** SAGEMAKER\_MODEL\_QUALITY\_JOB\_ENCRYPT\_IN\_TRANSIT

**Resource Types:** AWS::SageMaker::ModelQualityJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1487c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
