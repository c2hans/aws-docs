---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions.html
---

# Copy AWS Service Catalog products across different AWS accounts and AWS Regions
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions"></a>

*Sachin Vighe and Santosh Kale, Amazon Web Services*

## Summary
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions-summary"></a>

AWS Service Catalog is a Regional service and this means that AWS Service Catalog [portfolios and products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html) are only visible in the AWS Region where they are created. If you set up an [AWS Service Catalog hub](https://aws.amazon.com/about-aws/whats-new/2020/06/aws-service-catalog-now-supports-sharing-portfolios-across-an-organization-from-a-delegated-member-account/) in a new Region, you must recreate your existing products and this can be a time-consuming process.

This pattern's approach helps simplify this process by describing how to copy products from an AWS Service Catalog hub in a source AWS account or Region to a new hub in a destination account or Region. For more information about the AWS Service Catalog hub and spoke model, see [AWS Service Catalog hub and spoke model: How to automate the deployment and management of AWS Service Catalog to many accounts](https://aws.amazon.com/blogs/mt/aws-service-catalog-hub-and-spoke-model-how-to-automate-the-deployment-and-management-of-service-catalog-to-many-accounts/) on the AWS Management and Governance Blog.

The pattern also provides the separate code packages required to copy AWS Service Catalog products across accounts or to other Regions. By using this pattern, your organization can save time, make existing and previous product versions available in a new AWS Service Catalog hub, minimize the risk of manual errors, and scale the approach across multiple accounts or Regions.

**Note**
This pattern's *Epics *section provides two options for copying products. You can use Option 1 to copy products across accounts or choose Option 2 to copy products across Regions.

## Prerequisites and limitations
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Existing AWS Service Catalog products in a source account or Region.
+ An existing AWS Service Catalog hub in a destination account or Region.
+ If you want to copy products across accounts, you must share and then import the AWS Service Catalog portfolio containing the products into your destination account. For more information about this, see [Sharing and importing portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing.html) in the AWS Service Catalog documentation.

**Limitations **
+ AWS Service Catalog products that you want to copy across Regions or accounts cannot belong to more than one portfolio.

## Architecture
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions-architecture"></a>

The following diagram shows the copying of AWS Service Catalog products from a source account to a destination account.

![A cross-account role in Region 1, a Lambda execution role and a Lambda function in Region 2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7ede5d17-89eb-4455-928f-6953d145ac9f/images/26738220-1ed2-4f84-911b-3c88e954b60e.png)

 The following diagram shows the copying of AWS Service Catalog products from a source Region to a destination Region.

![Products copied by using the Lambda scProductCopy function in Region 2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7ede5d17-89eb-4455-928f-6953d145ac9f/images/0a936792-3bdc-45c2-ba05-17e828615061.png)

**Technology stack  **
+ Amazon CloudWatch
+ AWS Identity and Access Management (IAM)
+ AWS Lambda
+ AWS Service Catalog

**Automation and scale**

You can scale this pattern’s approach by using a Lambda function that can be scaled depending on the number of requests received or how many AWS Service Catalog products you need to copy. For more information about this, see [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html) in the AWS Lambda documentation.

## Tools
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) helps you centrally manage catalogs of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.

**Code**

You can use the ` cross-account-copy` package (attached) to copy AWS Service Catalog products across accounts or the `cross-region-copy` package (attached) to copy products across Regions.

The `cross-account-copy` package contains the following files:
+ `copyconf.properties` – The configuration file that contains the Region and AWS account ID parameters for copying products across accounts.
+ `scProductCopyLambda.py` – The Python function for copying products across accounts.
+ `createDestAccountRole.sh` – The script to create an IAM role in the destination account.
+ `createSrcAccountRole.sh` – The script to create an IAM role in the source account.
+ `copyProduct.sh` – The script to create and invoke the Lambda function for copying products across accounts.

The `cross-region-copy` package contains the following files:
+ `copyconf.properties` – The configuration file that contains the Region and AWS account ID parameters for copying products across Regions.
+ `scProductCopyLambda.py` – The Python function for copying products across Regions.
+ `copyProduct.sh` – The script to create an IAM role and create and invoke the Lambda function for copying products across Regions.

## Epics
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions-epics"></a>

