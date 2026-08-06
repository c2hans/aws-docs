---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/mainframe-modernization-devops-on-aws-with-micro-focus.html
---

# Mainframe modernization: DevOps on AWS with Rocket Software Enterprise Suite
<a name="mainframe-modernization-devops-on-aws-with-micro-focus"></a>

*Kevin Yung, Amazon Web Services*

## Summary
<a name="mainframe-modernization-devops-on-aws-with-micro-focus-summary"></a>

**Customer challenges**

Organizations that run core applications on mainframe hardware usually encounter a few challenges when the hardware needs to scale up to meet the demands of digital innovations. These challenges include the following constraints.
+ Mainframe development and test environments are unable to scale due to the inflexibility of mainframe hardware components and the high cost of changing.
+ Mainframe development is facing skill shortages, because new developers are not familiar and not interested in the traditional mainframe development tools. Modern technology such as containers, continuous integration/continuous delivery (CI/CD) pipelines, and modern test frameworks are not available in mainframe development.

**Pattern outcomes**

To address these challenges, Amazon Web Services (AWS) and Rocket Software Micro Focus, an AWS Partner Network (APN) Partner, have collaborated to create this pattern. The solution is designed to help you achieve the following outcomes.
+ Improved developer productivity. Developers can be given new mainframe development instances within minutes.
+ Use of the AWS Cloud to create new mainframe test environments with virtually unlimited capacity.
+ Rapid provisioning of new mainframe CI/CD infrastructure. Provisioning on AWS can be completed within an hour by using AWS CloudFormation and AWS Systems Manager.
+ Native use of AWS DevOps tools for mainframe development, including AWS CodeBuild, AWS CodeCommit, AWS CodePipeline, AWS CodeDeploy, and Amazon Elastic Container Registry (Amazon ECR).
+ Transform traditional waterfall development to agile development in mainframe projects.

**Technologies summary**

In this pattern, the target stack contains the following components.

|
|
| Logical components | Implementation solutions | Description |
| --- |--- |--- |
| Source code repositories | Rocket Software AccuRev Server, CodeCommit, Amazon ECR  | Source code management – The solution uses two types of source code: + Mainframe source code, for example, COBOL and JCL. <br />+ AWS infrastructure templates and automation scripts <br />Both types of source code need version control, but they are managed in different SCMs. Source code deployed into mainframe or Rocket Software Enterprise Servers is managed in Rocket Software Micro Focus AccuRev Server. AWS templates and automation scripts are managed in CodeCommit. Amazon ECR is used for the Docker image repositories.  |
| Enterprise developer instances | Amazon Elastic Compute Cloud (Amazon EC2), Rocket Software Enterprise Developer for Eclipse | Mainframe developers can develop code in Amazon EC2 by using Rocket Software Enterprise Developer for Eclipse. This eliminates the need to rely on mainframe hardware to write and test code.  |
| Rocket Software Enterprise Suite license management | Rocket Software Enterprise Suite License Manager | For centralized Rocket Software Enterprise Suite license management and governance, the solution uses Rocket Software Enterprise Suite License Manager to host the required license. |
| CI/CD pipelines | CodePipeline, CodeBuild, CodeDeploy, Rocket Software Enterprise Developer in a container, Rocket Software Enterprise Test Server in a container, Rocket Software Micro Focus Enterprise Server | Mainframe development teams need CI/CD pipelines to perform code compilation, integration tests, and regression tests. In AWS, CodePipeline and CodeBuild can work with Rocket Software Enterprise Developer and Enterprise Test Server in a container natively. |

## Prerequisites and limitations
<a name="mainframe-modernization-devops-on-aws-with-micro-focus-prereqs"></a>

**Prerequisites **

