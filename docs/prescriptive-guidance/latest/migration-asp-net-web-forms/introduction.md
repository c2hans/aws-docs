---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-asp-net-web-forms/introduction.html
---

# Migrating legacy ASP.NET Web Forms applications to AWS
<a name="introduction"></a>

*Fahad Mustafa and Adam Fisher, Amazon Web Services*

This guide explores the options available for migrating legacy ASP.NET Web Forms applications to the Amazon Web Services (AWS) Cloud. It covers the following aspects of migration:

[Hosting options](hosting.md):
+ Deploying the application on Amazon Elastic Compute Cloud (Amazon EC2) instances
+ Using AWS Elastic Beanstalk for streamlined deployment and management
+ Containerizing the application by using Docker and hosting it on Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS)

[Deployment strategies](deploying.md):
+ In-place upgrades and rolling deployments
+ Blue/green deployments for zero-downtime releases
+ Canary deployments for gradual rollouts

[High availability (HA) and scalability](ha-scaling.md):
+ Using Amazon EC2 Auto Scaling groups for automatic scaling
+ Implementing load balancing with Elastic Load Balancing (ELB)
+ Deploying the application across multiple Availability Zones for fault tolerance

[Monitoring and observability](monitoring.md):
+ Integrating with Amazon CloudWatch for application and infrastructure monitoring
+ Implementing centralized logging with Amazon CloudWatch Logs
+ Using AWS X-Ray for distributed tracing and performance analysis

Microsoft introduced ASP.NET Web Forms in 2002 as part of the original .NET Framework  release. It was designed to simplify web application development for Windows desktop application developers and gained widespread adoption among large enterprises because of its familiar programming model and drag-and-drop capabilities. Microsoft decided not to support ASP.NET Web Forms after .NET Framework version 4.8. As a result of this decision, ASP.NET Web Forms applications were restricted to running on the full .NET Framework in Windows, with Internet Information Services (IIS) as the web server.

Migrating these applications to newer .NET web frameworks, such as ASP.NET MVC or Blazor, requires a complete rewrite of the code base. Given the monolithic and feature-rich nature of many legacy ASP.NET Web Forms applications, rewriting them from scratch can be an expensive and time-consuming endeavor. As a result, many organizations opt to migrate their ASP.NET Web Forms applications to the AWS Cloud, to take advantage of the scalability, reliability, and cost-effectiveness offered by AWS.

This guide outlines various options for hosting, deploying, and scaling ASP.NET Web Forms applications on AWS, as well as high availability and observability options. By migrating to AWS, organizations can revitalize their legacy ASP.NET Web Forms applications. They can benefit from the robust infrastructure and scalability offered by AWS and its wide range of services and tools for modern application hosting and management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
