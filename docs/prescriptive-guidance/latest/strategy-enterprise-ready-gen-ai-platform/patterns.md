---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/patterns.html
---

# Layer 4: Repeatable application patterns for common generative AI use cases
<a name="patterns"></a>

As enterprises adopt generative AI, clear patterns have emerged for how organizations are using this technology to drive business value. These common use cases demonstrate proven approaches to applying generative AI across different business functions. These use cases can help organizations identify and prioritize their own implementation opportunities.

By understanding these established use cases, organizations can better evaluate where generative AI can deliver the most immediate impact while building a foundation for broader adoption. This section describes key areas where enterprises are successfully deploying generative AI solutions.

**This section contains the following topics:**
+ [Generative AI-powered assistants](#patterns-assistants)
+ [RAG chat-based assistants](#patterns-chat)
+ [Generative AI agents](#patterns-agents)
+ [Intelligent document processing](#patterns-idp)
+ [Content generation and summarization](#patterns-content)
+ [Code generation and analysis](#patterns-code)
+ [Multimodal AI applications](#patterns-multimodal-apps)
+ [Implementation recommendations](#patterns-implementation-recs)

## Generative AI-powered assistants
<a name="patterns-assistants"></a>

Generative AI-powered assistants offer personalized, context-aware support across various business functions. These are tools are ideal for power users. They supercharge the output of those employees who learn to integrate them into their workflow. By using language models, these assistants enhance efficiency, productivity, and user satisfaction across organizations.

AWS offers [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html), an enterprise-grade AI assistant that's ready to use and highly customizable. Implementation involves tailoring its knowledge base with organization-specific data to drive accurate, relevant responses. Integration with customer relationship management (CRM) and enterprise resource planning (ERP) systems enhances its utility and promotes smooth data flow and full functionality across the enterprise.

For software development teams, AWS provides [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html). This coding assistant is designed to boost productivity by assisting with code generation, bug detection, refactoring suggestions, and documentation creation. When integrated seamlessly into integrated development environments (IDEs), developers can access its features directly within their usual coding environment, which streamlines workflows and reduces context switching. For more information, see [Code generation and analysis](#patterns-code) in this strategy document.

Common use cases for generative AI-powered assistants include the following:
+ Executive assistants that support schedule management, report summarization, and brief preparation.
+ HR assistants that support employee onboarding, answer policy-related questions, and help with performance management.
+ Sales enablement tools that deliver real-time product information and competitive insights.

To maximize the effectiveness of generative AI-powered assistants, consider starting with a targeted deployment, such as within a specific department. This helps development teams to evaluate the impact and gather user feedback before rolling it out more broadly across the organization. This phased approach smooths the adoption process and optimizes the assistant's alignment with enterprise needs.

For more information about building enterprise generative AI-powered assistants, see [Develop a fully automated chat-based assistant using Amazon Bedrock agents and knowledge bases](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases.html).

## RAG chat-based assistants
<a name="patterns-chat"></a>

Out-of-the-box foundation models, while powerful, are constrained by their pretraining data. They lack knowledge of recent events beyond their training cutoff date and have no understanding of company-specific processes or custom data. This limitation makes them unsuitable for many business use cases that require knowledge of the organization.

Customizing models through fine-tuning is a complex and expensive process, and collecting high-quality training data for it can be a challenge. Retrieval Augmented Generation (RAG) addresses these limitations by combining large language models (LLMs) with an organization's proprietary data. RAG approaches create AI-powered interactions that are informed by specific domain knowledge. For more information about RAG and fine-tuning, see [Generative AI options for querying custom documents](https://docs.aws.amazon.com/en_us/prescriptive-guidance/latest/retrieval-augmented-generation-options/options.html).

Common use cases for RAG chat-based assistants include the following:
+ Customer support systems that have access to product documentation and FAQs
+ Internal knowledge management tools that quickly retrieve company-specific information
+ Legal or compliance chat-based assistants that reference organizational policies and regulations

AWS simplifies the implementation of RAG chat-based assistants through [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html). This service helps you set up a vector database to query and retrieve data from custom documents. Key features include integration with Amazon Simple Storage Service (Amazon S3) for data storage, compatibility with third-party services (such as Microsoft SharePoint and Atlassian Confluence), efficient vector search capabilities for relevant document retrieval, and integration with foundation models (such as Anthropic Claude) for building conversational chat-based assistants. To begin, identify a well-defined, limited-scope knowledge base and use it to create a proof-of-concept RAG chat-based assistant. As implementations scale, pay attention to data freshness and the computational costs of large-scale retrieval operations.

For more information about building RAG chat-based assistants, see the following:
+ [Retrieval Augmented Generation options and architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html)
+ [Deploy a RAG use case on AWS by using Terraform and Amazon Bedrock](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-rag-use-case-on-aws.html)
+ [Develop advanced generative AI chat-based assistants by using RAG and ReAct prompting](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting.html)

## Generative AI agents
<a name="patterns-agents"></a>

Generative AI agents represent a significant advancement in automating complex business processes. These agents can handle sophisticated workflows that traditionally required human intervention by breaking down tasks and interacting with various systems.

Typical applications of generative AI agents include automated workflow orchestration for multi-step business processes, intelligent virtual assistants for cross-departmental task completion, and data analysis and report generation agents that can query multiple databases.

AWS provides tools, such as [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), to help you create and deploy AI agents. Implementation involves defining custom actions and API integrations that are specific to your business needs. You also need to set up robust error handling and logging mechanisms. You can use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) for serverless function execution, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to manage APIs, and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for workflow orchestration.

Organizations can start by identifying a repetitive, multi-step process and mapping out its decision points and system interactions. This serves as a blueprint for the initial generative AI agent. Key considerations include validating proper error handling and maintaining transparency in decision-making processes.

## Intelligent document processing
<a name="patterns-idp"></a>

*Intelligent document processing (IDP) *uses generative AI and natural language processing (NLP) to automatically extract, classify, and process information from various types of documents. IDP can transform unstructured document processing into automated, scalable workflows.

Modern IDP solutions can take two approaches: traditional, pipeline-based processing or direct, multimodal processing through foundation models. To build a traditional pipeline on AWS, you can combine [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) for optical character recognition (OCR) and document understanding with [Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html) for advanced analysis. Alternatively, for direct, multimodal processing through foundation models, you can use state-of-the-art foundation models (such as Anthropic Claude in Amazon Bedrock) to directly process images, PDFs, and scanned documents in a single step.

Organizations can choose their approach based on their specific needs. Traditional pipelines excel in high-volume processing and scenarios that require fine-grained control. Direct, multimodal processing through foundation models is ideal for complex documents that require improved accuracy through sophisticated contextual understanding.

Common use cases for IDP include the following:
+ Claims processing that automates insurance claim document review, validation, and data extraction.
+ Invoice processing that extracts line items, totals, and vendor information for accounts payable automation.
+ Contract analysis that reviews legal documents in order to extract key terms, obligations, and expiration dates.
+ Medical record processing that analyzes patient records to extract relevant medical information and coding.

Implementation typically uses event-driven architectures that use Amazon S3, AWS Lambda, and Amazon Simple Queue Service (Amazon SQS). When you upload a document to an Amazon S3 bucket, it initiates processing workflows. Results are stored in databases, such as Amazon DynamoDB, or ingested into business systems through APIs. For optimal results, organizations should implement batching strategies, robust error handling, and audit trails. Start with a specific document type before expanding the scope.

This automation significantly reduces manual intervention, processing time, and human error. It also helps staff to focus on activities that require judgment and expertise.

For more information about document processing workflows, see [Automatically extract content from PDF files using Amazon Textract](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-extract-content-from-pdf-files-using-amazon-textract.html).

## Content generation and summarization
<a name="patterns-content"></a>

Generative AI models excel at generating and summarizing content. This makes them valuable tools for various business applications. You can use the natural language processing capabilities of large language models to create or condense text-based information.

Common use cases for content generation and summarization include the following:
+ Automated report generation from structured data
+ Content creation for marketing materials, product descriptions, and social media posts
+ Document summarization for research papers, legal documents, or lengthy reports

Implementation on AWS typically involves using Amazon Bedrock for text generation and summarization tasks. Amazon Comprehend can be employed for entity recognition and sentiment analysis, enhancing the context and quality of generated content.

Best practices for content generation and summarization applications include implementing human-in-the-loop processes for content review and quality control, using fine-tuned models for domain-specific content generation, and implementing content filters to ensure brand consistency and adherence to guidelines.

For example, you can use generative AI to analyze patient clinical data and generate summaries and clinical notes. For more information, see [Building a medical intelligence application with augmented patient data](https://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/case-1.html).

## Code generation and analysis
<a name="patterns-code"></a>

Generative AI models have remarkable capabilities to understand and generate code across various programming languages. Your developers can use these capabilities to assist write, refactor, and analyze code.

Common use cases include the following:
+ Automated code generation for boilerplate tasks
+ Code refactoring and optimization suggestions
+ Bug detection and security vulnerability analysis

AWS offers several services to help support this pattern. [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) provides AI-assisted code generation, helping developers write code faster and with fewer errors. [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/) offers intelligent code reviews and performance recommendations. You can integrate these services with AWS Lambda for serverless code execution and testing.

Best practices for code generation and analysis applications include integrating AI-assisted coding tools into existing development environments. Consider implementing strict code review processes to make sure that generated code meets quality standards. Use AI for initial code drafts but rely on human expertise for final implementation decisions.

For more information about building coding assistants, see [Use Amazon Q Developer as a coding assistant to increase your productivity](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-q-developer-as-coding-assistant-to-increase-productivity.html).

## Multimodal AI applications
<a name="patterns-multimodal-apps"></a>

Multimodal AI applications combine different types of data inputs and outputs, such as text, images, audio, and video. This pattern uses the ability of advanced generative AI models to understand and generate content across multiple modalities.

Common use cases for multimodal AI applications include the following:
+ Visual question-answering systems for customer support or internal documentation
+ Intelligent image and video content moderation
+ Multimodal data analysis for business intelligence

On AWS, you can use Amazon Bedrock for multimodal foundation models. Additional services include [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) for image and video analysis, [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) for speech-to-text conversion, and [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) for text-to-speech conversion. These services can enhance the multimodal capabilities of the application.

Best practices for multimodal AI applications include ensuring high-quality, diverse datasets for training and fine-tuning multimodal models. Also, implement robust error handling for different input modalities, and carefully consider the ethical implications and potential biases in multimodal AI systems.

For more information about building multimodal applications, see [Document institutional knowledge from voice inputs by using Amazon Bedrock and Amazon Transcribe](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/document-institutional-knowledge-from-voice-inputs-by-using-amazon-bedrock-and-amazon-transcribe.html).

## Implementation recommendations
<a name="patterns-implementation-recs"></a>

To effectively implement repeatable application patterns for generative AI across your organization, consider the following recommendations:
+ Begin with a pattern catalog that documents successful implementations and provides templates, reference architectures, and code samples that accelerate development.
+ Establish a centralized pattern governance process to evaluate, approve, and maintain standard patterns in order to promote consistency and quality across the enterprise.
+ Prioritize use cases based on business impact, technical feasibility, and alignment with strategic objectives.
+ Create a cross-functional pattern development team that includes AI specialists, domain experts, and end users who can make sure that patterns address real business needs.
+ Implement a "build once, reuse many times" approach by creating modular, composable components that can be assembled into different application patterns.
+ Develop clear evaluation criteria for each pattern type in order to measure effectiveness. Include metrics for business value, user satisfaction, and technical performance.
+ Establish a pattern maturity model that classifies patterns as experimental, proven, or enterprise-standard to guide teams in their selection process.
+ Create comprehensive documentation that promotes successful adoption for each pattern, including implementation guides, limitations, and best practices.
+ Conduct regular pattern reviews to identify opportunities for improvement, consolidation, or retirement as technology and business needs evolve.