|
|
| Name | Description |
| --- |--- |
| py3270 | py3270 is a Python interface to x3270, an IBM 3270 terminal emulator. It provides an API to a x3270 or s3270 subprocess. |
| x3270 | x3270 is an IBM 3270 terminal emulator for the X Window System and Windows.  This can be used by developer for unit testing locally. |
| Robot-Framework-Mainframe-3270-Library | Mainframe3270 is a library for Robot Framework based on py3270 project. |
| Rocket Software Verastream | Rocket Software Verastream is an integration platform that enables testing mainframe assets the way that mobile apps, web applications, and SOA web services are tested. |
| Rocket Software Unified Functional Testing (UFT) installer and license | Rocket Software Unified Functional Testing is software that provides functional and regression test automation for software applications and environments. |
| Rocket Software Enterprise Server installer and license | Enterprise Server provides the runtime environment for mainframe applications. |
| Rocket Software Enterprise Test Server installer and license | Rocket Software Enterprise Test Server is an IBM mainframe application test environment. |
| Rocket Software AccuRev installer and license for Server, and Rocket Software Micro Focus AccuRev installer and license for Windows and Linux operating systems  | AccuRev provides source code management (SCM). The AccuRev system is designed for use by a team of people who are developing a set of files. |
| Rocket Software Enterprise Developer for Eclipse installer, patch and license | Enterprise Developer provide mainframe developer a platform to develop and maintain the core mainframe online and batch applications. |

**Limitations **
+ Building a Windows Docker image is not supported in CodeBuild. This [reported issue](https://github.com/docker-library/docker/issues/49) needs support from Windows Kernel/HCS and Docker teams. The work-around is to create a Docker image build runbook by using Systems Manager. This pattern uses the work-around to build Rocket Software Enterpise Developer for Eclipse and Rocket Software Micro Focus Enterprise Test Server Container images.
+ Virtual private cloud (VPC) connectivity from CodeBuild is not supported in Windows yet, so the pattern does not use Rocket Software License Manager to manage licenses in OpenText Rocket Software Enterprise Developer and Rocket Software Enterprise Test Server containers.

**Product versions**
+ Rocket Software Enterprise Developer 5.5 or later
+ Rocket Software Enterprise Test Server 5.5 or later
+ Rocket Software Enterprise Server 5.5 or later
+ Rocket Software AccuRev 7.x or later
+ Windows Docker base image for Rocket Software Enterprise Developer and Enterprise Test Server: **microsoft/dotnet-framework-4.7.2-runtime**
+ Linux Docker base image for AccuRev client: **amazonlinux:2**

## Architecture
<a name="mainframe-modernization-devops-on-aws-with-micro-focus-architecture"></a>

**Mainframe environment**

In conventional mainframe development, the developers need to use mainframe hardware to develop and test programs. They face capacity limitations, for example restricted million instructions per second (MIPS) for the dev/test environment, and they must rely on the tools that are available on the mainframe computers.

In many organizations, mainframe development follows the waterfall development methodology, with teams relying on long cycles to release changes. These release cycles are usually longer than digital product development.

The following diagram shows multiple mainframe projects sharing mainframe hardware for their development. In mainframe hardware, it is expensive to scale out a development and test environment for more projects.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/84e717fc-5aea-41a6-977a-d7e7a7ca5da7.png)

*AWS*** architecture  **

This pattern extends mainframe development to the AWS Cloud. First, it uses AccuRev SCM to host the mainframe source code on AWS. Then it makes Enterprise Developer and Enterprise Test Server available for building and testing the mainframe code on AWS.

The following sections describe the pattern's three major components.

**1. SCM **

In AWS, the pattern uses AccuRev to create a set of SCM workspaces and version control for the mainframe source code. Its stream-based architecture enables parallel mainframe development for multiple teams. To merge a change, AccuRev uses the promote concept. To add that change to other workspaces, AccuRev uses the update concept.

At the project level, each team can create one or more streams in AccuRev to track project level changes. These are called project streams. These project streams are inherited from the same parent stream. The parent stream is used to merge the changes from different project streams.

Each project stream can promote code to AccuRev, and a promote post trigger is set up to initiate the AWS CI/CD pipeline. The successful build for a project stream change can be promoted to its parent stream for more regression tests.

Usually, the parent stream is called the system integration stream. When there is a promotion from a project stream to a system integration stream, a post promotion trigger initiates another CI/CD pipeline to run regression tests.

