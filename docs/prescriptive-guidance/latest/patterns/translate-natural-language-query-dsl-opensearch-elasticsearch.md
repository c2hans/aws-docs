---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/translate-natural-language-query-dsl-opensearch-elasticsearch.html
---

# Translate natural language into query DSL for OpenSearch and Elasticsearch queries
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch"></a>

*Tabby Ward, Nicholas Switzer, and Breanne Warner, Amazon Web Services*

## Summary
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-summary"></a>

This pattern demonstrates how to use large language models (LLMs) to convert natural language queries into query domain-specific language (query DSL), which makes it easier for users to interact with search services such as OpenSearch and Elasticsearch without extensive knowledge of the query language. This resource is particularly valuable for developers and data scientists who want to enhance search-based applications with natural language querying capabilities, ultimately improving user experience and search functionality.

The pattern illustrates techniques for prompt engineering, iterative refinement, and incorporation of specialized knowledge, all of which are crucial in synthetic data generation. Although this approach focuses primarily on query conversion, it implicitly demonstrates the potential for data augmentation and scalable synthetic data production. This foundation could be extended to more comprehensive synthetic data generation tasks, to highlight the power of LLMs in bridging unstructured natural language inputs with structured, application-specific outputs.

This solution doesn't involve migration or deployment tools in the traditional sense. Instead, it focuses on demonstrating a proof of concept (PoC) for converting natural language queries to query DSL by using LLMs.
+ The pattern uses a Jupyter notebook as a step-by-step guide for setting up the environment and implementing the text-to-query conversion.
+ It uses Amazon Bedrock to access LLMs, which are crucial for interpreting natural language and generating appropriate queries.
+ The solution is designed to work with Amazon OpenSearch Service. You can follow a similar process for Elasticsearch, and the generated queries could potentially be adapted for similar search engines.

