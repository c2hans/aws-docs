---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/provision-aws-service-catalog-products-using-github-actions.html
---

# Provision AWS Service Catalog products based on AWS CloudFormation templates by using GitHub Actions
<a name="provision-aws-service-catalog-products-using-github-actions"></a>

*Ashish Bhatt and Ruchika Modi, Amazon Web Services*

## Summary
<a name="provision-aws-service-catalog-products-using-github-actions-summary"></a>

This pattern provides organizations with a streamlined approach using [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) products and portfolios to provision standardized and compliant AWS services across teams. [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps to combine essential components in Service Catalog products and portfolios for provisioning base network infrastructure on AWS Cloud. This pattern also promotes DevOps practices by integrating infrastructure as code (IaC) into automated development workflows by using [GitHub Actions](https://github.com/features/actions).

AWS Service Catalog enables organizations to create and manage approved IT services on AWS, offering benefits such as standardization, centralized control, self-service provisioning, and cost management. By automating the deployment of Service Catalog portfolios and products through GitHub Actions, companies can do the following:
+ Achieve consistent and repeatable deployments.
+ Use version control for IaC.
+ Integrate cloud resource management with existing development workflows.

This combination streamlines cloud operations, enforces compliance, and accelerates the delivery of approved services while reducing manual errors and improving overall efficiency.

## Prerequisites and limitations
<a name="provision-aws-service-catalog-products-using-github-actions-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Access to [GitHub repository](https://docs.github.com/en/get-started/quickstart/create-a-repo)
+ Basic understanding of AWS CloudFormation and AWS Service Catalog
+ An Amazon Simple Storage Service (Amazon S3) bucket to host CloudFormation templates
+ An AWS Identity and Access Management (IAM) role named `github-actions` that is used for connectivity between GitHub and AWS

**Limitations **
+ This pattern’s reusable code has been tested only with GitHub Actions.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**

This pattern’s solution was created by using the following [GitHub Marketplace](https://github.com/marketplace) actions and their respective versions:
+ `actions/checkout@v4`
+ `aws-actions/configure-aws-credentials@v2`
+ `aws-actions/aws-cloudformation-github-deploy@v1.2.0`

## Architecture
<a name="provision-aws-service-catalog-products-using-github-actions-architecture"></a>

The following diagram shows the architecture for this solution.

![Using GitHub Actions to provision Service Catalog products based on CloudFormation templates.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/49f82fa7-0c74-4581-bf92-95505dca264c/images/a13c7b41-534e-4a9e-bdca-2974fa40a49a.png)

1. Administrators or platform engineers push standardized CloudFormation templates to a GitHub repository, where the templates are maintained. The GitHub repo also contains workflows that automate the provisioning of AWS Service Catalog using GitHub Actions.

1. GitHub Actions triggers a workflow that connects to the AWS Cloud using an OpenID Connect (OIDC) provider to provision Service Catalog.

1. Service Catalog contains the portfolio and products that developers can directly use to provision standardized AWS resources. This pattern bundles AWS resources such as virtual private clouds (VPCs), subnets, NAT and internet gateways, and route tables.

1. After the developer creates a Service Catalog product, Service Catalog converts it into pre-configured and standardized AWS resources. As a result, developers save time because they don’t need to provision individual resources and configure them manually.

## Tools
<a name="provision-aws-service-catalog-products-using-github-actions-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions. It's an infrastructure as code (IaC) service that can be easily used as one of the product types with AWS Service Catalog.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted.html) helps you centrally manages catalog of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Others**
+ [GitHub Actions](https://docs.github.com/en/actions) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.

**Code repository**

The code for this pattern is available in the GitHub [service-catalog-with-github-actions](https://github.com/aws-samples/service-catalog-with-github-actions) repository. The repo contains the following files of interest:
+ `github/workflows`:
  + `e2e-test.yaml` – This file calls `workflow.yaml`, which is the [reusable workflow](https://docs.github.com/en/actions/sharing-automations/reusing-workflows). This workflow is triggered as soon as there is a commit and push on a branch.
  + `workflow.yaml` – This file contains the reusable workflow for this solution and is configured with `workflow_call` as its trigger. As a reusable workflow, `workflow.yaml` can be called from any other workflow.
+ `templates`:
  + `servicecatalog-portfolio.yaml` – This CloudFormation template includes resources that provision the Service Catalog portfolio and Service Catalog product. The template contains a set of parameters that are used while provisioning the Service Catalog portfolio and products. One parameter accepts an Amazon S3 file URL where the template `vpc.yaml` is uploaded. Although this pattern includes the `vpc.yaml` file to provision AWS resources, you can also use the parameter S3 file URL for configuration.
  + `vpc.yaml` – This CloudFormation template contains AWS resources to be added in the Service Catalog product. AWS resources include VPCs, subnets, internet gateways, NAT gateways, and route tables. The `vpc.yaml` template is an example of how you can use any CloudFormation template with a Service Catalog product and portfolio template.

## Best practices
<a name="provision-aws-service-catalog-products-using-github-actions-best-practices"></a>
+ See [Security Best Practices for AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html) in the AWS Service Catalog documentation.
+ See [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) in the GitHub documentation.

## Epics
<a name="provision-aws-service-catalog-products-using-github-actions-epics"></a>

### Set up local workstation
<a name="set-up-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Git on your local workstation. | To install and configure Git on your local workstation, use the [Getting Started – Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) instructions in the Git documentation. | App developer |
| Clone the GitHub project repo. | To clone the GitHub project repo, do the following:1. Open the [GitHub repo](https://github.com/aws-samples/service-catalog-with-github-actions) for this pattern<br />2. Choose **Code** to see cloning options, and copy the URL provided in the **HTTPS** tab.<br />3. Create a folder for your project on your workstation.<br />4. Open a terminal, and navigate to this folder<br />5. To clone the GitHub repo, run the following command using the URL that you copied in step 2:<pre>git clone https://github.com/aws-samples/service-catalog-with-github-actions.git</pre><br />6. When cloning is complete, to change to the cloned repo in your project folder, run the following command:<pre>cd <folder-name>/service-catalog-with-github-actions</pre><br />7. Open the project in an integrated development environment (IDE) of your choice. | DevOps engineer |

### Set up the OIDC provider
<a name="set-up-the-oidc-provider"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure an OIDC provider. | Create an OpenID Connect (OIDC) provider that allows the GitHub Actions workflows to access resources in AWS, without needing to store the AWS credentials as long-lived GitHub secrets. For instructions, see [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) in the GitHub documentation.<br />After an OIDC provider is configured, the trust policy of the IAM role `github-actions`, mentioned earlier in the [Prerequisites](#provision-aws-service-catalog-products-using-github-actions-prereqs), will be updated. | AWS administrator, AWS DevOps, General AWS |

### Trigger GitHub Actions pipeline to deploy Service Catalog portfolio and products
<a name="trigger-github-actions-pipeline-to-deploy-sc-portfolio-and-products"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update `e2e-test.yaml`. | The `e2e-test.yaml` file triggers the reusable workflow at `workflow.yaml`. Update and validate the values for the following input parameters in `e2e-test.yaml`:+ `aws_account_id` – Specify the correct AWS account.<br />+ `aws_region` – Specify the correct AWS Region.<br />+ `s3BucketName` – Specify the Amazon S3 bucket to hold the CloudFormation templates.<br />+ The workflow file requires two IAM roles as input:`LaunchConstraintRole` - The IAM role that AWS Service Catalog assumes when an end user launches, updates, or terminates a product.`PrincipalArn` - The Amazon Resource Name (ARN) of the principal (IAM user, role, or group) that will be associated to the Service Catalog Portfolio. If the `PrincipalType` is `IAM`, the supported value is a fully defined [IAM Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns). If the `PrincipalType` is `IAM_PATTERN`, the supported value is an IAM ARN without an `AccountID `in the following format: `arn:partition:iam:::resource-type/resource-id` | DevOps engineer |

### Validate deployment
<a name="validate-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the Service Catalog resources. | To validate the Service Catalog resources, do the following:1. Sign in to the AWS Management Console of the AWS account, and verify that the AWS Region is correct.<br />2. Navigate to **AWS Service Catalog** and validate that a portfolio is present under **Administration**, **Portfolios**.<br />3. Choose the portfolio, and validate the information on the **Products**, **Constraints**, and **Access** tabs. | AWS DevOps |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the CloudFormation stack. | To delete the CloudFormation stack, do the following:1. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).<br />2. On the navigation bar at the top of the screen, choose the AWS Region where the stack is located.<br />3. On the **Stacks** page, choose the stack that you want to delete. The stack must be currently running.<br />4. In the stack details pane, choose **Delete**.<br />5. Select **Delete stack** when prompted.<br />For more information, see [Delete a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) in the CloudFormation documentation | DevOps engineer, AWS administrator |

## Troubleshooting
<a name="provision-aws-service-catalog-products-using-github-actions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `e2e-test`<br />`Can't find 'action.yml', 'action.yaml' or 'Dockerfile' under '*/home/runner/work/service-catalog-with-github-actions/service-catalog-with-github-actions`<br />`Did you forget to run actions/checkout before running your local action?` | To make sure that you have the correct repository settings enabled, do the following:1. Navigate to the Github repository, **Settings** tab.<br />2. Choose **Actions**, **General** from the menu on the left side<br />3. Go to the **Access** section, and select the option **Accessible from repositories in the 'XXX' organization**. |

## Related resources
<a name="provision-aws-service-catalog-products-using-github-actions-resources"></a>

**AWS documentation**
+ [Overview of Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html)

**Other resources**
+ [About events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#about-events-that-trigger-workflows) (GitHub documentation)
+ [Reusing workflows](https://docs.github.com/en/actions/sharing-automations/reusing-workflows) (GitHub documentation)

## Additional information
<a name="provision-aws-service-catalog-products-using-github-actions-additional"></a>

To see screenshots related to the [Epics](#provision-aws-service-catalog-products-using-github-actions-epics), go to the **Images **folder in this pattern's GitHub repo. The following screenshots are available:
+ [AWS Service Catalog portfolio, Administration section](https://github.com/aws-samples/service-catalog-with-github-actions/blob/main/images/SC_portfolio.png)
+ [AWS Service Catalog product, Administration section](https://github.com/aws-samples/service-catalog-with-github-actions/blob/main/images/SC_Product.png)
+ [AWS Service Catalog product, User/Provisioning section](https://github.com/aws-samples/service-catalog-with-github-actions/blob/main/images/SC_Product_User.png)
