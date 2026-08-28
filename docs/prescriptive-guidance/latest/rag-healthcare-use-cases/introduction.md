---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/introduction.html
---

# Creating Retrieval Augmented Generation solutions on AWS for healthcare
<a name="introduction"></a>

*Soonam Kurian, Amazon Web Services*

Before large language models (LLMs) and generative AI, the task of developing automated and high-precision applications in the healthcare industry was challenging. Traditional methods relied heavily on manual data entry and analysis. The complexity of analyzing medical imaging and patient records required extensive human intervention, which often resulted in fragmented and inefficient workflows. The advancement of AI technologies helps you build hyper-personalized applications at scale. Healthcare applications can now integrate with medical knowledge bases, interpret diagnostic images with increased accuracy, and forecast patient outcomes by using predictive models.

This guide explores how LLMs are revolutionizing healthcare through Retrieval Augmented Generation applications that you can build with AWS services. *Retrieval Augmented Generation (RAG)* is a generative AI technology in which an LLM references an authoritative data source that is outside of its training data sources before generating a response. RAG applications ground the model's output in real-world knowledge, which reduces hallucinations and increases response relevance. In the healthcare sector, RAG can be used to provide accurate and up-to-date medical information, ensuring that healthcare providers have access to the latest research and clinical guidelines. By transforming data into actionable insights and automating complex processes, these technologies help enhance patient care, streamline operations, and improve productivity of healthcare professionals.

In [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), you can fine-tune LLMs and integrate them with intelligent agents to create advanced healthcare solutions. Highlighting the synergy between [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) and [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html), the guide demonstrates how these services elevate RAG solutions through enhanced search relevance and advanced multi-source data retrieval. You can orchestrate comprehensive Amazon Bedrock solutions that use Amazon Bedrock agents and [LangChain](https://python.langchain.com/docs/introduction/) to seamlessly coordinate interactions across diverse data repositories. This integration demonstrates the power of combining specialized services to create more effective and efficient AI-driven systems.

## Patient care and productivity
<a name="intro-patient-care"></a>

This guide presents two real-world use cases for patient care and productivity: [patient data augmentation](case-1.md) and [predicting re-admission risks](case-2.md). It provides strategic blueprints for implementing these solutions at scale, offering healthcare organizations a clear path to industrializing AI-driven processes. Through these insights, healthcare institutions can use advanced AI technologies to create more efficient, intelligent workflows.

## Talent management
<a name="intro-talent-management"></a>

This guide also outlines strategies for re-skilling and empowering healthcare workers to seamlessly integrate generative AI into their daily routines. This can enhance both productivity and patient care quality. By equipping their workforce with the skills to effectively use advanced AI tools, healthcare organizations can maximize their return on investment and drive innovation in patient care.

This AI-powered [talent management solution](use-cases-talent-mgmt.md) includes the following key features:
+ **Intelligent talent resume parser** – By using the advanced LLMs available in Amazon Bedrock, this tool efficiently extracts and analyzes critical talent skills and attributes from resumes. This tool can streamline the recruitment process.
+ **Talent knowledge base** – Powered by Amazon Neptune, this dynamic database provides real-time insights into staffing levels, skill distribution, and industry trends. This helps you make data-driven decisions about workforce management.
+ **Learning recommendation engine** – This AI-driven tool identifies skill gaps within the organization and recommends personalized training programs for medical staff. This tool promotes continuous professional development and helps your workforce adapt to evolving healthcare technologies.

Together, these AI-driven features help optimize workforce performance, revolutionizing talent management with increased intelligence and efficiency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
