---
source_url: https://docs.aws.amazon.com/solutions/a-media-lake-on-aws/index.html
---

---
title: 'Guidance for a Media Lake on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/a-media-lake-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for a Media Lake on AWS

## Overview

This Guidance demonstrates how to deploy a media lake, which addresses media management challenges for organizations of all sizes using AWS services and partner integrations. It shows how to create a centralized system for managing digital media assets throughout their lifecycle, featuring automated and manual media workflows, global namespace organization, and advanced metadata management. The Guidance helps implement human-in-the-loop review capabilities and a unified media, archive, and metadata data catalog that connects through API and user interface layers. By following this Guidance, organizations can optimize processing times, reduce costs, and enhance content monetization.

## Benefits

### Accelerate decision-making for digital media assets

Automate metadata enrichment, intelligent search, and proxy generation for efficient asset discovery, repurposing, and monetization while reducing costs. Optimize content lifecycle management, speed up approval cycles, and enhance workflow efficiency.

### Reduce production workflow complexity

Streamline media operations with customizable, event-driven pipelines and automated quality controls such as similarity detection. Eliminate manual handoffs while maintaining creative oversight through human-in-the-loop review capabilities.

### Streamline media processing workflows

Accelerate content delivery with configurable pipelines that combine automated processing and controlled review stages while maintaining quality standards through structured approval processes.

## How it works

### Overview

This architecture diagram provides a functional overview of the capabilities of a media lake on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/a-media-lake-on-aws.pdf)Step 1Upload new media files to Amazon Simple Storage Service (Amazon S3). Upload triggers an event to initiate processing.Step 2AWS Lambda, Amazon Simple Queue Service (Amazon SQS), and Amazon EventBridge coordinate the flow of events after ingestion. Lambda functions handle initial processing, and EventBridge routes events to transformation, enrichment, and pipeline components.Step 3Search features support semantic and keyword search in addition to filtering of indexed assets.Step 4Organization logic groups related assets using metadata or similarity scoring. A storage browser is used to explore assets in the connector.Step 5Media transformation creates proxies, thumbnails, or derivative assets when triggered.Step 6Metadata management extracts technical- and user-defined metadata to support powerful search and discovery.Step 7Default or custom pipelines coordinate analysis, enrichment, and transformation using AWS and partner services.Step 8RESTful APIs enable integration with external systems, allowing ingestion, search, and asset retrieval.Step 9Lambda and EventBridge coordinate the execution of custom analysis and transformation pipelines, accessing credentials in AWS Secrets Manager enabling secure workflows.Step 10Amazon S3, Amazon API Gateway, Lambda, Amazon OpenSearch Service, Amazon DynamoDB, EventBridge, Amazon SQS, Amazon Bedrock AgentCore, Amazon CloudWatch, and AWS X-Ray power the media lake functions.### High-level application architecture

This architecture diagram shows the high-level API, storage, and back-end architecture of a media lake on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/a-media-lake-on-aws.pdf)Step 1Operators access the media lake user interface through Amazon CloudFront with protection provided by AWS Web Application Firewall (WAF). CloudFront serves the static web application from Amazon S3.Step 2Amazon Cognito performs user authentication with authorization managed through Amazon Verified Permissions.Step 3API Gateway routes authenticated requests, which are processed by Lambda functions that invoke backend services as needed.Step 4Lambda queries OpenSearch Service to return search and retrieval results. Amazon DynamoDB manages asset and service metadata.Step 5EventBridge receives internal events from the media lake through its API layer and pipeline layer, powering downstream processes such as pipeline execution, audit logging, and compliance tracking.Step 6Amazon S3 buckets are used to store media files and assets, host infrastructure as code packages, and templates used for translation pipelines.Step 7EventBridge triggers pipelines upon receiving events. These pipelines pull media from Amazon S3, metadata from Amazon DynamoDB, and credentials from Secrets Manager. Lambda functions carry out operations such as proxy generation, embedding generation, and media enrichment, all orchestrated through Step Functions.Step 8Amazon Bedrock AgentCore hosts and runs the coordinator agent. Users interact with the agent using natural language requests, such as, "Provide a summary of what's in this video" through the media lake's user interface. The coordinator agent connects with specialized agents to process these requests. Specialized agents use agent tools to interact with services to accomplish the user request.### Pipeline execution and deployment

This architecture diagram shows the deployment and execution of pipelines used in a media lake to process media and produce metadata to aid search and render new versions for use with downstream systems.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/a-media-lake-on-aws.pdf)Step 1Users define media processing workflows, through a no-code drag-and-drop canvas, save them, and deploy them as pipelines.Step 2User creates a pipeline by sending request to AWS Step Functions.Step 3Amazon S3 generates event notifications when new media is uploaded, which are copied and sent to the media lake analysis event bus. to the internal Media Lake event bus.Step 4The media lake creates EventBridge event rules that trigger pipelines based on new asset events or the completion of previous pipelines.Step 5Amazon SQS queues incoming events, allowing them to be buffered and processed asynchronously.Step 6Lambda handles events from the queue and triggers the Step Functions that represent deployed pipelines.Step 7Step Functions define each pipeline as an individual state machine, executing the logic configured in the canvas.Step 8Step Functions enable pipelines to integrate with AWS services, AWS internal software vendor (ISV) partners, or third-party systems as needed.Step 9Step Functions coordinates the entire pipeline, reading media from Amazon S3, invoking Lambda (monitored through CloudWatch and X-Ray) to extract metadata and write it to DynamoDB, and finally, using AWS Elemental MediaConvert to generate proxies. It then stores outputs back in Amazon S3. Amazon Bedrock AgentCore hosts agents that are used in pipelines.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-medialake)

[Read usage guidelines](/solutions/guidance-disclaimers/)
