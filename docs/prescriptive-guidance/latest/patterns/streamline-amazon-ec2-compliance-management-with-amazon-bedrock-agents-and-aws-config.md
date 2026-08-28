---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config.html
---

# Streamline Amazon EC2 compliance management with Amazon Bedrock agents and AWS Config
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config"></a>

*Anand Bukkapatnam Tirumala, Amazon Web Services*

## Summary
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-summary"></a>

This pattern describes how to integrate Amazon Bedrock with AWS Config rules to facilitate compliance management for Amazon Elastic Compute Cloud (Amazon EC2) instances. The approach uses advanced generative AI capabilities to provide tailored recommendations that are aligned with the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), to ensure optimal instance type selection and system efficiency. Key features of this pattern include:
+ Automated compliance monitoring: AWS Config rules continuously assess EC2 instances against predefined criteria for desired instance types.
+ AI-driven recommendations: The generative AI models in Amazon Bedrock analyze infrastructure patterns. These models provide intelligent suggestions for improvements based on best practices that are outlined in the AWS Well-Architected Framework.
+ Remediation: Amazon Bedrock action groups enable automated remediation steps to swiftly address non-compliant instances and minimize potential performance or cost inefficiencies.
+ Scalability and adaptability: The solution is designed to scale with your infrastructure and adapt to your evolving cloud architecture needs.
+ Enhanced security recommendations: Compliance with AWS Well-Architected principles contributes to improved security posture and system performance.

You can use this pattern as a blueprint to deploy your own generative AI-based infrastructure into multiple environments with minimal changes, using DevOps practices as necessary.

## Prerequisites and limitations
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An AWS Identity and Access Management (IAM) role with permissions to create and manage resources in Amazon Simple Storage Service (Amazon S3) buckets, AWS Config, AWS Lambda functions, Amazon Bedrock, IAM, Amazon CloudWatch Logs, and Amazon EC2.
+ An EC2 instance to flag as non-compliant. Do not use the  `t2.small` type for this instance.
+ [Amazon Titan Text Embeddings V2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) and Anthropic Claude 3 Haiku models enabled in your AWS account. To enable model access for the AWS Region where you are deploying the solution, see [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) in the Amazon Bedrock documentation.
+ [Terraform](https://developer.hashicorp.com/terraform/install), installed and configured.
+ The [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) v2 installed and configured in the deployment environment.
+ Completed review of the [Amazon Responsible AI policy](https://aws.amazon.com/ai/responsible-ai/policy/).

**Limitations **
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.
+ This solution has been tested by using the Amazon Titan Text Embeddings V2 and Claude 3 Haiku models. If you prefer to use other models, you can customize the Terraform code, which is parameterized for easy changes.
+ This solution does not include a chat history feature, and the chat isn't stored.

## Architecture
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Architecture and workflow for streamlining Amazon EC2 compliance management with Amazon Bedrock agents.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f43ae2bd-209e-412b-9364-e73996360992/images/4ebf4bce-4927-4d78-841e-95c44b8d780f.png)

The workflow consists of these steps:

1. The user interacts with the model through the Amazon Bedrock chat console. The user asks questions such as:
   + `What can you help me with?`
   + `List non-complaint resources`
   + `Suggest security best practices`

1. If the model is pre-trained, it responds to the prompts directly from its existing knowledge. Otherwise, the prompt goes to the Amazon Bedrock action group.

1. The action group reaches the [VPC endpoints ](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html)by using [AWS PrivateLink](https://aws.amazon.com/privatelink/) for secure service communication.

1. The request reaches the Lambda function through the VPC endpoints for Amazon Bedrock services.

1. The Lambda function is the primary execution engine. Based on the request, the function calls the API to perform actions on the AWS services. It also handles operation routing and execution.

1. The Lambda function calls AWS Config to determine non-complaint resources (the non-compliant EC2 instance that you created as a prerequisite).

1. AWS Config flags the non-complaint resource. This pattern deploys the AWS Config [desired-instance-type](https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-type.html) rule to find the ideal EC2 instance size.

1. AWS Config prompts the user to pause or remediate the instance, and takes action accordingly on the EC2 instance. Amazon Bedrock understands this return payload.

1. The user receives a response on the Amazon Bedrock chat console.

**Automation and scale**

This solution uses Terraform as an infrastructure as code (IaC) tool to enable easy deployment to AWS accounts and to function as a standalone utility across multiple accounts. This approach simplifies management and improves consistency in deployments.

## Tools
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-tools"></a>

**AWS services**
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) enables you to assess, audit, and evaluate the configurations of your AWS resources for compliance and desired settings.
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed AI service that provides access to many high-performing foundation models through a unified API.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

**Other tools**
+ [Git](https://git-scm.com/docs) is an open source, distributed version control system.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [sample-awsconfig-bedrock-compliance-manager](https://github.com/aws-samples/sample-awsconfig-bedrock-compliance-manager) repository.

## Best practices
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-best-practices"></a>
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices and use cases](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the IAM documentation.
+ Monitor Lambda execution logs regularly. For more information, see [Monitoring, debugging, and troubleshooting Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html) and [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) in the Lambda documentation.

## Epics
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-epics"></a>

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the repository for this pattern, use the following command:<pre>git clone "git@github.com:aws-samples/sample-awsconfig-bedrock-compliance-manager.git"</pre> | AWS DevOps, Build lead, DevOps engineer, Cloud administrator |
| Edit the environment variables. | In the root directory of the cloned repository on your local machine, edit the `terraform.tfvars` file. Review the placeholders that are marked with `[XXXXX]`, and edit them based on your environment. | AWS systems administrator, AWS DevOps, DevOps engineer, AWS administrator |
| Create the infrastructure. | 1. To create the infrastructure for this solution, run the following commands:<pre>terraform init<br />terraform plan</pre><br />2. Review the execution plan, and then run the command:<pre>terraform apply --auto-approve</pre> | AWS DevOps, DevOps engineer, AWS systems administrator, Cloud administrator |

### Use the agent
<a name="use-the-agent"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Chat with the agent. | Deploying the solution in the previous step deploys `security-bot-agent`, which is an Amazon Bedrock agent with a chat console.<br />To use the agent:1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/).<br />2. In the navigation pane, choose **Build**, **Agents**. Select **security-bot-agent**.<br />3. Start conversing with the agent. For example:<pre>List non-complaint EC2 instances</pre><br />and:<pre>Replace these non-complaint EC2 instances with compliant instances</pre> | AWS DevOps, DevOps engineer, AWS systems administrator, Cloud administrator |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the infrastructure and resources. | When you’ve completed your work with this solution, you can delete the infrastructure created by this pattern by running the command:<pre>terraform destroy --auto-approve</pre> | AWS DevOps, DevOps engineer, AWS systems administrator, Cloud administrator |

## Troubleshooting
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Agent behavior issues | For troubleshooting information, see [Test and troubleshoot agent behavior](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html) in the Amazon Bedrock documentation. |
| AWS Lambda network issues | For more information, see [Troubleshoot networking issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-networking.html) in the Lambda documentation. |
| IAM permissions | For more information, see [Troubleshoot IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html)in the IAM documentation. |

## Related resources
<a name="streamline-amazon-ec2-compliance-management-with-amazon-bedrock-agents-and-aws-config-resources"></a>
+ [Amazon Bedrock agents](https://aws.amazon.com/bedrock/agents/)
+ [Use action groups to define actions for your agent to perform](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html) (Amazon Bedrock documentation)
+ [desired-instance-type rule](https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-type.html) (AWS Config documentation)
+ [How AWS Config works](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html) (AWS Config documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
