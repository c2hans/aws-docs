---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository.html
---

# Provision a Terraform product in AWS Service Catalog by using a code repository
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository"></a>

*Dr. Rahul Sharad Gaikwad and Tamilselvan P, Amazon Web Services*

## Summary
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-summary"></a>

AWS Service Catalog supports self-service provisioning with governance for your [HashiCorp Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) configurations. If you use Terraform, you can use Service Catalog as the single tool to organize, govern, and distribute your Terraform configurations within AWS at scale. You can access Service Catalog key features, including cataloging of standardized and pre-approved infrastructure as code (IaC) templates, access control, cloud resources provisioning with least privilege access, versioning, sharing to thousands of AWS accounts, and tagging. End users, such as engineers, database administrators, and data scientists, see a list of products and versions they have access to, and they can deploy them through a single action.

This pattern helps you deploy AWS resources by using Terraform code. The Terraform code in the GitHub repository is accessed through Service Catalog. Using this approach, you integrate the products with your existing Terraform workflows. Administrators can create Service Catalog portfolios and add AWS Launch Wizard products to them by using Terraform.

The following are the benefits of this solution:
+ Because of the rollback feature in Service Catalog, if any issues occur during deployment, you can revert the product to a previous version.
+ You can easily identify the differences between product versions. This helps you resolve issues during deployment.
+ You can configure a repository connection in Service Catalog, such as to GitHub or GitLab. You can make product changes directly through the repository.

