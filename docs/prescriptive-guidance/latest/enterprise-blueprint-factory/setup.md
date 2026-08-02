---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/setup.html
---

# Setting up the Enterprise Blueprint Factory
<a name="setup"></a>

This section helps you set up the Enterprise Blueprint Factory in your AWS environment. It includes detailed instructions for setting up the required repositories and the AWS resources for the Enterprise Blueprint Factory.

## Prerequisites
<a name="setup-prereqs"></a>

The following are the prerequisites for setting up the Enterprise Blueprint Factory in your AWS environment:
+ The following AWS accounts:
  + An account that is used to administrate the Enterprise Blueprint Factory and to release products
  + One or more accounts that consume the released product
+ All accounts are:
  + Managed as an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
  + Located in the same [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit)
  + The organization follows the [account-per-tenant model](https://aws.amazon.com/blogs/mt/managing-the-account-lifecycle-in-account-per-tenant-saas-environments-on-aws/)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Permissions to deploy an AWS CloudFormation stack that creates the following AWS resources:
  + Amazon CloudWatch Logs log group
  + AWS CodePipeline pipelines
  + AWS CodeBuild projects
  + Amazon EventBridge event bus policy and rule
  + AWS Identity and Access Management (IAM) role and policy
  + AWS Key Management Service (AWS KMS) key and key policy
  + AWS Service Catalog portfolios, products, and provisioned products
  + Amazon Simple Notification Service (Amazon SNS) topic, topic policy, and subscription
  + Amazon Simple Storage Service (Amazon S3) buckets
  + AWS Systems Manager Parameter Store parameters

  For more information about setting up these permissions, see the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) and [Implementing policies for least-privilege permissions for AWS CloudFormation](https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/introduction.html).
+ A GitHub account

## Best practices
<a name="setup-best-practices"></a>

We recommend that you follow these best practices when setting up the Enterprise Blueprint Factory in your AWS environment:
+ When configuring the permissions necessary to deploy the Enterprise Blueprint Factory, follow the principle of least privilege and grant the minimum permissions required. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the IAM documentation.
+ When configuring access to Service Catalog portfolios, follow the principle of least privilege and grant access only to specific roles, users, or administrators. Follow the [security best practices](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html) for Service Catalog.

## Creating the repositories
<a name="setup-create-repos"></a>

