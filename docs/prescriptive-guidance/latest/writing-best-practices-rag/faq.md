---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/writing-best-practices-rag/faq.html
---

# FAQ
<a name="faq"></a>

## Why is it important to optimize documents for RAG applications?
<a name="faq-1"></a>

Raw documents are often written for human consumption without considering the requirements of advanced AI systems, such as Retrieval Augmented Generation (RAG) applications. Optimizing documents by following best practices can significantly improve the performance and accuracy of RAG applications by providing structured, unambiguous, and relevant information to the models.

## What are some common challenges with raw documents that can hinder RAG performance?
<a name="faq-2"></a>

Some key challenges include lack of structured formatting and metadata, informal or inconsistent language, verbosity and redundancy, ambiguous terms and phrases, inclusion of hyperlink elements, and lack of domain-specific context. These issues can confuse RAG models and lead to inaccurate or irrelevant responses. For more information, see [Challenges in source data that affect RAG applications](challenges.md) in this guide.

## How can the use of headings and subheadings improve RAG performance?
<a name="faq-3"></a>

Clear headings and subheadings help RAG models understand the structure and context of the content. This enables them to better navigate and extract relevant information from the documents and improves the quality of generated responses. For more information, see [Documentation best practices for RAG applications](best-practices.md) in this guide.

## Why is it recommended to replace table information with flat-level syntax?
<a name="faq-4"></a>

It can be challenging for RAG models to interpret tables because they require an understanding of the two-dimensional structure. Presenting table information in a flat-level syntax or bulleted list helps models to more easily process the information, leading to better performance. For more information, see [Documentation best practices for RAG applications](best-practices.md) in this guide.

## How can adding summaries enhance RAG performance?
<a name="faq-5"></a>

Including concise summaries at the beginning of each section or subsection can increase semantic coverage and reinforce key points. This improves the accuracy of similarity searches within the embedding space, which ultimately enhances the performance of the RAG application. For more information, see [Documentation best practices for RAG applications](best-practices.md) in this guide.

## Why is it important to define abbreviations and set context for LLMs?
<a name="faq-6"></a>

LLMs are trained on a broad range of data, but they lack context for enterprise-specific abbreviations or terminology. Defining abbreviations and providing context helps LLMs understand and respond more accurately. This can help prevent hallucinations or misinterpretations. For more information, see [Documentation best practices for RAG applications](best-practices.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
