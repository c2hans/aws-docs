---
source_url: https://docs.aws.amazon.com//solutions/cloud-native-fast-turnaround-media-workflows-on-aws//index.html
---

# Guidance for Cloud-Native Fast-Turnaround Media Workflows on AWS

## Overview

This Guidance demonstrates new tools for media workflows in cloud environments as part of the Cloud-Native Agile Production (CNAP) program. This initiative builds upon the Time Addressable Media Store (TAMS) API specification, originally developed by the British Broadcasting Corporation's Research & Development team. The aim of the CNAP program is to drive industry adoption of TAMS as a cloud-native, open, and interoperable framework for fast-turnaround media workflows in the creation of News, Sports, and Entertainment content. TAMS stores media as discrete chunks in object storage, accessible through an open-source API. This approach eliminates common challenges found in traditional cloud-based media workflows. By using timing and identity as primary identifiers, TAMS enables content-centric workflows that reduce duplicate content and scale effectively, unlike traditional file-based systems.

## How it works

### TAMS concept overview

This architecture diagram shows the concept about how a Time Addressable Media Store (TAMS) sits at the core of a fast-turnaround workflow for processing live or near-live video and audio content.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cloud-native-fast-turnaround-media-workflows-on-aws.pdf)Step 1All media is stored within a Time Addressable Media Store (TAMS). This holds chunked media on object storage with an API to provide the link between content and the media essence.

Step 2Live video feeds are uploaded as small chunks of media and registered with the TAMS to provide the effect of growing content.

Step 3File-based content can be uploaded natively or chunked prior to import as required.

Step 4Content can be processed in near real-time, generating additional versions, such as proxies, triggered through notifications from the storage system.

Step 5Content analysis can occur asynchronously and in near real-time, enabling rapid access to the outputs of machine learning and artificial intelligence (AI/ML) models. Examples include live subtitling, highlights generation, and content logging.

Step 6Simple clip-based editing can be performed, and the resulting edits can be published back to the TAMS, referencing the original content.

Step 7Craft editing can access content from the TAMS and publish back only new segments.

Step 8Content from the store can be played back as a real-time video stream into production galleries of linear channel playout facilities.

Step 9TAMS API can be easily converted into HTTP Live Streaming (HLS) manifests to enable live or on-demand content streaming from the TAMS.

Step 10Clips and files can be exported from the store for alternative purposes, such as the rapid distribution of content onto social media platforms.

Step 11The Media Asset Management (MAM) system maintains references to the content stored within the TAMS, along with the associated rich editorial and time-based metadata.

### TAMS data structure

This architecture diagram shows the high-level data structure represented in the TAMS API specification. This diagram establishes the connection between the content that a user would be aware of and the actual media essence, which is stored in multiple formats and segments on the object storage system.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cloud-native-fast-turnaround-media-workflows-on-aws.pdf)Step 1In the TAMS data structure, the parent source is equal to the actual content that a user interacts with. This parent source could be an editorial version of the content or a clip.

Step 2The secondary level source within the data structure allows for the aggregation of the various media types, such as video, audio, or data, into a cohesive collection.

Step 3The "flow" represents the technical manifestation of the content. This construct contains all the technical metadata necessary to describe the underlying media segments, such as bitrate, resolution, and frame rate.

Step 4Multiple flows can exist for a single piece of content, enabling the representation of different formats, such as HD and proxy, to coexist.

Step 5Flow types include video, audio, and data, allowing the different content types to be referenced in the store.

Step 6Segments are held on object storage and referenced in the TAMS API. The only interaction between the store and the segments occurs during deletion management.

Step 7The segments are linked to a flow and exist within the context of that flow's virtual timeline. A time range format, expressed as Epoch time plus nanoseconds, is used to represent the position of each segment along the timeline.

NotesA segment can be referenced in one or more flows, allowing the reuse of segments between content without duplication at the storage layer.

The TAMS maintains only the metadata required for the storage and referencing of the media content. The rich metadata should be managed within separate systems, such as the Media Asset Management system.

### AWS open source TAMS API

This architecture diagram shows the components and data flows within the AWS open source implementation of the TAMS API.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cloud-native-fast-turnaround-media-workflows-on-aws.pdf)Step 1Amazon Cognito provides user and system-to-system authentication.

Step 2The API is presented through Amazon API Gateway, including the validation of requests using the OpenAPI specification.

Step 3AWS Lambda functions process the API requests. Separate functions exist for the services, sources, flows, segments, and delete request endpoints.

Step 4Source and flow metadata is stored in an Amazon Neptune graph database.

Step 5Segment metadata is stored in Amazon DynamoDB for speed of retrieval.

Step 6Delete requests are forwarded to Amazon Simple Queue Service (Amazon SQS) for asynchronous deletion.

Step 7A Lambda function is responsible for processing delete operations by forwarding the requests to a secondary Amazon SQS queue, which then handles the deletion of the corresponding Amazon Simple Storage Service (Amazon S3) objects.

Step 8After the required wait period, a Lambda function evaluates delete requests and removes only unused objects from Amazon S3.

Step 9Events from core API functions are sent to Amazon EventBridge for subsequent reuse by other systems.

Step 10An optional Lambda function can process webhook requests to external systems according to the specification.

### AWS open source TAMS tools