For information about the overall benefits of AWS Service Catalog, see [What is Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

## Prerequisites and limitations
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A GitHub, BitBucket, or other repository that contains Terraform configuration files in ZIP format.
+ AWS Serverless Application Model Command Line Interface (AWS SAM CLI), [installed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ Go, [installed](https://go.dev/doc/install).
+ Python version 3.9 , [installed](https://www.python.org/downloads/release/python-3913/). AWS SAM CLI requires this version of Python.
+ Permissions to write and run AWS Lambda functions and permissions to access and manage Service Catalog products and portfolios.

## Architecture
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-architecture"></a>

![Architecture diagram of provisioning a Terraform product in Service Catalog from a code repo](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7d0d76e8-9485-4b3f-915f-481b6a7cdcd9/images/e83fa44a-4ca6-4438-a0d1-99f09a3541bb.png)

The diagram shows the following workflow:

1. When a Terraform configuration is ready, a developer creates a .zip file that contains all of the Terraform code. The developer uploads the .zip file into the code repository that is connected to Service Catalog.

1. An administrator associates the Terraform product to a portfolio in Service Catalog. The administrator also creates a launch constraint that allows end users to provision the product.

1. In Service Catalog, end users launch AWS resources by using the Terraform configuration. They can choose which product version to deploy.

## Tools
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-tools"></a>

**AWS services**
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) helps you centrally manage catalogs of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.

**Other services**
+ [Go](https://go.dev/doc/install) is an open source programming language that Google supports.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

If you require sample Terraform configurations that you can deploy through Service Catalog, you can use the configurations in the GitHub [Amazon Macie Organization Setup Using Terraform](https://github.com/aws-samples/aws-macie-customization-terraform-samples) repository. Use of the code samples in this repository is not required.

## Best practices
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-best-practices"></a>
+ Instead of providing the values for variables in the Terraform configuration file (`terraform.tfvars`), configure variable values when launching product through Service Catalog.
+ Grant access to the portfolio only to specific users or administrators.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPracticesAndUseCases.html) in the AWS Identity and Access Management (IAM) documentation.

## Epics
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-epics"></a>

### Set up your local workstation
<a name="set-up-your-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| (Optional) Install Docker. | If you want to run the AWS Lambda functions in your development environment, install Docker. For instructions, see [Install Docker Engine](https://docs.docker.com/engine/install/) in the Docker documentation. | DevOps engineer |
| Install the AWS Service Catalog Engine for Terraform. | 1. Enter the following command to clone the [AWS Service Catalog Engine for Terraform](https://github.com/aws-samples/service-catalog-engine-for-terraform-os) repository.<pre>git clone https://github.com/aws-samples/service-catalog-engine-for-terraform-os.git</pre><br />2. Navigate to the the root directory of the cloned repository.<br />3. Enter the following command. This installs the engine.<pre>run ./bin/bash/deploy-tre.sh -r</pre><br />The AWS Region set in your default profile is not used during the automated installation. Instead, you provide the Region when you run this command. | DevOps engineer, AWS administrator |

### Connect the GitHub repository
<a name="connect-the-github-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a connection to the GitHub repository. | 1. Sign in to the AWS Management Console, and then open the **Developer Tools** console. You can access the Developer Tools console by choosing a service such as AWS CodePipeline or AWS CodeDeploy.<br />2. In the left navigation pane, choose **Settings**, and then choose **Connections**.<br />3. Choose **Create connection**.<br />4. Select the repository where you maintain the Terraform source code. For example, you can choose **Bitbucket**, **GitHub**, or **GitHub Enterprise Server**.<br />5. Enter a name for the connection, and then choose **Connect**.<br />6. When you are prompted, authenticate the repository.<br />After authentication is complete, the connection is created and the status changes to **active**. | AWS administrator |

### Create a Terraform product in Service Catalog
<a name="create-a-terraform-product-in-service-catalog"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Service Catalog product. | 1. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />2. Navigate to the **Administration** section, and then choose **Product list**.<br />3. Choose **Create product**.<br />4. On the **Create product** page in the **Product details** section, choose the **External** product type. Service Catalog uses this product type to support Terraform Community Edition products.<br />5. Enter a name and owner for the Service Catalog product.<br />6. Select **Specify your code repository using a CodeStar provider**.<br />7. Enter the following information for your repository:**Connect to your provider using AWS CodeConnections** – Select the connection you created previously.**Repository** – Select the repository.**Branch** – Select the branch.**Template file path** – Choose the path where the code template file is stored. The file name should end with `tar.gz`.<br />8. Under **Version name and description**, provide information about the product version.<br />9. Choose **Create product**. | AWS administrator |
| Create a portfolio. | 1. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />2. Navigate to the **Administration** section, and then choose, choose **Portfolios**.<br />3. Choose **Create portfolio**.<br />4. Enter the following values:**Portfolio name** – `Sample terraform`**Portfolio description** – `Sample portfolio for Terraform configurations`**Owner** – Your contact information, such as an email address<br />5. Choose **Create**. | AWS administrator |
| Add the Terraform product to the portfolio. | 1. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />2. Navigate to the **Administration** section, and then choose **Product list**.<br />3. Select the Terraform product that you created previously.<br />4. Choose **Actions**, and then choose **Add product to portfolio**.<br />5. Choose the `Sample terraform` portfolio.<br />6. Choose **Add product to portfolio**. | AWS administrator |
| Create the access policy. | 1. Open the [AWS Identity and Access Management (IAM) console](https://console.aws.amazon.com/iam/).<br />2. In the navigation pane, choose **Policies**.<br />3. In the content pane, choose **Create policy**.<br />4. Choose the **JSON **option.<br />5. Enter the sample JSON policy in *Access policy* in the [Additional information](#provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-additional) section of this pattern.<br />6. Choose **Next**.<br />7. On the **Review and create** page, in the **Policy name** box, enter `TerraformResourceCreationAndArtifactAccessPolicy`.<br />8. Choose **Create policy**. | AWS administrator |
| Create a custom trust policy. | 1. Open the [IAM console](https://console.aws.amazon.com/iam/).<br />2. In the navigation pane, choose **Roles**.<br />3. Choose **Create role**.<br />4. Under **Trusted entity type**, choose **Custom trust policy**.<br />5. In the JSON policy editor, enter the sample JSON policy in *Trust policy* in the [Additional information](#provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-additional) section of this pattern.<br />6. Choose **Next**.<br />7. Under **Permissions policies**, choose the `TerraformResourceCreationAndArtifactAccessPolicy` that you previously created.<br />8. Choose **Next**.<br />9. Under **Role details**, in the **Role name** box, enter `SCLaunch-product`.  The role name must begin with `SCLaunch`.<br />10. Choose **Create role**. | AWS administrator |
| Add a launch constraint to the Service Catalog product. | 1. Sign in to the AWS Management Console as a user with administrative permissions.<br />2. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />3. In the navigation pane, choose **Portfolios**.<br />4. Choose the portfolio that you created previously.<br />5. On the **Portfolio details** page, choose the **Constraints** tab, and then choose **Create constraint**.<br />6. For **Product**, select the Terraform product you created previously.<br />7. Under **Launch constraint**, for **Method**, choose **Enter role name**.<br />8. In the **Role name** box, enter `SCLaunch-product`.<br />9. Choose **Create**. | AWS administrator |
| Grant access to the product. | 1. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />2. In the navigation pane, choose **Portfolios**.<br />3. Choose the portfolio that you created previously.<br />4. Choose the **Access** tab, and then choose **Grant access**.<br />5. Choose the **Roles** tab, and then select the role that should have access to deploy this product.<br />6. Choose **Grant Access**. | AWS administrator |
| Launch the product. | 1. Sign in to the AWS Management Console as a user with permissions to deploy the Service Catalog product.<br />2. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />3. In the navigation pane, choose **Products**.<br />4. Choose the produce you created previously, and then choose **Launch product**.<br />5. Enter a product name and define any required parameters.<br />6. Choose **Launch product**. | DevOps engineer |

### Verify the deployment
<a name="verify-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the deployment. | There are two AWS Step Functions state machines for the Service Catalog provisioning workflow:+ `ManageProvisionedProductStateMachine` – Service Catalog invokes this state machine when provisioning a new Terraform product and when updating an existing Terraform provisioned product.<br />+ `TerminateProvisionedProductStateMachine` – Service Catalog invokes this state machine when terminating an existing Terraform provisioned product.<br />You check the logs for the `ManageProvisionedProductStateMachine` state machine to confirm that the product was provisioned.1. Sign in to the AWS Management Console, and then open the [AWS Step Functions console](https://console.aws.amazon.com/states/home).<br />2. In the left navigation pane, choose **State machines**.<br />3. Choose `ManageProvisionedProductStateMachine`.<br />4. In the **Executions** list, enter the provisioned product ID to locate the execution.The state file backend bucket names start with `sc-terraform-engine-state-`.<br />5. Validate that all the required resources have been created in the account. | DevOps engineer |

### Clean up infrastructure
<a name="clean-up-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete provisioned products. | 1. Sign in to the AWS Management Console as a user with permissions to deploy the Service Catalog product.<br />2. Open the [AWS Service Catalog console](https://console.aws.amazon.com/servicecatalog/).<br />3. In the left navigation, choose **Provisioned products**.<br />4. Select the product you created.<br />5. In the **Actions** list, choose **Terminate**.<br />6. In the confirmation text box, enter `terminate`, and then choose **Terminate provisioned product**.<br />7. Repeat these steps to terminate all provisioned products. | DevOps engineer |
| Remove the AWS Service Catalog Engine for Terraform. | 1. Sign in to the AWS Management Console as a user with administrative permissions.<br />2. Open the [Amazon Simple Storage Service (Amazon S3) console](https://console.aws.amazon.com/s3/).<br />3. In the navigation pane, choose **Buckets**.<br />4. Select the `sc-terraform-engine-logging-XXXX` bucket.<br />5. Choose **Empty**.<br />6. Repeat steps 4–5 for the following buckets:`sc-terraform-engine-state-XXXX``terraform-engine-bootstrap-XXXX`<br />7. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), and then validate you're in the correct AWS Region.<br />8. In the left navigation, choose **Stacks**.<br />9. Select `SAM-TRE`, and then choose **Delete**. Wait until the stack has been deleted.<br />10. Select `Bootstrap-TRE`, and then choose **Delete**. Wait until the stack has been deleted. | AWS administrator |

## Related resources
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-resources"></a>

**AWS documentation**
+ [Getting started with a Terraform product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-Terraform.html)

**Terraform documentation**
+ [Terraform installation](https://learn.hashicorp.com/tutorials/terraform/install-cli)
+ [Terraform backend configuration](https://developer.hashicorp.com/terraform/language/backend)
+ [Terraform AWS Provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

## Additional information
<a name="provision-a-terraform-product-in-aws-service-catalog-by-using-a-code-repository-additional"></a>

**Access policy**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "s3:ExistingObjectTag/servicecatalog:provisioning": "true"
                }
            }
        },
        {
            "Action": [
                "s3:CreateBucket*",
                "s3:DeleteBucket*",
                "s3:Get*",
                "s3:List*",
                "s3:PutBucketTagging"
            ],
            "Resource": "arn:aws:s3:::*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "resource-groups:CreateGroup",
                "resource-groups:ListGroupResources",
                "resource-groups:DeleteGroup",
                "resource-groups:Tag"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "tag:GetResources",
                "tag:GetTagKeys",
                "tag:GetTagValues",
                "tag:TagResources",
                "tag:UntagResources"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

**Trust policy**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GivePermissionsToServiceCatalog",
            "Effect": "Allow",
            "Principal": {
                "Service": "servicecatalog.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::account_id:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::accounti_id:role/TerraformEngine/TerraformExecutionRole*",
                        "arn:aws:iam::accounti_id:role/TerraformEngine/ServiceCatalogExternalParameterParserRole*",
                        "arn:aws:iam::accounti_id:role/TerraformEngine/ServiceCatalogTerraformOSParameterParserRole*"
                    ]
                }
            }
        }
    ]
}
```
