---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-fully-managed-bedrock.html
---

# Knowledge bases for Amazon Bedrock
<a name="rag-fully-managed-bedrock"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API. [Knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) is an Amazon Bedrock capability that helps you implement the entire RAG workflow, from ingestion to retrieval and prompt augmentation. There is no need to build custom integrations to data sources or to manage data flows. Session context management is built in so that your generative AI application can readily support multi-turn conversations.

After you specify the location of your data, knowledge bases for Amazon Bedrock internally fetches the documents, chunks them into blocks of text, converts the text to embeddings, and then stores the embeddings in your choice of vector database. Amazon Bedrock manages and updates the embeddings, keeping the vector database in sync with the data. For more information about how knowledge bases work, see [How Amazon Bedrock knowledge bases work](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html).

If you add knowledge bases to an Amazon Bedrock agent, the agent identifies the appropriate knowledge base based on the user input. The agent retrieves the relevant information and adds the information to the input prompt. The updated prompt provides the model with more context information to generate a response. To improve transparency and minimize hallucinations, the information retrieved from the knowledge base is traceable to its source.

![The Amazon Bedrock agent retrieves information from the knowledge base and passes it to the LLM.](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/e3452591-694b-40f4-aa19-d39040a44631.png)

Amazon Bedrock supports the following two APIs for RAG:
+ [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) – You can use this API to query your knowledge base and generate responses from the information it retrieves. Internally, Amazon Bedrock converts the queries into embeddings, queries the knowledge base, augments the prompt with the search results as context information, and returns the LLM-generated response. Amazon Bedrock also manages the short-term memory of the conversation to provide more contextual results.
+ [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) – You can use this API to query your knowledge base with information retrieved directly from the knowledge base. You can use the information returned from this API to process the retrieved text, evaluate their relevance, or develop a separate workflow for response generation. Internally, Amazon Bedrock converts the queries into embeddings, searches the knowledge base, and returns the relevant results. You can build additional workflows on top of the search results. For example, you can use the [LangChain](https://python.langchain.com/docs/integrations/retrievers/bedrock/) `AmazonKnowledgeBasesRetriever` plugin to integrate RAG workflows into generative AI applications.

For sample architectural patterns and step-by-step instructions for using the APIs, see [Knowledge Bases now delivers fully managed RAG experience in Amazon Bedrock](https://aws.amazon.com/blogs/aws/knowledge-bases-now-delivers-fully-managed-rag-experience-in-amazon-bedrock/) (AWS blog post). For more information about how to use the `RetrieveAndGenerate` API to build a RAG workflow for an intelligent chat-based application, see [Build a contextual chatbot application using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/build-a-contextual-chatbot-application-using-knowledge-bases-for-amazon-bedrock/) (AWS blog post).

## Data sources for knowledge bases
<a name="rag-fully-managed-bedrock-data-sources"></a>

You can connect your proprietary data to a knowledge base. After you've configured a data source connector, you can sync or keep your data up to date with your knowledge base and make your data available for querying. Amazon Bedrock knowledge bases support connections to the following data sources:
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/bedrock/latest/userguide/s3-data-source-connector.html) – You can connect an Amazon S3 bucket to an Amazon Bedrock knowledge base by using either the console or the API. The knowledge base ingests and indexes the files in the bucket. This type of data source supports the following features:
  + **Document metadata fields** – You can include a separate file to specify the metadata for the files in the Amazon S3 bucket. You can then use these metadata fields to filter and improve the relevancy of responses.
  + **Inclusion or exclusion filters** – You can include or exclude certain content when crawling.
  + **Incremental syncing** – The content changes are tracked, and only content that has changed since the last sync is crawled.
+ [Confluence](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html) – You can connect an Atlassian Confluence instance to an Amazon Bedrock knowledge base by using the console or the API. This type of data source supports the following features:
  + **Auto detection of main document fields** – The metadata fields are automatically detected and crawled. You can use these fields for filtering.
  + **Inclusion or exclusion content filters** – You can include or exclude certain content by using a prefix or a regular expression pattern on the space, page title, blog title, comment, attachment name, or extension.
  + **Incremental syncing** - The content changes are tracked, and only content that has changed since the last sync is crawled.
  + **OAuth 2.0 authentication, authentication with Confluence API token** – The authentication credentials are stored in AWS Secrets Manager.
+ [Microsoft SharePoint](https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html) – You can connect a SharePoint instance to a knowledge base by using either the console or the API. This type of data source supports the following features:
  + **Auto detection of main document fields** – The metadata fields are automatically detected and crawled. You can use these fields for filtering.
  + **Inclusion or exclusion content filters** – You can include or exclude certain content by using a prefix or a regular expression pattern on the main page title, event name, and file name (including its extension).
  + **Incremental syncing** - The content changes are tracked, and only content that has changed since the last sync is crawled.
  + **OAuth 2.0 authentication** – The authentication credentials are stored in AWS Secrets Manager.
+ [Salesforce](https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html) – You can connect a Salesforce instance to a knowledge base by using either the console or the API. This type of data source supports the following features:
  + **Auto detection of main document fields** – The metadata fields are automatically detected and crawled. You can use these fields for filtering.
  + **Inclusion or exclusion content filters** – You can include or exclude certain content by using a prefix or a regular expression pattern. For a list of content types that you can apply filters to, see *Inclusion/exclusion filters* in the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html#configuration-salesforce-connector).
  + **Incremental syncing** - The content changes are tracked, and only content that has changed since the last sync is crawled.
  + **OAuth 2.0 authentication** – The authentication credentials are stored in AWS Secrets Manager.
+ [Web Crawler](https://docs.aws.amazon.com/bedrock/latest/userguide/webcrawl-data-source-connector.html) – An Amazon Bedrock Web Crawler connects to and crawls the URLs that you provide. The following features are supported:
  + Select multiple URLs to crawl
  + Respect standard robots.txt directives, such as `Allow` and `Disallow`
  + Exclude URLs that match a pattern
  + Limit the rate of crawling
  + In Amazon CloudWatch, view the status of each URL crawled

For more information about the data sources that you can connect to your Amazon Bedrock knowledge base, see [Create a data source connector for your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/data-source-connectors.html).

## Vector databases for knowledge bases
<a name="rag-fully-managed-bedrock-vector-stores"></a>

When you set up a connection between the knowledge base and the data source, you must configure a vector database, also known as a *vector store*. A vector database is where Amazon Bedrock stores, updates, and manages the embeddings that represent your data. Each data source supports different types of vector database. To determine which vector database are available for your data source, see the [data source types](https://docs.aws.amazon.com/bedrock/latest/userguide/data-source-connectors.html).

If you prefer for Amazon Bedrock to automatically create a vector database in Amazon OpenSearch Serverless for you, you can choose this option when you create the knowledge base. However, you can also choose to set up your own vector database. If you set up your own vector database, see [Prerequisites for your own vector store for a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html). Each type of vector database has its own prerequisites.

Depending on your data source type, Amazon Bedrock knowledge bases support the following vector databases:
+ [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html)
+ [Pinecone](https://docs.pinecone.io/docs/amazon-bedrock) (Pinecone documentation)
+ [Redis Enterprise Cloud](https://docs.redis.com/latest/rc/cloud-integrations/aws-marketplace/aws-bedrock/) (Redis documentation)
+ [MongoDB Atlas](https://dochub.mongodb.org/core/amazon-bedrock) (MongoDB documentation)
