---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/deploy-the-solution.html
---

# Deploy the guidance
<a name="deploy-the-solution"></a>

This guidance uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates to describe the AWS resources included in this guidance and their properties. The CloudFormation stack provisions the resources that are described in the template.

## Deployment process overview
<a name="deployment-process-overview"></a>

Before you launch the guidance, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security-1.md), and [other considerations](plan-your-deployment.md) discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the guidance into your account.

 **Time to deploy:** Approximately 30-45 minutes

 [Step 1: Launch the stack](step-1-launch-the-stack.md)
+ Launch the AWS CloudFormation template into your AWS account.
+ Enter values for the required parameters.
+ Review the template parameters, and adjust if necessary.

 [Step 2. Launch the chatbot content designer](step-2-launch-the-chatbot-content-designer.md)
+ Update password and sign in to the content designer.

 [Step 3: Populate the chatbot with your questions and answers](step-3-populate-the-chatbot-with-your-questions-and-answers.md)
+ Enter question and answer pairs.

 [Step 4: Interact with the chatbot](step-4-interact-with-the-chatbot.md)
+ Interact with the chatbot through voice or text.

**Important**
This guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the guidance. For more information, see the [Anonymized data collection](reference.md#anonymized-data-collection) section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
