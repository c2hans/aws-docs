---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-enterprise-economics-with-serverless/aws-serverless-capabilities.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS serverless capabilities
<a name="aws-serverless-capabilities"></a>

 Like any other traditional server and VM-based architecture, serverless provides core capabilities such as compute, storage, messaging and more to its users. However, serverless services are distributed across multiple managed services rather than spread across software-installed virtual machines.

 As a result, AWS provides a complete serverless application that requires a broad array of services, tools, and capabilities spanning storage, messaging diagnostics, and more. Each of these services is available in the developer’s toolbox to build a practical application.

## Service offerings
<a name="service-offerings"></a>

 Since the introduction of Lambda in 2014, AWS has introduced a wide variety of fully-managed serverless services that enable organizations to create serverless apps that can integrate seamlessly with other AWS services and third-party services.

 The launched serverless services include, but are not limited to, Amazon API Gateway (2015), Amazon EventBridge (2019), and Amazon Aurora Serverless v2 (2020). The pace of innovation has not stopped for individual services, as Lambda has had more than [100 major feature releases since its launch](https://docs.aws.amazon.com/lambda/latest/dg/lambda-releases.html). The following figure illustrates a subset of the components in the AWS serverless platform and their relationships.

![Diagram showing AWS serverless platform components](https://docs.aws.amazon.com/whitepapers/latest/optimizing-enterprise-economics-with-serverless/images/serverless-components.png)

 Serverless offerings from AWS consist of services that span across all infrastructure layers, including compute, storage, and orchestration. In addition, AWS provides tools needed to author, build, deploy, and diagnose serverless architectures.

 Running a serverless application in production requires a reliable, flexible, and trustworthy platform that can handle the demands of small startups to global, worldwide corporations. The platform must scale *all* of an application’s elements and provide end-to-end reliability.

 Just as with conventional applications, helping developers create and deliver serverless solutions is a multi-dimensional challenge. To meet the needs of large-scale enterprises across various industries, the AWS serverless platform offers the following capabilities through a diverse set of services.
+  **A high-performance, scalable, and reliable *serverless compute layer*** - The serverless compute layer is at the core of any serverless architecture, such as AWS Lambda or AWS Fargate, responsible for running the business logic. Because these services are run in response to events, simple integration with both first-party and third-party event sources is essential to making solutions simple to express and enabling them to scale automatically in response to varying workloads. In addition, serverless architectures eliminate all of the scaling and management code typically required to integrate such systems, shifting that operational burden to AWS.
+  **Highly available, durable, and scalable storage layer –** AWS offers fully managed storage layers that offload the overhead of ever-increasing storage requirements to support the serverless compute layer. Instead of manually adding more servers and storage, services such as Amazon Aurora Serverless v2, Amazon DynamoDB, and Amazon Simple Storage Service (Amazon S3) scales based on usage and users are only billed for the consumed resources. In addition, AWS offers purpose-built storage services to meet diverse customer needs, from DynamoDB for key-value storage, Amazon S3 for object storage, and Aurora Serverless v2 for relational data storage.
+  **Support for loosely coupled and scalable decoupled serverless workloads –** As applications mature and grow, they become more challenging to maintain or add new features, and some transform into monolithic applications. As a result, they make it challenging to implement changes and slow down the development pace. What is needed is individual components that are decoupled and can scale independently. Amazon Simple Queue Service (Amazon SQS), Amazon Simple Notification Service (Amazon SNS), Amazon EventBridge, and Amazon Kinesis enable developers to decouple individual components, allowing developers to create and innovate without being dependent on one another. In addition, these components all being serverless implies that customers are only being billed for the resources that each component is consuming, eliminating unnecessary resources being wasted.
+  ***Orchestration* offering state and workflow management** – Orchestration and state management are also critical to a serverless platform’s success. As companies adopt serverless architectures, there is an increased need to orchestrate complex workflows with decoupled components. AWS Step Functions is a visual workflow service that satisfies this need. It is used to orchestrate AWS services, automate business processes, and build serverless applications. Step Functions manage failures, retries, parallelization, service integrations, and observability so developers can focus on higher-value business logic. Building applications from individual components that perform a discrete function lets you scale easily and change applications quickly. Developers can change and add steps without writing code, enabling your team to evolve your application and innovate faster.
+  ***Native service integrations* between serverless** services mentioned above, such as Amazon Simple Queue Service (SQS), Amazon Simple Notification Service (Amazon SNS), and Amazon EventBridge, act as application integration services, enabling communication between decoupled components within microservices. Another benefit of these services is that minimal code is needed to allow interoperability between them, so you can focus on building your application instead of configuring it. For instance, integration between Amazon API Gateway -a fully managed service for hosting APIs - to a Lambda function can be done without writing any code and simply walking through the AWS console.

## Developer support
<a name="developer-support"></a>

 Providing the right tool and support for developers and architects is essential to boosting productivity. AWS Developer Tools are built to work with AWS, making it easier for teams to set up and be productive.

 In addition to popular and well-known developer tools such as AWS Command Line Interface (AWS CLI) and AWS Software Development Kits (AWS SDKs), AWS also provides various AWS, open-source, and third-party web frameworks that simplify serverless application development and deployment.

 This includes the AWS Serverless Application Model (AWS SAM) and AWS Cloud Development Kit (AWS CDK) (AWS CDK) that allows customers to onboard faster to serverless architectures, offloading undifferentiated heavy lifting of managing the infrastructure for your applications.

 This enables developers to focus on writing code that creates value for their customers. In addition, AWS provides the following support for developers adopting serverless technologies.
+  **A collection of fit-for-purpose *application modeling frameworks* –**Application modeling frameworks, such as the open specification AWS SAM or AWS CDK, enable a developer to express the components that make up a serverless application and enable the tools and workflows required to build, deploy, and monitor those applications. Both frameworks work nicely with the AWS SAM Command Line Interface (AWS SAM CLI), making it easy for them to create and manage serverless applications. It also allows developers to build, test locally, and debug serverless applications then deploy them on AWS. It can also create secure continuous integration and deployment (CI/CD) pipelines that follow best practices and integrate with AWS’ native and third-party CI/CD systems.
+  **A vibrant *developer ecosystem* that helps developers discover and apply solutions in a variety of domains and for a broad set of third-party systems and use cases** - Thriving on a serverless platform requires that a company be able to get started quickly, including finding ready-made templates for everyday use cases, whether they involve first-party or third-party services. These integration libraries are essential to convey [successful patterns](https://serverlessland.com/patterns)—such as processing streams of records or implementing webhooks—especially when developers are migrating from server-based to serverless architectures. A closely related need is a broad and diverse ecosystem that surrounds the core platform. A large, vibrant ecosystem helps developers discover and use solutions from the community and makes it easy to contribute new ideas and approaches. Given the variety of toolchains in use for application lifecycle management, a healthy ecosystem is also necessary to ensure that every language, Integrated Development Environment (IDE), and enterprise build technology has the runtimes, plugins, and open-source solutions essential to integrate the building and to deployment of serverless applications into existing approaches. Finally, a broad ecosystem provides significant acceleration across domains and enables developers to repurpose existing code more readily in a serverless architecture.

## Security
<a name="security"></a>

 All AWS customers benefit from a data center and network architecture built to satisfy the requirements of our most security-sensitive customers. This means that you get a resilient infrastructure designed for high security without a traditional data center’s capital outlay and operational overhead. Serverless architecture is no exception.

 To accomplish this, AWS’ serverless services offer a broad array of *security and access controls*, including support for virtual private networks, role-based and access-based permissions, robust integration with API-based authentication and access control mechanisms and support for encrypting application elements, such as environment variable settings.

 These out-of-the-box offered features and services can help developers deploy and publish workloads confidently and reduce time to market. Serverless systems, by their design, also provides an additional level of security and control for the following reasons:
+  **First-class fleet management, including security patching** – For managed serverless services such as Lambda, API Gateway, and Amazon SQS, the servers that host the services are constantly monitored, cycled, and security scanned. As a result, they can be patched within hours of essential security update availability instead of many enterprises’ compute fleets with much looser service level agreements (SLAs) for patching and updating.
+  **Per-request authentication, access control, and auditing** – Every request between natively-integrated services is individually authenticated, authorized to access specified resources, and can be fully audited. Requests arriving from outside of AWS via Amazon API Gateway provide other internet-facing defense systems. For example, AWS Web Application Firewall (AWS WAF) is a web application firewall that integrates natively with Amazon API Gateway. It helps protect hosted APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources, including distributed denial-of-service (DDoS) attack defenses. In addition, companies migrating to serverless architectures can use AWS CloudTrail to gain detailed insight into which users are accessing which systems with what privileges. Finally, they can use AWS tools to process the audit records programmatically.

 These security features of serverless help eliminate additional costs often overlooked when calculating the TCO of one’s infrastructure. Such costs include security and monitoring software licenses installed on servers, staffing of information security personnel to ensure that all servers are secure, as well as costs associated with regulatory compliance, and many others.

 Serverless architectures also have a smaller blast radius compared to monolithic applications running on virtual machines. As AWS takes responsibility of the security of the servers behind the scenes, customers can focus on implementing least privilege access between the services. Once least privilege access is implemented, the blast radius is dramatically reduced.

 The decoupled nature of the architecture will limit the impact to a smaller set of services, compared to a scenario where a malicious actor gains access to an internal server. Considering the significant financial impact of a security breach, this is also an added benefit that help enterprises optimize on infrastructure costs.

 Adopting serverless architectures help in reducing or eliminating such expenses that are no longer needed, and capital can be repurposed, and teams are freed to work on higher-value activities.

## Partners
<a name="partners"></a>

 AWS has an expansive partner network that assists our customers with building solutions and services on AWS. AWS works closely with validated AWS Lambda Partners for building serverless architectures that help customers develop services and applications without provisioning or managing servers.

 Lambda Partners provide developer tooling solutions validated by AWS serverless experts against the AWS Well-Architected Framework. Customers can simplify their technology evaluation process and increase purchasing confidence, knowing these companies’ solutions have passed a strict AWS validation of security, performance, and reliability.

 Customers can ultimately reduce time to market with the assistance of qualified partners leveraging serverless technologies. For a complete list of AWS Lambda Ready Partners, visit our [AWS Partner Network page](https://aws.amazon.com/partners/).
