---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/addf-architecture-terminology.html
---

# ADDF architecture and terminology
<a name="addf-architecture-terminology"></a>

Before you can understand the security and operational topics in this guide, it's important to have a high-level understanding of the terminology, components, and architecture of Autonomous Driving Data Framework (ADDF). This section consists of the following topics:
+ [ADDF terminology](#addf-terminology)
+ [ADDF architecture](#addf-architecture)

## ADDF terminology
<a name="addf-terminology"></a>

The key terminology for ADDF is as follows:
+ **ADDF module** – A module is infrastructure as code (IaC) that implements a common task in an advanced driver-assistance system (ADAS). Common tasks include configuring centralized data storage, data processing pipelines, visualization mechanisms, search interfaces, simulation workloads, analytics interfaces, and prebuilt dashboards. You can create a module based on your requirements, or you can re-use or customize an existing module.

  You can use the AWS Cloud Development Kit (AWS CDK) to define ADDF modules, or you can use any common IaC framework, such as Hashicorp Terraform or AWS CloudFormation, to implement the ADDF modules. A module has a set of input parameters. Input parameters can depend on output values from other modules. An ADDF module is the smallest unit of deployment for an ADDF target AWS account.
+ **ADDF deployment manifest file** – This file defines an orchestration of standalone ADDF modules. *Orchestration* refers to the deployment order of the modules. In the ADDF deployment manifest file, you can use *ADDF groups* to group related modules together. In this file, you also define the ADDF toolchain AWS account, the ADDF target AWS accounts, and the target AWS Regions.
+ **ADDF deployment framework** – This framework deploys ADDF modules into the ADDF target AWS accounts based on the orchestration defined in the ADDF deployment manifest file. The ADDF deployment framework is implemented by using the following AWS open-source projects:
  + [SeedFarmer](https://github.com/awslabs/seed-farmer) (GitHub) – SeedFarmer is the CLI tool used for ADDF deployments. It manages each module state, prepares and packages the module code, creates the least-privilege policies for the ADDF deployment roles, and provides semantic instructions that CodeSeeder uses for deployment. You can interact directly with SeedFarmer to run ADDF deployments, or you can integrate it into a continuous integration and continuous deployment (CI/CD) pipeline.
  + [CodeSeeder](https://github.com/awslabs/aws-codeseeder) (GitHub) – CodeSeeder deploys arbitrary infrastructure as code packages through an AWS CodeBuild job. SeedFarmer automatically orchestrates and runs CodeSeeder. Only SeedFarmer directly interacts with CodeSeeder.

  The ADDF deployment framework is designed to support deployments in single-account and multi-account architectures. Based on your organization's requirements, you decide whether a single-account or multi-account architecture is required.
+ **ADDF toolchain AWS account** – This account orchestrates and manages the deployment of modules into the ADDF target AWS accounts, based on the definitions in the ADDF deployment manifest file. An ADDF deployment can only have one ADDF toolchain AWS account. In a single-account architecture, the ADDF toolchain AWS account is also the ADDF target AWS account. This account contains an AWS Identity and Access Management (IAM) role, called *ADDF toolchain IAM role*, which is assumed by SeedFarmer during the ADDF deployment process. In this guide, we refer to an ADDF toolchain AWS account as a *toolchain account*.
+ **ADDF target AWS accounts** – These are the target accounts where you are deploying ADDF modules. You can have one or more target accounts. These accounts contain the resources and application logic described in the ADDF deployment manifest file and its mapped modules. In a single-account architecture, the ADDF target AWS account is also the ADDF toolchain AWS account. Each ADDF target account contains an IAM role, called *ADDF deployment IAM role*, that is assumed by CodeSeeder during the deployment process. In this guide, we refer to an ADDF target AWS account as a *target account*.
+ **ADDF instance **– When you deploy ADDF and your modules in the cloud, as defined in your ADDF deployment manifest file, this becomes an *ADDF instance*. An ADDF instance can have a single-account or multi-account architecture, and you can deploy multiple ADDF instances. For more information about choosing the number of instances and designing an account architecture for your use case, see [Defining your ADDF architecture](defining-your-addf-architecture.md).

## ADDF architecture
<a name="addf-architecture"></a>

The following diagram shows a high-level architecture for an ADDF instance in the AWS Cloud. It shows a multi-account architecture, including a dedicated toolchain account and two target accounts. This guide discusses the end-to-end process of using ADDF to deploy resources to the target accounts.

![ADDF local code, deployment manifest file, and AWS architecture with toolchain and target accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/images/guide-img/b7c99a03-2a36-4dc2-9b13-9b2a1cbf7eb9/images/1f24d28f-7e67-4f5d-bf05-a79f75b470b9.png)

1. **Create and bootstrap the ADDF AWS accounts.**

   To function properly, each account must be bootstrapped to ADDF and to AWS CDK. If this a new ADDF deployment or you are adding new target accounts, do the following:

   1. Bootstrap AWS CDK in the toolchain account and each target account. For instructions, see [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (AWS CDK documentation). ADDF uses AWS CDK to deploy its infrastructure.

   1. Bootstrap ADDF in the toolchain account and each target account. For instructions, see *Bootstrap AWS Account(s)* in the [ADDF Deployment Guide](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/docs/deployment_guide.md). This sets up all ADDF-specific IAM roles required by SeedFarmer and CodeSeeder.
**Note**
You need to perform this step only if you're initially deploying ADDF or adding new target accounts. This step is not part of reoccurring ADDF deployments to already established ADDF instances.

1. **Create or customize the ADDF modules.**

   Create or customize ADDF modules based on the specific problem you are trying to solve. Your module should represent an isolated task or group of tasks. Define the input parameters for the module as needed, and use the module output values as input parameters for other modules.

1. **Define the module orchestration in the ADDF deployment manifest file.**

   In the ADDF manifest file, organize modules into groups and define the deployment order and dependencies between them. In this file, you also specify the single toolchain account and the target accounts (including AWS Regions) for each ADDF group and its modules.

1. **Evaluate the ADDF deployment manifest file and establish the deployment scope.**

   The ADDF developer or a CI/CD pipeline, such as AWS CodePipeline, starts an evaluation of the ADDF deployment manifest file by calling the CLI tool, SeedFarmer. To start the evaluation:
   + SeedFarmer uses the ADDF deployment manifest file as an input parameter for the evaluation.
   + To assume the ADDF toolchain IAM role, SeedFarmer expects the same, valid IAM role or user credentials that was defined during the ADDF bootstrap process, in step 1.

   If SeedFarmer does not have the correct credentials to assume the ADDF toolchain IAM role or can't access the ADDF deployment manifest file, the evaluation does not start.

   If SeedFarmer can start the evaluation, it assumes the ADDF toolchain IAM role in the toolchain account. From there, SeedFarmer can access any target account, by assuming the ADDF deployment IAM role in that account. SeedFarmer then tries to read any ADDF metadata in the toolchain account and target accounts. One of the following happens:
   + If there is no ADDF metadata to read, that indicates that this is a new ADDF instance. SeedFarmer determines that the deployment scope is the entire the ADDF deployment manifest file and its contents.
   + If ADDF metadata exists, SeedFarmer compares the ADDF deployment manifest file and its contents to the MD5 hashes of the existing deployed artifacts in the target accounts. If deployable changes are detected, this process continues. If no deployable changes are detected, the process is complete.

1. **Deploy the in-scope ADDF modules to the target accounts.**

   CodeSeeder now has an ordered list of deployments to run, according to the ADDF deployment manifest file and the evaluation results from the previous step. Based on that ordered list, CodeSeeder assumes the ADDF deployment IAM role in each associated target account. It then runs CodeSeeder in an AWS CodeBuild job to create or update the individual IaC deployments, such as AWS CDK applications, for the ADDF module. By default, ADDF uses AWS CDK as its IaC framework, but other common IaC frameworks are also supported. After the process is complete for each target account, you have a fully deployed, cross-account, end-to-end ADAS-based workflow, as you defined in the ADDF deployment manifest file.

   If you use a single-account architecture, the toolchain account and the target accounts are the same account, and the one account has all of the described functionality.

1. **Use the ADDF-deployed infrastructure.**

   An ADAS developer can use the deployed ADAS-based workflow, as defined by your use case.

   This workflow describes the architecture of a single instance of an ADDF multi-account environment. Depending on your development, deployment, and operations model, we recommend that you run multiple ADDF instances in a multi-stage environment. A typical setup might include a dedicated ADDF instance with dedicated AWS accounts for each deployment stage, such as branches for development, testing, and production. You can also run multiple ADDF instances in the same single-account or multi-account environment in the same AWS Region, assuming that you created a unique resource namespace for each ADDF instance. For more information, see [Defining your ADDF architecture](defining-your-addf-architecture.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
