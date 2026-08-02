---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this latest revision, the cost for running the default basic implementation of this solution in the US East (N. Virginia) Region is approximately **$547.33 per month**.

**Note**
Amazon Kendra and Amazon Connect are **not** part of the default solution implementation, but the solution does provide the capability to integrate with them. Because the solution does not create resources for Amazon Kendra or Amazon Connect automatically, they are not included in the example cost table. If you intend to integrate Amazon Kendra and Amazon Connect, review the [Amazon Kendra pricing](https://aws.amazon.com/kendra/pricing/) and [Amazon Connect pricing](https://aws.amazon.com/connect/pricing/) to adjust your cost estimate accordingly.

We recommend creating a [budget](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution. For additional information, see [Creating a cost budget](https://docs.aws.amazon.com/cost-management/latest/userguide/create-cost-budget.html) in the *AWS Cost Management User Guide*.

## Option 1: Default basic deployment
<a name="option-1-default-basic-deployment"></a>

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month.

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Amazon API Gateway | 1,000,000 REST API calls per month | $3.50 |
| Amazon Cognito | 1,000 active users per month without the advanced security feature | $0.00 |
| Amazon S3 | 100 GB data transfer \+ 1,000,000 requests (100 records x 100 KB from Amazon Kinesis) | $3.27 |
| AWS Lambda | 2,000,000 requests with 200 ms duration | $1.23 |
| Systems Manager Parameter Store | 2,000,000 requests with 10 standard parameters | $0.00 |
| Amazon Lex | 100,000 text requests per month | $75.00 |
| Amazon Data Firehose | 100,000 records per month with 100 KB per record | $0.28 |
| Amazon DynamoDB | 2 GB storage \+ 2 reads and 2 writes per second \+ 20 hours peak read/write per month | $16.14 |
| Amazon Polly | 10,000 requests \+ 50 characters per request | $4.00 |
| Amazon Translate | 100,000 requests \+ 50 characters per request (OPTIONAL for non-English) | $75.00 |
| Amazon Comprehend | 100,000 requests \+ 50 characters per request | $5.00 |
| Amazon OpenSearch Service | m6g.large.search instance running all hours in a month for 4 nodes | $368.64 |
|  **Total for a default basic deployment:**  |  |  **$547.33**  |

## Option 2: Amazon Bedrock embeddings only
<a name="option-2-amazon-bedrock-embeddings-only"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Amazon Bedrock for text embeddings (optional) | Daily average of 8,000 requests of 2,000 input tokens estimated using Amazon Titan Embeddings Text | $48.00 |
|  **Total with Amazon Bedrock embeddings only ($547.33 \+ $48.00):**  |  |  **$595.33**  |

## Option 3: Amazon Bedrock embeddings and LLMs
<a name="option-3-amazon-bedrock-embeddings-and-llms"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Amazon Bedrock for LLM question answering (optional) | Daily average of 8,000 requests each made of 2,000 input tokens and 200 output tokens estimated using [Anthropic Claude 3 Haiku](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1&/providers%3Fmodel=anthropic.claude-3-haiku-20240307-v1%3A0#/models) (lower cost LLM option) or [Anthropic Claude 3 Sonnet](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1&/providers%3Fmodel=anthropic.claude-3-sonnet-20240229-v1%3A0#/models) (higher cost LLM option) | $180.00 (Haiku) to $2,160.00 (Sonnet) |
|  **Total with Amazon Bedrock embeddings and LLMs ($595.33 \+ $180.00 to $2,160.00):**  |  |  **$775.33 to $2,755.33**  |

## Option 4a: Amazon Bedrock embeddings and LLM and Amazon Kendra
<a name="option-4a-amazon-bedrock-embeddings-and-llm-and-amazon-kendra"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Amazon Kendra index | 0-8,000 queries a day and up to 100,000 documents with Amazon Kendra Enterprise Edition with 0-50 data sources | $1,008.00 |
|  **Total with Amazon Bedrock embeddings and LLM and Amazon Kendra ($775.33 to $2,755.33 \+ $1,008.00 ):**  |  |  **$1,783.33 to $3,763.33**  |

## Option 4b: Amazon Bedrock embeddings and LLM and RAG using Amazon Bedrock knowledge base
<a name="option-4b-amazon-bedrock-embeddings-and-llm-and-rag-using-amazon-bedrock-knowledge-base"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Amazon Bedrock knowledge base (optional) | 8,000 questions a day with 5 GB of data stored in Amazon OpenSearch Service Serverless vector store and using Anthropic Claude 3 Haiku (lower cost LLM option) or Anthropic Claude 3 Sonnet (higher cost LLM option) | $733.00 (Haiku) to $2,713.00 (Sonnet) |
|  **Total with Amazon Bedrock embeddings and LLM and RAG using Amazon Bedrock knowledge base ($775.33 to $2,755.33 \+ $733.00 to $2,713.00 ):**  |  |  **$1,508.33 to $5,468.33**  |

## Option 5a: Amazon Bedrock Guardrails Integration (Optional)
<a name="option-5a-amazon-bedrock-guardrails-integration"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Content Filters | 8,000 requests/day (1 text unit (400 characters) for both query and FM response) | $14.40 |
| Denied Topics | 8,000 requests/day (1 text unit (400 characters) for both query and FM response) | $14.40 |
| Sensitive Information Filter (PII) | 8,000 requests/day (1 text unit (400 characters) for both query and FM response) | $9.60 |
| Contextual grounding check | 8,000 requests/day (1 text unit (600 characters) for both query and FM response) | $14.40 |
| Sensitive Information filter (Regex) | Free | - |
| Word Filters | Free | - |
|  **Total with Amazon Bedrock embeddings and LLM and RAG using Amazon Bedrock knowledge base ($2,084.77 to $5,468.33 \+ $52.80):**  |  |  **$2,137.57 to $5,491.13**  |

## Option 5b: Amazon Bedrock Pre-process Guardrails Integration (Optional)
<a name="option-5b-amazon-bedrock-guardrails-integration"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Content Filters | 8,000 requests/day (1 text unit (100 characters - questions only) for both query and FM response) | $3.60 |
| Denied Topics | 8,000 requests/day (1 text unit (100 characters - questions only) for both query and FM response) | $3.60 |
| Sensitive Information Filter (PII) | 8,000 requests/day (1 text unit (100 characters - questions only) for both query and FM response) | $2.40 |
| Contextual grounding check | N/A |  |
| Sensitive Information filter (Regex) | Free | - |
| Word Filters | Free | - |
|  **Total with Amazon Bedrock embeddings and LLM and RAG using Amazon Bedrock knowledge base ($2,084.77 to $5,468.33 \+ $9.60):**  |  |  **$2,094.37 to $5,477.93**  |

## Option 5c: Amazon Bedrock Post-process Guardrails Integration (Optional)
<a name="option-5c-amazon-bedrock-guardrails-integration"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Content Filters | 8,000 requests/day (1 text unit (300 characters - answers only) for both query and FM response) | $10.80 |
| Denied Topics | 8,000 requests/day (1 text unit (300 characters - answers only) for both query and FM response) | $10.80 |
| Sensitive Information Filter (PII) | 8,000 requests/day (1 text unit (300 characters - answers only) for both query and FM response) | $7.20 |
| Contextual grounding check | N/A |  |
| Sensitive Information filter (Regex) | Free | - |
| Word Filters | Free | - |
|  **Total with Amazon Bedrock embeddings and LLM and RAG using Amazon Bedrock knowledge base ($2,084.77 to $5,468.33 \+ $28.80):**  |  |  **$2,113.57 to $5,497.13**  |

## Option 6: Streaming Responses for QnABot
<a name="option-6-llm-streaming-responses"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| DynamoDB Table (optional) | 1 GB storage \+ 1 read and 1 write per second \+ 20 hours peak read/write per month | $11.41 |
| Lambda (optional) | 2,000,000 requests with 200 ms duration | $1.23 |
| WebSocket API (optional) | 100,000 messages per day with 25,000 connections for 10 minutes | $4.94 |
|  **Total with Streaming Responses for QnABot only ($547.33 \+ $17.58):**  |  |  **$564.91**  |

## Option 7: QnABot with OpenSearch Dedicated Master Nodes
<a name="option-7-opensearch-dedicated-master-nodes"></a>

| AWS service | Dimensions | Cost [$USD] |
| --- | --- | --- |
| Amazon OpenSearch Service | m6g.large.search instance running all hours in a month for 3 dedicated master nodes | $276.48 |
|  **Total with Streaming Responses for QnABot only ($547.33 \+ $276.48):**  |  |  **$823.81**  |
