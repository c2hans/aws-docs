---
source_url: https://docs.aws.amazon.com/solutions/querying-sustainability-documents-using-generative-ai-for-esg-reporting-on-aws/index.html
---

---
title: 'Guidance for Querying Sustainability Documents Using Generative AI for ESG Reporting on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/querying-sustainability-documents-using-generative-ai-for-esg-reporting-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Querying Sustainability Documents Using Generative AI for ESG Reporting on AWS

## Overview

This Guidance demonstrates how to use Retrieval-Augmented Generation (RAG) for your environmental, social, and governance (ESG) or sustainability knowledge base by combining Amazon Kendra and a large language model (LLM) from Amazon Bedrock—a fully managed service offering high-performing foundation models. Designed to provide rapid insights, the RAG process enables efficient navigation and summarization of diverse ESG information sources like corporate reports, regulatory filings, and industry standards. It allows you to analyze extensive text data quickly, extract key insights, and draw informed conclusions to support your organization’s ESG reporting needs.

## How it works

This architecture diagram demonstrates how to implement a Retrieval-Augmented Generation (RAG) process into your sustainability workflow by combining the capabilities of Amazon Kendra with a large language model (LLM) on Amazon Bedrock.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/querying-sustainability-documents-using-generative-ai-for-esg-reporting-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/querying-sustainability-documents-using-generative-ai-for-esg-reporting-on-aws/images/querying-sustainability-documents-using-generative-ai-for-esg-reporting-on-aws-1.png)

1. **Step 1**: A user asks questions and receives generated responses through various frontend integration options. For example, Amazon Lex V2 for conversational chatbots, AWS Amplify for custom frontend web applications, and Amazon API Gateway for processing user requests with backend services.
1. **Step 2**: AWS Lambda acts as a backend response orchestrator.
1. **Step 3**: Lambda stores all inputted questions and generated responses into Amazon DynamoDB as conversational memory to facilitate future user requests.
1. **Step 4**: Amazon Kendra performs semantic searches on your sustainability knowledge base. This consists of objects related to sustainability frameworks, such as the Corporate Sustainability Reporting Directive (CSRD) and the International Sustainability Standards Board (ISSB). It also consists of corporate reports, such as the Carbon Disclosure Project (CDP) questionnaires and the Form 10-K. The knowledge base can be stored on Amazon Simple Storage Service (Amazon S3) or third-party repositories like Dropbox and Confluence. It can also be accessed with public or internal websites over HTTPS using an Amazon Kendra Web Crawler.
1. **Step 5**: The Lambda function uses the Amazon Kendra Retrieve API, which is optimized for Retrieval-Augmented Generation (RAG), to identify and extract relevant passages. Document metadata filters are specified in the query API to help narrow the results, including only documents relevant to the user's question.
1. **Step 6**: The user's question and the relevant context are passed by the Lambda function to a large language model (LLM) hosted on Amazon Bedrock, a fully managed service that offers a choice of high-performing foundation models (FMs). LLMs such as Anthropic's Claude or Meta Llama can compare, analyze, and summarize large volumes of text from the sustainability knowledge base.
1. **Step 7**: The generated response from the LLM on Amazon Bedrock is returned to the Lambda function, which updates the conversational memory in DynamoDB and presents the response back to the user through your implementation of frontend integrations.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-querying-sustainability-documents-using-genai-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock and Lambda provide serverless compute capabilities, helps to eliminate virtual machine imaging, operating system upgrades, and patching. Amazon Kendra offers an optimized Retriever API with a semantic ranker, tailored for RAG with Amazon Bedrock. Together, these services automate critical aspects like LLM deployment, code implementation, scaling, and failover. By reducing human intervention and accelerating response times during operations, they help minimize the likelihood of errors and help provide consistent, efficient operations. This allows you to harness the power of generative artificial intelligence (AI) while maintaining a streamlined, low-maintenance architecture. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) integrates with Lambda, enabling authentication across services like Amazon Kendra and Amazon Bedrock without storing long-term credentials in your application code. IAM identity-based policies also enable granular control over access to Amazon Kendra resources, such as denying specific users from querying certain indexes. By governing access and permitted actions across all involved services, IAM enforces the principle of least privilege. This robust, policy-driven security model helps ensure this Guidance allows you to maintain tight access controls. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Bedrock, Lambda, Amazon Kendra, and DynamoDB are fully managed, serverless offerings that are deployed across multiple Availability Zones by default, providing inherent redundancy and fault tolerance without manual configuration. By avoiding long-running compute or databases requiring maintenance, potential failure points are reduced. You benefit from a highly available, reliable solution backed by the global infrastructure of AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock is a fully managed generative AI service offering a choice of foundation models accessible through a unified API. This single integration point allows quick experimentation across providers and seamless adoption of the latest model versions—all with minimal code changes. Using a multi-model API provides flexibility and scalability. You can efficiently utilize the right resources for each task, seamlessly adapting as requirements evolve. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda, Amazon Bedrock, and Amazon Kendra are fully managed services that automatically scale based on demand. These services also offer the capability to adopt a pay-as-you-go pricing model, ensuring you only pay for the resources actively processing requests. For example, Amazon Bedrock offers on-demand and batch modes, allowing for the use of FMs without time-based commitments. Additionally, these services reduce the operational burden on DevOps teams by minimizing infrastructure management and maintenance tasks, lowering associated costs. By minimizing idle resource usage, adopting efficient pricing models, reducing maintenance overhead, and optimizing data handling, Lambda, Amazon Bedrock, and Amazon Kendra can lead to lower operational costs while maintaining your required performance levels. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using the managed services provided in this Guidance, the responsibility of maintaining high utilization and optimization is shifted to AWS. AWS is on a path to matching 100% of the electricity powering our operations with renewable energy by 2025 and committed to achieving net-zero carbon emissions by 2040. Moreover, the RAG approach using Amazon Kendra and Amazon Bedrock is effective for augmenting LLM capabilities by retrieving and integrating relevant external information from predefined datasets. This strategy aims to minimize the resources required to train models on new data or build new models from the beginning. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **The executive’s guide to generative AI for sustainability**: This blog post serves as a starting point for any executive seeking to navigate the intersection of generative artificial intelligence (generative AI) and sustainability.

[Learn more](https://aws.amazon.com/blogs/machine-learning/the-executives-guide-to-generative-ai-for-sustainability/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
