---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/options.html
---

# Generative AI options for querying custom documents
<a name="options"></a>

Organizations often have various sources of structured and unstructured data. This guide focuses on how you can use generative AI to answer questions from unstructured data.

Unstructured data in your organization can come from various sources. These might be PDFs, text files, internal wikis, technical documents, public facing websites, knowledge bases, or others. If you want a foundation model that can answer questions about unstructured data, the following options are available:
+ Train a new foundation model by using your custom documents and other training data
+ Fine-tune an existing foundation model by using data from your custom documents
+ Use in-context learning to pass a document to the foundation model when you ask a question
+ Use a Retrieval Augmented Generation (RAG) approach

Training a new foundation model from scratch that includes your custom data is an ambitious undertaking. A few companies have done it successfully, such as Bloomberg with their [BloombergGPT](https://www.bloomberg.com/company/press/bloomberggpt-50-billion-parameter-llm-tuned-finance/) model. Another example is the multimodal [EXAONE](https://www.lgresearch.ai/ourwork/research?tab=PF) model by LG AI Research, which was trained by using 600 billion pieces of artwork and 250 million high-resolution images, accompanied with text. According to [The Cost of AI: Should You Build or Buy Your Foundation Model](https://www.linkedin.com/pulse/cost-ai-should-you-build-buy-your-foundation-model-ritesh-vajariya/) (LinkedIn), a model similar to Meta Llama 2 costs around USD $4.8 million to train. There are two primary prerequisites for training a model from scratch: access to resources (financial, technical, time) and a clear return on investment. If this does not seem the right fit, then the next option is to fine-tune an existing foundation model.

Fine-tuning an existing model involves taking a model, such as an Amazon Titan, Mistral, or Llama model, and then adapting the model to your custom data. There are various techniques for fine-tuning, most of which involve modifying only a few parameters instead of modifying all of the parameters in the model. This is called *parameter-efficient fine-tuning*. There are two primary methods for fine-tuning:
+ *Supervised fine-tuning* uses labeled data and helps you train the model for a new kind of task. For example, if you wanted to generate a report based on a PDF form, then you might have to teach the model how to do that by providing enough examples.
+ *Unsupervised fine-tuning* is task-agnostic and adapts the foundation model to your own data. It trains the model to understand the context of your documents. The fine-tuned model then creates content, such as a report, by using a style that is more custom your organization.

However, fine-tuning may not be ideal for question-answer use cases. For more information, see [Comparing RAG and fine-tuning](rag-vs-fine-tuning.md) in this guide.

When you ask a question, you can pass a document the foundation model and use the model's in-context learning to return answers from the document. This option is suitable for ad-hoc querying of a single document. However, this solution doesn't work well for querying multiple documents or for querying systems and applications, such as Microsoft SharePoint or Atlassian Confluence.

The final option is to use RAG. With RAG, the foundation model references your custom documents before generating a response. RAG extends the model's capabilities to your organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving the model output so that it remains relevant, accurate, and useful in various contexts.

**Topics in this section:**
+ [Understanding RAG](what-is-rag.md)
+ [Comparing RAG and fine-tuning](rag-vs-fine-tuning.md)
+ [Use cases for RAG](rag-use-cases.md)
