---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions.html
---

# Manage AWS Service Catalog products in multiple AWS accounts and AWS Regions
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-summary"></a>

Amazon Web Services (AWS) Service Catalog simplifies and accelerates the governance and distribution of infrastructure as code (IaC) templates for enterprises. You use AWS CloudFormation templates to define a collection of AWS resources (*stacks*) required for a product. AWS CloudFormation StackSets extends this functionality by enabling you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation.

AWS Service Catalog administrators create products by using CloudFormation templates that are authored by developers, and publish them. These products are then associated with a portfolio, and constraints are applied for governance. To make your products available to users in other AWS accounts or organizational units (OUs), you typically [share your portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing.html) with them. This pattern describes an alternative approach for managing AWS Service Catalog product offerings that is based on AWS CloudFormation StackSets. Instead of sharing portfolios, you use stack set constraints to set AWS Regions and accounts where your product can be deployed and used. By using this approach, you can provision your AWS Service Catalog products in multiple accounts, OUs, and AWS Regions, and manage them from a central location, while meeting your governance requirements.

Benefits of this approach:
+ The product is provisioned and managed from the primary account, and not shared with other accounts.
+ This approach provides a consolidated view of all provisioned products (stacks) that are based on a specific product.
+ Configuration with AWS Service Management Connector is easier, because it targets only one account.
+ It's easier to query and use products from AWS Service Catalog.

## Prerequisites and limitations
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-prereqs"></a>

**Prerequisites**
+ AWS CloudFormation templates for IaC and versioning
+ Multi-account setup and AWS Service Catalog for provisioning and managing AWS resources

**Limitations **
+ This approach uses AWS CloudFormation StackSets, and the limitations of StackSets apply:
  + StackSets doesn't support CloudFormation template deployment through macros. If you're using a macro to preprocess the template, you won't be able to use a StackSets-based deployment.
  + StackSets provides the ability to disassociate a stack from the stack set, so you can target a specific stack to fix an issue. However, a disassociated stack cannot be re-associated with the stack set.
+ AWS Service Catalog autogenerates StackSet names. Customization isn't currently supported.

## Architecture
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-architecture"></a>

**Target architecture**

![User manages AWS Service Catalog product using AWS CloudFormation template and StackSets.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/16458fcd-861d-4ed4-8b91-47e19289a6bb/images/97d23325-b5c6-4ca9-8288-8dec1650c975.png)

1. The user creates an AWS CloudFormation template to provision AWS resources, in JSON or YAML format.

1. The CloudFormation template creates a product in AWS Service Catalog, which is added to a portfolio.

1. The user creates a provisioned product, which creates CloudFormation stacks in the target accounts.

1. Each stack provisions the resources specified in the CloudFormation templates.

## Tools
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) helps you centrally manage catalogs of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.

## Epics
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-epics"></a>

### Provision products across accounts
<a name="provision-products-across-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a portfolio. | A portfolio is a container that includes one or more products that are grouped together based on specific criteria. Using a portfolio for your products helps you apply common constraints across your product set.<br />To create a portfolio, follow the instructions in the [AWS Service Catalog documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/portfoliomgmt-create.html). If you're using the AWS CLI, here's an example command:<pre>aws servicecatalog create-portfolio --provider-name my-provider --display-name my-portfolio</pre><br />For more information, see the [AWS CLI documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio.html). | AWS Service Catalog, IAM |
| Create a CloudFormation template. | Create a CloudFormation template that describes the resources. Resource property values should be parameterized where applicable. | AWS CloudFormation, JSON/YAML |
| Create a product with version information. | The CloudFormation template becomes a product when you publish it in the AWS Service Catalog. Provide values for the optional version detail parameters, such as version title and description; this will be helpful for querying for the product later.<br />To create a product, follow the instructions in the [AWS Service Catalog documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-cloudresource.html). If you're using the AWS CLI, an example command is:<pre>aws servicecatalog create-product --cli-input-json file://create-product-input.json</pre><br />where `create-product-input.json` is the file that passes the parameters for the product. For an example of this file, see the *Additional information* section. For more information, see the [AWS CLI documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html). | AWS Service Catalog |
| Apply constraints. | Apply stack set constraints to the portfolio, to configure product deployment options such as multiple AWS accounts, Regions, and permissions. For instructions, see the [AWS Service Catalog documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-stackset.html). | AWS Service Catalog |
| Add permissions. | Provide permissions to users so that they can launch the products in the portfolio. For console instructions, see the [AWS Service Catalog documentation](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html). If you're using the AWS CLI, here's an example command:<pre>aws servicecatalog associate-principal-with-portfolio \<br />    --portfolio-id port-2s6abcdefwdh4 \<br />    --principal-arn arn:aws:iam::444455556666:role/Admin \<br />    --principal-type IAM</pre><br />For more information, see the [AWS CLI documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html). | AWS Service Catalog, IAM |
| Provision the product. | A provisioned product is a resourced instance of a product. Provisioning a product based on a CloudFormation template launches a CloudFormation stack and its underlying resources.<br />Provision the product by targeting the applicable AWS Regions and accounts, based on stack set constraints. In the AWS CLI, here's an example command:<pre>aws servicecatalog provision-product \<br />    --product-id prod-abcdfz3syn2rg \<br />    --provisioning-artifact-id pa-abc347pcsccfm \<br />    --provisioned-product-name "mytestppname3"</pre><br />For more information, see the [AWS CLI documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html). | AWS Service Catalog |

## Related resources
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-resources"></a>

**References**
+ [Overview of AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html)
+ [Using AWS CloudFormation StackSets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html)

**Tutorials and videos **
+ [AWS re:Invent 2019: Automate everything: Options and best practices](https://www.youtube.com/watch?v=bGBVPIpQMYk) (video)

## Additional information
<a name="manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions-additional"></a>

When you use the `create-product` command, the `cli-input-json` parameter points to a file that specifies information such as product owner, support email, and CloudFormation template details. Here's an example of such a file:

```
{
   "Owner": "Test admin",
      "SupportDescription": "Testing",
         "Name": "SNS",
            "SupportEmail": "example@example.com",
            "ProductType": "CLOUD_FORMATION_TEMPLATE",
               "AcceptLanguage": "en",
                  "ProvisioningArtifactParameters": {
                     "Description": "SNS product",
                        "DisableTemplateValidation": true,
                           "Info": {
                              "LoadTemplateFromURL": "<url>"
                     },
                           "Name": "version 1"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
