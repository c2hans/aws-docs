---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/introduction.html
---

# Building a scalable web crawling system for ESG data on AWS
<a name="introduction"></a>

*Vijit Vashishtha and Mansi Doshi, Amazon Web Services*

Environmental, social, and governance (ESG) factors are critical considerations for investors when evaluating potential investments:
+ **Environmental** ­– Focuses on a company's impact on the natural world. It includes factors like carbon emissions, resource management, and energy efficiency.
+ **Social** ­– Examines how a company manages relationships with employees, suppliers, customers, and communities. It covers aspects like labor practices, diversity, and community engagement.
+ **Governance** ­– Looks at a company's leadership, internal controls, and shareholder rights. It includes board composition, executive compensation, and business ethics.

Companies with robust ESG practices are increasingly viewed as better positioned for long-term sustainability and profitability. There is growing investor demand for ESG information. Companies that can demonstrate their sustainability credentials through reliable, useful ESG data are better positioned to attract capital and remain competitive. Companies publish ESG data through various sources, such as news, articles, and annual reports. Because this information is scattered, a web crawler can help you efficiently gather this data.

This comprehensive guide demonstrates how to use [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html), [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html), and [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to build a robust, scalable, and responsible data collection pipeline. It discusses the following:
+ Architecting a scalable crawling system by using the following AWS services:
  + Fargate or Amazon EC2 for running the crawler application
  + AWS Batch for efficiently orchestrating large-scale crawling jobs
  + Amazon S3 for secure and durable data storage
+ Implementing best practices for ethical crawling, including:
  + Respecting robots.txt and website policies
  + Managing rate limiting to avoid overwhelming target sites
  + Ensuring data privacy and responsible use of collected information
+ Developing a Python-based crawler that is optimized for AWS infrastructure
+ Optimizing crawler performance while maintaining ethical standards

## Intended audience
<a name="intended-audience"></a>

This guide is intended for data engineers and cloud architects who want to efficiently collect large amounts of up-to-date ESG data from public websites. It is particularly relevant for projects that involve market analysis, sustainable financial assessment, or financial research.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The following are common reasons that companies use ESG data:
+ **Risk management** – ESG data helps you identify and mitigate potential risks related to environmental, social, and governance issues.
+ **Investor attraction** – Many investors now consider ESG factors when making investment decisions. They view strong ESG practices as indicators of long-term sustainability and profitability.
+ **Reputation management** – Good ESG performance can enhance a company's reputation among customers, employees, and the general public.
+ **Regulatory compliance** – As ESG-related regulations increase, adopting ESG practices helps companies stay ahead of compliance requirements.
+ **Innovation and efficiency** – Focusing on ESG factors can drive innovation in products, services, and operations. This leads to improved efficiency and cost savings.
+ **Competitive advantage** – Strong ESG performance can differentiate a company from its competitors and open up new market opportunities.
+ **Stakeholder engagement** – ESG practices help companies better engage with and meet the expectations of various stakeholders, including employees, customers, and local communities.
