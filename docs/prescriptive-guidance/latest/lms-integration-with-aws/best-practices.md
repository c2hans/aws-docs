---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/best-practices.html
---

# Detailed integration architecture options
<a name="best-practices"></a>

This section provides architectural guidelines, implementation details, and best practices for each key integration option. Each pattern includes components, workflow, security considerations, and practical implementation guidance to help you design effective AWS-LMS integrations.

## LMS plugin integration
<a name="lms-plugin-integration"></a>

LMS Plugin Integration directly extends the LMS platform's functionality through its native extension framework, providing a seamless experience for users while leveraging AWS services for enhanced capabilities.

### Architecture and Components
<a name="architecture-and-components.69e97828-87fb-5b2f-905c-db0c6f960409"></a>

The LMS plugin integration architecture connects the Learning Management System with AWS services through a secure, scalable interface:

1. **LMS Environment**: Hosts the LMS platform and the custom plugin code within the LMS application server. This is where users interact with the plugin interface. It contains four interconnected components:
   + **LMS UI with Plugin UI**: The interface users interact with directly
   + **Custom LMS Plugin**: The extension code that adds AWS-powered capabilities
   + **LMS Core Functionality**: Native LMS features that the plugin interacts with
   + **LMS Content**: Educational materials and data accessed by the plugin

