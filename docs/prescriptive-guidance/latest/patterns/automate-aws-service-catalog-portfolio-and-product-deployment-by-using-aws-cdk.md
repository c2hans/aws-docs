---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk.html
---

# Automate AWS Service Catalog portfolio and product deployment by using AWS CDK
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk"></a>

*Sandeep Gawande, Viyoma Sachdeva, and RAJNEESH TYAGI, Amazon Web Services*

## Summary
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-summary"></a>

AWS Service Catalog helps you centrally manage catalogs of IT services, or *products*, that are approved for use in your organization’s AWS environment. A collection of products is called a *portfolio*, and a portfolio also contains configuration information. With AWS Service Catalog, you can create a customized portfolio for each type of user in your organization and then grant access to the appropriate portfolio. Those users can then quickly deploy any product they need from within the portfolio.

If you have a complex networking infrastructure, such as multi-Region and multi-account architectures, it is recommended that you create and manage Service Catalog portfolios in a single, central account. This pattern describes how to use AWS Cloud Development Kit (AWS CDK) to automate creation of Service Catalog portfolios in a central account, grant end users access to them, and then, optionally, provision products in one or more target AWS accounts. This ready-to-use solution creates the Service Catalog portfolios in the source account. It also, optionally, provisions products in target accounts by using AWS CloudFormation stacks and helps you configure TagOptions for the products:
+ **AWS CloudFormation StackSets** – You can use StackSets to launch Service Catalog products across multiple AWS Regions and accounts. In this solution, you have the option to automatically provision products when you deploy this solution. For more information, see [Using AWS CloudFormation StackSets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html) (Service Catalog documentation) and [StackSets concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html) (CloudFormation documentation).
+ **TagOption library** – You can manage tags on provisioned products by using TagOption library. A *TagOption* is a key-value pair managed in AWS Service Catalog. It is not an AWS tag, but it serves as a template for creating an AWS tag based on the TagOption. For more information, see [TagOption library](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions.html) (Service Catalog documentation).

## Prerequisites and limitations
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-prereqs"></a>

**Prerequisites**
+ An active AWS account that you want to use as the source account for administering Service Catalog portfolios.
+ If you are using this solution to provision products in one or more target accounts, the target account must already exist and be active.
+ AWS Identity and Access Management (IAM) permissions to access AWS Service Catalog, AWS CloudFormation, and AWS IAM.

**Product versions**
+ AWS CDK version 2.27.0

## Architecture
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-architecture"></a>

**Target technology stack**
+ Service Catalog portfolios in a centralized AWS account
+ Service Catalog products deployed in target account

**Target architecture**

![AWS CDK creating Service Catalog portfolios and provisioning products in the target account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e8f217a7-aec4-4c85-8f6b-f91995506be0/images/1f027b82-14c3-485a-909b-1544e974b90a.png)

1. In the portfolio (or *source*) account, you update the **config.json** file with the AWS account, AWS Region, IAM role, portfolio, and product information for your use case.

1. You deploy the AWS CDK application.

1. The AWS CDK application assumes the deployment IAM role and creates the Service Catalog portfolios and products defined in the **config.json** file.

   If you configured StackSets to deploy products in a target account, the process continues. If you didn’t configure StackSets to provision any products, then the process is complete.

1. The AWS CDK application assumes the **StackSet administrator** role and deploys the AWS CloudFormation stack set you defined in the **config.json** file.

1. In the target account, StackSets assumes the **StackSet execution** role and provisions the products.

## Tools
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) is a command line cloud development kit that helps you interact with your AWS CDK app.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) helps you centrally manage catalogs of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.

**Code repository**

