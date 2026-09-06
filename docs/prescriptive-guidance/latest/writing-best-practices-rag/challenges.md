---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/writing-best-practices-rag/challenges.html
---

# Challenges in source data that affect RAG applications
<a name="challenges"></a>

One of the significant challenges in developing an optimal Retrieval-Augmented Generation (RAG) application lies in the nature of the raw data or documents used. Often, enterprises use existing documents that were created for human reference. These documents often include hyperlinks and image screenshots to promote understanding. However, these elements obstruct semantic retrieval due to excerpt token limits. This results in poor retriever performance.

The following are the most common raw document challenges for an optimal RAG application:
+ **Lack of structured formatting and metadata** – Raw documents can lack clear section headings, subheadings, or metadata. This makes it challenging to identify and extract relevant information. For example, a long document without clear headings can make it difficult to determine the context of specific information.
+ **Informal and inconsistent language** – Raw documents often contain informal language or inconsistent terminology. This can confuse RAG models. For instance, abbreviations that are not defined in the document or already known by the LLM might be used throughout a document.
+ **Verbosity and redundancy** – Raw documents may be verbose and contain unnecessary or redundant information. This can overwhelm RAG models, leading to less concise and relevant responses. Examples include a document that repeats the same information multiple times or multiple documents that contain similar or contradictory information.
+ **Ambiguous terms and phrases** – Raw documents can contain ambiguous terms or phrases that might be interpreted in multiple ways. This ambiguity can lead to misinterpretation by RAG models and inaccurate responses. For example, a document that uses a term with multiple meanings can result in a response that does not align with the intended meaning.
+ **Injection of graphic and hyperlink elements** – Raw documents that contain graphics and hyperlink information work well for human consumption. However, these elements can consume the retrieval token limit. The result is that excerpts might be incomplete. For example, graphics and hyperlink URLs are returned as part of the retrieval, which uses up the retrieval tokens, and key information from subsequent paragraphs is missing.
+ **Lack of domain-specific knowledge or context** – Raw documents can lack the necessary domain-specific knowledge or context required for accurate generation. This can limit the ability of RAG models to generate relevant and accurate responses. An example is a document that references specialized concepts without providing context. This might lead to responses that are not meaningful in the given domain.

Although this list isn't comprehensive, it provides a starting point for enterprises to think about what is not working and why. Documents might have one or more of these challenges. The key to optimizing a RAG application is to use a set of documents that adhere to writing best practices that optimize retrieval.
