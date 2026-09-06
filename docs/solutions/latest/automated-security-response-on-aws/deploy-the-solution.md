---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

**Important**
If the [consolidated control findings](deciding-where-to-deploy-each-stack.md#consolidated-controls-findings) feature is turned on in AWS Security Hub, only enable the Security Control (SC) playbook when deploying this solution. If the feature is not turned on, **only** enable the playbooks for the security standards that are enabled in Security Hub. Consolidated control findings is enabled by default if you enable Security Hub CSPM on or after February 23, 2023.

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

In order for the solution to function, three templates must be deployed. First, decide where to deploy the templates, then decide how to deploy them.

This overview will describe the templates and how to decide where and how to deploy them. The next sections will have more detailed instructions for deploying each stack as a Stack or StackSet.
