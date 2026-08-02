---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/opt-in-regions.html
---

# Opt-in Regions
<a name="opt-in-regions"></a>

We built the opt-in Region configuration to help customers use the Landing Zone Accelerator on AWS solution in [opt-in Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable).

**Note**
Not all AWS services are available in all Regions, including the AWS opt-in Regions. We update our [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services) list daily with which services are available in which Regions.

You must initially launch Landing Zone Accelerator on AWS in a Region where CodeCommit, AWS CodeBuild, and AWS CodePipeline are available. This will deploy the default resources that are depicted in the [Architecture overview](architecture-overview.md).

The following installation instructions leverage opt-in AWS Regions. Following these instructions deploys the default resources into the management account for items 1-8 of the [architecture diagram](architecture-overview.md#architecture-diagram). Items 9-10 of the architecture diagram, centralized logging and workload accounts, deploy in the opt-in (target) AWS Region.

**Note**
While the Landing Zone Accelerator on AWS solution can help you align with frameworks and best practices, customers are responsible for their own security and compliance practices.

## Prerequisites
<a name="opt-in-prerequisites"></a>

To launch the Landing Zone Accelerator on AWS solution into opt-in AWS Regions, verify that the user who launches the solution can:
+  [Allow opt-in AWS Regions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws-enable-disable-regions.html)
+ Perform IAM administration tasks

## Architecture
<a name="opt-inarchitecture"></a>

 **Architecture diagram depicting Landing Zone Accelerator on AWS architecture in opt-in (Target) Regions.**

![image12](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image12.png)

## Deployment
<a name="opt-in-deployment"></a>

### Using an opt-in Region as the target Region
<a name="using-an-opt-in-region-as-the-target-region"></a>

Deploying this solution with the default parameters builds the environment depicted in the previous figure. The default parameters use the **Home Region** for the Landing Zone Accelerator on AWS [Core pipeline](awsaccelerator-pipeline.md) and the **Target Region** for [centralized logging](centralized-logging.md).

#### Step 1. Deploy the solution in your AWS Management account
<a name="step-1.-deploy-the-solution-in-your-aws-management-account"></a>

1. Identify the **Home Region** that you want to use. This Region must have Amazon S3, CodeBuild, and CodePipeline availability.
**Note**
Two main factors contribute to which Region to select as your **Home Region**: latency and cost. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. AWS services are priced differently from one Region to another.

1.  [Prepare for an AWS Organizations based installation (without AWS Control Tower)](prerequisites.md#for-aws-organizations-based-installation-without-aws-control-tower). Use the following notes to guide you:
   + For a new environment, set up AWS Organizations.
   + Create a **LogArchive** account and an **Audit/Security Tooling** account.
   + Create a **Security** OU and **Infrastructure** OU.

1.  [Set up Landing Zone Accelerator on AWS in your AWS standard account](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/automated-deployment.html).

#### Step 2. Allow your desired opt-in AWS Regions for all accounts
<a name="step-2.-allow-your-desired-opt-in-aws-regions-for-all-accounts"></a>

1. Sign in to your management account.

1.  [Allow the Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) you want to use.
**Note**
When you allow a Region, AWS prepares your account in that Region, such as by distributing your IAM resources to the Region. This process takes a few minutes for most accounts, but it can take several hours. You can’t use the Region until this process is complete.

1. Log in to the **LogArchive** and **Audit/Security Tooling** accounts to repeat the actions to allow the opt-in Regions that you want to use.

#### Step 3. Update the configuration file in your AWS Management account
<a name="step-3.-update-the-configuration-file-in-your-aws-management-account"></a>

1. Using your management account, update the `global-config.yaml` file to list the new Region under the `enabledRegions` option, as shown in the following sample. In the sample, Europe (London) (`eu-west-2`) is the home Region and Middle East (Bahrain) (`me-south-1`) is the opt-in (target) Region:

   ```
   homeRegion: eu-west-2
   enabledRegions:
     - eu-west-2
     - me-south-1
   ```

1. Using your management account, update the `global-config.yaml` file to list the opt-in Region under the `centralizedLoggingRegion` option, as shown in the following sample:

   ```
   logging:
     account: LogArchive
     centralizedLoggingRegion: me-south-1
     cloudtrail:
       enable: true
       organizationTrail: true
       organizationTrailSettings:
         multiRegionTrail: true
         globalServiceEvents: true
         managementEvents: true
         s3DataEvents: true
         lambdaDataEvents: true
         sendToCloudWatchLogs: true
         apiErrorRateInsight: false
         apiCallRateInsight: false
       accountTrails: []
       lifecycleRules: []
     sessionManager:
       sendToCloudWatchLogs: false
       sendToS3: false
       excludeRegions: []
       excludeAccounts: []
       lifecycleRules: []
       attachPolicyToIamRoles: []
   ```

1. After the commit, confirm that the pipeline runs successfully.
