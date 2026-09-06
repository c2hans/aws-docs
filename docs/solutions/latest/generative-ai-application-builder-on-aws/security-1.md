---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, virtualization layer, and physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## Using foundation models on Amazon Bedrock
<a name="using-third-party-models-on-amazon-bedrock"></a>

Amazon Bedrock hosts a collection of models from Amazon Nova models to other leading foundation models (FMs). When using Amazon Bedrock, all models are hosted within the AWS infrastructure. This means that when using Amazon Bedrock as the LLM provider, all of your inference requests will remain within the AWS network and network traffic will not leave your Region.

**Note**
All foundation models (FMs) available through Amazon Bedrock are hosted directly on AWS infrastructure managed and owned by AWS. Model providers do not have access to customer data such as prompts and continuations, or Amazon Bedrock service logs. For additional information about Amazon Bedrock’s security posture, refer to [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/) in the *Amazon Bedrock User Guide*.

## IAM roles
<a name="iam-roles"></a>

IAM roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates IAM roles that grant the solution’s Lambda functions access to create Regional resources.

## CloudWatch Logs
<a name="cloudwatch-logs"></a>

You can enable verbose mode while deploying a use case using the Deployment Dashboard model selection page, under Additional Settings. Verbose mode enables detailed CloudWatch logs which can be helpful for debugging and prompt experimentation.

**Note**
When verbose mode is enabled, retrieved documents from the knowledge base (if RAG is enabled) and prompts will also be logged, which may contain sensitive information.
