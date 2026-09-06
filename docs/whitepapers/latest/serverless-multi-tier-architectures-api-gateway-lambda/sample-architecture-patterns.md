---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/sample-architecture-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Sample architecture patterns
<a name="sample-architecture-patterns"></a>

 You can implement popular architecture patterns using API Gateway and AWS Lambda as your logic tier. This whitepaper includes the most popular architecture patterns that leverage AWS Lambda-based logic tiers:
+  **Mobile backend -** A mobile application communicates with API Gateway and Lambda to access application data. This pattern can be extended to generic HTTPS clients that don't use serverless AWS resources to host presentation tier resources (such as desktop clients, web server running on EC2, and so forth).
+  **Single page application **- A single page application hosted in Amazon S3 and CloudFront communicates with API Gateway and AWS Lambda to access application data.
+  **Web application ** – The web application is a general-purpose, event-driven, web application back-end that uses AWS Lambda with API Gateway for its business logic. It also uses DynamoDB as its database and Amazon Cognito for user management. All static content is hosted using Amplify.

 In addition to these two patterns, this whitepaper discusses the applicability of Lambda and API Gateway to a general microservice architecture. A microservice architecture is a popular pattern that, although not a standard three-tier architecture, involves decoupling application components and deploying them as stateless, individual units of functionality that communicate with each other.
