---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/creating-serverless-applications-with-aws-lambda.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Creating Serverless Applications with AWS Lambda
<a name="creating-serverless-applications-with-aws-lambda"></a>

Containers provide a high level of flexibility; however, you still need to manage your container images, including the guest OS and any application dependencies.

For example, suppose you need to deploy an ASP.NET Core application. In addition to the application, the container image must also include a choice of guest OS, the .NET Core runtime library, the ASP.NET [Kestrel](https://kestrelcomputer.github.io/kestrel/) engine, and a web server such as [Nginx](https://www.nginx.com/) or Apache. Although this gives you more control over your runtime environment, it also means additional undifferentiated efforts, and in most cases this level of control is not required.

[AWS Lambda](https://aws.amazon.com/lambda/) solves this problem by providing a serverless Function-as-a-Service (FaaS) model, which automatically manages the underlying compute resources for you. C\# code can be uploaded into a Lambda function, and everything else is handled by Lambda.

Lambda provides the highest level of abstraction, simplicity, efficiency and scalability for running .NET code in the cloud. It is simple because it allows developers to run their code without having to worry about the infrastructure that runs it; efficient because there is no charge when the code is not running; and scalable because it seamlessly handles load fluctuations. Lambda supports many popular programming languages, including C\# and PowerShell. Lambda already includes .NET Core 2.1 and 3.1 as managed runtime environments. You can also run .NET 5 applications on Lambda using an event-driven [custom container image](https://aws.amazon.com/blogs/developer/net-5-aws-lambda-support-with-container-images/) as your function, or using [custom runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html).

Lambda functions are often deployed behind API instances in [Amazon API Gateway](https://aws.amazon.com/api-gateway/), which provide managed endpoints that act as front doors for consuming applications to access data or backend functionality. API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization and access control, monitoring, and API version management. API Gateway can also be used with workloads running on EC2 instances or ECS tasks.

When you don’t need the governance features API Gateway offers, you can deploy Lambda functions behind an Application Load Balancer (ALB), which allows load to scale elastically without having to maintain a set of managed APIs.

For more information on how to create applications using AWS Lambda, see the [*Serverless Architectures with AWS Lambda*](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/welcome.html) whitepaper.

**Load Balancing .NET Applications on AWS**

Load balancing is a common problem for building and deploying scalable applications. AWS provides a variety of solutions for load balancing. Each solution is optimized to address a specific set of requirements.
+  **Application Load Balancer** **(ALB)** is best suited for load balancing of HTTP and HTTPS traffic, and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers. Application Load Balancer routes traffic to targets within the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) based on the content of the request. AWS ALB also supports end-to-end HTTP/2 and [gRPC](https://grpc.io/), with health-check on target endpoints. This is a popular solution for microservice integration and client-server communications. For more information, see [this blog post](https://aws.amazon.com/blogs/aws/new-application-load-balancer-support-for-end-to-end-http-2-and-grpc/).
+  **Network Load Balancer (NLB)** is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Transport Layer Security (TLS) traffic where extreme performance is required. Network Load Balancer routes traffic to targets within the Amazon VPC, and is capable of handling millions of requests per second while maintaining ultra-low latencies.
+  **Gateway Load Balancer** makes it easy to deploy, scale, and run third-party virtual networking appliances. Providing load balancing and auto scaling for fleets of third-party appliances, Gateway Load Balancer is transparent to the source and destination of traffic. This capability makes it well suited for working with third-party appliances for security, network analytics, and other use cases.
