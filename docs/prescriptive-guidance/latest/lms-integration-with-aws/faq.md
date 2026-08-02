---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/faq.html
---

# Concrete generative AI example with Amazon Bedrock
<a name="faq"></a>

This section demonstrates practical implementation approaches for integrating Amazon Bedrock's generative AI capabilities with Learning Management Systems. The most appropriate pattern should be chosen based on the particular use case.

Amazon Bedrock is particularly valuable for LMS integration as it provides access to multiple foundation models, built-in RAG capabilities, and agent functionality without requiring machine learning expertise. Additionally, Amazon Bedrock offers comprehensive guardrails functionality that enables educational institutions to implement appropriate content filtering and moderation policies. These guardrails help ensure AI-generated content meets educational standards and institutional policies by managing toxicity, harmful content, and inappropriate responses—a critical consideration in educational environments.

These patterns demonstrate how to leverage these capabilities to enhance teaching and learning experiences while maintaining appropriate content safeguards.

## Pattern comparison
<a name="pattern-comparison.a9cca74b-330e-5aaf-bbcd-a61dd868446e"></a>

|
|
| **Pattern** | **Complexity** | **Use Cases** | **Implementation Time** | **Key Benefits** |
| --- |--- |--- |--- |--- |
| Direct Model Access | Low | Text transformationSummarizationTranslation | Days | Quick implementationFlexible integration points |
| Moodle AI Subsystem | Medium | Native Moodle integrationStandardized AI features | Days-Weeks | Native UIAdmin controlsPlatform integration |
| Knowledge Base Integration | Medium-High | Context-aware Q&ACourse-specific assistance | Weeks | Improved accuracy with course contextPersonalized responses |
| Agents Integration | High | Interactive tutoringComplex workflowsPersonalized support | Weeks-Months | Conversational experienceMulti-step task completion |

### Responsible AI
<a name="responsible-ai"></a>

When implementing generative AI capabilities within educational environments, institutions should consider:
+ Content Appropriateness: Implement appropriate guardrails to ensure AI-generated content is academically appropriate and aligns with institutional values.
+ Attribution and Academic Integrity: Define clear policies on how AI-generated content should be used in academic work and how it should be attributed.
+ Monitoring and Oversight: Establish processes to review AI interactions periodically to ensure quality and appropriateness.
+ Transparency: Clearly communicate to users when they are interacting with AI systems versus human instructors.
+ Bias Mitigation: Regularly review AI outputs for potential biases in educational content or assessment.
+ Usage Quotas and Cost Controls: Implement appropriate usage limits to manage costs while ensuring equitable access.

Implement the [recommendations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-transform-adm-operating-model-gen-ai/recommendations.html) from [Transforming application development and maintenance operating models on ](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-transform-adm-operating-model-gen-ai)AWS[ with generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-transform-adm-operating-model-gen-ai).

**Implementing Guardrails**: Utilize [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) to establish appropriate content boundaries. Configure guardrails to:
+ Filter inappropriate or harmful content in AI responses
+ Block specific topics that may be outside the educational context
+ Ensure responses align with institutional policies and educational objectives
+ Implement different guardrail configurations based on user roles (for example,, stricter controls for younger students)

### Direct model access
<a name="direct-model-access"></a>