In addition to mainframe code, this pattern includes AWS CloudFormation templates, Systems Manager Automation documents, and scripts. Following infrastructure-as-code best practices, they are version-controlled in CodeCommit.

If you need to synchronize mainframe code back to a mainframe environment for deployment, Rocket Software provides the Enterprise Sync solution, which synchronizes code from the AccuRev SCM back to the mainframe SCM.

**2. Developer and test environments**

In a large organization, scaling more than a hundred or even more than a thousand mainframe developers is challenging. To address this constraint, the pattern uses Amazon EC2 Windows instances for development. On the instances, Enterprise Developer for Eclipse tools are installed. The developer can perform all mainframe code test and debugging locally on the instance.

AWS Systems Manager State Manager and Automation documents are used to automate the developer instance provisioning. The average time to create a developer instance is within 15 minutes. The following software and configurations are prepared:
+ AccuRev Windows client for checking out and committing source code into AccuRev
+ Enterprise Developers for Eclipse tool, for writing, testing, and debugging mainframe code locally
+ Open source testing frameworks Python behavior-driven development (BDD) test framework Behave, py3270, and the x3270 emulator for creating scripts to test applications
+ A Docker developer tool for building the Enterprise Test Server Docker image and testing the application in the Enterprise Test Server Docker container

In the development cycle, developers use the EC2 instance to develop and test mainframe code locally. When the local changes are tested successfully, developers promote the change into the AccuRev server.

**3. CI/CD pipelines**

In the pattern, CI/CD pipelines are used for integration tests and regression tests before deployment to the production environment.

As explained in the SCM section, AccuRev uses two types of streams: a project stream and an integration stream. Each stream is hooked up with CI/CD pipelines. To perform the integration between the AccuRev server and AWS CodePipeline, the pattern uses AccuRev post promotion script to create an event to initiate CI/CD.

For example, when a developer promotes a change to a project stream in AccuRev, it initiates a post promotion script to run in AccuRev Server. Then the script uploads the metadata of the change into an Amazon Simple Storage Service (Amazon S3) bucket to create an Amazon S3 event. This event will initiate a CodePipeline configured pipeline to run.

The same event-initiating mechanism is used for the integration stream and its associated pipelines.

In the CI/CD pipeline, CodePipeline uses CodeBuild with the AccuRev Linux client container to check out the latest code from the AccuRev streams. Then the pipeline starts CodeBuild to use the Enterprise Developer Windows container to compile the source code, and to use the Enterprise Test Server Windows container in CodeBuild to test mainframe applications.

The CI/CD pipelines are built using CloudFormation templates, and the blueprint will be used for new projects. By using the templates, it takes less than an hour for a project to create a new CI/CD pipeline in AWS.

To scale your mainframe test capability on AWS, the pattern builds out the Rocket Software DevOps test suite, Verastream and UFT server. By using the modern DevOps tools, you can run as many tests on AWS as you need.

An example mainframe development environment with Rocket Software on AWS is shown in the following diagram.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/27da6a52-4573-44cb-8716-1ac49430f618.png)

*Target technology stack *

This section provides a closer look at the architecture of each component in the pattern.

**1. Source code repository – AccuRev SCM **

AccuRev SCM is set up to manage mainframe source code versions. For high availability, AccuRev supports primary and replica modes. Operators can fail over to the replica when performing maintenance on the primary node.

To speed up the response of the CI/CD pipeline, the pattern uses Amazon CloudWatch Events to detect source code changes and initiate the start of the pipeline.

1. The pipeline is set up to use an Amazon S3 source.

1. A CloudWatch Events rule is set up to capture S3 events from a source S3 bucket.

1. The CloudWatch Events rule sets a target to the pipeline.

1. AccuRev SCM is configured to run a post promotion script locally after promotion is complete.

1. AccuRev SCM generates an XML file that contains the metadata of the promotion, and the script uploads the XML file to the source S3 bucket.

1. After the upload, the source S3 bucket sends events to match the CloudWatch Events rule, and the CloudWatch Events rule initiates the pipeline to run.

