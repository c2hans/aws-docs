---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 The multi-tier application (three-tier, *n*-tier, and so forth.) has been a cornerstone architecture pattern for decades, and remains a popular pattern for user-facing applications. Although the language used to describe a multi-tier architecture varies, a multi-tier application generally consists of the following components:
+  **Presentation tier**: Component that the user directly interacts with (for example, webpages and mobile app UIs).
+  **Logic tier**: Code required to translate user actions to application functionality (for example, CRUD database operations and data processing).
+  **Data tier**: Storage media (for example, databases, object stores, caches and file systems) that hold the data relevant to the application.

 The multi-tier architecture pattern provides a general framework to ensure decoupled and independently scalable application components can be separately developed, managed, and maintained (often by distinct teams).

 As a consequence of this pattern in which the network (a tier must make a network call to interact with another tier) acts as the boundary between tiers, developing a multi-tier application often requires creating many undifferentiated application components. Some of these components include:
+  Code that defines a message queue for communication between tiers
+  Code that defines an application programming interface (API) and a data model
+  Security-related code that ensures appropriate access to the application

 All of these examples can be considered “boilerplate” components that, while necessary in multi-tier applications, do not vary greatly in their implementation from one application to the next.

 AWS offers a number of services that enable the creation of serverless multi-tier applications – greatly simplifying the process of deploying such applications to production and removing the overhead associated with traditional server management. [Amazon API Gateway](https://aws.amazon.com/api-gateway), a service for creating and managing APIs, and [AWS Lambda](https://aws.amazon.com/lambda), a service for running arbitrary code functions, can be used together to simplify the creation of robust multi-tier applications.

 Amazon API Gateway’s integration with AWS Lambda enables user-defined code functions to be initiated directly through HTTPS requests. Regardless of the request volume, both API Gateway and Lambda scale automatically to support exactly the needs of your application (refer to [API Gateway Amazon API Gateway quotas and important notes](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) for scalability information). By combining these two services, you can create a tier that enables you to write only the code that matters to your application and not focus on various other undifferentiating aspects of implementing a multi-tiered architecture such as architecting for high availability, writing client SDKs, server and operating system (OS) management, scaling, and implementing a client authorization mechanism.

 API Gateway and Lambda enable the creation of a serverless logic tier. Depending on your application requirements, AWS also provides options to create a serverless presentation tier (for example, with [Amazon CloudFront](https://aws.amazon.com/cloudfront) and [Amazon Simple Storage Service](https://aws.amazon.com/s3)) and data tier (for example, [Amazon Aurora](https://aws.amazon.com/aurora), [Amazon DynamoDB](https://aws.amazon.com/dynamodb)).

 This whitepaper focuses on the most popular example of a multi-tiered architecture, the **three-tier** web application. However, you can apply this multi-tier pattern well beyond a typical three-tier web application.

## Three-tier architecture overview
<a name="three-tier-architecture-overview"></a>

 The three-tier architecture is the most popular implementation of a multi-tier architecture and consists of a single presentation tier, logic tier, and data tier. The following illustration shows an example of a simple, generic three-tier application.

![Architectural pattern for a three-tier application](http://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/images/image2.png)

* Architectural pattern for a three-tier application *

 There are many great online resources where you can learn more about the *general* three-tier architecture pattern. This whitepaper focuses on a specific implementation pattern for this architecture using Amazon API Gateway and AWS Lambda.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