This architecture diagram demonstrates how the multiple components of the AWS TAMS Tools repository can be used alongside the core AWS open source TAMS implementation.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cloud-native-fast-turnaround-media-workflows-on-aws.pdf)Step 1The TAMS Store capability is provided by the AWS open source implementation.

Step 2A React-based user interface application, deployed through AWS Amplify, enables users to navigate the store, view video content through the HLS endpoint, and control the live and file-based ingestion processes.

Step 3Live video ingestion is facilitated using AWS Elemental MediaLive, which creates segments on Amazon S3 that are subsequently uploaded to the TAMS.

Step 4File-based import is enabled using AWS Elemental MediaConvert, orchestrated by AWS Step Functions, to chunk up the media and upload into the TAMS.

Step 5An HLS endpoint is provided to convert the TAMS native API calls into a set of HLS manifests to allow content to be played back within a web-based HLS player.

Step 6The media processing workflow uses event notifications from the TAMS to trigger additional post-processing of the ingested content. This includes the extraction of images and the creation of proxy versions using Lambda, as well as the export of concatenated files for integration with other systems.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs. [Open guide](https://aws-solutions-library-samples.github.io/media-entertainment/cloud-native-fast-turnaround-media-workflows-on-aws/index.html)
- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs. [Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-cloud-native-fast-turnaround-media-workflows-on-aws)

## Well-Architected Pillars

### Operational Excellence

The AWS open source implementation of the TAMS API uses [AWS X-Ray](https://aws.amazon.com/xray/) to trace requests through the serverless infrastructure, including **API Gateway**, **Lambda**, and **DynamoDB**. The **X-Ray** service aids developers and support teams in tracking and analyzing requests as they flow through the various components of the AWS open-source implementation of the TAMS API. In addition, all logs and metrics are collected within [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to facilitate monitoring and analysis. The metrics collected within CloudWatch support the creation of dashboards and the configuration of alarms. [Read the Operational Excellence whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The TAMS API uses **Amazon S3** pre-signed URLs to provide consumers with time-limited access to only the required segments, helping ensure that access control is managed centrally by the API, regardless of the consumer's location, whether within AWS or on-premises. The AWS open-source implementation of the TAMS specification uses **Amazon Cognito** by default for authentication, providing OAuth2-based access control on the API, in addition to the ability to federate with other authentication providers. The current API implementation supports coarse-grained, role-based permissions across the various CRUD operations, with the team actively working on extending this to incorporate attribute-based access control (ABAC) in the near future. [Read the Security whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The AWS open-source implementation of the TAMS API exclusively uses AWS Regional-level services, including **Amazon S3**, **API Gateway**, **Lambda**, and **DynamoDB**. This design approach eliminates the need for AWS customers to manage Availability Zone-level resilience. Additionally, all the services employed will automatically scale and recover from any underlying issues. [Read the Reliability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

In the AWS open-source implementation of the TAMS, the database technologies have been carefully selected to provide optimal performance for the diverse access patterns. The sources and flows require complex linking and filtering capabilities, for which **Neptune**, a graph database, has been chosen as the appropriate solution. For the segments, the access patterns are more straightforward, but speed and performance are critical to handle the ingestion of new segments as they arrive. As a result, **DynamoDB** has been utilized to deliver the required performance characteristics. [Read the Performance Efficiency whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The TAMS-based approach eliminates the need for high-performance file storage alongside the object storage, as it maintains a single copy of the media on lower-cost object storage. The API facilitates the reuse of media segments across different content, thereby deduplicating the media at the storage level and resulting in savings in both storage space and cost. The AWS open-source implementation of the TAMS is built around serverless components that scale and incur costs based on usage. Given that most media workloads exhibit peaky demand patterns, this design approach reduces costs to just the persistence layer (**Amazon S3**, **DynamoDB**, **Neptune**) when the system is not actively in use. [Read the Cost Optimization whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The TAMS approach to live media workflows is inherently more optimized and, consequently, more sustainable than traditional methods. At the storage level, there is no longer a requirement for high-performance file systems alongside **Amazon S3** object storage, and the storage can be deduplicated, resulting in reduced space requirements. The use of serverless technologies helps ensure that during periods of low usage, the resources are automatically scaled back, thereby reducing the environmental impact. In contrast, traditional on-premises broadcast solutions would typically remain operational 24/7, regardless of usage patterns. The edit-by-reference model employed in the TAMS has the potential to reduce the need for rendering on edit workstations, thereby saving compute time and potentially allowing the use of smaller compute instances. [Read the Sustainability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Time addressable media store**: This sample code deploys the AWS Infrastructure required to create a sample implementation of the BBC TAMS API.

[Go to sample code](https://github.com/awslabs/time-addressable-media-store)

- **Time addressable media store tools**: This sample code contains a set of tools to help customers and partners get started with the TAMS API.

[Go to sample code](https://github.com/aws-samples/time-addressable-media-store-tools)

- **Cloud Native Agile Production (CNAP) project**: This blog post announces the launch of the CNAP project to re-think the creation and delivery of live media in the cloud.

[Read blog](https://aws.amazon.com/blogs/media/aws-bbc-adobe-and-others-introduce-open-source-framework-for-fast-turnaround-media-workflows-at-ibc-2024/)

- **Time Addressable Media Store community and news**: This website is dedicated to the Time Addressable Media Store (TAMS) community and provides the latest news about TAMS.

[Visit website](https://timeaddressablemediastore.org/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
