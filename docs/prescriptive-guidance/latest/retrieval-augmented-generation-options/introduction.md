---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html
---

# Retrieval Augmented Generation options and architectures on AWS
<a name="introduction"></a>

*Mithil Shah, Natacha Fort, and Rajeev Muralidhar, Amazon Web Services*

*Generative AI* refers to a subset of AI models that can create new content and artifacts, such as images, videos, text, and audio, from a simple text prompt. Generative AI models are trained on vast amounts of data that encompasses a wide range of subjects and tasks. This enables them to demonstrate remarkable versatility in performing various tasks, even those for which they have not been explicitly trained. Due to a single model's ability to perform multiple tasks, these models are often referred to as *foundation models* (FMs).

One of the notable applications of generative AI models is their proficiency in answering questions. However, there are specific challenges that arise when these models are used to answer questions based on custom documents. Custom documents can include proprietary information, internal websites, internal documentation, Confluence pages, SharePoint pages, and others. One option is to use *Retrieval Augmented Generation (RAG)*. With RAG, the foundation model references an authoritative data source that is outside of its training data sources (such as your custom documents) before generating a response.

This guide describes the distinct generative AI options that are available for answering questions from custom documentation, including Retrieval Augmented Generation (RAG) systems. It also provides an overview of building RAG systems on Amazon Web Services (AWS). By reviewing the RAG options and architectures, you can choose between fully managed services on AWS and custom RAG architectures.

## Intended audience
<a name="intended-audience"></a>

The intended audience for this guide is generative AI architects and managers who want to build a RAG solution, to review the available architectures, and to understand the benefits and drawbacks of each option.

## Objectives
<a name="objectives"></a>

This guide helps you do the following:
+ Understand the generative AI options available for answering questions from custom documents
+ Review the architecture options for RAG systems on AWS
+ Understand the advantages and disadvantages of each RAG option
+ Choose a RAG architecture for your AWS environment
