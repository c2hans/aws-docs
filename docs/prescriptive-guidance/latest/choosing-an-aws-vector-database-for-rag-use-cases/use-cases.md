---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/use-cases.html
---

# Vector database use cases
<a name="use-cases"></a>

The following examples highlight how different vector database options can be used effectively to enhance knowledge management, improve operational efficiency, and deliver better business outcomes. These use cases illustrate practical applications of the vector database solutions discussed earlier in this guide and provide insights into their real-world performance and benefits.

## Knowledge management with Amazon Kendra
<a name="knowledge-management-with-kendra"></a>

**Customer problem** – One of the largest general contractors in Japan was facing a decline in experienced personnel. The company needed a way to transfer the knowledge and skills of the experience personnel to the younger generation efficiently. They required a solution to capture and disseminate complex construction engineering knowledge and past experiences.

**AWS solution** – To address this problem, the customer turned to Amazon Kendra, an AI solution that could quickly and accurately handle their internal knowledge base and allow natural language queries. With Amazon Kendra, employees can now find the information they need much faster, improving productivity and facilitating knowledge transfer from experienced personnel to younger staff.

**Impact** – By implementing a generative AI chatbot powered by Amazon Kendra, the company created a unified knowledge platform. The chatbot allows employees to quickly access technical knowledge and past experiences on construction engineering. This solution has significantly improved the efficiency of knowledge transfer and decision-making processes within the organization, helping to ensure that valuable expertise is preserved and easily accessible to all employees. The cost of this solution may vary depending on your usage and configuration. For a detailed cost estimate, see the [AWS Pricing Calculator](https://calculator.aws/#/). For vector database cost estimation, see the [Cost comparison and considerations](cost.md)section of this guide or see [Amazon Kendra pricing](https://aws.amazon.com/kendra/pricing/).

For information about other customer use cases, see [Amazon Kendra customers](https://aws.amazon.com/kendra/customers/?p=pm&amp;c=ml&amp;pd=kd&amp;z=5).

## Real-time analytics with OpenSearch Serverless
<a name="real-time-analytics-with-opensearch"></a>

**Customer problem** – A leading financial services provider faced the challenge of managing an enormous data ecosystem. It processed 300 million authorizations and 90 billion transactions annually, accumulating to approximately 1.1 petabytes (PB) of data. The existing system, serving 300,000 users who required access to over 6,000 reports, needed modernization to provide global consistency and enable real-time decision-making.

**AWS solution** – The solution architecture used foundation models available through Amazon Bedrock (including Anthropic, Sonnet 3, Sonnet 3.5, and Haiku) for natural language processing. The customer chose OpenSearch Serverless as the vector database for its superior scalability and ability to handle the massive data volume efficiently. This architecture enabled seamless processing of complex queries and dynamic report generation.

**Impact **– The implementation achieved a 50 percent increase in productivity by eliminating the need for manual generation of over 100 business intelligence dashboards. Users can now generate reports through natural language queries with response times of between 20-40 seconds. The cost of this solution may vary depending on your usage and configuration. For a detailed cost estimate, see the [AWS Pricing Calculator](https://calculator.aws/#/). For vector database cost estimation, see the [Cost comparison and considerations](cost.md)section of this guide or see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/). For information about other customer use cases, see [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
