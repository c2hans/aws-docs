---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html
---

# Modernize and deploy mainframe applications using AWS Transform and Terraform
<a name="modernize-mainframe-app-transform-terraform"></a>

*Mason Cahill, Polaris Jhandi, Prachi Khanna, Sivasubramanian Ramani, and Santosh Kumar Singh, Amazon Web Services*

## Summary
<a name="modernize-mainframe-app-transform-terraform-summary"></a>

[AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) can accelerate large-scale modernization of .NET, mainframe, and VMware workloads. It deploys specialized AI agents that automate complex tasks like assessments, code analysis, refactoring, decomposition, dependency mapping, validation, and transformation planning. This pattern demonstrates how to use AWS Transform to modernize a mainframe application and then deploy it to AWS infrastructure by using [Hashicorp Terraform](https://developer.hashicorp.com/terraform/intro). These step-by-step instructions help you transform [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo), which is a sample open source mainframe application, from COBOL to a modern Java application.

## Prerequisites and limitations
<a name="modernize-mainframe-app-transform-terraform-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Administrative permissions to create AWS resources and deploy applications
+ Terraform version 1.5.7 or higher, [configured](https://developer.hashicorp.com/terraform/tutorials/aws-get-started?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS)
+ AWS Provider for Terraform, [configured](https://registry.terraform.io/providers/hashicorp/aws/2.36.0/docs#authentication)
+ AWS IAM Identity Center, [enabled](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html)
+ AWS Transform, [enabled](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html)
+ A user, [onboarded](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-management.html) to an AWS Transform workspace with a contributor role that can run transformation jobs

**Limitations**
+ AWS Transform is available only in some AWS Regions. For a complete list of supported Regions, see [Supported Regions for AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/regions.html).
+ There is a service quota for mainframe transformation capabilities in AWS Transform. For more information, see [Quotas for AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-limits.html).
+ To collaborate on a shared workspace, all users must be registered users of the same instance of AWS IAM Identity Center that is associated with your instance of the AWS Transform web application.
+ The Amazon Simple Storage Service (Amazon S3) bucket and AWS Transform must be in the same AWS account and Region.

## Architecture
<a name="modernize-mainframe-app-transform-terraform-architecture"></a>

The following diagram shows the end-to-end modernization of the legacy application and deployment to the AWS Cloud. Application and database credentials are stored in AWS Secrets Manager, and Amazon CloudWatch provides monitoring and logging capabilities.

![AWS Transform modernizing a mainframe application and deployment through Terraform.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/78bc1e6e-cd3d-4c6d-ae4b-0675a6898fd9/images/332ccf35-f55a-449e-a05d-7e321b3867b7.png)

The diagram shows the following workflow:

1. Through AWS IAM Identity Center, the user authenticates and accesses AWS Transform in the AWS account.

1. The user uploads the COBOL mainframe code to the Amazon S3 bucket and initiates the transformation in AWS Transform.

1. AWS Transform modernizes the COBOL code into cloud-native Java code and stores the modernized code in the Amazon S3 bucket.

1. Terraform creates the AWS infrastructure to deploy the modernized application, including an Application Load Balancer, Amazon Elastic Compute Cloud (Amazon EC2) instance, and Amazon Relational Database Service (Amazon RDS) database. Terraform deploys the modernized code to the Amazon EC2 instance.

1. The VSAM files are uploaded to Amazon EC2 and are migrated from Amazon EC2 to the Amazon RDS database.

## Tools
<a name="modernize-mainframe-app-transform-terraform-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down. In this pattern, SQL Server failover cluster instances are installed on Amazon EC2 instances.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to your AWS accounts and cloud applications.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) uses agentic AI to help you accelerate the modernization of legacy workloads, such as .NET, mainframe, and VMware workloads.

**Other tools**
+ [Apache Maven](https://maven.apache.org/) is an open source software project management and build automation tool for Java projects.
+ [Apache Tomcat](https://tomcat.apache.org/) is an open source Servlet container and web server for Java code.
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.
+ [Spring Boot](https://spring.io/projects/spring-boot) is an open source framework built on top of the Spring Framework in Java.

**Code repository**

The code for this pattern is available in the GitHub [Mainframe Transformation E2E](https://github.com/aws-samples/sample-mainframe-transformation-e2e) repository. This pattern uses the open source AWS [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) mainframe application as a sample application.

## Best practices
<a name="modernize-mainframe-app-transform-terraform-best-practices"></a>
+ Assign full ownership of code and resources targeted for migration.
+ Develop and test a proof of concept before scaling to a full migration.
+ Secure commitment from all stakeholders.
+ Establish clear communication channels.
+ Define and document minimum viable product (MVP) requirements.
+ Set clear success criteria.

## Epics
<a name="modernize-mainframe-app-transform-terraform-epics"></a>

### Prepare and upload the mainframe application code
<a name="prepare-and-upload-the-mainframe-application-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a bucket. | Create an Amazon S3 bucket in the same AWS account and Region where AWS Transform is enabled. You use this bucket to store the mainframe application code, data and additional scripts required to build and run the application. AWS Transform uses this bucket to store the refactored code and other files associated with the transformation. For instructions, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. | General AWS, AWS administrator |
| Set the CORS permissions for the bucket. | When setting up your bucket for AWS Transform access, you need to configure cross-origin resource sharing (CORS) for the bucket. If this is not set up correctly, you might not be able to use the inline viewing or file comparison functionalities of AWS Transform. For instructions about how to configure CORS for a bucket, see [Using cross-origin resource sharing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html) in the Amazon S3 bucket. For the policy, see [S3 bucket CORS permissions](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-setup-connector-s3) in the AWS Transform documentation. | General AWS, AWS administrator |
| Prepare the sample mainframe application code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | General AWS, App developer |

### Transform the mainframe application
<a name="transform-the-mainframe-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the AWS Transform job. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, App owner |
| Set up a connector. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, App owner |
| Transform the code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, App owner |

### Deploy the infrastructure through Terraform
<a name="deploy-the-infrastructure-through-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the templates. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html)For production or production-like environments, configure additional security components. For example, enable [AWS WAF protections for your Application Load Balancer](https://aws.amazon.com/about-aws/whats-new/2024/02/aws-application-load-balancer-one-click-waf-integrations/). | General AWS, AWS administrator |
| Deploy the infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | Terraform |

### Install and configure Apache Tomcat on the Amazon EC2 instance
<a name="install-and-configure-apache-tomcat-on-the-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the required software. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |
| Verify software installation. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |

### Compile and package the modernized application code
<a name="compile-and-package-the-modernized-application-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download and extract the generated code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |
| Build the modernized application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |

### Migrate the database
<a name="migrate-the-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the database and JICS schemas. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |
| Validate database creation. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |
| Migrate data to the JICS database. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |

### Install the modernized application
<a name="install-the-modernized-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the modernized application on the Amazon EC2 instance. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Cloud architect |
| Restart the Tomcat server. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Cloud architect |
| Migrate the VSAM dataset. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Migration engineer |
| Update the parameters in the Groovy scripts. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the modernized application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Test engineer |
| Verify the batch scripts. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | App developer, Test engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare to delete the infrastructure. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | General AWS |
| Delete the infrastructure. | These steps will permanently delete your resources. Make sure you have backed up any important data before proceeding.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) | General AWS |

## Troubleshooting
<a name="modernize-mainframe-app-transform-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Terraform authentication | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) |
| Tomcat-related errors | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-mainframe-app-transform-terraform.html) |
| URL name not loading | Make sure that the Application Load Balancer security group has your IP address in the inbound rule as a source. |
| Authentication issue in Tomcat log | Confirm that the database secret password in AWS Secrets Manager and the password in **server.xml** match. |

## Related resources
<a name="modernize-mainframe-app-transform-terraform-resources"></a>

**AWS Prescriptive Guidance**
+ [Modernize the CardDemo mainframe application by using AWS Transform](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-carddemo-mainframe-app.html)

**AWS service documentation**
+ [AWS Blu Age Blusam Adminstration Console](https://docs.aws.amazon.com/m2/latest/userguide/ba-shared-bac-userguide.html)
+ [Infrastructure setup requirements for AWS Blu Age Runtime (non-managed)](https://docs.aws.amazon.com/m2/latest/userguide/ba-infrastructure-setup.html)
+ [Onboarding AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-setup-onboard.html)
+ [Modernization of mainframe applications](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/transform-app-mainframe.html)
+ [Set up configuration for AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config.html)

**AWS blog posts**
+ [Accelerate Your Mainframe Modernization Journey using AI Agents with AWS Transform](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/)