When the pipeline runs, it kicks off a CodeBuild project to use an AccuRev Linux client container to check out the latest mainframe code from an associated AccuRev stream.

The following diagram shows an AccuRev Server setup.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/e60345cc-2283-4b03-8f57-e3dac1770978.png)

**2. Enterprise Developer template**

The pattern uses Amazon EC2 templates to simplify creation of the developer instance. By using State Manager, it can apply software and license settings to EC2 instances consistently.

The Amazon EC2 template builds in its VPC context settings and default instance settings, and it follows enterprise tagging requirements. By using a template, a team can create their own new development instances.

When a developer instance starts, by associating with tags, Systems Manager uses State Manager to apply automation. The automation includes the following general steps.

1. Install Enterprise Developer software and install patches.

1. Install the AccuRev client for Windows.

1. Install the pre-configured script for developers to join the AccuRev stream. Initialize Eclipse workspaces.

1. Install development tools, including x3270, py3270, and Docker.

1. Configure license settings to point to a License Manager load balancer.

The following diagram shows an Enterprise developer instance created by the Amazon EC2 template, with software and configuration applied to the instance by State Manager. Enterprise developer instances connect to AWS License Manager to activate their license.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/7ca8f538-8362-4a11-a842-7ecff6fa0248.png)

**3.  CI/CD pipelines**

As explained in the AWS architecture section, in the pattern, there are project-level CI/CD pipelines and system integration pipelines. Each mainframe project team creates a pipeline or multiple CI/CD pipelines for building the programs that they are developing in a project. These project CI/CD pipelines check out source code from an associated AccuRev stream.

In a project team, developers promote their code in the associated AccuRev stream. Then the promotion initiates the project pipeline to build the code and run integration tests.

Each project CI/CD pipeline uses CodeBuild projects with the Enterprise Developer tool Amazon ECR image and Enterprise Test Server tool Amazon ECR image.

CodePipeline and CodeBuild are used to create the CI/CD pipelines. Because CodeBuild and CodePipeline have no upfront fees or commitments, you pay only for what you use. Compared to mainframe hardware, the AWS solution greatly reduces hardware provisioning lead time and lowers the cost of your testing environment.

In modern development, multiple test methodologies are used. For example, test-driven development (TDD), BDD, and Robot Framework. With this pattern, developers can use these modern tools for mainframe testing. For example, by using x3270, py3270 and the Behave python test tool, you can define an online application's behavior. You can also use build mainframe 3270 robot framework in these CI/CD pipelines.

The following diagram shows the team stream CI/CD pipeline.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/da59f837-2f23-404f-948b-41402cc6fe0c.png)

The following diagram shows the project CI/CD test report produced by CodePipeline in Mainframe3270 Robot Framework.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/4752321a-c60d-455c-ac2f-6f0e2bc3dca0.png)

The following diagram shows the project CI/CD test report produced by CodePipeline in Py3270 and Behave BDD.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/d005466e-aeb8-4fd6-8342-743ed049f98a.png)

After project level tests are passed successfully, the tested code is manually promoted to the integration stream in AccuRev SCM. You can automate this step after the teams have a confidence on the tests coverage of their project pipeline.

When code is promoted, the system integration CI/CD pipeline checks out the merged code and performs regression tests. The merged code is promoted from all parallel project streams.

Depending on how fine grain the test environment is required, customers can have more system integration CI/CD pipelines in a different environment, for example UAT, Pre-Production.

In the pattern, the tools used in the system integration pipeline are Enterprise Test Server, UFT Server, and Verastream. All these tools can be deployed into the Docker container and used with CodeBuild.

After successfully testing of the mainframe programs, the artifact is stored, with version control, in an S3 bucket.

The following diagram shows a system integration CI/CD pipeline.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/693212e5-1cd0-4f82-a910-39b00d977c38.png)

After the artifact has been successfully tested in the system integration CI/CD pipelines, it can be promoted for production deployment.

If you need to deploy source code back to the mainframe, Rocket Software offers the Enterprise Sync solution to synchronize source code from AccuRev back to Mainframe Endeavour.

