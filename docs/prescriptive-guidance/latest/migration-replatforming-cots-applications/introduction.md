---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/introduction.html
---

# Replatforming COTS and in-house applications during a migration to the AWS Cloud
<a name="introduction"></a>

*Anbu Selvan, Amazon Web Services*

This guide describes seven areas that you should focus on when you replatform commercial off-the-shelf (COTS) and in-house applications in the Amazon Web Services (AWS) Cloud. The guide also provides strategies, tools, and AWS services to help you replatform application components. COTS applications are third-party applications that are ready-made and can be purchased in a commercial market (for example, [AWS Marketplace](https://aws.amazon.com/marketplace)). In-house applications are developed and used internally by your organization.

After you decide to migrate your COTS or in-house applications to the AWS Cloud, you must evaluate which of the seven common migration strategies (7 Rs) to use. These strategies are refactor, replatform, repurchase, rehost, relocate, retain, and retire. We recommend that you replatform applications that use components or databases that reached, or are close to reaching, their end-of-support (EOS) date. EOS is when a vendor withdraws technical support for a product. If you choose to replatform an application in the AWS Cloud, you can benefit from the following capabilities:
+ Automate [in-place operating system (OS) upgrades](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/os-inplaceupgrade.html) with AWS Systems Manager.
+ Use snapshot storage volumes to quickly create Amazon Machine Images (AMIs) from Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ Create a private subnet to isolate workloads that run on outdated operating systems (OSs).
+ Use high-speed networking to rapidly replicate production environments for testing the replatforming.
+ Quickly set up a separate application stack with on-demand EC2 instances, without using additional on-premises hardware.

To benefit from these and other capabilities available on the AWS Cloud, we recommend that you first rehost your application by using [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html). You can then upgrade the application in the AWS Cloud. The following list provides examples of when an application should be replatformed:
+ Support is no longer available for the application's OS, runtimes (for example, [Apache Tomcat](https://tomcat.apache.org/), [JBoss, ](https://jbossas.jboss.org/)or [Oracle WebLogic Server](https://www.oracle.com/middleware/technologies/weblogic.html)), databases, or runtime components (for example, Java, Python, or Perl).
+ The application must become more resilient and automatically recover from failures (for example, software bugs or infrastructure issues).
+ New application functionalities are required for new customer segments or to support increased loads.
+ The application is unstable and requires improvements to enhance operational stability.

Before you begin a replatforming journey, you should explore alternatives to your application's functionalities; for example, evaluate whether you can replace them with a software as a service (SaaS) solution from an independent software vendor (ISV). You might also be able to rebuild application functionalities by using AWS services such as AWS Lambda, Amazon Cognito, Amazon MQ, AWS Glue, Amazon QuickSight, or Amazon Aurora.

This guide is for IT administrators, application owners, architects, technical leads, and project managers. The guide provides the following seven areas to focus on when you replatform COTS and in-house applications in the AWS Cloud:
+ [Choosing the replatforming environment](choosing-replatforming-environment.md)
+ [Replatforming application components running on unsupported OSs](replatforming-application-components.md)
+ [Replatforming backend databases](replatforming-backend-databases.md)
+ [Replatforming file shares](replatforming-file-shares.md)
+ [Updating the logging and monitoring components](updating-logging-monitoring.md)
+ [Testing and validating your applications](testing-validating-application.md)
+ [Automating ongoing OS patching](automating-os-patching.md)

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You should expect the following four outcomes after replatforming COTS and in-house applications in the AWS Cloud:
+ Reduce security risks from legacy applications that run unsupported software or OSs.
+ Lower your overall application ownership costs by removing expensive, non-essential database editions or adopting open-source databases.
+ Reduce operational overhead by using AWS managed databases (for example, [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) or Aurora) to achieve higher levels of availability and reliability for your applications.
+ Make legacy applications more resilient by adopting cloud-native automation and monitoring features, such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) monitoring or Systems Manager-based OS patching.
