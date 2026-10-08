---
source_url: https://docs.aws.amazon.com/solutions/image-to-text-and-image-to-speech-on-aws/index.html
---

---
title: 'Guidance for Image-to-Text and Image-to-Speech on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/image-to-text-and-image-to-speech-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Image-to-Text and Image-to-Speech on AWS

## Overview

This Guidance shows how to convert images to text and speech with machine learning and generative AI services on AWS. Converting images to text is done with the help of Amazon Kendra, a search engine that can be used to index an image repository and search for data. Next, generative AI is used for captioning the images, recognizing objects and features to generate a human-readable textual description, typically a caption based on extracted visual features. This Guidance also shows how to convert image to speech and can be extended to serve content through voice-enabled devices, such as Amazon Alexa. This involves the [Describe for Me](https://www.describeforme.com/) web app which generates a caption of an image and reads it back in a clear, human-sounding voice, including a variety of languages and dialects.

## How it works

### How it works

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/image-to-text-and-image-to-speech-on-aws.pdf)Step 1Users upload images to an image repository like an Amazon Simple Storage Service (Amazon S3) bucket.Step 2An AWS Lambda function is invoked to enrich the Amazon Kendra index on demand.Step 3Amazon Kendra, a search engine that can be used to search for structured and unstructured data, indexes the image repository. The Lambda function invokes both Amazon Textract and the generative AI model that is deployed on Amazon SageMaker as a near real-time inference endpoint.Step 4The generative AI model for image captioning processes the uploaded images, recognizing objects and features to generate a human-readable textual description, typically a caption based on extracted visual features.Step 5Simultaneously, another component of the solution utilizes Amazon Textract. Amazon Textract is used to extract any text that is visible within the image and is invoked by the Lambda function. This extracted text is also considered as part of the metadata for the image.Step 6The image captions are stored in an Amazon S3 bucket.Step 7Both the generated image description from the generative AI model and the extracted text from Amazon Textract are considered as metadata for the uploaded image. This metadata is associated with the image within the Amazon Kendra index. Users can then search for images using natural language queries, such as "Find images of red roses" or "Show me pictures of dogs playing in the park," through the Amazon Kendra console, an AWS software development kit (AWS SDK), or API. These queries are processed by Amazon Kendra, which uses machine learning (ML) algorithms to understand the meaning behind the queries and retrieve relevant images from the indexed repository.### How it works

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/image-to-text-and-image-to-speech-on-aws.pdf)Step 1An AWS SDK connects the mobile client to AWS Amplify.Step 2The Amazon Cognito identity pool grants users temporary access to the Amazon S3 bucket.Step 3A user can upload an image file to the Amazon S3 bucket.Step 4The Describe for Me web app invokes the backend artificial intelligence (AI) services by sending the Amazon S3 object key in the payload to Amazon API Gateway.Step 5API Gateway instantiates an AWS Step Functions workflow. The state machine uses Lambda functions to orchestrate the AI/ML services Amazon Textract, Amazon Rekognition, Amazon SageMaker, Amazon Translate, and Amazon Polly.Step 6The Step Functions workflow creates an audio file output and stores it in Amazon S3 in MP3 format.Step 7A presigned URL with the location of the audio file stored in Amazon S3 is sent back to the user's browser through API Gateway. The user's mobile device plays the audio file using the presigned URL.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses AWS services like Lambda and Step Functions to automate tasks, reducing manual work and errors, and Amazon S3 to provide reliable data storage. These services easily adapt to changing workloads and support efficient, consistent operations. Additionally, you can use Amazon CloudWatch to monitor operations and gain insights. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses Lambda and Step Functions to automate security-related tasks, reducing the risk of human error in security processes. Additionally, API Gateway enforces secure management of API endpoints, Amazon Cognito enhances user authentication and authorization processes, and AWS Identity and Access Management (IAM) controls access to AWS resources. Finally, CloudWatch helps detect security incidents or anomalous activities in real time, facilitating swift incident responses and threat mitigation. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses automation through Lambda and Step Functions to reduce the risk of human errors that might compromise reliability. Additionally, Amazon S3 provides data replication and redundancy features that increase data reliability, and API Gateway grants users consistent and secure access to APIs to maintain workload reliability. CloudWatch monitors operations, aiding in issue detection and resolution. This proactive approach enhances workload reliability by minimizing downtime and disruptions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance reduces latency and resource inefficiency by using Lambda and Step Functions to automate processes and streamline workflows. Additionally, SageMaker and Amazon Polly facilitate real-time content generation, supporting faster and more efficient workloads, and API Gateway optimizes API management, delivering low latency and consistent access to promote high performance efficiency. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance minimizes operational expenses by using Lambda and Step Functions to facilitate efficient resource use and reduce the need for constant manual intervention, minimizing human error and resource waste. Additionally, Amazon Polly reduces the need for costly manual content creation, API Gateway optimizes API management, decreasing compute-related costs, and Amazon Kendra improves search efficiency, reducing the time and resources spent on information retrieval. Finally, Amazon S3 offers scalable and cost-effective storage solutions so that you can store and access data efficiently without incurring unnecessary expenses. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses serverless services like Lambda and API Gateway for their energy efficiency, their efficient use of resources, and their incorporation of renewable energy sources. These practices align with sustainability goals, helping you reduce your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Automate caption creation and search for images at enterprise scale using generative AI and Amazon Kendra**: This blog post demonstrates how to use CDE in Amazon Kendra using a Generative AI model deployed on Amazon SageMaker.

[Learn more](https://aws.amazon.com/blogs/machine-learning/automate-caption-creation-and-search-for-images-at-enterprise-scale-using-generative-ai-and-amazon-kendra/)

- **Introducing an image-to-speech Generative AI application using Amazon SageMaker and Hugging Face**: This blog post walks you through the Solution Architecture and design considerations behind “Describe For Me”, a website which helps the visually impaired understand images through image caption, facial recognition, and text-to-speech.

[Learn more](https://aws.amazon.com/blogs/machine-learning/introducing-an-image-to-speech-generative-ai-application-using-amazon-sagemaker-and-hugging-face/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
