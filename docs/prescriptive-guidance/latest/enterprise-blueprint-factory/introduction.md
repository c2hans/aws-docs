---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/introduction.html
---

# Building an Enterprise Blueprint Factory by using AWS Service Catalog
<a name="introduction"></a>

*Haofei Feng, Joe Guo, Shreejesh MV, and Cam Maxwell, Amazon Web Services*

## Business overview
<a name="business-overview"></a>

Many enterprises face challenges when scaling their workloads in the cloud. These organizational challenges include the following:
+ Creating infrastructure as code (IaC) templates that can be reused at scale for multiple AWS services
+ Validating that IaC templates follow security best practices
+ Reducing undifferentiated or repetitive tasks that can significantly reduce developer productivity and extend the time to market
+ Establishing consistency for IaC templates
+ Reducing resource utilization, particularly for the security team, to avoid repeatable manual reviews

Creating an IaC template that follows security best practices requires that you establish guardrails and security controls. Traditionally, the cloud platform team or security team would manually review the code in each IaC template. Alternatively, developers would deploy the IaC template in non-production environment and rely on detective controls to find any security issues. Both of these approaches require iterative feedback cycles, slow down the development process, and increase the manual engineering effort.

As a result, many enterprises want to streamline the creation, validation, and release of IaC templates. They also want a means of managing and governing those templates after release. Proper management and governance mechanisms help you update templates and make sure that developers have access to the latest versions. These mechanisms also help you oversee and audit the use of templates across the organization.

## Solution overview
<a name="solution-overview"></a>

This guide explains the Enterprise Blueprint Factory solution, which helps you streamline the creation, validation, publishing, distribution, and consumption of infrastructure as code (IaC) templates across your organization. These IaC templates are also called *blueprints*. This solution supports blueprint files that are AWS CloudFormation [templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html#cfn-concepts-templates) or AWS Cloud Development Kit (AWS CDK) [constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html).

The Enterprise Blueprint Factory uses a config-driven approach to automate the sharing, publishing, and distribution of blueprints. A developer adds a blueprint to a product repository and then adds the blueprint information to a config file. This automatically initiates a continuous integration and continuous delivery (CI/CD) release pipeline. This pipeline validates that the blueprint follows AWS security best practices. This helps make sure that your organization's blueprints are secure by design. *Security by design* is a system engineering approach that takes security into account through the whole development process.

The Enterprise Blueprint Factory releases blueprints as *products* in [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html). By using Service Catalog, end users can quickly deploy the approved blueprints that you provide. Service Catalog is also designed to provide management and governance features so that administrators can define fine-grained access controls and oversee blueprint usage.

## Intended audience
<a name="intended-audience"></a>

The [Enterprise Blueprint Factory architecture](architecture.md) section helps architects, managers, and technical leads evaluate this solution and determine whether it is a good fit for their organization. This section describes what blueprints are, how you can use Service Catalog to manage them, and the architecture of the Enterprise Blueprint Factory.

The [Setting up the Enterprise Blueprint Factory](setup.md) section helps DevOps engineers deploy the Enterprise Blueprint Factory in your AWS environment. It includes detailed instructions for setting up the required repositories and the configuration pipeline.

The [Using the Enterprise Blueprint Factory](using-factory.md) section helps blueprint developers create, update, or delete blueprints in your environment. It provides detailed instructions for managing a blueprint throughout its life cycle. To create blueprints, developers must understand how to create IaC templates, such as CloudFormation templates. This guide does not include information or instructions about how to define these blueprints.

## Objectives
<a name="objectives"></a>

The Enterprise Blueprint Factory helps your organization achieve the following benefits:
+ Validate that blueprints follow AWS security best practices
+ Automate and standardize the release and validation process for blueprints
+ Improve developer productivity by reducing the number of manual tasks they must perform
+ Use fine-grained access controls to determine which blueprints end users can access
+ Use version control to manage blueprint updates and share them with end users
+ Help end users self-serve the discovery and launch of blueprints
+ Oversee and audit the use of blueprints across the organization
