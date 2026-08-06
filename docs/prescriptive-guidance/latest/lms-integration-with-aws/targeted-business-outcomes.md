---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/lms-integration-with-aws/targeted-business-outcomes.html
---

# Integration options overview
<a name="targeted-business-outcomes"></a>

Multiple integration patterns exist for connecting AWS services with Learning Management Systems (LMS), each offering different advantages depending on your specific use case. Organizations should evaluate which approach (or combination of approaches) best meets their requirements by considering factors such as:
+ Technical complexity and available expertise
+ User experience requirements
+ Data flow needs
+ Existing LMS capabilities and constraints
+ Implementation timeframes and resources

Integration patterns generally fall into two broad categories:

1. **Front-end integration**: Focuses on an interactive experience for the LMS user

1. **Back-end integration**: Connects data and services between systems without user interaction

Depending on your learning objectives, technical landscape, and organizational needs, you may benefit from implementing one specific pattern or combining multiple approaches to create a comprehensive solution.

## Front-end integration approaches
<a name="2-1-front-end-integration-options"></a>

|
|
| Integration Approach | Description | Pros | Cons | Best For |
| --- |--- |--- |--- |--- |
| **Native LMS Plugin/Extension** | Custom code that extends LMS functionality directly within the platform's extension framework | + Deep LMS integration<br />+ Native user experience<br />+ Direct access to LMS data models | + LMS-specific development<br />+ Maintenance challenges with LMS version updates<br />+ Limited by LMS plugin architecture constraints | + Single LMS environments<br />+ Organizations with expertise in the specific LMS technology stack |
| **Learning Tools Interoperability (LTI)** | Standards-based integration that embeds external tools while maintaining interoperability across LMS platforms | + Cross-platform compatibility<br />+ Independent release cycles<br />+ Standardized authentication and data exchange | + Operates in iframe / separate context limiting some UX options<br />+ Requires implementing LTI standards | + Multi-LMS environments, vendors building tools for multiple institutions<br />+ Standardized deployments |

## Back-end integration approaches
<a name="untitled"></a>

The back-end integration approaches can be used in isolation or are often combined to achieve the best possible outcome.

|
|
| Integration Approach | Description | AWSServices | Best For |
| --- |--- |--- |--- |
| **API Integration** | Custom code running on AWS communicating with LMS services through APIs | + [AWS Lambda](https://aws.amazon.com/lambda/)<br />+ [Amazon EC2](https://aws.amazon.com/ec2/)<br />+ Containers | + Real-time data integration for external applications |
| **ETL/ELT Data Pipeline** | Batch data extraction and transformation for analytics | + [AWS Glue](https://aws.amazon.com/glue/)<br />+ [Amazon S3](https://aws.amazon.com/s3/)<br />+ [Amazon AppFlow](https://aws.amazon.com/appflow/) | + Analytics use cases<br />+ Reporting |
| **Event-Driven Architecture** | Event producers and consumers that react to changes in LMS or AWS systems | + [Amazon EventBridge](https://aws.amazon.com/eventbridge/)<br />+ [Amazon Simple Notification Service](https://aws.amazon.com/sns/)<br />+ [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) | + Near real-time requirements<br />+ Complex workflows |

## Use case mapping by integration option
<a name="use-case-mapping-by-integration-option"></a>

### Use Cases Requiring UI Integration
<a name="use-cases-requiring-ui-integration.228a5617-1ccb-53d9-8ef4-93f0059afab2"></a>

These are example scenarios that integrate directly with AWS services through the LMS interface:
+ **AI Writing Assistant**: LTI or plugin provides real-time writing feedback and suggestions using Amazon Bedrock foundation models.
+ **Interactive AI Tutor**: LTI or plugin with conversational interface using [Amazon Bedrock agents](https://aws.amazon.com/bedrock/agents/) to answer student questions about course content.
+ **Document Summarization Tool**: LTI tool that processes course documents with Amazon Bedrock to generate concise summaries and key points.
+ **Language Translation**: Plugin that translates course content into multiple languages using Amazon Bedrock.
+ **Quiz Generation**: LTI or plugin that creates assessments from course materials using [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) with course specific content.

### Use Cases Not Requiring UI Integration
<a name="use-cases-not-requiring-ui-integration.f8c327a6-cbfc-514a-8c47-6f4590c0fa50"></a>

These are example scenarios that typically leverage back-end integration patterns where users interact primarily with the LMS, while AWS services work behind the scene:
+ **Student Performance Analytics**: ETL pipeline extracts LMS data to AWS analytics services for comprehensive performance dashboards beyond native LMS capabilities.
+ **Automated Content Recommendations**: Event-driven architecture responds to student activities in the LMS to trigger personalised content recommendations using AI services.
+ **Predictive Learner Support**: machine learning (ML) models process LMS data via ETL to identify at-risk students before performance issues become critical.
+ **Automated Assignment Grading**: Integration processes submissions through Amazon Bedrock for objective assessment without UI changes.
+ **Knowledge Base Population:** Upload new course content to an Amazon Bedrock Knowledge Base to power Retrieval Augmented Generation (RAG) workloads such as chat applications and question generation.
