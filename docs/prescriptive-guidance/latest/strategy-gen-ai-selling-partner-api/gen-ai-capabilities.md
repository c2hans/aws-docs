---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/gen-ai-capabilities.html
---

# Implementing a generative AI strategy for your Amazon selling partner data
<a name="gen-ai-capabilities"></a>

Amazon vendors and sellers can use generative artificial intelligence (generative AI) services and features on AWS to gain deeper insights, automate repetitive tasks, and enhance your customer experience on Amazon. For example, you can use generative AI to automatically create optimized, high-quality product descriptions for your Amazon listings, generate marketing copy or customer communications, or forecast sales, inventory, and other key business metrics. Generative AI can provide insights into the data that you've ingested from the Amazon Selling Partner API.

The following architecture diagram shows how you can use AWS services, such as [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) or [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html), to kick-start your generative AI journey on AWS. Using this architecture, you build a generative AI pipeline that uses a modern data analytics approach to derive insights from the data.

![Using AWS generative AI services to unlock insights from the Amazon Selling Partner API data](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/images/guide-img/fd951ab0-b7f5-4ded-9451-ea838cf4c59a/images/9ccd931e-e334-4a06-bceb-913219a44821.png)

The architecture diagram includes the following components:

1. [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) is used to build the scalable data lake and to centrally manage the security, access control, and audit trails.

1. [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is used as the data lake storage.

1. [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that offers a choice of industry-leading foundation models (FMs). It also provides a broad set of capabilities that you need to build generative AI applications, simplifying development with security, privacy, and responsible AI. You can store the model output data in an Amazon S3 bucket and can integrate it to Amazon Quick.

1. [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) provides ML-powered business intelligence. [Quick Q](https://docs.aws.amazon.com/quicksight/latest/user/working-with-quicksight-q.html) enhances business productivity with generative BI capabilities to accelerate decision making. With new dashboard-authoring capabilities, you can use natural language prompts to quickly build, discover, and share meaningful insights.

1. [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) is a generative AI–powered assistant that can answer questions, provide summaries, generate content, and securely complete tasks based on data and information in your enterprise systems. It helps you be more creative, data-driven, efficient, prepared, and productive.

1. You can create a custom web application that consumes the data from Amazon Q Business.

## Examples of using Quick Q
<a name="examples-of-using-qs-q"></a>

The following examples show how Quick Q helps you understand data with executive summaries, a context-aware data Q&A experience, and customizable, interactive data stories that help drive decisions from insights.

### Example 1
<a name="example-1.e5963145-49ab-5422-a331-ef7cffe2737c"></a>

You can ask Quick Q "What are the top sold items in 2023?" Quick Q gathers and analyzes the data in order to provide an executive summary.

![An executive-level summary and chart.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/images/guide-img/fd951ab0-b7f5-4ded-9451-ea838cf4c59a/images/dcd82d3a-878f-4871-a34c-cc9a6ae13abb.png)

### Example 2
<a name="example-2.c1d14b25-2e3a-50d2-a370-1ae573299409"></a>

You can ask Quick Q what are the top products that an enterprise sells on Amazon.

![Prompts for data about top products.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/images/guide-img/fd951ab0-b7f5-4ded-9451-ea838cf4c59a/images/22bbbf15-f5d9-4793-9dec-336985edb9e8.png)

### Example 3
<a name="example-3.b3aa8ba8-3e5e-5ee0-83a9-7113cd40fa20"></a>

You can ask Quick Q to provide sales metrics for a product, based on month or year-to-date.

![Prompts for sales metrics for different time periods.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/images/guide-img/fd951ab0-b7f5-4ded-9451-ea838cf4c59a/images/80ba0f0a-0c9e-4a4c-a3bb-f91e1084e0ea.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