The following diagram shows a production CI/CD pipeline deploying the artifact into Enterprise Servers. In this example, CodeDeploy orchestrates the deployment of the tested mainframe artifact into Enterprise Server.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2359db4c-f351-45a6-8516-88a3b62e61f9/images/56749c2a-e038-4e56-9487-b2ff83894725.png)

In addition to the architecture walkthrough of the CI/CD pipeline, see the AWS DevOps blog post [Automate thousands of mainframe tests on AWS with the Micro Focus Enterprise Suite](https://aws.amazon.com/blogs/devops/automate-mainframe-tests-on-aws-with-micro-focus/) for more information on testing mainframe applications in CodeBuild and CodePipeline. (Micro Focus is now Rocket Software.) Refer to the blog post for the best practices and details of doing mainframe tests on AWS.

## Tools
<a name="mainframe-modernization-devops-on-aws-with-micro-focus-tools"></a>

**AWS automation tools**
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

**Rocket Software tools**
+ [Rocket Enterprise Developer for Eclipse](https://www.microfocus.com/documentation/enterprise-developer/ed60/ED-Eclipse/GUID-8D6B7358-AC35-4DAF-A445-607D8D97EBB2.html)
+ [Rocket Enterprise Test Server](https://www.microfocus.com/documentation/enterprise-developer/ed60/ETS-help/GUID-ECA56693-D9FE-4590-8798-133257BFEBE7.html)
+ [Rocket Enterprise Server](https://www.microfocus.com/documentation/enterprise-developer/es_60/) (production deployment)
+ [Rocket Software AccuRev](https://supportline.microfocus.com/documentation/books/AccuRev/AccuRev/6.2/webhelp/wwhelp/wwhimpl/js/html/wwhelp.htm)
+ [Rocket Software Enterprise Suite License Manager](https://www.microfocus.com/documentation/slm/)
+ [Rocket Software Verastream Host Integrator](https://www.microfocus.com/documentation/verastream-host-integrator/)
+ [Rocket Software UFT One](https://admhelp.microfocus.com/uft/en/24.4/UFT_Help/Content/User_Guide/Ch_UFT_Intro.htm)

**Other tools**
+ x3270
+ [py3270](https://pypi.org/project/py3270/)
+ [Robot-Framework-Mainframe-3270-Library](https://github.com/Altran-PT-GDC/Robot-Framework-Mainframe-3270-Library)

## Epics
<a name="mainframe-modernization-devops-on-aws-with-micro-focus-epics"></a>

### Create the AccuRev SCM infrastructure
<a name="create-the-accurev-scm-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy a primary AccuRev SCM server by using CloudFormation. |  | AWS CloudFormation |
| Create the AccuRev Administrator user. | Log in to AccuRev SCM Server, and run the CLI command to create an Administrator user. | AccuRev SCM Server Administrator |
| Create AccuRev streams. | Create AccuRev streams that inherit from upper streams in sequence: Production, System Integration, Team streams. | AccuRev SCM Administrator |
| Create the developer AccuRev login accounts. | Use AccuRev SCM CLI commands to create AccuRev users login accounts for mainframe developers. | AccuRev SCM Administrator |

### Create the Enterprise Developer Amazon EC2 launch template
<a name="create-the-enterprise-developer-ec2-launch-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Amazon EC2 launch template by using CloudFormation. | Use CloudFormation to deploy an Amazon EC2 launch template for Enterprise Developer instances. The template includes a Systems Manager Automation document for the Rocket Enterprise Developer instance. | AWS CloudFormation |
| Create the Enterprise Developer instance from the Amazon EC2 template. |  | AWS Console Login and Mainframe Developer Skills |

### Create the Enterprise Developer tool Docker image
<a name="create-the-enterprise-developer-tool-docker-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Enterprise Developer tool Docker image. | Use the Docker command and the Enterprise Developer tool Dockerfile to create the Docker image. | Docker |
| Create the Docker repository in Amazon ECR. | On the Amazon ECR console, create the repository for the Enterprise Developer Docker image. | Amazon ECR |
| Push the Enterprise Developer tool Docker image to Amazon ECR. | Run the Docker push command to push the Enterprise Developer tool Docker image to save it in the Docker repository in Amazon ECR. | Docker |

### Create the Enterprise Test Server Docker image
<a name="create-the-enterprise-test-server-docker-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Enterprise Test Server Docker image. | Use the Docker command and the Enterprise Test Server Dockerfile to create the Docker image. | Docker |
| Create the Docker repository in Amazon ECR. | On the Amazon ECR console, create the Amazon ECR repository for the Enterprise Test Server Docker image. | Amazon ECR |
| Push the Enterprise Test Server Docker image to Amazon ECR. | Run the Docker push command to push and save the Enterprise Test Server Docker image in Amazon ECR. | Docker |

### Create the team stream CI/CD pipeline
<a name="create-the-team-stream-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CodeCommit repository. | On the CodeCommit console, create a Git-based repository for infrastructure and CloudFormation code. | AWS CodeCommit |
| Upload the CloudFormation template and the automation code into the CodeCommit repository. | Run the Git push command to upload CloudFormation template and automation code into the repository. | Git |
| Deploy the team stream CI/CD pipeline by using CloudFormation. | Use the prepared CloudFormation template to deploy a team stream CI/CD pipeline. | AWS CloudFormation |

### Create the system integration CI/CD pipeline
<a name="create-the-system-integration-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the UFT Docker image. | Use the Docker command and the UFT Dockerfile to create the Docker image. | Docker |
| Create the Docker repository in Amazon ECR for the UFT image. | On the Amazon ECR console, create the Docker repository for the UFT image. | Amazon ECR |
| Push the UFT Docker image to Amazon ECR. | Run the Docker push command to push and save the Enterprise Test Server Docker image in Amazon ECR. | Docker |
| Create the Verastream Docker image. | Use the Docker command and the Verastream Dockerfile to create the Docker image. | Docker |
| Create the Docker repository in Amazon ECR for the Verastream image. | On the Amazon ECR console, create the Docker repository for the Verastream image. | Amazon ECR |
| Deploy the system integration CI/CD pipeline by using CloudFormation. | Use the prepared CloudFormation template to deploy a system integration CI/CD pipeline. | AWS CloudFormation |

### Create production deployment CI/CD pipeline
<a name="create-production-deployment-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy Enterprise Server by using the AWS Quick Start. | To deploy Enterprise Server by using CloudFormation, launch the Enterprise Server on AWS Quick Start. | AWS CloudFormation |
| Deploy a production deployment CI/CD pipeline. | On the CloudFormation console, use the CloudFormation template to deploy a production deployment CI/CD pipeline. | AWS CloudFormation |

## Related resources
<a name="mainframe-modernization-devops-on-aws-with-micro-focus-resources"></a>

**References**
+ [AWS DevOps Blog - Automate thousands of mainframe tests on AWS with the Micro Focus Enterprise Suite](https://aws.amazon.com/blogs/devops/automate-mainframe-tests-on-aws-with-micro-focus/) (Micro Focus is now Rocket Software.)
+ [py3270/py3270 GitHub repository](https://github.com/py3270/py3270)
+ [Altran-PT-GDC/Robot-Framework-Mainframe-3270-Library GitHub repository](https://github.com/Altran-PT-GDC/Robot-Framework-Mainframe-3270-Library)
+ [Welcome to behave\!](https://behave.readthedocs.io/en/latest/index.html)
+ [APN Partner Blog - Tag: Micro Focus](https://aws.amazon.com/blogs/apn/tag/micro-focus/) (Micro Focus is now Rocket Software.)
+ [Launching an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)

**AWS Marketplace**
+ [Rocket Software UFT One](https://aws.amazon.com/marketplace/pp/B01EGCA5OS?ref_=srh_res_product_title)

**AWS Quick Start**
+ [Rocket Enterprise Server on AWS](https://aws.amazon.com/quickstart/architecture/micro-focus-enterprise-server/)
