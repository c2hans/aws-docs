---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this guidance
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this guidance](architecture-details.md#aws-services-in-this-solution). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Select one of the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](step-2-launch-the-chatbot-content-designer.md) in this guidance. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this guidance successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User’s Guide*.

## Amazon Lex quotas
<a name="amazon-lex-quotas"></a>

Your AWS account has Amazon Lex quotas, which you can view by following these steps:

1. Sign in to the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas).

1. Choose **AWS services** from the left navigation menu.

1. Enter `Amazon Lex` in the **Find services** field.

1. Choose **Amazon Lex**.

Amazon Lex V2 requires the fulfillment Lambda’s maximum output size to be set to 50 KB. You cannot adjust this setting through the AWS account’s Service endpoints and quotas. You might reach this quota when you are trying to return very large responses by increasing the number of words or context in the response. Additionally, when you use RAG with Amazon Kendra or Knowledge Bases for Amazon Bedrock, you might want to limit your output by customizing the settings such as prompt templates, max retrieved results, or documents.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
