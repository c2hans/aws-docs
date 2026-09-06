---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/faq.html
---

# FAQ about healthcare and life science use cases
<a name="faq"></a>

The following are frequently asked questions related to using Amazon Comprehend Medical or LLMs for medical NLP tasks.

## How do I choose between Amazon Comprehend Medical and an LLM?
<a name="faq-1"></a>

If your task is to detect medical entities within your medical text, then review the [Amazon Comprehend Medical documentation](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html) to understand which medical entities can be extracted and if any of the [ontologies](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-ontologies.html) address your use case. If not, consider using an LLM. For more information, see [Use cases for Amazon Comprehend Medical](comprehend-medical.md#comprehend-medical-use-cases) and [Use cases for an LLM](llms.md#llm-use-cases) in this guide.

## How can I provide Amazon Comprehend Medical results to an LLM?
<a name="faq-2"></a>

You can incorporate Amazon Comprehend Medical results as context within your LLM prompts. This provides additional medical knowledge and terminology to the LLM. The provided context can improve the LLM's performance on tasks such as entity recognition, summarization, or question-answering. The guide provides several examples of how to structure prompts with Amazon Comprehend Medical results. For more information, see [Combining Amazon Comprehend Medical with large language models](comprehend-medical-rag.md) in this guide.

## What are some best practices when using Amazon Comprehend Medical with LLMs?
<a name="faq-3"></a>

We recommend using the Amazon Comprehend Medical confidence scores to filter or prioritize entities within your prompts. It's also important to evaluate its performance on your specific data and validate that the entity definitions align with your requirements. Combining Amazon Comprehend Medical with domain-specific knowledge sources can further enhance the LLM's performance. For more information, see [Best practices for using Amazon Comprehend Medical in a RAG workflow](comprehend-medical-rag.md#comprehend-medical-rag-best-practices) in this guide.

## Should I use a pretrained medical LLM or fine-tune a general LLM for my healthcare use case?
<a name="faq-4"></a>

The decision depends on your specific requirements and the availability of high-quality training data. Pretrained medical LLMs can provide a good starting point. However, you might still need to fine-tune them with your domain-specific data. If you have sufficient labeled data, fine-tuning a general LLM can be a viable option. For more information, see [Choosing an LLM](llms.md#llm-selection) and [Choosing an NLP approach](choosing-approach.md) in this guide.

## How do I evaluate the performance of LLMs for medical NLP tasks?
<a name="faq-5"></a>

We recommend using quantitative metrics, such as accuracy, precision, recall, and F1 score for text classification and named entity recognition tasks. You can use ROUGE and METEOR for text generation tasks. It's important to have reliable ground truth data labeled by subject matter experts and to implement processes for monitoring model performance over time. For more information, see [Evaluating LLMs for healthcare and life science applications](evaluation.md) in this guide.

## What are the trade-offs between high-complexity and low-complexity LLM solutions?
<a name="faq-6"></a>

Fine-tuning an LLM or building a custom LLM are highly complex solutions. These approaches can improve performance but come with higher costs and maintenance requirements. Simpler solutions, such as using pretrained LLMs or Amazon Comprehend Medical, might provide acceptable performance with lower costs and faster development cycles. However, these approaches might not meet stringent accuracy requirements for some use cases. For more information, see [Business maturity considerations](choosing-approach.md#business-maturity) in this guide.
