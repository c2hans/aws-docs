---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/lifecycle.html
---

# Data lifecycle in generative AI
<a name="lifecycle"></a>

Implementing generative AI in an enterprise involves a data lifecycle that parallels the traditional AI/ML lifecycle. However, there are unique considerations at each stage. The key phases include data preparation, integration into model workflows (such as retrieval or fine-tuning), feedback collection, and ongoing updates. This section explores these interconnected data lifecycle stages and details the essential processes, challenges, and best practices that organizations must consider when developing and deploying generative AI solutions.

**This section contains the following topics:**
+ [Data preparation and cleaning for pre-training](#lifecycle-preparation)
+ [Retrieval Augmented Generation](#lifecycle-rag)
+ [Fine-tuning and specialized training](#lifecycle-fine-tuning)
+ [Evaluation dataset](#lifecycle-evaluation)
+ [User-generated data and feedback loops](#lifecycle-feedback-loops)

## Data preparation and cleaning for pre-training
<a name="lifecycle-preparation"></a>

*Garbage in, garbage out* is the concept that poor quality inputs result in similarly low-quality outputs. Just as in any AI project, data quality is a make-or-break factor. Generative AI often starts with massive datasets, but volume alone is not enough. Careful cleaning, filtering, and preprocessing are critical.

In this stage, data teams aggregate raw data, such as large bodies of text or image collections. Then, they remove noise, errors, and biases. For instance, preparing text for an LLM might involve eliminating duplicates, purging sensitive personal information, and filtering out toxic or irrelevant content. The goal is to create a high-quality dataset that truly represents the knowledge or style the model should capture. Data might also be normalized or formatted into a structure suitable for model ingestion. For example, you might tokenize text, remove HTML tags, or normalize image resolution.

In generative AI, this preparation can be especially intensive because of scale. Models such as Anthropic Claude are trained on hundreds of billions of [tokens](https://en.wikipedia.org/wiki/Lexical_analysis#Token) (Wikipedia) that come from a wide range of publicly available and licensed data sources. Even small percentages of bad data can have outsized effects on outputs, including offensive content or factual errors. For example, various LLM providers reported excluding a Reddit community's content from their training dataset because the posts consisted mainly of long sequences of the letter *M* in order to mimic the noise of a microwave. These posts were disrupting model training and performance.

At this stage, some enterprises adopt data augmentation to boost coverage of certain scenarios. *Data augmentation* is the process of synthesizing additional training data. For more information, see [Data synthesizing](differences.md#differences-synthesizing) in this guide.

When training the model on the prepared and pre-processed data, you can use mitigation techniques to notably address bias. Techniques include embedding ethical principles within the model's architecture, known as *constitutional AI*. Another technique is *adversarial debiasing*, which challenges the model during training to enforce fairer outcomes across different groups. Finally, after training, you can make *post-processing adjustments* to refine the model through fine-tuning. This can help correct any remaining biases and improve overall fairness.

## Retrieval Augmented Generation
<a name="lifecycle-rag"></a>

Static ML models make predictions purely from a fixed training set. However, many enterprise generative AI solutions use Retrieval Augmented Generation (RAG) to keep a model's knowledge current and relevant. RAG involves connecting an LLM to an external knowledge repository that might contain enterprise documents, databases, or other data sources.

In practice, RAG necessitates the implementation of an additional data pipeline. This introduces a certain degree of complexity and involves the following sequential steps:

1. **Ingestion and filtering** – Collect high-quality, relevant data from diverse sources. Implement filtering mechanisms to exclude redundant or irrelevant information, and make sure that the dataset is relevant to the application's domain. Note that regular updates and maintenance of the data repository are essential to preserve the accuracy and relevance of the information.

1. **Parsing and extraction** – After data ingestion, the data should be parsed to extract meaningful content. Use parsers that can handle various data formats, such as HTML, JSON, or plain text. The parsers convert the raw data into structured forms. This process facilitates easier data manipulation and analysis in subsequent stages.

1. **Chunking strategies** – Divide the data into manageable pieces, or *chunks*. This step is vital for efficient retrieval and processing. Chunking strategies include but are not limited to the following:

o   **Standard, token-based chunking** – Split text into fixed-size segments based on a specific number of tokens. This is the most basic chunking strategy, but it helps maintain uniform chunk lengths.

o   **Hierarchical chunking** – Organize content into a hierarchy (such as chapters, sections, or paragraphs) to preserve contextual relationships. This strategy enhances the model's understanding of the data structure.

o   **Semantic chunking** – Segment text based on semantic coherence. Make sure that each chunk represents a complete idea or topic. This strategy can improve the relevance of retrieved information.

1. **Embedding model selection** – Vector databases store *embeddings*, which are numerical representations of a chunk of text that preserve its meaning and context. An embedding is a format that an ML model can understand and compare to perform a semantic search. Choosing the appropriate embedding model is critical for capturing the semantic essence of data chunks. Select models that align with your domain-specific needs and that can generate embeddings that accurately reflect the content's meaning. Choosing the best embedding model for your use case can improve relevancy and contextual accuracy.

1. **Indexing and search algorithms** – Index the embeddings in a vector database that is optimized for similarity searches. Employ search algorithms that efficiently handle high-dimensional data and support rapid retrieval of relevant information. Techniques such as approximate nearest neighbor (ANN) search can significantly enhance retrieval speed without compromising accuracy.

RAG pipelines are inherently complex. They require multiple stages, varying levels of integration, and a high degree of expertise to design effectively. When implemented correctly, they can significantly enhance the performance and accuracy of a generative AI solution. However, maintaining these systems is resource-intensive and necessitates continuous monitoring, optimization, and scaling. This complexity has led to the emergence of *RAGOps*, a dedicated approach to operationalizing and managing RAG pipelines efficiently, to promote long-term reliability and effectiveness.

For more information about RAG on AWS, see the following resources:
+ [Retrieval Augmented Generation options and architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html) (AWS Prescriptive Guidance)
+ [Choosing an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html) (AWS Prescriptive Guidance)
+ [Deploy a RAG use case on AWS by using Terraform and Amazon Bedrock](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-rag-use-case-on-aws.html) (AWS Prescriptive Guidance)

## Fine-tuning and specialized training
<a name="lifecycle-fine-tuning"></a>

Fine-tuning can take two distinct forms: *domain fine-tuning* and *task fine-tuning*. Each serves a different purpose in adapting a pre-trained model. Unsupervised domain fine-tuning involves further training the model on a body of domain-specific text to help it better understand the language, terminology, and context unique to a particular field or industry. For example, you might fine-tune a media-specific LLM on a collection of internal articles and jargon to reflect the company's tone of voice and specialized vocabulary.

In contrast, supervised task fine-tuning focuses on teaching the model to perform a specific function or output format. For example, you might teach it to answer customer queries, summarize legal documents, or extract structured data. This typically requires preparing a labelled dataset that contains examples of inputs and desired outputs for the target task.

Both approaches require careful collection and curation of fine-tuning data. For task fine-tuning, datasets are explicitly labelled. For domain fine-tuning, you can use unlabeled text to improve general language understanding in the relevant context. Regardless of the approach, data quality is paramount. Clean, representative, and appropriately sized datasets are essential to maintain and enhance the model's performance. Typically, fine-tuning datasets are much smaller than those used for initial pre-training but must be thoughtfully selected to ensure effective model adaptation.

An alternative to fine-tuning is *model distillation*, a technique that involves training a smaller, specialized model to replicate the performance of a larger, more general model. Instead of fine-tuning an existing LLM, model distillation transfers knowledge by training a lightweight model (the *student*) on outputs generated by the original, more complex model (the *teacher*). This approach is particularly beneficial when computational efficiency is a priority because distilled models require fewer resources while retaining task-specific performance.

Rather than requiring extensive domain-specific training data, model distillation relies on synthetic or teacher-generated datasets. The complex model produces high-quality examples for the lightweight model to learn from. This reduces the burden of curating proprietary data but still demands careful selection of diverse and unbiased training examples to maintain generalization capabilities. Furthermore, distillation can help mitigate risks associated with data privacy because you can train the lightweight model on protected data without directly exposing sensitive records.

That said, most organizations are unlikely to undertake fine-tuning or distillation because it is often unnecessary for their use cases and introduces an additional layer of operational and technical complexity. Many business needs can be met effectively using pre-trained foundation models, sometimes with light customization through prompt engineering or tools such as RAG. Fine-tuning requires considerable investment in terms of technical capability, data curation, and model governance. This makes it more suitable for highly specialized or large-scale enterprise applications where such effort is justified.

## Evaluation dataset
<a name="lifecycle-evaluation"></a>

Developing a robust data strategy is essential when constructing *evaluation datasets* for generative AI solutions. These evaluation datasets act as benchmarks for assessing model performance. They should be anchored in reliable *ground truth data*, which is data that is known to be accurate, verified, and representative of real-world outcomes. For example, ground truth data might be real data that you withhold from a training or a fine-tuning dataset. Ground truth data can come from several sources, and each presents its own challenges.

Synthetic data generation provides a scalable way to create controlled datasets for testing specific model capabilities without exposing sensitive information. However, its effectiveness depends on how closely it replicates genuine ground truth distributions.

Alternatively, manually curated datasets, often called *golden datasets*, contain rigorously verified question-answer pairs or labelled examples. This datasets can serve as high-quality ground truth data for robust model evaluation. However, these datasets are time-consuming and resource-intensive to compile. Incorporating actual customer interactions as evaluation data can further enhance the relevance and coverage of ground truth data, though this requires strict privacy safeguards and regulatory compliance (such as with GDPR and CCPA).

A comprehensive data strategy should balance these approaches. To effectively evaluate generative AI models, consider factors such as data quality, representativeness, ethical considerations, and alignment with business objectives. For more information, see [Amazon Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/).

## User-generated data and feedback loops
<a name="lifecycle-feedback-loops"></a>

Once a generative AI system is deployed, it begins to produce outputs and interact with users. These interactions themselves become a valuable source of data. User-generated data includes user questions and prompts, the model's responses, and any explicit feedback that users provide (such as ratings). Enterprises should treat this as part of the generative AI data lifecycle and feed it back into monitoring and improvement processes. Importantly, user-generated data can be incorporated into your ground truth dataset. This helps to further optimize prompts and enhance the overall performance of your application over time. Another critical reason is to manage model drift and performance over time. After real-world use, the model might start to diverge from its training domain. Examples of this are new slang appearing in queries or users asking questions about emerging topics that are not present in the training data. Monitoring this live data can reveal *data drift*, where the input distribution shifts, which can potentially degrade model accuracy.

To combat this, organizations establish feedback loops by capturing user interactions and periodically retraining or fine-tuning the model on a recent sample of them. Sometimes, you can simply use the feedback to adjust prompts and retrieval data. For example, if an internal chatbot assistant consistently hallucinates answers about a newly released product, the team might collect those failed Q&A pairs and include the correct information as additional training or retrieval data.

In some cases, *reinforcement learning from human feedback (RLHF)* is used to further align a LLM during the post-training or fine-tuning phase. It helps the model produce responses that better reflect human preferences and values. Reinforcement learning (RL) techniques train software to make decisions that maximize rewards, making their outcomes more accurate. RLHF incorporates human feedback in the rewards function, so the ML model can perform tasks more aligned with human goals, wants, and needs. For more information about using RLHF in Amazon SageMaker AI, see [Improving your LLMs with RLHF on Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/improving-your-llms-with-rlhf-on-amazon-sagemaker/) on the AWS AI blog.

Even without formal RLHF, a simpler approach is manual review of a fraction of model outputs on an ongoing basis, akin to quality assurance. The key is that continuous monitoring, observability, and learning are built into the process. For more information about how to gather and store human feedback from generative AI applications on AWS, see [Guidance for Chatbot User Feedback and Analytics on AWS](https://aws.amazon.com/solutions/guidance/chatbot-user-feedback-and-analytics-on-aws/) in the AWS Solutions Library.

To preempt or address drift, enterprises need to plan for continuous model updates, which can take several forms. One approach is scheduling regular fine-tuning or continuous pre-training. For example, you might update the model monthly with the latest internal data, support cases, or news articles. During continuous pre-training, a pre-trained language model is further trained on additional data to enhance its performance, particularly in specific domains or tasks. This process involves exposing the model to new, unlabeled text data, allowing it to refine its understanding and adapt to new information without starting from scratch. To assist with that potentially complex process, Amazon Bedrock allows you to do fine-tuning and continuous pre-training in a fully secure and managed environment. For more information, see [Customize models in Amazon Bedrock with your own data using fine-tuning and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/) on the AWS News Blog.

In the scenario where you use off-the-shelf models with RAG, you can rely on cloud AI services, such as Amazon Bedrock. These services offer regular model upgrades as they are released and add them to the available catalog. This helps you update your solutions to use the latest versions of these foundation models.