This section helps you set up the [configuration repository](architecture-components.md#architecture-config-repo) and the [product repository](architecture-components.md#architecture-product-repo) for the Enterprise Blueprint Factory. To set up your repositories, you [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the provided repositories in GitHub. Then, you use AWS CodeConnections to create a [connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-github.html) to your GitHub repository. Then, you clone the GitHub repositories to your local machine.

**To fork the GitHub repositories**

1. Log in to [GitHub](https://github.com/login).

1. Navigate to the [Configuration repo](https://github.com/aws-samples/aws-enterprise-blueprint-factory-config-repo) GitHub repository.

1. Choose **Fork**.

1. On the **Create a new fork** page, in the **Repository name** box, enter `ServiceCatalog-ConfigRepo`.

1. (Optional) Enter a description.

1. Select **Copy the main branch only**.

1. Choose **Create fork**.

1. Repeat these steps to fork the [Code repo](https://github.com/aws-samples/aws-enterprise-blueprint-factory-code-repo) GitHub repository. Enter the name `ServiceCatalog-CodeRepo` for this repository.

1. Repeat these steps to fork the [Product repo](https://github.com/aws-samples/aws-enterprise-blueprint-factory-blueprint-repo) GitHub repository. Enter the name `ServiceCatalog-BlueprintProductRepo` for this repository.

**To create the CodeConnections connection**

1. In the AWS CLI, enter the following command to create a CodeConnections connection to GitHub:

   ```
   aws codeconnections create-connection --provider-type GitHub --connection-name <MyConnection>
   ```

1. Use the AWS Developer Tools console to complete the connection. For more information, see [Update a pending connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-update.html).

**To clone the forked repositories**

1. Enter the following commands to clone the GitHub repositories to your local workstation:

   ```
   git clone git@github.com:<user>/aws-enterprise-blueprint-factory-config-repo ServiceCatalog-ConfigRepo
   git clone git@github.com:<user>/aws-enterprise-blueprint-factory-blueprint-repo ServiceCatalog-BlueprintProductRepo
   git clone git@github.com:<user>/aws-enterprise-blueprint-factory-code-repo ServiceCatalog-CodeRepo
   ```

## Setting up the Enterprise Blueprint Factory
<a name="setup-factory"></a>

The instructions in this section describe how to set up the Enterprise Blueprint Factory in your target account. The product repo that you cloned from GitHub contains two sample CloudFormation templates, `BP-S3` and `BP-SNS`. By following these instructions, you deploy these two sample blueprints as products in Service Catalog.

**To set up the roles**

1. In the Blueprint Developer's account, create the following trust policy, and then save it as `sc-enduserrole-trust-policy.json`:

   ```
   {
     "Version": "2012-10-17",
     "Statement": {
       "Effect": "Allow",
       "Principal": {
         "AWS": "arn:aws:iam::123456789012:role/ServiceCatalogEndUserRole"
       },
       "Action": "sts:AssumeRole"
     }
   }
   ```

1. Enter the following command to create the `ServiceCatalogEndUserRole` IAM role:

   ```
   aws iam create-role \
   --role-name ServiceCatalogEndUserRole \
   --assume-role-policy-document file://sc-enduserrole-trust-policy.json
   aws iam attach-role-policy \
   --policy-arn arn:aws:iam::aws:policy/AWSServiceCatalogEndUserFullAccess \
   -- role-name ServiceCatalogEndUserRole
   ```
**Note**
Developers use the `ServiceCatalogEndUserRole` role to provision the Service Catalog product. This role does not need permissions to create the resources defined in the blueprint. This follows the best practices of least privileged permissions and segregation of duties.

1. Create the following trust policy and then save it as `sc-launchconstraintrole-trust-policy.json`:

   ```
   {
     "Version": "2012-10-17",
     "Statement": {
       "Effect": "Allow",
       "Principal": {
         "Service": "servicecatalog.amazonaws.com"
       },
       "Action": "sts:AssumeRole"
     }
   }
   ```

1. Enter the following command to create the `ServiceCataloglogLaunchConstraintRole` IAM role:

   ```
   aws iam create-role \
   --role-name ServiceCataloglogLaunchConstraintRole \
   --assume-role-policy-document file://sc-launchconstraintrole-trust-policy.json
   aws iam attach-role-policy \
   --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess \
   --role-name ServiceCataloglogLaunchConstraintRole
   aws iam attach-role-policy \
   --policy-arn arn:aws:iam::aws:policy/AWSCloudFormationFullAccess \
   --role-name ServiceCataloglogLaunchConstraintRole
   ```

1. Add the following policy to the `ServiceCataloglogLaunchConstraintRole` IAM role. Include any other permissions that are required for the product resources, as described in [Configuring a Launch Role](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html#constraints-launch-role) in the Service Catalog documentation:

   ```
   {
             "Statement":[
         {
            "Effect":"Allow",
            "Action":[
               "s3:GetObject"
            ],
            "Resource":"*",
            "Condition":{
               "StringEquals":{
                  "s3:ExistingObjectTag/servicecatalog:provisioning":"true"
               }
            }
      ]
   }
   ```
**Note**
Service Catalog uses this role to deploy the CloudFormation stack as a product in Service Catalog. The trust policy for this role makes sure that only Service Catalog can assume it. Other users or services cannot assume this role. This follows the best practice of segregation of duties.

1. Create the following trust policy, and then save it as `sc-codebuild-trust-policy.json`:

   ```
   {
     "Version": "2012-10-17",
     "Statement": {
       "Effect": "Allow",
       "Principal": {
         "Service": "codebuild.amazonaws.com"
       },
       "Action": "sts:AssumeRole"
     }
   }
   ```

1. Enter the following command to create the `codebuild-servicecatalog-admin-role` IAM role:

   ```
   aws iam create-role \
   --role-name codebuild-servicecatalog-admin-role \
   --assume-role-policy-document file://sc-codebuild-trust-policy.json
   aws iam attach-role-policy \
   --policy-arn arn:aws:iam::aws:policy/AWSCodeBuildAdminAccess \
   --role-name codebuild-servicecatalog-admin-role
   ```
**Note**
The CodeBuild jobs in the config pipeline use this role.

**To set up the Amazon S3 bucket**

1. To create an Amazon Simple Storage Service (Amazon S3) bucket that is used to store the CodePipeline artifacts, follow the instructions in [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. Follow the [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html).

**To set up the AWS Systems Manager parameters**

1. Follow the instructions in [Creating Parameter Store parameters in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html) in order to create the Systems Manager parameters in the following table. These parameters are used in the CloudFormation template that deploys the configuration pipeline.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/setup.html)

**To update the CloudFormation templates**

1. In the code repository (`ServiceCatalog-CodeRepo`), open the **ServiceCatalog-Pipeline.yml** file.

1. Edit the default values for the following parameters in this file:
   + `ConfigRepositoryName` is the Systems Manager parameter that stores the GitHub repo where the Enterprise Blueprint Factory configuration files are stored. The default value is `/blueprints/resources/ConfigRepo`.
   + `CodeRepositoryName` is the Systems Manager parameter that stores the GitHub repo where the Enterprise Blueprint Factory configuration pipeline code and the `Bootstrapping-Admin-Product` code are stored. The default value is `/blueprints/resources/CodeRepo`.
   + `BlueprintRepositoryName` is the Systems Manager parameter that stores the GitHub repo where the Enterprise Blueprint Factory blueprints are stored. The default value is `/blueprints/resources/BlueprintRepo`.
   + `BranchName` is the branch of the config repository where the config file is stored. The default value is `main`.
   + `VPCID` is the Systems Manager parameter that stores the ID of the target VPC. The default value is `/blueprints/resources/vpc_id`.
   + `Subnets` is the Systems Manager parameter that stores the IDs of the target subnets. The default value is `/blueprints/resources/subnets`.
   + `SecurityGroupIds` is the Systems Manager parameter that stores the IDs of the target security groups. The default value is `/blueprints/resources/securitygroups`.
   + `IamRoleName` is the name of the IAM role that the CodeBuild jobs use. The default value is `codebuild-servicecatalog-admin-role`.
   + `EnvironmentType` is the environment where you are deploying the Enterprise Blueprint Factory. The default value is `DEV`.
   + `ArtifactBucket` is the Systems Manager parameter that stores the Amazon S3 bucket where CodePipeline stores artifacts. The default value is `/blueprints/resources/artifacts-bucket-name`.
   + `CodeConnectionArn` is the Amazon Resource Name (ARN) of the CodeConnections connection to GitHub.

1. Save and close the **ServiceCatalog-Pipeline.yml** file.

1. Enter the following commands to merge the changes into the code repository:

   ```
   cd ServiceCatalog-CodeRepo
   git add ServiceCatalog-Pipeline.yml
   git commit -m "<description of change>"
   git push origin main
   ```

1. In the configuration repository (`ServiceCatalog-ConfigRepo`), open the **bp\_config.yml** file.

1. Update the values in the portfolio section as needed for your organization. For example, update the `portfolio_access_roles` and `share_to_ou` attributes. For more information, see [Configuration file](architecture-components.md#architecture-config-file) in this guide.

1. Save and close the **bp\_config.yml** file.

1. Enter the following commands to merge the changes into the code repository:

   ```
   cd ServiceCatalog-ConfigRepo
   git add bp_config.yml
   git commit -m "<description of change>"
   git push origin main
   ```

**To deploy the CloudFormation stack**

1. Sign in to the Enterprise Blueprint Factory administrative account.

1. Switch to an IAM role that has [administrative permissions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html).

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the target AWS Region.

1. On the **Stacks** page, choose **Create stack** at top right, and then choose **With new resources (standard)**.

1. For **Prepare template**, choose **Template is ready**.

1. Under **Specify template**, choose **Upload a template file**.

1. Choose **Choose File**, navigate to the `ServiceCatalog-CodeRepo` folder, and then choose **ServiceCatalog-Pipeline.yml**.

1. Choose **Next** to continue and to validate the template.

1. For **Stack name**, enter a name for the stack.

1. In the **Parameters** section, do not change the default values.

1. Choose **Next**.

1. On the **Configure stack options **page, do not change the default values, and then choose **Next**.

1. On the **Review and create** page, verify the template and stack details, and then choose **Submit**.

1. Monitor the progress of the stack deployment. For more information, see the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/monitor-stack-progress.html).

1. Wait for the status to change to `CREATE_COMPLETE`.

**To validate the deployment**

1. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. In the navigation pane, choose **Products**.

1. Confirm that **ServiceCatalog-Pipeline** is available in the list of products.

1. Open the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home).

1. In **Name**, choose the configuration pipeline. By default, the pipeline name is `ServiceCatalog-Pipeline`.

1. Choose **View history**.

1. View the status of the pipeline and stage execution. For more information about the status, see [View execution status](https://docs.aws.amazon.com/codepipeline/latest/userguide/executions-view.html#pipelines-executions-status-console) in the CodePipeline documentation.

1. Wait until the configuration pipeline status is `Succeeded`.

1. Open the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. In the navigation pane, choose **Products**.

1. Confirm that the **BP-S3-Product** and **BP-SNS-Product** products are available. This indicates that the product release pipelines for the sample blueprints completed successfully.

1. If you want to delete the sample blueprints that you deployed when setting up the Enterprise Blueprint Factory, follow the instructions in [Deleting a blueprint](using-factory.md#using-factory-delete).

## Delete the Enterprise Blueprint Factory
<a name="setup-delete-factory"></a>

If you are not using the Enterprise Blueprint Factory, you can delete it to stop incurring the costs associated with its AWS resources.

**To delete the resources**

1. Enter the following commands to delete the IAM roles that were deployed in the Enterprise Blueprint Factory administrative account:

   ```
   aws iam detach-role-policy \
   --policy-arn arn:aws:iam::aws:policy/AWSServiceCatalogEndUserFullAccess \
   --role-name ServiceCatalogEndUserRole
   aws iam delete-role --role-name ServiceCatalogEndUserRole
   aws iam detach-role-policy \
   --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess \
   --role-name ServiceCataloglogLaunchConstraintRole
   aws iam delete-role --role-name ServiceCataloglogLaunchConstraintRole
   ```

1. Delete the CloudFormation stack for the Enterprise Blueprint Factory. For instructions, see [Delete a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) or [Delete a stack from the AWS CLI](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/service_code_examples.html#delete-stack-sdk).

1. Delete the Amazon S3 bucket that is used to store the CodePipeline artifacts. For instructions, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon S3 documentation.

1. Delete the following Systems Manager parameters from Parameter Store:
   + `/blueprints/resources/vpc_id`
   + `/blueprints/resources/subnets`
   + `/blueprints/resources/securitygroups`
   + `/blueprints/resources/artifacts-bucket-name`
   + `/blueprints/resources/BlueprintRepo`
   + `/blueprints/resources/CodeRepo`
   + `/blueprints/resources/ConfigRepo`

   For instructions, see [Deleting parameters from Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/deleting-parameters.html) in the Systems Manager documentation.
