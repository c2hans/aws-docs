---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/vectors.html
---

# Overview of vectors
<a name="vectors"></a>

*Vectors *are numerical representations that help machines understand and process data. In generative AI, they serve two key purposes:
+ Representing latent spaces that capture data structure in compressed form
+ Creating embeddings for data, such as words, sentences, and images

Embedding models like [Word2Vec](https://aws.amazon.com/what-is/embeddings-in-machine-learning/), [GloVe](https://github.com/stanfordnlp/GloVe), and [Amazon Titan Text Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) convert data into vectors through a process called *embedding*. These embedding models can do the following:
+ Learn from context to represent words as vectors
+ Place similar words closer together in vector space
+ Enable machines to process data in a continuous space

The following diagram provides a high-level overview of the embedding process:

1. An [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket contains files that are the data sources from which the system will read and process information. The Amazon S3 bucket is specified during the [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) knowledge base configuration, which also includes [syncing data with the knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html).

1. The embedding model converts the raw data from the object files in the Amazon S3 bucket into vector embeddings. For example, `Object1` is converted into a vector `[0.6, 0.7, ...]` that represents its content in a multi-dimensional space.

![Embedding model converts objects in Amazon S3 bucket to vector embeddings.](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/images/guide-img/34bd35bb-382d-4951-8f14-111521edb094/images/36c98d6b-eab5-49b1-abee-f1dd2bb99fb6.png)

Word embeddings are crucial for natural language processing (NLP) because they do the following:
+ Capture semantic relationships between words
+ Enable generation of contextually relevant text
+ Power large language models (LLMs) to produce human-like responses