The Direct Model Access pattern provides the simplest integration approach, connecting your LMS to [Amazon Bedrock ](https://aws.amazon.com/bedrock/guardrails/)foundation models. This pattern is ideal for straightforward text transformation tasks like summarization, translation, or explanation generation that don't require additional context beyond what's provided in the prompt.

In this section, we'll use Moodle as our example LMS platform to demonstrate the implementation, though the core concepts can be adapted to other LMS platforms with similar plugin architectures.

#### Use Cases
<a name="use-cases.951513b5-0984-5023-8b1c-d5366117582a"></a>
+ **Content Summarization**: Condensing lengthy course materials or student submissions
+ **Language Translation**: Translating course content to support multilingual learners
+ **Explanation Generation**: Creating simplified explanations of complex concepts
+ **Format Conversion**: Transforming content between different formats (for example, bullet points to paragraphs)

#### Architecture and Components
<a name="architecture-and-components.b04bc88c-3550-582f-95fb-cc6b03583bed"></a>

![Moodle plugin calls API Gateway, Lambda, and Amazon Bedrock for AI responses.](http://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/803d15f1-bcc9-4951-abe8-dded8f474b92.png)

[https://aws.amazon.com/bedrock/guardrails/](https://aws.amazon.com/bedrock/guardrails/)

*Figure 6: LMS Plugin Integration with *

 The Moodle plugin calls an API Gateway endpoint backed by a Lambda function. It makes a POST request to interact with the Bedrock service.

1. **Custom LMS Plugin Component**: Native extension to the LMS that provides the UI and handles user interaction.

1. **API Gateway**: Secure endpoint that receives requests from the plugin.

1. **AWS Lambda**: Processes requests, formats prompts for the model, and handles responses.

1. **Amazon Bedrock**: Provides access to foundation models like Claude or Amazon Nova.

#### User Flow Example
<a name="user-flow-example.8f4ce176-8071-5c44-a11c-169f7586abb8"></a>

The architecture follows this flow:

1. User selects text in the LMS and activates the plugin function (for example, "Summarize this")

1. Plugin sends the text to API Gateway with the requested operation

1. Lambda function formats an appropriate prompt for the selected operation

1. Amazon Bedrock processes the prompt and returns generated content

1. Lambda processes the response and returns it to the plugin

1. Plugin displays the results to the user within the LMS interface

#### Moodle Plugin Implementation Approach
<a name="moodle-plugin-implementation-approach.8325fea7-fabd-5466-8da5-a7ef2e90878b"></a>

Moodle plugins are extensions that allow institutions to extend Moodle's core functionality with customized features. For educational applications, these plugins can leverage Amazon Bedrock's generative AI capabilities to enhance teaching and learning experiences. To integrate Amazon Bedrock with Moodle, you can create a custom plugin based on the specific integration point you need. Moodle supports several plugin types that are well-suited for generative AI implementations:

|
|
| Plugin type | Description of plugin | Generative AI examples |
| --- |--- |--- |
| Block plugin | Small displays or tools that can be moved around pages | AI chatbot for Q&ADaily study recommendations |
| Editor plugin | Alternative text editors | AI writing assistantIn line content generation (for example, text, code) |
| Report plugin | Create reports for admins | Report generationSummarization |
| Search engine | Enhance search functionality (supports systems like Elasticsearch) | AI enabled semantic search |
| Assignment feedback plugin | Feedback to users about an assignment | AI generated feedback |

The choice of plugin type depends on your specific use case, where in the Moodle interface you want the AI functionality to appear, and how deeply you need to integrate with Moodle's core systems. For more details on plugin types, see [Moodle Plugin Types](https://moodledev.io/docs/5.1/apis/plugintypes#naming-conventions).

As Moodle is written in PHP, plugins must also be written using PHP. They allow for full control of functionality and customization. Each plugin requires a specific file structure that can vary depending on the plugin type.

A simple way to get started is using a block plugin as it offers a balance of visibility, flexibility, and implementation simplicity. Block plugins can be easily added to course pages and provide a dedicated interface for AI interactions without disrupting existing course components.

#### Implementation Considerations
<a name="implementation-considerations.05ead687-3055-515f-b34c-2c450b65f8ba"></a>
+ **Token Limits**: Manage content length to stay within model token limits
+ **Cost Management**: Implement usage tracking and quotas to control costs
+ **Error Handling**: Gracefully handle errors and provide feedback to users
+ **Prompt Engineering**: Create effective prompts that yield consistent, high-quality outputs
+ **User training**: Provide clear guidance on appropriate use and limitations

### Moodle AI subsystem
<a name="moodle-ai-subsystem"></a>

LMS providers are rapidly integrating AI technology into their platforms, such as the Blackboard Learn AI Design Assistant. This section focuses on how Moodle integrates with AI technology through its dedicated AI subsystem.

Moodle 4.5 introduced a dedicated AI subsystem. This new functionality provides the foundation for integrating a wide range of AI capabilities directly into the Moodle LMS. The AI subsystem is designed to be provider-agnostic, allowing Moodle sites to leverage any open source or commercial large language model (LLM) through customized provider plugins.

As of version 4.5, Moodle's AI subsystem does not support AWS and Amazon Bedrock out of the box. The underlying architecture is engineered to support future expansion, with additional provider integrations planned for upcoming Moodle versions. However, a custom plugin is available and can be downloaded to integrate Amazon Bedrock as a model provider for Moodle's AI subsystem. For installation instructions, see [the aiprovider\_bedrock plugin.](https://moodle.org/plugins/aiprovider_bedrock)

#### Use Cases
<a name="use-cases.dec70f1d-f2f1-5ad1-9481-37b540972628"></a>
+ **Text Summarization**: Summarize text content such as course content
+ **Image Generation**: Create images through AI
+ **Text Generation**: Generate text through AI

#### Architecture and Components
<a name="architecture-and-components.6e46faa3-9991-5ea5-af2d-956c01e7b3cd"></a>

![Moodle AI subsystem uses aiprovider_bedrock plugin to call Amazon Bedrock.](http://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/e1992f90-3ab5-4cd5-83a9-dc7a4898ea62.png)

*Figure 7: Moodle AI Subsystem Integration with Amazon Bedrock*
+ **Placements** define the specific areas within Moodle where AI-powered features can be accessed and utilized by users. For now, 2 placements are supported in Moodle core. For more information, see [AI placements](https://docs.moodle.org/405/en/AI_placements).
+ **Actions** represent the diverse range of AI functionalities made available, such as generating text, creating images, and summarizing course content. For more information, see [AI actions](https://moodledev.io/docs/4.5/apis/subsystems/ai#actions).
+ **Providers** are the external AI services that power these actions, with each provider plugin handling the necessary integrations and configurations.

Administrators can decide which actions and placements to enable for each provider. Placements and providers are considered as plugins by Moodle and can be modified and customized. For more information, see the AI Plugins [documentation](https://moodledev.io/docs/4.5/apis/plugintypes/ai).

The AI subsystem supports system and user level quotas to help manage LLM costs.

#### Implementation with Amazon Bedrock
<a name="implementation-with-amazon-bedrock.46527d86-9178-55b1-8c5d-2b8cc6508bc3"></a>

The [aiprovider\_bedrock ](https://moodle.org/plugins/aiprovider_bedrock)plugin allows Moodle administrators to:

1. Configure Amazon Bedrock as an AI provider in the Moodle AI subsystem

1. Select which models to use for different AI actions

1. Set permission controls for who can access AI features

1. Monitor usage and costs associated with AI functionality

This integration leverages Moodle's native AI framework while connecting to Amazon Bedrock's powerful foundation models, offering a standardized way to access generative AI capabilities across the Moodle platform.

### Knowledge base integration
<a name="knowledge-base-integration"></a>

The Knowledge Base Integration pattern enhances AI capabilities by incorporating course-specific content into responses, creating a more contextually aware educational assistant. This approach uses Amazon Bedrock Knowledge Bases to implement [Retrieval Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/), which enables the system to retrieve relevant information from course materials and incorporate that content into generated responses. The system can also provide citations to original course materials, helping students identify authoritative sources while maintaining academic integrity.

Unlike the direct model access approach, this pattern indexes course materials from the LMS into Amazon Bedrock Knowledge Bases, enabling more accurate and relevant responses tailored to specific courses and educational contexts.

#### Use Cases
<a name="use-cases.1b889d8d-8565-5ccf-9431-40052e1d3979"></a>
+ **Contextual Q&A**: Answer student questions using course-specific knowledge
+ **Enhanced Research Support**: Help students explore course literature with deeper context
+ **Content Discovery**: Help users find relevant materials across large course libraries
+ **Customized Learning Resources**: Generate additional learning materials based on course content

#### Architecture and Components
<a name="architecture-and-components.7b5c9584-6c6d-5bab-8f36-ae3ec92075cf"></a>

![Event-driven and scheduled paths sync LMS content to Bedrock Knowledge Bases.](http://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/3b61fa73-6bef-478b-9222-e21da6553e77.png)

*Figure 8: Moodle Integration with Amazon Bedrock Knowledge Bases*

#### Content Synchronization Flow
<a name="content-synchronization-flow.48c55784-58a9-5a4b-920d-6c7705402674"></a>

This flow ensures course materials from the LMS are accurately represented in the Knowledge Base:
+ **Event-Driven Path**:
  + LMS events are triggered by content updates when materials change
  + LMS events are forwarded to EventBridge in near real-time for processing
  + Ensures the knowledge repository is updated in near real-time
+ **Scheduled Path**:
  + Scheduled jobs periodically scan for new or updated content
  + Useful for LMS platforms with limited event capabilities or initial population of the Knowledge Base
  + Ensures comprehensive coverage even if events are missed
+ **Content Processing**:
  + Content is extracted directly from the LMS API
  + Amazon Bedrock Knowledge Bases will:
    + Extract the text from various file formats
    + Chunk the content for optimal retrieval
    + Pass the chunk though an embedding model to generate vectors representing the content
    + Allow metadata to be added for improved context retrieval
    + Ingest the content and vectors into the knowledge base

#### Query Processing Flow
<a name="query-processing-flow.90e34f9d-cc6b-5600-b896-5f54e1b45409"></a>

This flow occurs when users interact with the system to ask questions:
+ User submits a question through the LMS interface
+ Query is enriched with course context (course ID, module, user role)
+ Knowledge Base retrieves relevant content chunks from course materials based on the context
+ Foundation model generates a response using both the question and retrieved context
+ Response with citations is presented to the user

#### Implementation Considerations
<a name="implementation-considerations.fb455267-9793-5eca-8170-20f25abf7c0c"></a>
+ **Content Synchronization**: Establish processes for keeping the knowledge base updated with LMS content including updates and deletes
+ **Knowledge Organization**: Apply appropriate metadata attributes such as course ID, department, or topic to ingested content and implement metadata filtering in queries to improve relevance and scoping of retrievals
+ **Citation and Attribution**: Ensure generated responses include references to source materials
+ **Permission Management**: Apply appropriate access controls to respect content licensing and privacy
+ **Vector Store Optimization**: Consider chunking and embedding strategies for optimal retrieval

### Agents integration
<a name="agents-integration"></a>

The Agents integration leverages Amazon Bedrock Agents to create purposeful, interactive AI assistants that can perform complex tasks and workflows within the educational context, going beyond simple Q&A to provide more comprehensive support through structured agent capabilities.

#### Use Cases
<a name="use-cases.92cc3846-c61b-535f-9adf-54307f766bc6"></a>
+ **Learning Coach**: Agent that guides students through difficult concepts with personalized explanations
+ **Research Assistant**: Agent that can search, summarize, and synthesize academic resources
+ **Course Designer**: Agent that helps instructors create and refine course content
+ **Student Support**: Agent that leverages Knowledge Bases containing institutional FAQs, policies, and course resources to answer common questions and direct students to appropriate resources, combining retrieval-based responses with action capabilities to help students navigate support systems
+ **Assessment Helper**: Agent that provides feedback on drafts and helps with revisions

The example below uses an LTI for integration but this could also be an LMS plugin.

#### Architecture with AWS services
<a name="architecture-with-9999999999999999aws--services.b1d7ffeb-fbea-52c0-9a6a-9291ac9da274"></a>

![LTI tool invokes Amazon Bedrock Agents with knowledge base and action groups.](http://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/ada62d99-8a02-46d2-8731-6dd7ba93d9e8.png)

*Figure 9: Moodle Integration with Amazon Bedrock Agents*

 **Learning Management System**:
+ **LMS Embedded Agent Interface**: The component where users interact with the AI agent within the LMS
+ **LTI Launch Interface**: Handles the LTI protocol to securely launch the tool from the LMS
+ **LMS Core Functionality**: Native features and functions of the LMS
+ **LMS Content**: Course materials and educational data stored in the LMS
+ **LMS API**: Interface allowing external applications to interact with LMS data

**Other External Systems:**
+ **API: **Interface allowing external applications to interact. Examples include Student Information Systems and Enterprise Resource Planning

**AWS Cloud**:
+ **LTI Tool Frontend**: Web application rendered inside an iframe that provides the agent's interface
+ **API Gateway**: Secures and manages API requests between components
+ **Lambda**: Invokes the Amazon Bedrock agent
+ Amazon Bedrock **Agents**: Orchestrates interactions and determines which actions to perform
+ **Amazon Bedrock Knowledge Bases**: Stores and retrieves course-specific content for contextual responses
+ **AWS Lambda (Actions)**: Executes specific tasks requested by the agent, including queries back to the LMS API or other APIs

#### User Flow
<a name="user-flow.889faca9-8c64-544a-81e2-f895ce435aae"></a>

1. Student or instructor launches the AI assistant from within the LMS

1. LTI launches the assistant interface with appropriate context

1. User engages in conversation with the agent

1. Agent processes queries through Bedrock and performs actions as needed

1. Results are presented to the user in a conversational format

1. Session state is preserved for continued interaction

#### Implementation Considerations
<a name="implementation-considerations.828d4c9b-b7a2-5cc6-b15d-24731f77a251"></a>
+ **Agent Design**: Define clear action groups based on educational workflows
+ **Conversation Management**: Implement effective dialogue management strategies
+ **Integration with LMS Data**: Create secure methods for agents to access relevant LMS data
+ **User Permissions**: Apply role-based controls to agent capabilities
+ **Usage Monitoring**: Track interaction patterns to improve agent effectiveness
+ **Conversation History**: Manage conversation storage with appropriate privacy controls
