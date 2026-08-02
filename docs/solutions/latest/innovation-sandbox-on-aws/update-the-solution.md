---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

**Important**
Always review the solution release notes before updating to understand any changes, new features, or configuration requirements that may affect your deployment.

## Overview
<a name="update-overview"></a>

The Innovation Sandbox on AWS solution can be updated to newer versions via two methods:
+ Via **CloudFormation templates**, update your existing stacks through the AWS CloudFormation console
+ Via **source code (Git)**, pull the latest changes from the Git repository and redeploy

**Note**
During the update process, you should enable maintenance mode through [AWS AppConfig](https://console.aws.amazon.com/systems-manager/appconfig/) to prevent users and managers from making api requests while the update is in progress.

## Update via CloudFormation templates
<a name="update-via-cloudformation-templates"></a>

If you originally deployed the solution using CloudFormation templates, follow these steps to update to a newer version:

1. Download the latest CloudFormation templates:
   +  [AccountPool template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-AccountPool.template)
   +  [IDC template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-IDC.template)
   +  [Data template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Data.template)
   +  [Compute template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Compute.template)

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. The stacks should be updated in the following order: AccountPool, IDC, Data, then Compute

1. Choose **Update stack** from the stack actions

1. Select **Replace current template** and specify the new template URL or upload the downloaded template

1. On the **Specify stack detail** page, under **Parameters** review the parameters and modify them as necessary

1. On the **Configure stack options** page, under **Stack failure options** section, ensure **Rollback all stack resources** is selected to automatically revert changes if the update fails

1. Complete the stack update process

1. Repeat for each stack that needs to be updated

**Note**
If you enabled maintenance mode during the update process, remember to disable it once all updates are complete to restore normal user access.

## Update via source code (Git)
<a name="update-via-source-code"></a>

If you originally deployed the solution from the Git repository source code, follow these steps to update to a newer version:

**Note**
Before updating from source code, ensure your development environment is properly configured by referring to the [README](https://github.com/aws-solutions/innovation-sandbox-on-aws) for setup instructions.

1. Navigate to your local copy of the [Innovation Sandbox on AWS repository](https://github.com/aws-solutions/innovation-sandbox-on-aws)

1. Pull the latest changes from the remote repository:

   ```
   git pull origin main
   ```

1. Review the updated code and configuration files for any changes that may affect your deployment

1. If you made custom modifications, resolve any merge conflicts that may arise

1. Redeploy the solution using npm commands:
   + To deploy all stacks:

     ```
     npm run deploy:all
     ```
   + Alternatively, stacks can be deployed individually in the following order:

     ```
     npm run deploy:account-pool
     npm run deploy:idc
     npm run deploy:data
     npm run deploy:compute
     ```

1. Verify that the product’s user workflow works as expected after the update