[Query DSL](https://opensearch.org/docs/latest/query-dsl/) is a flexible, JSON-based search language that's used to construct complex queries in both Elasticsearch and OpenSearch. It enables you to specify queries in the query parameter of search operations, and supports various query types. A DSL query includes leaf queries and compound queries. Leaf queries search for specific values in certain fields and encompass full-text, term-level, geographic, joining, span, and specialized queries. Compound queries act as wrappers for multiple leaf or compound clauses, and combine their results or modify their behavior. Query DSL supports the creation of sophisticated searches, ranging from simple, match-all queries to complex, multi-clause queries that produce highly specific results. Query DSL is particularly valuable for projects that require advanced search capabilities, flexible query construction, and JSON-based query structures.

This pattern uses techniques such as few-shot prompting, system prompts, structured output, prompt chaining, context provision, and task-specific prompts for text-to-query DSL conversion. For definitions and examples of these techniques, see the [Additional information](#translate-natural-language-query-dsl-opensearch-elasticsearch-additional) section.

## Prerequisites and limitations
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-prereqs"></a>

**Prerequisites**

To effectively use the Jupyter notebook for converting natural language queries into query DSL queries, you need:
+ **Familiarity with Jupyter notebooks**. Basic understanding of how to navigate and run code in a Jupyter notebook environment.
+ **Python environment**. A working Python environment, preferably Python 3.x, with the necessary libraries installed.
+ **Elasticsearch or OpenSearch knowledge**. Basic knowledge of Elasticsearch or OpenSearch, including its architecture and how to perform queries.
+ **AWS account**. An active AWS account to access Amazon Bedrock and other related services.
+ **Libraries and dependencies**. Installation of specific libraries mentioned in the notebook, such as `boto3` for AWS interaction, and any other dependencies required for LLM integration.
+ **Model access within Amazon Bedrock**. This pattern uses three Claude LLMs from Anthropic. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/) and choose **Model access**. On the next screen, choose **Enable specific models** and select these three models:
  + Claude 3 Sonnet
  + Claude 3.5 Sonnet
  + Claude 3 Haiku
+ **Proper IAM policies and IAM role**. To run the notebook in an AWS account, your AWS Identity and Access Management (IAM) role requires the `SagemakerFullAccess` policy as well as the policy that’s provided in the [Additional information](#translate-natural-language-query-dsl-opensearch-elasticsearch-additional) section, which you can name `APGtext2querydslpolicy`. This policy includes subscribing to the three Claude models listed.

Having these prerequisites in place ensures a smooth experience when you work with the notebook and implement the text-to-query functionality.

**Limitations**
+ **Proof of concept status**. This project is primarily intended as a proof of concept (PoC). It demonstrates the potential of using LLMs to convert natural language queries into query DSL, but it might not be fully optimized or production-ready.
+ **Model limitations**:

  **Context window constraints***.* When using the LLMs that are available on Amazon Bedrock, be aware of the context window limitations:

  Claude models (as of September 2024):
  + Claude 3 Opus: 200,000 tokens
  + Claude 3 Sonnet: 200,000 tokens
  + Claude 3 Haiku: 200,000 tokens

  Other models on Amazon Bedrock might have different context window sizes. Always check the latest documentation for the latest information.

  **Model availability***. *The availability of specific models on Amazon Bedrock can vary. Make sure that you have access to the required models before you implement this solution.
+ **Additional limitations**
  + **Query complexity**. The effectiveness of the natural language to query DSL conversion might vary depending on the complexity of the input query.
  + **Version compatibility**. The generated query DSL might need adjustments based on the specific version of Elasticsearch or OpenSearch that you use.
  + **Performance**. This pattern provides a PoC implementation, so query generation speed and accuracy might not be optimal for large-scale production use.
  + **Cost**. Using LLMs in Amazon Bedrock incurs costs. Be aware of the pricing structure for your chosen model. For more information, see [Amazon Bedrock pricing](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html).
  + **Maintenance**. Regular updates to the prompts and model selection might be necessary to keep up with advancements in LLM technology and changes in query DSL syntax.

**Product versions**

This solution was tested in Amazon OpenSearch Service. If you want to use Elasticsearch, you might have to make some changes to replicate the exact functionality of this pattern.
+ **OpenSearch version compatibility**.** **OpenSearch maintains backward compatibility within major versions. For example:
  + OpenSearch 1.x clients are generally compatible with OpenSearch 1.x clusters.
  + OpenSearch 2.x clients are generally compatible with OpenSearch 2.x clusters.

  However, it's always best to use the same minor version for both client and cluster when possible.
+ **OpenSearch API compatibility**.** **OpenSearch maintains API compatibility with Elasticsearch OSS 7.10.2 for most operations. However, some differences exist, especially in newer versions.
+ **OpenSearch upgrade considerations**:
  + Direct downgrades are not supported. Use snapshots for rollback if needed.
  + When you upgrade, check the [compatibility matrix and release notes](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-operations.html) for any breaking changes.

**Elasticsearch considerations**
+ **Elasticsearch version**. The major version of Elasticsearch you're using is crucial, because query syntax and features can change between major versions. Currently, the latest stable version is Elasticsearch 8.x. Make sure that your queries are compatible with your specific Elasticsearch version.
+ **Elasticsearch query DSL library version**. If you're using the Elasticsearch query DSL Python library, make sure that its version matches your Elasticsearch version. For example:
  + For Elasticsearch 8.x, use an `elasticsearch-dsl` version that's greater or equal to 8.0.0 but smaller than 9.0.0.
  + For Elasticsearch 7.x, use an `elasticsearch-dsl` version that's greater or equal to 7.0.0  but smaller than 8.0.0.
+ **Client library version**. Whether you're using the official Elasticsearch client or a language-specific client, make sure that it's compatible with your Elasticsearch version.
+ **Query DSL version**. Query DSL evolves with Elasticsearch versions. Some query types or parameters might be deprecated or introduced in different versions.
+ **Mapping version**. The way you define mappings for your indexes and change between versions. Always check the mapping documentation for your specific Elasticsearch version.
+ **Analysis tools versions**. If you're using analyzers, tokenizers, or other text analysis tools, their behavior or availability might change between versions.

## Architecture
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-architecture"></a>

**Target architecture**

The following diagram illustrates the architecture for this pattern.

![Architecture for translating natural language to query DSL in Amazon Bedrock.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/75296405-2893-4328-9551-9bcc6ec7fd3e/images/ffb1b893-d23c-4e1c-b679-8063b4f85a8a.png)

where:

1. User input and system prompt with few-shot prompting examples. The process begins with a user who provides a natural language query or a request for schema generation.

1. Amazon Bedrock. The input is sent to Amazon Bedrock, which serves as the interface to access the Claude LLM.

1. Claude 3 Sonnet LLM. Amazon Bedrock uses Claude 3 Sonnet from the Claude 3 family of LLMs to process the input. It interprets and generates the appropriate Elasticsearch or OpenSearch query DSL. For schema requests, it generates synthetic Elasticsearch or OpenSearch mappings.

1. Query DSL generation. For natural language queries, the application takes the LLM's output and formats it into a valid Elasticsearch or OpenSearch Service query DSL.

1. Synthetic data generation. The application also takes schemas to create synthetic Elasticsearch or OpenSearch data to be loaded into an OpenSearch Serverless collection for testing.

1. OpenSearch or Elasticsearch. The generated Query DSL is queried against an OpenSearch Serverless collection on all indexes. JSON output contains the relevant data and number of *hits* from the data that resides in the OpenSearch Serverless collection.

**Automation and scale**

The code that's provided with this pattern is built strictly for PoC purposes. The following list provides a few suggestions for automating and scaling the solution further and moving the code to production. These enhancements are outside the scope of this pattern.
+ Containerization:
  + Dockerize the application to ensure consistency across different environments.
  + Use container orchestration platforms such as Amazon Elastic Container Service (Amazon ECS) or Kubernetes for scalable deployments.
+ Serverless architecture:
  + Convert the core functionality into AWS Lambda functions.
  + Use Amazon API Gateway to create RESTful endpoints for the natural language query input.
+ Asynchronous processing:
  + Implement Amazon Simple Queue Service (Amazon SQS) to queue incoming queries.
  + Use AWS Step Functions to orchestrate the workflow of processing queries and generating query DSL.
+ Caching:
  + Implement a mechanism to cache the prompts.
+ Monitoring and logging:
  + Use Amazon CloudWatch for monitoring and alerting.
  + Implement centralized logging with Amazon CloudWatch Logs or Amazon OpenSearch Service for log analytics.
+ Security enhancements:
  + Implement IAM roles for fine-grained access control.
  + Use AWS Secrets Manager to securely store and manage API keys and credentials.
+ Multi-Region deployment:
  + Consider deploying the solution across multiple AWS Regions for improved latency and disaster recovery.
  + Use Amazon Route 53 for intelligent request routing.

By implementing these suggestions, you can transform this PoC into a robust, scalable, and production-ready solution. We recommend that you thoroughly test each component and the entire system before full deployment.

## Tools
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-tools"></a>

**Tools**
+ [Amazon SageMaker AI notebooks](https://aws.amazon.com/sagemaker/notebooks/) are fully managed Jupyter notebooks for machine learning development. This pattern uses notebooks as an interactive environment for data exploration, model development, and experimentation in Amazon SageMaker AI. Notebooks provide seamless integration with other SageMaker AI features and AWS services.
+ [Python](https://www.python.org/) is a general-purpose computer programming language. This pattern uses Python as the core language to implement the solution.
+ [Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API. Amazon Bedrock provides access to LLMs for natural language processing. This pattern uses Anthropic Claude 3 models.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services, including Amazon Bedrock.
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is a managed service that helps you deploy, operate, and scale OpenSearch Service clusters in the AWS Cloud. This pattern uses OpenSearch Service as the target system for generating query DSL.

**Code repository**

The code for this pattern is available in the GitHub [Prompt Engineering Text-to-QueryDSL Using Claude 3 Models](https://github.com/aws-samples/text-to-queryDSL/blob/main/text2ES_prompting_guide.ipynb) repository. The example uses a health social media app that creates posts for users and user profiles associated with the health application.

## Best practices
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-best-practices"></a>

When working with this solution, consider the following:
+ The need for proper AWS credentials and permissions to access Amazon Bedrock
+ Potential costs associated with using AWS services and LLMs
+ The importance of understanding query DSL to validate and potentially modify the generated queries

## Epics
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-epics"></a>

### Set up the environment and prepare data
<a name="set-up-the-environment-and-prepare-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the development environment. | For detailed instructions and code for this and the other steps in this pattern, see the comprehensive walkthrough in the [GitHub repository](https://github.com/aws-samples/text-to-queryDSL/blob/main/text2ES_prompting_guide.ipynb).[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/translate-natural-language-query-dsl-opensearch-elasticsearch.html) | Python, pip, AWS SDK |
| Set up AWS access. | Set up the Amazon Bedrock client and SageMaker AI session. Retrieve the Amazon Resource Name (ARN) for the SageMaker AI execution role for later use in creating the OpenSearch Serverless collection. | IAM, AWS CLI, Amazon Bedrock, Amazon SageMaker |
| Load health app schemas. | Read and parse JSON schemas for health posts and user profiles from predefined files. Convert schemas to strings for later use in prompts. | DevOps engineer, General AWS, Python, JSON |

### Generate synthetic data
<a name="generate-synthetic-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an LLM-based data generator. | Implement the **generate\_data()** function to call the Amazon Bedrock Converse API with Claude 3 models. Set up model IDs for Sonnet, Sonnet 3.5, and Haiku:<pre>model_id_sonnet3_5 = "anthropic.claude-3-5-sonnet-20240620-v1:0" <br />model_id_sonnet = "anthropic.claude-3-sonnet-20240229-v1:0" <br />model_id_haiku = "anthropic.claude-3-haiku-20240307-v1:0"</pre> | Python, Amazon Bedrock API, LLM prompting |
| Create synthetic health posts. | Use the **generate\_data()** function with a specific message prompt to create synthetic health post entries based on the provided schema. The function call looks like this: <pre>health_post_data = generate_data(bedrock_rt, model_id_sonnet, system_prompt, message_healthpost, inference_config)</pre> | Python, JSON |
| Create synthetic user profiles. | Use the **generate\_data()** function with a specific message prompt to create synthetic user profile entries based on the provided schema. This is similar to health posts generation, but uses a different prompt. | Python, JSON |

### Set up OpenSearch and ingest data
<a name="set-up-opensearch-and-ingest-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up an OpenSearch Serverless collection. | Use Boto3 to create an OpenSearch Serverless collection with appropriate encryption, network, and access policies. The collection creation looks like this: <pre>collection = aoss_client.create_collection(name=es_name, type='SEARCH')</pre><br /> For more information about OpenSearch Serverless, see the [AWS documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html). | OpenSearch Serverless, IAM |
| Define OpenSearch indexes. | Create indiexes for health posts and user profiles by using the OpenSearch client, based on the predefined schema mappings. The index creation looks like this:<pre>response_health = oss_client.indices.create(healthpost_index, body=healthpost_body)</pre> | OpenSearch, JSON |
| Load data into OpenSearch. | Run the **ingest\_data()** function to bulk insert the synthetic health posts and user profiles into their respective OpenSearch indexes. The function uses the bulk helper from `opensearch-py`:<pre>success, failed = bulk(oss_client, actions)</pre> | Python, OpenSearch API, bulk data operations |

### Generate and run queries
<a name="generate-and-run-queries"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Design few-shot prompt examples. | Generate example queries and corresponding natural language questions by using Claude 3 models to serve as few-shot examples for query generation. The system prompt includes these examples:<pre>system_prompt_query_generation = [{"text": f"""You are an expert query dsl generator. ... Examples: {example_prompt} ..."""}]</pre> | LLM prompting, query DSL |
| Create a text-to-query DSL converter. | Implement the system prompt, which includes schemas, data, and few-shot examples, for query generation. Use the system prompt to convert natural language queries to query DSL. The function call looks like this:<pre>query_response = generate_data(bedrock_rt, model_id, system_prompt_query_generation, query, inference_config)</pre> | Python, Amazon Bedrock API, LLM prompting |
| Test query DSL on OpenSearch. | Run the **query\_oss()** function to run the generated query DSL against the OpenSearch Serverless collection and return results. The function uses the OpenSearch client's search method:<pre>response = oss_client.search(index="_all", body=temp)</pre> | Python, OpenSearch API, query DSL |

### Test and evaluate
<a name="test-and-evaluate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a test query set. | Use Claude 3 to generate a diverse set of test questions based on the synthetic data and schemas:<pre>test_queries = generate_data(bedrock_rt, model_id_sonnet, query_system_prompt, query_prompt, inference_config)</pre> | LLM prompting |
| Assess the accuracy of the query DSL conversion. | Test the generated query DSL by running queries against OpenSearch and analyzing the returned results for relevance and accuracy. This involves running the query and inspecting the hits:<pre>output = query_oss(response1) print("Response after running query against Opensearch") print(output)</pre> | Python, data analysis, query DSL |
| Benchmark Claude 3 models.  | Compare the performance of different Claude 3 models (Haiku, Sonnet, Sonnet 3.5) for query generation in terms of accuracy and latency. To compare, change the `model_id` when you call **generate\_data()** and measure execution time. | Python, performance benchmarking |

### Clean up and document
<a name="clean-up-and-document"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Develop a cleanup process. | Delete all indexes from the OpenSearch Serverless collection after use. | Python, AWS SDK, OpenSearch API |

## Related resources
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-resources"></a>
+ [Query DSL](https://opensearch.org/docs/latest/query-dsl/) (OpenSearch documentation)
+ [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
+ [OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html)
+ [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
+ [Amazon SageMaker AI documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
+ [AWS SDK for Python (Boto3) documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Additional information
<a name="translate-natural-language-query-dsl-opensearch-elasticsearch-additional"></a>

**IAM policy**

Here’s the `APGtext2querydslpolicy` policy for the IAM role used in this pattern:

```
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*"
    },
    { "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::sagemaker-*",
        "arn:aws:s3:::sagemaker-*/*"
      ]
    },
    { "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/*"
    },
    { "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": "*"
    },
    { "Effect": "Allow",
      "Action": [
        "aoss:*"
      ],
      "Resource": "*"
    },
    { "Effect": "Allow",
      "Action": [
        "iam:PassRole",
        "sagemaker:*"
      ],
      "Resource": [
        "arn:aws:iam::*:role/*", "*"
      ],
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "sagemaker.amazonaws.com"
          }
      }
    },
    { "Effect": "Allow",
      "Action": [
        "codecommit:GetBranch",
        "codecommit:GetCommit",
        "codecommit:GetRepository",
        "codecommit:ListBranches",
        "codecommit:ListRepositories"
      ],
      "Resource": "*"
    },
    { "Effect": "Allow",
      "Action": [
        "aws-marketplace:Subscribe"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "aws-marketplace:ProductId": [
            "prod-6dw3qvchef7zy",
            "prod-m5ilt4siql27k",
            "prod-ozonys2hmmpeu"
          ]
        }
      }
    },
    { "Effect": "Allow",
      "Action": [
        "aws-marketplace:Unsubscribe",
        "aws-marketplace:ViewSubscriptions"
      ],
      "Resource": "*"
    },
    { "Effect": "Allow",
      "Action": "iam:*",
      "Resource": "*"
    }
  ]
}
```

**Prompt techniques with Anthropic Claude 3 models**

This pattern demonstrates the following prompting techniques for text-to-query DSL conversion using Claude 3 models.
+ **Few-shot prompting:** Few-shot prompting is a powerful technique for improving the performance of Claude 3 models on Amazon Bedrock. This approach involves providing the model with a small number of examples that demonstrate the desired input/output behavior before asking it to perform a similar task. When you use Claude 3 models on Amazon Bedrock, few-shot prompting can be particularly effective for tasks that require specific formatting, reasoning patterns, or domain knowledge. To implement this technique, you typically structure your prompt with two main components: the example section and the actual query. The example section contains one or more input/output pairs that illustrate the task, and the query section presents the new input for which you want a response. This method helps Claude 3 understand the context and expected output format, and often results in a more accurate and consistent response.

  Example:

  ```
  "query": {
    "bool": {
      "must": [
        {"match": {"post_type": "recipe"}},
        {"range": {"likes_count": {"gte": 100}}},
        {"exists": {"field": "media_urls"}}
      ]
    }
  }
  Question: Find all recipe posts that have at least 100 likes and include media URLs.
  ```
+ **System prompts: **In addition to few-shot prompting, Claude 3 models on Amazon Bedrock also support the use of system prompts. System prompts are a way to provide overall context, instructions, or guidelines to the model before presenting it with specific user inputs. They are particularly useful for setting the tone, defining the model's role, or establishing constraints for the entire conversation. To use a system prompt with Claude 3 on Amazon Bedrock, you include it in the `system` parameter of your API request. This is separate from the user messages and applies to the entire interaction. Detailed system prompts are used to set context and provide guidelines for the model.

  Example:

  ```
  You are an expert query dsl generator. Your task is to take an input question and generate a query dsl to answer the question. Use the schemas and data below to generate the query.

  Schemas: [schema details]
  Data: [sample data]
  Guidelines:
  - Ensure the generated query adheres to DSL query syntax
  - Do not create new mappings or other items that aren't included in the provided schemas.
  ```
+ **Structured output**: You can instruct the model to provide output in specific formats, such as JSON or within XML tags.

  Example:

  ```
  Put the query in json tags
  ```
+ **Prompt chaining**: The notebook uses the output of one LLM call as input for another, such as using generated synthetic data to create example questions.
+ **Context provision**: Relevant context, including schemas and sample data, is provided in the prompts.

  Example:

  ```
  Schemas: [schema details]
  Data: [sample data]
  ```
+ **Task-specific prompts**: Different prompts are crafted for specific tasks, such as generating synthetic data, creating example questions, and converting natural language queries to query DSL.

  Example for generating test questions:

  ```
  Your task is to generate 5 example questions users can ask the health app based on provided schemas and data. Only include the questions generated in the response.
  ```