### Option 1 – Copy AWS Service Catalog products across accounts
<a name="option-1-ndash-copy-aws-service-catalog-products-across-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the configuration file. | 1. Download the `cross-account-copy` package (attached) to your local machine.<br />2. Update the `copyconf.properties` configuration file with the following values:`srcRegion` – Provide the source Region that contains the products.`destRegion` – Provide the destination Region for the products.`sourceAccountId` – Provide the AWS account ID for your source account.`destAccountId` – Provide the AWS account ID for your destination account. | AWS administrator, AWS systems administrator, Cloud administrator |
| Configure your credentials for AWS CLI in the destination account. | Configure your credentials to access AWS CLI in your destination account by running the `aws configure` command and providing the following values :<pre>$aws configure <br />AWS Access Key ID [None]: <your_access_key_id> <br />AWS Secret Access Key [None]: <your_secret_access_key> <br />Default region name [None]: Region<br />Default output format [None]:</pre><br />For more information about this, see [Configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the AWS Command Line Interface documentation.  | AWS administrator, AWS systems administrator, Cloud administrator |
| Configure your credentials for AWS CLI in the source account. | Configure your credentials to access AWS CLI in your source account by running the `aws configure` command and providing the following values: <pre>$aws configure<br />AWS Access Key ID [None]: <your_access_key_id><br />AWS Secret Access Key [None]: <your_secret_access_key><br />Default region name [None]: Region<br />Default output format [None]:</pre><br />For more information about this, see [Configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the AWS Command Line Interface documentation.  | AWS administrator, AWS systems administrator, Cloud administrator |
| Create a Lambda execution role in your destination account. | Run the `createDestAccountRole.sh `script in your destination account. The script implements the following actions:+ Creates a Lambda execution role in your destination account<br />+ Creates and attaches the IAM policy for the Lambda execution role  | AWS administrator, AWS systems administrator, Cloud administrator |
| Create the cross-account IAM role in your source account. | Run the `createSrcAccountRole.sh `script in your source account. The script implements the following actions:+ Creates a cross-account IAM role in your source account that is assumed by the Lambda execution role in the destination account to copy products<br />+ Creates and attaches an IAM policy for the cross-account role in your source account | AWS administrator, AWS systems administrator, Cloud administrator |
| Run the copyProduct script in the destination account. | Run the `copyProduct.sh `script in your destination account. The script implements the following actions:+ Creates and invokes the Lambda function to copy products from the source account to the destination account | AWS administrator, AWS systems administrator, Cloud administrator |

### Option 2 – Copy AWS Service Catalog products from a source Region to a destination Region
<a name="option-2-ndash-copy-aws-service-catalog-products-from-a-source-region-to-a-destination-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the configuration file. | 1. Download the `cross-region-copy` package (attached) to your local machine.<br />2. Update the `copyconf.properties` configuration file with the following values:`srcRegion` – Provide the source Region that contains the products.`destRegion` – Provide the destination Region for the products.`accountId` – Provide your AWS account ID. | AWS systems administrator, Cloud administrator, AWS administrator |
| Configure your credentials for AWS CLI. | Configure your credentials to access AWS CLI in your environment by running the `aws configure` command and providing the following values:<pre>$aws configure<br />AWS Access Key ID [None]: <your_access_key_id><br />AWS Secret Access Key [None]: <your_secret_access_key><br />Default region name [None]: Region<br />Default output format [None]:</pre><br />For more information about this, see [Configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the AWS Command Line Interface documentation.  | AWS administrator, AWS systems administrator, Cloud administrator |
| Run the copyProduct script. | Run the `copyProduct.sh` script in your destination Region. The script implements the following actions:+ Creates a Lambda execution role<br />+ Creates and attaches the IAM policy for the Lambda execution role<br />+ Creates and invokes the Lambda function to copy products from the source Region to the destination Region | AWS administrator, AWS systems administrator, Cloud administrator |

## Related resources
<a name="copy-aws-service-catalog-products-across-different-aws-accounts-and-aws-regions-resources"></a>
+ [Create a Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) (AWS Lambda documentation)
+ [Create a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html) (AWS Lambda documentation)
+ [AWS Service Catalog API reference](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations_AWS_Service_Catalog.html)
+ [AWS Service Catalog documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html)

## Attachments
<a name="attachments-7ede5d17-89eb-4455-928f-6953d145ac9f"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/7ede5d17-89eb-4455-928f-6953d145ac9f/attachments/attachment.zip)