The code for this pattern is available on GitHub, in the [aws-cdk-servicecatalog-automation](https://github.com/aws-samples/aws-cdk-servicecatalog-automation.git) repository. The code repository contains the following files and folders:
+ **cdk-sevicecatalog-app** – This folder contains the AWS CDK application for this solution.
+ **config** – This folder contains the **config.json** file and the CloudFormation template for deploying the products in the Service Catalog portfolio.
+ **config/config.json** – This file contains all of the configuration information. You update this file to customize this solution for your use case.
+ **config/templates** – This folder contains the CloudFormation templates for the Service Center products.
+ **setup.sh** – This script deploys the solution.
+ **uninstall.sh** – This script deletes the stack and all of the AWS resources created when deploying this solution.

To use the sample code, follow the instructions in the [Epics](#automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-epics) section.

## Best practices
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-best-practices"></a>
+ IAM roles used to deploy this solution should adhere to the [principle of least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) (IAM documentation).
+ Adhere to the [Best practices for developing cloud applications with AWS CDK](https://aws.amazon.com/blogs/devops/best-practices-for-developing-cloud-applications-with-aws-cdk/) (AWS blog post).
+ Adhere to the [AWS CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) (CloudFormation documentation).

## Epics
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the AWS CDK Toolkit. | Make sure you have AWS CDK Toolkit installed. Enter the following command to confirm whether it is installed and check the version. <pre>cdk --version</pre><br />If AWS CDK Toolkit is not installed, then enter the following command to install it.<pre>npm install -g aws-cdk@2.27.0</pre><br />If AWS CDK Toolkit version is earlier than 2.27.0, then enter the following command to update it to version 2.27.0.<pre>npm install -g aws-cdk@2.27.0 --force</pre> | AWS DevOps, DevOps engineer |
| Clone the repository. | Enter the following command. In *Clone the repository* in the [Additional information](#automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-additional) section, you can copy the full command containing the URL for the repository. This clones the [aws-cdk-servicecatalog-automation](https://github.com/aws-samples/aws-cdk-servicecatalog-automation) repository from GitHub.<pre>git clone <repository-URL>.git</pre><br />This creates a `cd aws-cdk-servicecatalog-automation` folder in the target directory. Enter the following command to navigate into this folder.<pre>cd aws-cdk-servicecatalog-automation</pre> | AWS DevOps, DevOps engineer |
| Set up AWS credentials. | Enter the following commands. These export the following variables, which define the AWS account and Region where you are deploying the stack.<pre>export CDK_DEFAULT_ACCOUNT=<12-digit AWS account number></pre><pre>export CDK_DEFAULT_REGION=<AWS Region></pre><br />AWS credentials for AWS CDK are provided through environment variables. | AWS DevOps, DevOps engineer |
| Configure permissions for end user IAM roles. | If you are going to use IAM roles to grant access to the portfolio and the products in it, the roles must have permissions to be assumed by the **servicecatalog.amazonaws.com** service principal. For instructions about how to grant these permissions, see [Enabling trusted access with Service Catalog](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-servicecatalog.html#integrate-enable-ta-servicecatalog) (AWS Organizations documentation). | AWS DevOps, DevOps engineer |
| Configure IAM roles required by StackSets. | If you are using StackSets to automatically provision products in target accounts, you need to configure the IAM roles that administer and run the stack set.1. In the source account, confirm whether the `AWSCloudFormationStackSetAdministrationRole` already exists. In the target accounts, confirm whether `AWSCloudFormationStackSetExecutionRole` already exists. If these roles already exist, you can skip to the next epic.<br />2. Follow the instructions in [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) (IAM documentation) to create the stack set administration role in the portfolio account and create the execution role in each target account. | AWS DevOps, DevOps engineer |

### Customize and deploy the solution
<a name="customize-and-deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CloudFormation templates. | In the `config/templates` folder, create CloudFormation templates for any products that you want to include in your portfolios. For more information, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) (CloudFormation documentation). | App developer, AWS DevOps, DevOps engineer |
| Customize the config file. | In the `config` folder, open the **config.json** file and define the parameters as appropriate for your use case. The following parameters are required unless otherwise noted:+ (Optional) In the `tagOption`** **section, define TagOptions for the products:`key` – Name of the TagOption key`value` – Allowed string values for the TagOption<br />For more information, see [TagOption library](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions.html) (Service Catalog documentation).<br />+ In the** **`products` section, define the following parameters for the products:`portfolioName` – The name of the portfolio where you want to add the product. You can specify only one portfolio.`productName` – The name of the product.`owner` – The owner of the product.`productVersionName` – The name of the product version in string value, such as `v1`.`templatePath` – The file path for the CloudFormation template for the product.`deployWithStackSets` – (Optional) Specify one or more accounts and Regions where you want to use StackSets to automatically provision products in the portfolios. If you use this deployment option, all of the following parameters in this section are required:`accounts` – The target accounts.`regions` – The target Regions.`stackSetAdministrationRoleName` – The name of the IAM role used to administer the StackSets configuration. Do not change this value. This role must have this exact name.`stackSetExecutionRoleName` – The name of the IAM role in the target account that deploys the stack instances. Do not change this value. This role must have this exact name.<br />For an example of a completed config file, see *Sample config file* in the [Additional information](#automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-additional) section. | App developer, DevOps engineer, AWS DevOps |
| Deploy the solution. | Enter the following command. This deploys the AWS CDK app and provisions the Service Catalog portfolios and products as specified in the **config.json** file.<pre>sh +x setup.sh</pre> | App developer, DevOps engineer, AWS DevOps |
| Verify the deployment. | Verify successful deployment by doing the following: 1. Sign in to the AWS Management Console with credentials that can access one or more of the portfolios you defined in the config file.<br />2. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/). <br />3. In the navigation pane, under **Provisioning**, choose **Products**. Verify that you see a list of products that you specified for the portfolio.<br />4. Follow the instructions in [Launching a product](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-launch.html) (Service Catalog documentation) to launch one of the available products. Confirm that the available product versions and tags match the values you provided in the config file.<br />5. If you chose to automatically provision products in one or more target accounts by using StackSets, do the following:Sign in with credentials that give you permissions to view the provisioned products in one of the target accounts.In the Service Catalog console, in the navigation pane, under **Provisioning**, choose **Provisioned products**.Confirm that the expected products appear in the list. | General AWS |
| (Optional) Update the portfolios and products. | If you want to use this solution to update the portfolios or products or to provision new products:1. Make the required changes in the **config.json** file.<br />2. Add or modify any CloudFormation templates as needed in the `config/template` folder.<br />3. Redeploy the solution.<br />For example, you can add additional portfolios or provision more resources. The AWS CDK app implements only the changes. If there are no changes to previously deployed portfolios or products, the redeployment doesn’t affect them. | App developer, DevOps engineer, General AWS |

### Clean up the solution
<a name="clean-up-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| (Optional) Remove AWS resources deployed by this solution. | If you want to delete a provisioned product, follow the instructions in [Deleting provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html) (Service Catalog documentation).<br />If you want to delete all the resources created by this solution, enter the following command.<pre>sh uninstall.sh</pre> | AWS DevOps, DevOps engineer, App developer |

## Related resources
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-resources"></a>
+ [AWS Service Catalog Construct Library](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_servicecatalog-readme.html) (AWS API Reference)
+ [StackSets concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html) (CloudFormation documentation)
+ [AWS Service Catalog](https://aws.amazon.com/servicecatalog) (AWS marketing)
+ [Using Service Catalog with the AWS CDK](https://catalog.us-east-1.prod.workshops.aws/workshops/d40750d7-a330-49be-9945-cde864610de9/en-US/4-builders-devs/sc-cdk) (AWS workshop)

## Additional information
<a name="automate-aws-service-catalog-portfolio-and-product-deployment-by-using-aws-cdk-additional"></a>

**Clone the repository**

Enter the following command to clone the repository from GitHub.

```
git clone https://github.com/aws-samples/aws-cdk-servicecatalog-automation.git
```

**Sample config file**

The following is a sample **config.json** file with example values.

```
{
    "portfolios": [
        {
            "displayName": "EC2 Product Portfolio",
            "providerName": "User1",
            "description": "Test1",
            "roles": [
                "<Names of IAM roles that can access the products>"
            ],
            "users": [
                "<Names of IAM users who can access the products>"
            ],
            "groups": [
                "<Names of IAM user groups that can access the products>"
            ]
        },
        {
            "displayName": "Autoscaling Product Portfolio",
            "providerName": "User2",
            "description": "Test2",
            "roles": [
                "<Name of IAM role>"
            ]
        }
    ],
    "tagOption": [
        {
            "key": "Group",
            "value": [
                "finance",
                "engineering",
                "marketing",
                "research"
            ]
        },
        {
            "key": "CostCenter",
            "value": [
                "01",
                "02",
                "03",
                "04"
            ]
        },
        {
            "key": "Environment",
            "value": [
                "dev",
                "prod",
                "stage"
            ]
        }
    ],
    "products": [
        {
            "portfolioName": "EC2 Product Profile",
            "productName": "Ec2",
            "owner": "owner1",
            "productVersionName": "v1",
            "templatePath": "../../config/templates/template1.json"
        },
        {
            "portfolioName": "Autoscaling Product Profile",
            "productName": "autoscaling",
            "owner": "owner1",
            "productVersionName": "v1",
            "templatePath": "../../config/templates/template2.json",
            "deployWithStackSets": {
                "accounts": [
                    "012345678901",
                ],
                "regions": [
                    "us-west-2"
                ],
                "stackSetAdministrationRoleName": "AWSCloudFormationStackSetAdministrationRole",
                "stackSetExecutionRoleName": "AWSCloudFormationStackSetExecutionRole"
            }
        }
    ]
}
```
