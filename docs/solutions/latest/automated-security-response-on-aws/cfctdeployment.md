---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/cfctdeployment.html
---

# AWS Control Tower (CT) deployment
<a name="cfctdeployment"></a>

The Customizations for AWS Control Tower (CfCT) guide is for administrators, DevOps professionals, independent software vendors, IT infrastructure architects, and systems integrators who want to customize and extend their AWS Control Tower environments for their company and customers. It provides information about customizing and extending the AWS Control Tower environment with the CfCT customization package.

 **Time to deploy:** Approximately 30 minutes

## Prerequisites
<a name="cfctprerequisites"></a>

Before deploying this solution, ensure that it is intended for **AWS Control Tower administrators**.

When you’re ready to set up your landing zone using the AWS Control Tower console or APIs, follow these steps:

To get started with AWS Control Tower, see: [Getting Started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)

To learn how to customize your landing zone, refer to: [Customizing Your Landing Zone](https://docs.aws.amazon.com/controltower/latest/userguide/customize-landing-zone.html)

To launch and deploy your landing zone, see: [Landing Zone Deployment Guide](https://docs.aws.amazon.com/controltower/latest/userguide/deployment.html)

## Deployment overview
<a name="cfctdeployment-overview"></a>

Use the following steps to deploy this solution on AWS.

 [Step 1: Build and deploy S3 bucket](#step-1-cfn)

**Note**
S3 bucket Configuration – for ADMIN only. This is a one-time setup step and should not be repeated by end users. The S3 buckets store the deployment package, including the AWS CloudFormation template and Lambda code required for ASR to run. These resources are deployed using CfCt or StackSet.

**1. Configure the S3 Bucket**
Set up the S3 bucket that will be used for storing and serving your deployment packages.

**2. Set Up the Environment**
Prepare the necessary environment variables, credentials, and tools required for the build and deployment process.

**3. Configure S3 Bucket Policies**
Define and apply the appropriate bucket policies to control access and permissions.

**4. Prepare the Build**
Compile, package, or otherwise prepare your application or assets for deployment.

**5. Deploy Packages to S3**
Upload the prepared build artifacts to the designated S3 bucket.

 [Step 2: Stacks deployment to AWS Control Tower](#step-2-cfn)

**1. Create Build Manifest for ASR Components**
Define a build manifest that lists all ASR components, their versions, dependencies, and build instructions.

**2. Update the CodePipeline**
Modify the AWS CodePipeline configuration to include the new build steps, artifacts, or stages required for deploying the ASR components.

## Step 1: Build and deploy to S3 bucket
<a name="step-1-cfn"></a>

AWS Solutions use two buckets: a bucket for global access to templates, which is accessed via HTTPS, and regional buckets for access to assets within the region, such as Lambda code.

**1. Configure the S3 Bucket**
Pick a unique bucket name, for example, asr-staging. Set two environment variables on your terminal, one should be the base bucket name with -reference as suffix, the other with your intended deployment region as suffix:

```
export BASE_BUCKET_NAME=asr-staging-$(date +%s)
export TEMPLATE_BUCKET_NAME=$BASE_BUCKET_NAME-reference
export REGION=us-east-1
export ASSET_BUCKET_NAME=$BASE_BUCKET_NAME-$REGION
```

**2. Environment Setup**
In your AWS account, create two buckets with these names, for example, asr-staging-reference and asr-staging-us-east-1. (The reference bucket will hold the CloudFormation templates, the regional bucket will hold all other assets like the lambda code bundle.) Your buckets must be encrypted and must disallow public access

```
aws s3 mb s3://$TEMPLATE_BUCKET_NAME/
aws s3 mb s3://$ASSET_BUCKET_NAME/
```

**Note**
When creating your buckets, ensure they are not publicly accessible. Use random bucket names. Disable public access. Use KMS encryption. And verify bucket ownership before uploading.

**3. S3 buckets policy setup**
Update the $TEMPLATE\_BUCKET\_NAME S3 bucket policy to include PutObject permissions for the execute account ID. Assign this permission to an IAM role within the execute account that is authorized to write to the bucket. This setup allows you to avoid creating the bucket in the Management account.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::template-bucket-name/*",
                "arn:aws:s3:::template-bucket-name"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "org-id"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": [
                "arn:aws:s3:::template-bucket-name/*",
                "arn:aws:s3:::template-bucket-name"
            ],
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": "arn:aws:iam::account-id:role/iam-role-name"
                }
            }
        }
    ]
}
```

Alter the asset S3 bucket policy to include permissions. Assign this permission to an IAM role within the execute account that is authorized to write to the bucket. Repeat this setup for each regional asset bucket (for example, asr-staging-us-east-1, asr-staging-eu-west-1, and so on), allowing deployments across multiple Regions without needing to create the buckets in the Management account.

**4. Build Preparation**
+ Prerequisites:
  + AWS CLI v2
  + Python 3.11\+ with pip
  + AWS CDK 2.171.1\+
  + Node.js 22\+ with npm
  + Poetry v2 with plugin to export
+ Git clone [automated-security-response-on-aws GitHub repository](https://github.com/aws-solutions/automated-security-response-on-aws.git)

First ensure that you’ve run npm install in the source folder.

Next from the deployment folder in your cloned repo, run build-s3-dist.sh, passing the root name of your bucket (for example, mybucket) and the version you are building (for example, v1.0.0). Use a semver version based on the version downloaded from GitHub (for example, GitHub: v1.0.0, your build: v1.0.0.mybuild).

```
chmod +x build-s3-dist.sh
export SOLUTION_NAME=automated-security-response-on-aws
export SOLUTION_VERSION=v1.0.0.mybuild
./build-s3-dist.sh -b $BASE_BUCKET_NAME -v $SOLUTION_VERSION
```

 **5. Deploy packages to S3**

```
cd deployment
aws s3 cp global-s3-assets/  s3://$TEMPLATE_BUCKET_NAME/$SOLUTION_NAME/$SOLUTION_VERSION/ --recursive
aws s3 cp regional-s3-assets/  s3://$ASSET_BUCKET_NAME/$SOLUTION_NAME/$SOLUTION_VERSION/ --recursive
```

## Step 2: Stacks deployment to AWS Control Tower
<a name="step-2-cfn"></a>

**1. Build manifest for ASR components**
After deploying ASR artifacts to the S3 buckets, update the AWS Control Tower [pipeline manifest](https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-byo-customizations.html) to reference the new version, and then trigger the pipeline run. For more information, see [AWS Control Tower deployment](https://docs.aws.amazon.com/controltower/latest/userguide/deployment.html).

**Important**
For correct deployment of the ASR solution, refer to the official AWS documentation for detailed information on the CloudFormation templates overview and parameters description. Info links below: [CloudFormation Templates](aws-cloudformation-template.md) [Parameters overview Guide](deployment.md)

The manifest for the ASR components looks like this:

```
region: us-east-1 #<HOME_REGION_NAME>
version: 2021-03-15

# Control Tower Custom CloudFormation Resources
resources:
  - name: <ADMIN STACK NAME>
    resource_file: s3://<ADMIN TEMPLATE BUCKET path>
    parameters:
      - parameter_key: UseCloudWatchMetricsAlarms
        parameter_value: "yes"
      - parameter_key: TicketGenFunctionName
        parameter_value: ""
      - parameter_key: ShouldDeployWebUI
        parameter_value: "yes"
      - parameter_key: AdminUserEmail
        parameter_value: "<YOUR EMAIL ADDRESS>"
      - parameter_key: LoadSCAdminStack
        parameter_value: "yes"
      - parameter_key: LoadCIS120AdminStack
        parameter_value: "no"
      - parameter_key: LoadCIS300AdminStack
        parameter_value: "no"
      - parameter_key: UseCloudWatchMetrics
        parameter_value: "yes"
      - parameter_key: LoadNIST80053AdminStack
        parameter_value: "no"
      - parameter_key: LoadCIS140AdminStack
        parameter_value: "no"
      - parameter_key: ReuseOrchestratorLogGroup
        parameter_value: "yes"
      - parameter_key: LoadPCI321AdminStack
        parameter_value: "no"
      - parameter_key: RemediationFailureAlarmThreshold
        parameter_value: "5"
      - parameter_key: LoadAFSBPAdminStack
        parameter_value: "no"
      - parameter_key: EnableEnhancedCloudWatchMetrics
        parameter_value: "no"
    deploy_method: stack_set
    deployment_targets:
     accounts: # :type: list
        - <ACCOUNT_NAME> # and/or
        - <ACCOUNT_NUMBER>
    regions:
      - <REGION_NAME>

  - name:  <ROLE MEMBER STACK NAME>
    resource_file: s3://<ROLE MEMBER TEMPLATE BUCKET path>
    parameters:
      - parameter_key: SecHubAdminAccount
        parameter_value: <ADMIN_ACCOUNT_NAME>
      - parameter_key: Namespace
        parameter_value: <NAMESPACE>
    deploy_method: stack_set
    deployment_targets:
      organizational_units:
        - <ORG UNIT>

  - name:  <MEMBER STACK NAME>
    resource_file: s3://<MEMBER TEMPLATE BUCKET path>
    parameters:
      - parameter_key: SecHubAdminAccount
        parameter_value: <ADMIN_ACCOUNT_NAME>
      - parameter_key: LoadCIS120MemberStack
        parameter_value: "no"
      - parameter_key: LoadNIST80053MemberStack
        parameter_value: "no"
      - parameter_key: Namespace
        parameter_value: <NAMESPACE>
      - parameter_key: CreateS3BucketForRedshiftAuditLogging
        parameter_value: "no"
      - parameter_key: LoadAFSBPMemberStack
        parameter_value: "no"
      - parameter_key: LoadSCMemberStack
        parameter_value: "yes"
      - parameter_key: LoadPCI321MemberStack
        parameter_value: "no"
      - parameter_key: LoadCIS140MemberStack
        parameter_value: "no"
      - parameter_key: EnableCloudTrailForASRActionLog
        parameter_value: "no"
      - parameter_key: LogGroupName
        parameter_value: <LOG_GROUP_NAME>
      - parameter_key: LoadCIS300MemberStack
        parameter_value: "no"
    deploy_method: stack_set
    deployment_targets:
      accounts: # :type: list
        - <ACCOUNT_NAME> # and/or
        - <ACCOUNT_NUMBER>
      organizational_units:
        - <ORG UNIT>
    regions: # :type: list
      - <REGION_NAME>
```

**2. Code pipeline update**
Add a manifest file to a custom-control-tower-configuration.zip and run a CodePipeline, refer to: [code pipeline overview](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-codepipeline-overview.html)

You can verify the deployment by checking the AWS Control Tower pipeline status in the AWS CodePipeline console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
