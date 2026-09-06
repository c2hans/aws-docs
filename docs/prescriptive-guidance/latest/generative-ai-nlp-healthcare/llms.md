---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/llms.html
---

# Using large language models for healthcare and life science use cases
<a name="llms"></a>

This describes how you can use large language models (LLMs) for healthcare and life science applications. Some use cases require the use of a large language model for generative AI capabilities. There are advantages and limitations for even the most state-of-the-art LLMs, and the recommendations in this section are designed to help you achieve your target results.

You can use the decision path to determine the appropriate LLM solution for your use case, considering factors such as domain knowledge and available training data. Additionally, this section discusses popular pretrained medical LLMs and best practices for their selection and use. It also discusses the trade-offs between complex, high-performance solutions and simpler, lower-cost approaches.

## Use cases for an LLM
<a name="llm-use-cases"></a>

Amazon Comprehend Medical can perform specific NLP tasks. For more information, see [Use cases for Amazon Comprehend Medical](comprehend-medical.md#comprehend-medical-use-cases).

The logical and generative AI capabilities of an LLM might be required for the advanced healthcare and life science use cases, such as the following:
+ Classifying custom medical entities or text categories
+ Answering clinical questions
+ Summarizing medical reports
+ Generating and detecting insights from medical information

## Customization approaches
<a name="llm-customization"></a>

It's critical to understand how LLMs are implemented. LLMs are commonly trained with billions of parameters, including training data from many domains. This training allows the LLM to address most generalized tasks. However, challenges often arise when domain-specific knowledge is required. Examples of domain knowledge in healthcare and life science are clinic codes, medical terminology, and health information that is required to generate accurate answers. Therefore, using the LLM as is (zero-shot prompting without supplementing domain knowledge) for these use cases likely results in inaccurate results. There are several popular approaches you can use to overcome this challenge: prompt engineering, Retrieval Augmented Generation (RAG), and fine-tuning.

### Prompt engineering
<a name="llm-customization-prompt-engineering"></a>

*Prompt engineering* is the process where you guide generative AI solutions to create the desired outputs by adjusting the inputs to the LLM. By crafting precise prompts with relevant context, it's possible to guide the model towards completion of specialized healthcare tasks that require reasoning. Effective prompt engineering can significantly improve model performance for healthcare use cases without requiring model modifications. For more information about prompt engineering, see [Implementing advanced prompt engineering with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/implementing-advanced-prompt-engineering-with-amazon-bedrock/) (AWS blog post). Few-shot prompting and chain-of-thought prompting are techniques that you can use in prompt engineering.

#### Few-shot prompting
<a name="few-shot-prompting.5d7d8ffe-985a-5f7a-a5f2-8e71773adefb"></a>

Few-shot prompting is a technique where you provide the LLM with a few examples of the desired input-output before asking it to perform a similar task. In healthcare contexts, this approach is particularly valuable for specialized tasks, such as medical entity recognition or clinical note summarization. By including 3–5 high-quality examples in your prompt, you can significantly improve the model's understanding of medical terminology and domain-specific patterns. For an example of few-shot prompting, see [Few-shot prompt engineering and fine-tuning for LLMs in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/few-shot-prompt-engineering-and-fine-tuning-for-llms-in-amazon-bedrock/) (AWS blog post).

For example, when you extract medication dosages from clinical notes, you can provide examples of different notation styles that help the model recognize variations in how healthcare professionals document prescriptions. This approach is especially effective when working with standardized documentation formats or when consistent patterns exist in the data.

#### Chain-of-thought prompting
<a name="chain-of-thought-prompting.3242b825-0229-5d87-8513-d8c299cadd67"></a>

*Chain-of-thought (CoT) prompting* guides the LLM through a step-by-step reasoning process. This makes it valuable for complex medical decision support and diagnostic reasoning tasks. By explicitly instructing the model to "think step by step" when analyzing clinical scenarios, you can improve its ability to follow medical reasoning protocols and reduce diagnostic errors.

This technique excels when clinical reasoning requires multiple logical steps, such as differential diagnosis or treatment planning. However, this approach has limitations when dealing with highly specialized medical knowledge outside the model's training data or when absolute precision is required for critical care decisions.

In these cases, combining CoT with another approach can yield better results. One option is to combine CoT with self-consistency prompting. For more information, see [Enhance performance of generative language models with self-consistency prompting on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/enhance-performance-of-generative-language-models-with-self-consistency-prompting-on-amazon-bedrock/) (AWS blog post). Another option is to combine reasoning frameworks, such as ReAct prompting, with RAG. For more information, see [Develop advanced generative AI chat-based assistants by using RAG and ReAct prompting](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting.html) (AWS Prescriptive Guidance).

### Retrieval Augmented Generation
<a name="retrieval-augmented-generation.0f0158df-9fba-55fc-ae4b-4dcd12c6abc6"></a>

*Retrieval Augmented Generation (RAG)* is a generative AI technology in which an LLM references an authoritative data source that is outside of its training data sources before generating a response. A RAG system can retrieve medical ontology information (such as international classifications of diseases, national drug files, and medical subject headings) from a knowledge source. This provides additional context to the LLM to support the medical NLP task.

As discussed in the [Combining Amazon Comprehend Medical with large language models](comprehend-medical-rag.md) section, you can use a RAG approach to retrieve context from Amazon Comprehend Medical. Other common knowledge sources include medical domain data that is stored in a database service, such as Amazon OpenSearch Service, Amazon Kendra, or Amazon Aurora. Extracting information from these knowledge sources can affect retrieval performance, especially with semantic queries that use a vector database.

Another option for storing and retrieving domain-specific knowledge is by using [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) in your RAG workflow. Amazon Q Business can index internal document repositories or public-facing web sites (such as [CMS.gov](https://cms.gov/) for ICD-10 data). Amazon Q Business can then extract relevant information from these sources before passing your query to the LLM.

There are multiple ways to build a custom RAG workflow. For example, there are many ways to retrieve data from a knowledge source. For simplicity, we recommend the common retrieval approach of using a vector database, such as Amazon OpenSearch Service, to store knowledge as embeddings. This requires that you use an embedding model, such as a sentence transformer, to generate embeddings for the query and for the knowledge stored in the vector database.

For more information about fully managed and custom RAG approaches, see [Retrieval Augmented Generation options and architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html).

### Fine-tuning
<a name="fine-tuning.06f697dc-eb5e-5e24-aa91-3f2cefb93b1c"></a>

*Fine-tuning* an existing model involves taking an LLM, such as an Amazon Titan, Mistral, or Llama model, and then adapting the model to your custom data. There are various techniques for fine-tuning, most of which involve modifying only a few parameters instead of modifying all of the parameters in the model. This is called *parameter-efficient fine-tuning (PEFT)*. For more information, see [Hugging Face PEFT](https://github.com/huggingface/peft) on GitHub.

The following are two common use cases when you might choose to fine-tune an LLM for a medical NLP task:
+ **Generative task** – Decoder-based models perform generative AI tasks. AI/ML practitioners use ground truth data to fine-tune an existing LLM. For example, you might train the LLM by using [MedQuAD](https://github.com/abachaa/MedQuAD), a public medical question-answering dataset. When you invoke a query to the fine-tuned LLM, you don't need a RAG approach to provide the additional context to the LLM.
+ **Embeddings** – Encoder-based models generate embeddings by transforming text into numerical vectors. These encoder-based models are typically called *embedding models*. A *sentence-transformer model* is a specific type of embedding model that is optimized for sentences. The objective is to generate embeddings from input text. The embeddings are then used for semantic analysis or in retrieval tasks. To fine-tune the embedding model, you must have a corpus of medical knowledge, such as documents, that you can use as training data. This is accomplished with pairs of text based on similarity or sentiment to fine-tune a sentence transformer model. For more information, see [Training and Finetuning Embedding Models with Sentence Transformers v3](https://huggingface.co/blog/train-sentence-transformers) on Hugging Face.

You can use [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) to build a high-quality, labeled training dataset. You can use the labeled dataset output from Ground Truth to train your own models. You can also use the output as a training dataset for an Amazon SageMaker AI model. For more information about named entity recognition, single label text classification, and multi-label text classification, see [Text labeling with Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-label-text.html) in the Amazon SageMaker AI documentation.

For more information about fine-tuning, see [Fine-tuning large language models in healthcare](fine-tuning.md) in this guide.

## Choosing an LLM
<a name="llm-selection"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is the recommended starting point to evaluate high-performing LLMs. For more information, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). You can use model evaluation jobs in Amazon Bedrock in order to compare the outputs from multiple outputs and then choose the model that is best suited for your use case. For more information, see [Choose the best performing model using Amazon Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) in the Amazon Bedrock documentation.

Some LLMs have limited training on medical domain data. If your use case requires fine-tuning an LLM or an LLM that Amazon Bedrock doesn't support, consider using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html). In SageMaker AI, you can use a fine-tuned LLM or choose a custom LLM that has been trained on medical domain data.

The following table lists popular LLMs that have been trained on medical domain data.

|
|
| LLM | Tasks | Knowledge | Architecture |
| --- |--- |--- |--- |
| [BioBERT](https://github.com/dmis-lab/biobert) | Information retrieval, text classification, and named entity recognition | Abstracts from PubMed, full-text articles from PubMedCentral, and general domain knowledge | Encoder |
| [ClinicalBERT](https://github.com/kexinhuang12345/clinicalBERT) | Information retrieval, text classification, and named entity recognition | Large, multi-center dataset along with over 3,000,000 patient records from electronic health record (EHR) systems | Encoder |
| [ClinicalGPT](https://huggingface.co/medicalai/ClinicalGPT-base-zh) | Summarization, question-answering, and text generation | Extensive and diverse medical datasets, including medical records, domain-specific knowledge, and multi-round dialogue consultations | Decoder |
| [GatorTron-OG](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/clara/models/gatortron_og) | Summarization, question-answering, text generation, and information retrieval | Clinical notes and biomedical literature | Encoder |
| [Med-BERT](https://github.com/ZhiGroup/Med-BERT) | Information retrieval, text classification, and named entity recognition | Large dataset of medical texts, clinical notes, research papers, and healthcare-related documents | Encoder |
| [Med-PaLM](https://sites.research.google/med-palm/) | Question-answering for medical purposes | Datasets of medical and biomedical text | Decoder |
| [medAlpaca](https://github.com/kbressem/medAlpaca) | Question-answering and medical dialogue tasks | A variety of medical texts, encompassing resources such as medical flashcards, wikis, and dialogue datasets | Decoder |
| [BiomedBERT](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) | Information retrieval, text classification, and named entity recognition | Exclusively abstracts from PubMed and full-text articles from PubMedCentral | Encoder |
| [BioMedLM](https://github.com/stanford-crfm/BioMedLM) | Summarization, question-answering, and text generation | Biomedical literature from PubMed knowledge sources | Decoder |

The following are best practices for using pretrained medical LLMs:
+ Understand the training data and its relevance to your medical NLP task.
+ Identify the LLM architecture and its purpose. Encoders are appropriate for embeddings and NLP tasks. Decoders are for generation tasks.
+ Evaluate the infrastructure, performance, and cost requirements for hosting the pretrained medical LLM.
+ If fine-tuning is required, ensure accurate ground truth or knowledge for the training data. Make sure that you mask or redact any personally identifiable information (PII) or protected health information (PHI).

Real-world medical NLP tasks might differ from pretrained LLMs in terms of knowledge or intended use cases. If a domain-specific LLM does not meet your evaluation benchmarks, you can fine-tune an LLM with your own dataset or you can train a new foundation model. Training a new foundation model is an ambitious, and often expensive, undertaking. For most use cases, we recommend fine-tuning an existing model.

When you use or fine-tune a pretrained medical LLM, it's important to address infrastructure, security, and guardrails.

### Infrastructure
<a name="infrastructure.22af4a08-b7f8-5df8-a560-f3367e105149"></a>

Compared to using Amazon Bedrock for on-demand or batch inference, hosting pretrained medical LLMs (commonly from Hugging Face) requires significant resources. To host pretrained medical LLMs, it's common to use an Amazon SageMaker AI image that runs on an Amazon Elastic Compute Cloud (Amazon EC2) instance with one or more GPUs, such as ml.g5 instances for accelerated computing or ml.inf2 instances for AWS Inferentia. This is because LLMs consume a large amount of memory and disk space.

### Security and guardrails
<a name="security-and-guardrails.bc427d29-fbb1-5284-bc3c-d57c71db2376"></a>

Depending on your business compliance requirements, consider using Amazon Comprehend and Amazon Comprehend Medical to mask or redact personally identifiable information (PII) and protected health information (PHI) from training data. This helps prevent the LLM from using confidential data when it generates responses.

We recommend that you consider and evaluate bias, fairness, and hallucinations in your generative AI applications. Whether you are using a preexisting LLM or fine-tuning one, implement guardrails to prevent harmful responses. *Guardrails* are safeguards that you customize to your generative AI application requirements and responsible AI policies. For example, you can use [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html).
