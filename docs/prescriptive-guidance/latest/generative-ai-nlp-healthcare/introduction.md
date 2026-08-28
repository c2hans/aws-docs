---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/introduction.html
---

# Using Amazon Comprehend Medical and LLMs for healthcare and life sciences
<a name="introduction"></a>

*Joe King, Ross Claytor, Ankith Ede, Jillian Forde, Clement Perrot, Rajesh Sitaraman, and Shivi Ummat, Amazon Web Services*

## Overview
<a name="overview"></a>

The ever-increasing volume of medical data and the need for efficient and accurate processing have driven the adoption of [natural language processing (NLP)](https://aws.amazon.com/what-is/nlp/) with artificial intelligence and machine learning (AI/ML) technologies. Pretrained classifier models and [large language models (LLMs)](https://aws.amazon.com/what-is/large-language-model/) have emerged as powerful tools for various medical NLP tasks, including clinical question-answering, report summarization, and insight generation. However, the healthcare and life science domain presents unique challenges due to the complexity of medical terminology, domain-specific knowledge, and regulatory requirements. Effectively using pretrained classifiers or LLMs in this domain requires a well-designed approach that combines the strengths of these models with domain-specific resources and techniques.

Industry practices in healthcare and life science have traditionally relied on rule-based systems, manual coding, and expert review processes. These systems and processes are time-consuming and error-prone. The integration of AI and NLP technologies, such as [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html) and the foundation models in [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), offers efficient and scalable solutions for processing medical data while improving accuracy and consistency.

This guide explores the use of Amazon Comprehend Medical and LLMs for intelligent automation in the healthcare industry. It outlines best practices, challenges, and practical approaches to streamlining medical coding, patient information extraction, and record summarization processes. By using the capabilities of Amazon Comprehend Medical and LLMs, healthcare organizations can unlock new levels of operational efficiency, reduce costs, and potentially improve patient care.

The guide details the unique considerations of the healthcare domain, such as understanding medical terminology, using domain-specific LLMs, and addressing the limitations of AI/ML systems. It provides a comprehensive decision path for healthcare IT managers, architects, and technical leads to assess organizational readiness, evaluate implementation options, and use the appropriate AWS services and tools for successful automation.

By following the guidelines and best practices outlined in this guide, healthcare organizations can harness the power of AI/ML technologies while navigating the complexities of the medical domain. This approach supports compliance with ethical and regulatory guidelines and promotes the responsible use of AI systems in healthcare. It is designed to generate insights that are accurate and private.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for technology stakeholders, architects, technical leads, and decision makers who want to implement AI-powered natural language processing solutions for medical data analysis and automation.

## Objectives
<a name="objectives"></a>

Healthcare and life science organizations can meet multiple business goals by using Amazon Comprehend Medical and LLMs. These outcomes commonly include increasing operational efficiency, reducing costs, and improving patient care. This section outlines key business objectives and the associated benefits of implementing the strategies and best practices outlined in this guide.

The following are the some of the objectives that organizations can achieve by implementing the guidelines and best practices in this guide:
+ **Reduce the development time **– This guide's ultimate goal is to reduce development time with cost, decrease technical debt, and mitigate potential project failure from POC. By understanding key AI/ML services, such as Amazon Comprehend Medical, and the advantages and limitations of LLM usage for healthcare tasks, businesses can achieve faster time to market and increase their velocity in meeting business objectives.
+ **Extract information to automate medical coding tasks **– After patient visits, coding specialist and providers can extract insights from medical text, such as subjective, objective, assessment, and plan (SOAP) notes. This can reduce manual documentation efforts and help the provider focus on the patient's needs. By combining the entity recognition capabilities of Amazon Comprehend Medical with LLMs, organizations can extract relevant medical information from patient records, clinical notes, and other healthcare data sources. This can minimize human errors and promote consistent practices.
+ **Summarize patient records and clinical documentation** – Automated summarization of patient history, treatment plans, and medical results can save valuable time for healthcare providers. LLMs can help generate comprehensive and structured clinical documentation. You can get additional context with Amazon Comprehend Medical, use a medical domain LLM, or fine-tune an LLM with medical data. These approaches can help provide accurate summaries and make sure that documentation adheres to compliance requirements and standards.
+ **Support clinical decisions and patient care **– By using [ontology linking](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-howitworks.html#link-standard) in Amazon Comprehend Medical and by using LLMs, providers can answer medical questions or seek recommendations addressing patient care. This empowers healthcare professionals to make informed decisions that improve patient outcomes and reduce the risk of medical errors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