1. [Amazon API Gateway](https://aws.amazon.com/api-gateway/)**/**[** **AWS AppSync](https://aws.amazon.com/appsync/): Serves as the secure bridge between the LMS and AWS services by:
   + Receiving requests from the LMS plugin
   + Routing authenticated requests to appropriate backend services
   + Returning responses to the LMS environment

1. **Authentication Layer**: Secures API access through either:
   + [AWS Lambda Authorizer](https://aws.amazon.com/lambda/): Provides custom authorization logic for validating requests based on LMS context
   + AWS Identity and Access Management**: **A role associated with an EC2 instance or IAM access keys can be used to sign requests using [SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). IAM access keys are not recommended as they are long-term credentials.

1. **AWS services**: Backend services that provide the actual functionality, such as Amazon Bedrock for generative AI capabilities, Amazon S3 for content storage, and other AWS services as needed for specific use cases

![LMS plugin connects to AWS services through API Gateway and an authentication layer.](https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/e9283084-4f7f-43fa-b591-7e0a12d644d2.png)

*Figure 1: LMS Plugin Integration Pattern*

### User Flow
<a name="user-flow.09d6c3f2-4890-53c8-a7ea-742167a1653c"></a>

When a user interacts with the plugin in the LMS:

1. The plugin captures the user's input and relevant LMS context

1. The plugin sends an authenticated request to API Gateway

1. API Gateway authorizes the request using either a Lambda Authorizer or IAM

1. Upon successful authentication, the request is forwarded to appropriate AWS services

1. AWS services process the request and return results

1. Results flow back through API Gateway to the plugin

1. The plugin renders the results within the LMS interface

This architecture ensures secure communication between the LMS and AWS while maintaining a seamless user experience within the familiar LMS environment.

### Implementation Technologies
<a name="implementation-technologies.301982c2-24ce-5626-8759-0318480fa6dc"></a>

The plugin implementation depends on the LMS platform's technology stack:
+ **Moodle**: PHP with specific plugin structure requirements
+ **Blackboard**: Java/Spring and JavaScript adhering to Blackboard's Building Block API
+ **Canvas**: Does not support native plugins but recommends the use of LTI or Canvas APIs for integration

When developing plugins for any LMS platform, developers must:

1. Understand the specific LMS's plugin architecture and guidelines

1. Follow security best practices for the platform

1. Implement appropriate authentication and authorization mechanisms

1. Adhere to the platform's UI/UX guidelines

1. Consider performance implications and scalability

1. Maintain compatibility with LMS version updates

### Authentication and Security
<a name="authentication-and-security.f5849a7a-d631-521d-a793-bb19100d769a"></a>

When integrating AWSservices from an LMS plugin, the recommended approach is to use a proxy API integration: The plugin calls a custom API endpoint (for example, API Gateway) that acts as a proxy to the AWS services. Authentication and authorization are handled at the API layer. AWS service logic is isolated from the LMS environment. For this proxy API approach:
+ **API Authorization**: IAM roles, LMS token, IAM Access Key (if other options are not viable)
+ **Plugin Implementation**: The plugin makes HTTPS requests to your secured API endpoints
+ **Credential Protection**: If using long term credentials such as IAM Access Key these will need to appropriately stored and protected

This architecture creates a clear security boundary between the LMS and AWS environments. The LMS plugin only needs to know the API Gateway endpoint URL and appropriate authentication method for the API (such as IAM Role or OAuth token). Regardless of the specific integration approach, LMS plugin development requires careful consideration of security, performance, and maintainability. Proper authentication, authorization, and data protection mechanisms must be implemented to ensure the integrity of the overall system.

### Advantages
<a name="advantages.3d0d07eb-c586-541d-aa11-93cc2a4ed32c"></a>
+ **Tight UI/UX integration**: The plugin becomes part of the native LMS interface, providing a seamless experience for users who don't want to leave the LMS environment.
+ **Direct Access to the LMS Context**: Plugins have access to course context, user roles, and other LMS-specific data that external applications would need to request.
+ **Leverage Existing Authentication**: Can utilize the LMS's authentication and authorization mechanisms, simplifying security implementation.

### Limitations
<a name="limitations.482513db-1491-5fcc-9a60-db49338a5dd3"></a>
+ Requires plugin development expertise for each LMS
+ Must maintain compatibility with LMS version updates
+ Subject to LMS plugin architecture constraints
+ Requires separate implementations for each LMS platform

## Learning Tools Interoperability (LTI)
<a name="learning-tools-interoperability-lti"></a>

[Learning Tools Interoperability (LTI)](https://www.1edtech.org/standards/lti) is an education technology standard developed and maintained by 1EdTech (formerly IMS Global Learning Consortium). LTI enables third-party tools to integrate seamlessly with LMS platforms by providing a standardized way for external applications to authenticate with an LMS and exchange data. This standard ensures secure, efficient, and consistent interoperability between learning platforms and external educational tools. It allows any LTI compliant tool to plug into any compliant LMS.

Common LTI implementations include digital textbook launches, grade assessment tools, and interactive learning modules. These integrations work well for straightforward use cases where the need for data exchange is minimal and the interaction model is simple. Grade passback scenarios, such as quiz scores from external platforms or assignment completion status, also function adequately within LTI's constraints.

However, the integration of Generative AI tools presents even more demanding requirements. These systems need training data from student interactions, course content and materials, assessment responses and feedback, learning patterns and preferences, and cross-course correlations. They require real-time data processing, continuous learning and adaptation, deep content understanding, and the ability to handle complex interaction patterns – all of which exceed LTI's capabilities.

For modern educational technology needs, LTI often serves best as one component of a larger integration strategy. Many successful implementations use LTI for its strengths (secure launches, basic data passing, grade return) while supplementing it with additional integration methods for more complex requirements.

### Architecture and Components
<a name="architecture-and-components.4edeceac-65e5-5271-a295-d5bc6ea4739a"></a>

The LTI integration architecture consists of:

1. **LMS Environment**: Any LTI-compliant LMS ( for example Moodle, Canvas, Blackboard)
   + **LMS UI with iFrame Container**: The standard LMS interface where the LTI tool will appear embedded
   + **LTI Launch Interface**: Handles the LTI launch process and OAuth-based security protocol
   + **LMS Core Functionality**: Native features of the LMS that the LTI tool might interact with
   + **LMS Content**: Course materials and data that might be accessed by the LTI tool

1. **LTI Tool Application**: A web application hosted on AWS that implements the LTI standard
   + **LTI Tool Frontend**: Web application hosted on AWS that renders inside the iFrame container
   + **LTI Tool Backend**: Server-side component that processes requests and business logic

1. **AWS Services Layer**: Backend AWS services providing enhanced functionality such as Amazon Bedrock

The LTI standard enables secure communication between the LMS and the AWS-hosted tool while maintaining separation between the systems. This provides flexibility for the tool's development while ensuring secure data exchange with the LMS environment.

![LTI tool frontend renders in an iframe, with backend connecting to AWS services.](https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/87b4ef0c-351c-448a-af0a-17e28b6e5cd7.png)

*Figure 2: LTI Integration Pattern*

### User Flow
<a name="user-flow.e6537608-5bc7-5a59-a2bf-5ec1ac1ea27b"></a>

When a user interacts with the LTI plugin in the LMS:

1. The LMS and the LTI tool perform a handshake process that enables the exchange of information.

1. Upon success, the LTI tool is displayed inside an iFrame on the LMS.

1. The tool makes authenticated calls to an AWS backend.

1. The tool returns the requested information.

1. Alternatively, the tool can also pass information back to the LMS.

### Implementation Technologies
<a name="implementation-technologies.26e7d9f8-b94e-5b59-ac65-027ad4e0cbee"></a>
+ **Frontend**: Any modern web framework can be used (React, Vue, Angular)
+ **Backend**: Node.js, Python, or other web technologies with LTI library support
+ **LTI Version**: Preferably LTI 1.3 with LTI Advantage features for enhanced capabilities
+ **Hosting**: Commonly deployed as a containerized application on [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) / [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) or as a serverless application using API Gateway and Lambda

### Authentication and Security
<a name="authentication-and-security.b8077b10-528b-5f9d-b10c-707f6e20a42d"></a>

LTI implements a secure authentication mechanism based on OAuth 2.0:

1. User clicks an LTI tool link within the LMS

1. LMS generates a signed JSON Web Token (JWT) containing user context and launch parameters

1. User is redirected to the LTI tool with the JWT

1. LTI tool validates the JWT signature using the LMS's public key

1. Tool creates a session and displays the appropriate content

1. AWS services are accessed by the LTI application's backend using IAM roles

This approach keeps AWS credentials entirely separate from the LMS environment, improving security posture.

### Advantages
<a name="advantages.c31b47fe-774b-5a06-8aad-ebc0d45c5f79"></a>
+ Cross-platform compatibility across LMS environments (Moodle, Canvas, Blackboard, etc.)
+ Independent development and release cycles
+ Standardised authentication and data exchange
+ Portable across institutions and departments

### Limitations
<a name="limitations.369a25c0-5cc3-5a58-9f2b-f2bdbd41b228"></a>
+ Functions within iframe/separate context, limiting some UX options
+ Requires implementing and maintaining LTI standards compliance
+ More complex authentication flow than direct plugin integration
+ Might have limited access to certain LMS features

## Standalone application with API integration
<a name="standalone-application-with-api-integration"></a>

This pattern involves developing a standalone application that interfaces with the LMS through its APIs. While operating independently, the application can both read from and write data to the LMS as needed. This integration approach is particularly valuable when LMS data needs to be accessed by external systems. For instance, when creating analytics solutions for student engagement or developing dashboards for non-LMS users (such as registrar office staff or deans), a separate application might be more appropriate than trying to extend the LMS itself. This allows for specialized tools tailored to these specific user groups' needs.

### Architecture and Components
<a name="architecture-and-components.76796080-f559-5f99-89b8-c61fce65899c"></a>

1. **Standalone Web/Mobile Application**:
   + **LMS API**: The interface exposed by the LMS that allows external applications to read and write data
   + **LMS Core Functionality**: Native features and functions of the LMS
   + **LMS Content**: Course Materials, user, data, and other educational content stored in the LMS

1. **AWS Cloud:**
   + **LMS API Client**: Component that handles pull/push API calls to communicate with the LMS API
   + **Application Frontend**: User interface layer that users interact with directly
   + **Application Backend**: Server-side components that processes business logic
   + **AWS Services**: Backend services that provide specialized functionality such as Amazon S3 or Amazon Bedrock.

![Standalone application uses an API client to bridge LMS and AWS services.](https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/8d893af4-720f-41a3-9413-c039a36aa7b6.png)

*Figure 3: Standalone API Integration Pattern*

### User Flow
<a name="user-flow.f4202d87-f257-5e64-800e-5d887d219d9b"></a>

1. User authenticates with the standalone application

1. Application authenticates with LMS using OAuth 2.0 or API keys

1. Application retrieves or updates necessary data from LMS API

1. User interacts with application features that leverage the retrieved data and AWS services

1. AWS-processed results are displayed to user and optionally saved back to LMS

### Implementation Technologies
<a name="implementation-technologies.0566edda-b5e4-58a6-9dea-971b583a52d0"></a>
+ **Application Hosting**: [Amplify](https://aws.amazon.com/amplify/), [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), or container services
+ **Authentication**: OAuth2, LMS Access Key
+ **LMS Communication**: Software Development Kits (SDKs) or REST client libraries for the specific LMS

### Authentication and Security
<a name="authentication-and-security.6303ea5c-23a3-5962-add2-9c24f92d9c22"></a>

When authenticated against the LMS API most platform use either OAuth 2.0 or other tokens to authenticate the request from the application.

### Advantages
<a name="advantages.12825441-276f-5631-b595-7e207ef8aae0"></a>
+ Complete flexibility in application design and user experience
+ Independent deployment and scaling from the LMS
+ Full control over the technology stack

### Limitations
<a name="limitations.2f86d242-e9ed-5ef9-bbdd-8484c8b79600"></a>
+ Limited by available LMS API capabilities
+ Might require ongoing updates as LMS APIs evolve
+ Additional complexity in maintaining data consistency
+ Many requests to the LMS API might have a negative impact on LMS system performance so rate limiting should be implemented
+ Tight coupling between systems, patterns such as messaging, API Gateways or facades can limit this

## Event-driven integration
<a name="event-driven-integration"></a>

Event-driven integration leverages the LMS' event system to trigger actions in AWS services based on user activities or system changes within the LMS.

### Architecture and Components
<a name="architecture-and-components.2de0ec08-5cc7-5a30-829d-832bae472723"></a>

1. **LMS Environment**: Hosts the LMS platform and the custom plugin code within the LMS application servers. This is where users interact with the LMS to generate events. It contains three interconnected components:
   + **Custom LMS Plugin: **Extension code that is invoked for each event raised and passes the event to Amazon EventBridge or publishes to the stream
   + **LMS Core Functionality**: Native LMS features that the user interacts with creating LMS Events
   + **LMS Content**: Educational materials and data created and accessed by the users

1. **EventBridge / Streaming**: Receives the events from the LMS Plugin and either triggers rules to invoke downstream services when the event matches a defined pattern, or processes records in the stream to invoke appropriate AWS services. Streaming services can be [Amazon Kinesis Data Streams](https://aws.amazon.com/pm/kinesis/)or [Amazon Managed Streaming for Apache Kafka.](https://aws.amazon.com/msk)

1. **AWS Services**: Backend services that provide the actual functionality, such as Lambda for executing custom code.

![LMS plugin forwards events to Amazon EventBridge or Kinesis for AWS processing.](https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/696c70a0-a251-4d8c-83d1-b5f496b32394.png)

*Figure 4: Event-Driven Integration Pattern*

### System Flow
<a name="system-flow.eb2bfaf3-2f9c-55e4-a096-852283369206"></a>

When an event occurs in the LMS, the following process takes place:

1. LMS captures the event in its Events subsystem

1. Custom LMS Plugin observes each created event

1. The plugin sends an authenticated request to EventBridge or streaming service with the event payload

1. AWS API validates the request using IAM

1. Upon successful authentication, the request is added to an EventBridge event bus or stream

1. A rule receives incoming events and routes them to appropriate AWS services based on matching event patterns or records are processed off the stream and processed by the consumer.

This architecture ensures secure communication between the LMS and AWS services allowing LMS platform capabilities to be extended with AWS services.

### Implementation Technologies
<a name="implementation-technologies.75be0a7c-9fbd-5f90-a7c8-244d1d391cb2"></a>

The LMS plugin implementation depends on the platform's technology stack, for example:
+ **Moodle**: [The Moodle Events API](https://docs.moodle.org/dev/Events_API) can be used with a [local plugin](https://moodledev.io/docs/4.5/apis/plugintypes/local) to send the events to EventBridge.
+ **Canvas**: [Canvas Live Events ](https://developerdocs.instructure.com/services/canvas/data-services/live-events/overview/file.data_service_introduction)can be published to Amazon SQS so AWS services can pull the messages or can be invoked via a Lambda function. Using a Lambda function to write the events on the Amazon SQS queue to EventBridgemight still be useful to decouple the subscribers.
+ **Blackboard Learn**: [Learn Activity Streams ](https://docs.anthology.com/docs/blackboard/caliper/getting-started)are an implementation of the [Caliper Specification](https://www.1edtech.org/standards/caliper) which enables the collection of learning data in a standardized way. The events are sent to a Caliper Event Store which can be used to invoke AWS services.

The plugin implementation must adhere to the LMS's plugin development guidelines and APIs. This often involves:
+ Implementing specific plugin lifecycle methods and configuration pages
+ Accessing LMS data through provided APIs, data access patterns and security practices.

### Authentication and Security
<a name="authentication-and-security.48fa1b75-cf69-52a2-81c2-d6dd44d051a8"></a>

When integrating with AWS, three primary authentication methods exist:

1. IAM **Role (Preferred Method):**
   + Attach a role to EC2 instances or container if the LMS is running on AWS
   + Provides temporary, secure credentials for AWS API calls
   + Eliminates need to store long-term access keys in configuration

1. [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)** (Recommended for Non-AWS Hosted Moodle):**
   + Uses X.509 certificates to obtain temporary AWS credentials for workloads running outside AWS
   + Provides temporary credentials without long-lived access keys
   + Requires attaching an appropriate IAM policy to your [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) role
   + See [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)for setup instructions

1. **AWS Access Key (Alternative Method):**
   + Use when an IAM Role cannot be assumed
   + Requires careful security management
   + Long-term credentials that must be manually rotated

AWS SDK support these methods.

### Advantages
<a name="advantages.e08d20b9-4538-50e3-b56a-61bdde264544"></a>
+ Access to broad range of AWS capabilities
+ Enhanced scalability
+ System decoupling
+ Near real-time updates
+ Improved reliability as events / stream records can be persisted and replayed
+ Independent development and release cycles
+ Flexibility in development language

### Limitations
<a name="limitations.6f0381ab-05b5-5868-8bb0-f3416b6dd583"></a>
+ Unable to integrate with LMS user interface
+ Callbacks to the LMS from downstream services might cause unintended system load

## ETL integration
<a name="etl-integration"></a>

ETL (Extract, Transform, Load) integration focuses on batch processing of LMS data for analytics, reporting, and other data-intensive use cases.

### Architecture and Components
<a name="architecture-and-components.f6e0b24f-f012-512b-aba9-fdb47f00aca7"></a>

1. **Learning Management System**:
   + **LMS API**: The interface exposed by the LMS that provides access to educational data
   + **LMS Core Functionality**: Native features and functions of the LMS
   + **LMS Content**: Course materials, user data, and other educational content stored in the LMS

1. **AWS Cloud**:
   + **Scheduled Extraction**: Time-based trigger that initiates the ETL process
   + **AWS Glue ETL Jobs**: Service that extracts data from the LMS API, transforms it, and loads it into storage
   + **Amazon S3 (data lake)**: Storage repository for processed educational data
   + **AWS** **Analytics Services**: Tools for analyzing and visualizing the processed data
   + **AWS Lambda**: Function that can process data or write results back to the LMS (indicated by dotted lines)

![Scheduled ETL extracts LMS data via AWS Glue into S3 for analytics services.](https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/images/guide-img/0295b1b3-2981-4c83-b66b-d5ae2700aca8/images/55a1da6d-f3f7-4b54-94ea-3c5b9f67289b.png)

*Figure 5: ETL Pipeline Integration Pattern*

### System Flow Example
<a name="system-flow-example.a3ceb252-0a36-5edb-853c-783f57a5d17f"></a>

1. **Scheduled Extraction** triggers **AWS Glue ETL Jobs** at predetermined intervals

1. **AWS Glue ETL Jobs** connect to the **LMS API** to extract data

1. Extracted data is transformed and loaded into **Amazon S3 (data lake)**

1. **AWS Analytics Services** access the data lake to perform analysis

1. Optionally, insights and processed data can be fed back to the LMS via **AWS Lambda** functions (shown by dotted lines)

### Implementation Technologies
<a name="implementation-technologies.5c6fabf8-1cbf-55f6-88b4-e3c51e1248c6"></a>
+ **ETL Processing**: AWS Glue for serverless data integration
+ **Data Storage**: Amazon S3 for the data lake architecture
+ **Analytics**: Amazon Athena for SQL queries, Amazon Quick Sight for visualization
+ **Scheduling**: Amazon EventBridge or AWS Glue triggers for triggering extraction on schedule
+ **Optional Processing**: AWS Lambda for additional transformations or writing data back to LMS

### Authentication and Security
<a name="authentication-and-security.6303ea5c-23a3-5962-add2-9c24f92d9c22"></a>

When authenticated against the LMS API most platform use either OAuth 2.0 or other tokens to authenticate the request from the application.

### Advantages
<a name="advantages.433fea6d-45ae-5675-8653-9b213bde0ad4"></a>
+ Allows LMS data to be processed and visualized using modern analytics and AI tools
+ Design for scalable extraction of potentially large datasets

### Limitations
<a name="limitations.e30b0216-ab34-5531-8b0b-6648f429331e"></a>
+ Full extractions might lead to excessive system load, investigate change data capture mechanisms or consider a separate LMS instance for extraction
+ Extraction during core hours might impact user performance
+ Additional data governance required to address privacy and compliance requirements outside of the LMS

The following AWS Workshops are useful for exploring ETL based integration in more detail:
+ [Higher Education Data Lake Immersion Day](https://catalog.workshops.aws/dataedu-student-datalake/en-US)
+ [Amazon SageMaker Unified Studio Workshop - Improve Student Engagement](https://catalog.us-east-1.prod.workshops.aws/workshops/1e711c46-2bda-4c72-9f62-fde6347800f8/en-US)
