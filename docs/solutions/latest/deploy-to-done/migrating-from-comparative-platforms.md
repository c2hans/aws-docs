---
source_url: https://docs.aws.amazon.com/solutions/latest/deploy-to-done/migrating-from-comparative-platforms.html
---

# Migrating From Comparative Platforms
<a name="migrating-from-comparative-platforms"></a>

If you are moving applications from another platform, this section provides entry paths based on your current environment.

## From Heroku, Render, or Railway
<a name="from-heroku-render-railway"></a>

Teams commonly migrate from these platforms when they encounter cost scaling pressure at growth, compliance requirements (HIPAA, PCI, FedRAMP) that the platform cannot satisfy, need for VPC network isolation, or portfolio-scale operations (running many applications under one consistent operational model instead of configuring each one separately) that single-app platforms cannot address.

These platforms accept application source code and manage the runtime. Elastic Beanstalk accepts the same inputs: source code with a supported runtime, a Dockerfile, or a pre-built container image. Key differences after migration:
+ Elastic Beanstalk environments run in your AWS account (full VPC, IAM, and networking control available if needed)
+ No per-dyno or per-service platform fee. You pay for the underlying AWS resources.
+ Applications that outgrew single-app platforms gain portfolio-scale operations under one interface
+ Compliance eligibility (HIPAA, PCI, SOC, FedRAMP) that developer-focused platforms typically cannot provide

**Migration approach:** Start with a parallel environment. Deploy your application to Elastic Beanstalk alongside your existing platform. Validate health checks, scaling behavior, deployment rollback, secrets management, and observability. Cut traffic over once validated.

## From On-Premises .NET/Java/PHP
<a name="from-on-premises"></a>

Applications running on Windows Server/IIS, Tomcat, or Apache can land on Elastic Beanstalk without re-architecture:
+ **Windows/.NET Framework:** Use the `eb migrate` command to discover IIS configurations and deploy directly to Elastic Beanstalk Windows environments
+ **.NET Core/6\+:** Deploy to Linux-based environments for cost efficiency
+ **Java (Spring Boot, Tomcat):** Provide a WAR/JAR file or source. Elastic Beanstalk provisions Tomcat and manages the runtime
+ **PHP (Laravel, WordPress):** Provide source. Elastic Beanstalk provisions Apache/nginx and manages the stack

## From Azure App Service
<a name="from-azure-app-service"></a>

Azure App Service and Elastic Beanstalk serve similar operational roles: accept application code, manage the runtime environment. Key architectural differences:
+ **Resource visibility:** Elastic Beanstalk environments run in your AWS account with full visibility into underlying resources (EC2, ALB, Auto Scaling groups). App Service abstracts infrastructure entirely.
+ **Networking:** Azure VNet integration maps to AWS VPC configuration. Review subnet layouts, private endpoints, and DNS resolution patterns before migrating.
+ **Identity:** Azure AD/Entra ID integration maps to AWS IAM and Amazon Cognito. Service-to-service authentication patterns will need re-mapping.

**Service mapping:** Key Vault to AWS Secrets Manager, Azure Monitor to Amazon CloudWatch, Azure SQL to Amazon RDS, Azure Blob Storage to Amazon S3, Azure Service Bus to Amazon SQS/SNS.

Review your networking, identity, and data dependencies before migrating. The [Prescriptive Guidance pattern for Azure-to-EB migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk.html) provides a step-by-step architectural walkthrough.

## From Self-Managed EC2 Instances
<a name="from-self-managed-ec2"></a>

If your team currently deploys to EC2 instances with hand-configured Auto Scaling groups, load balancers, and patching scripts, Elastic Beanstalk manages all of those components as part of the application environment. You retain the same underlying infrastructure (EC2, ALB, Auto Scaling) but transfer the operational responsibility for orchestrating them.

**Get architecture guidance for your specific migration scenario.** [Request a specialist session](https://aws.amazon.com/contact-us/)

## Go Deeper
<a name="migrating-go-deeper"></a>

**Go Deeper**
[Migrate an ASP.NET Web Application to Elastic Beanstalk (Hands-on Tutorial)](https://aws.amazon.com/getting-started/hands-on/migrate-aspnet-web-application-elastic-beanstalk/) - Step-by-step IIS migration
[Performing Basic IIS Migrations with eb migrate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-onpremmigration.html) - CLI-based Windows migration
[Migrate a .NET Application from Azure App Service to AWS Elastic Beanstalk](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-net-application-from-microsoft-azure-app-service-to-aws-elastic-beanstalk.html) - Prescriptive Guidance pattern
[Application Migration Workshop: Replatform with Elastic Beanstalk](https://catalog.us-east-1.prod.workshops.aws/workshops/c6bdf8dc-d2b2-4dbd-b673-90836e954745/en-US/04-application-migration/03-eb) - Hands-on lab
[Simplify Application Migrations to AWS with Elastic Beanstalk](https://aws.amazon.com/blogs/migration-and-modernization/simplify-application-migrations-to-aws-with-elastic-beanstalk/) - Migration walkthrough for PaaS and on-premises workloads
