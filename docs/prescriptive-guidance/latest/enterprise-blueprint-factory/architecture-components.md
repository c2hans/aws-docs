---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/architecture-components.html
---

# Enterprise Blueprint Factory components
<a name="architecture-components"></a>

The Enterprise Blueprint Factory consists of the following components:
+ [Product repository](#architecture-product-repo) – A repository where you store the blueprints.
+ [Configuration repository](#architecture-config-repo) – A repository where you store the config file that defines your AWS Service Catalog portfolios and products.
+ [Configuration file](#architecture-config-file) ­– The config file that defines what blueprints are available, who can use them, and how they can use them.
+ [Configuration pipeline](#architecture-config-pipeline) – A DevOps CI/CD pipeline that sets up the Service Catalog portfolio and portfolio shares and creates a release pipeline for each product.
+ [Release pipeline](#architecture-release-pipeline) – A DevOps CI/CD pipeline that releases blueprints as Service Catalog products.

The cloud infrastructure team typically manages the overall Enterprise Blueprint Factory because they must approve each blueprint. However, the DevOps code team is typically responsible for the configuration pipeline and release pipeline. In order to release new blueprints, developers interact only with the product repository, configuration repository, and configuration file.

## Product repository
<a name="architecture-product-repo"></a>

The product repository is a centralized location where you store the blueprints that your organization approves.  A blueprint administrative team and security team review the pull requests to this repository to make sure that each blueprint meets organizational and security requirements. In this guide, we use GitHub for the repository, but you could use an alternative.

## Configuration repository
<a name="architecture-config-repo"></a>

The configuration repository (config repo) is the location where your organization stores the configuration file for your Service Catalog portfolios and products that are released through the Enterprise Blueprint Factory. In this guide, we use GitHub for the repository, but you could use an alternative.

## Configuration file
<a name="architecture-config-file"></a>

The Enterprise Blueprint Factory configuration file (config file) is stored in the configuration repository, which is owned by the blueprint administrative team. The name of this file is **bp\_config.yml**. When a developer updates this file, the blueprint administrative team reviews the changes. Merging the changes into the main branch initiates the configuration pipeline. The config file orchestrates the publishing, sharing, and distribution of all blueprints that are managed through the Enterprise Blueprint Factory.

The config file is a YAML file that consists of two main objects: `portfolios` and `products`. The following is an example of a sample config file:

```
portfolios:
  - portfolio_name: blueprint-portfolio
    owner: Blueprint-team
    provider_name: AWS
    description: "Blueprint portfolio"
    portfolio_access_role:
       - arn:aws:iam::123456789012:role/examplerole
       - arn:aws:iam::123456789012:user/exampleuser
    share_to_ou:
     - org_id: "o-exampleOrgID"
    stack_tags:
      DataClassification: Confidential
      Organization: AWS
products:
  - name: BP-S3-Product
    description: "Blueprint for BP-S3 product"
    product_config_file: 'BP-S3/product_config.json'
    owner: Blueprint-team
    stack_tags:
      DataClassification: Confidential
      Organization: AWS
    portfolio_associations:
      - blueprint-portfolio
    launch_constraint_role: arn:aws:iam::123456789012:role/examplelaunchrole
```

In the `portfolios` object, you define your target Service Catalog portfolios. For each portfolio, you provide the following attributes:
+ `portfolio_name` is the name of the portfolio. This attribute is required.
+ `owner` is the name of the team who owns the portfolio. This attribute is optional.
+ `provider_name` is the name of the team or organization that manages the portfolio. The default value is `AWS`. This attribute is required.
+ `description` is a brief description of the portfolio. This attribute is optional.
+ `portfolio_access_roles` are the AWS Identity and Access Management (IAM) [identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) (users, roles, or groups) that are allowed to access the portfolio and its associated products. This attribute is optional.
+ `share_to_ou` is the [organizational unit](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) (OU) in AWS Organizations that the portfolio is shared with. End users can deploy this portfolio's products in AWS accounts that are members of the target OU. This attribute is optional.
+ `stack_tags` are the [tags](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) applied to the portfolio. This attribute is optional.

In the `products` object, you define each blueprint that you want to release as a product in Service Catalog. For each product, you provide the following attributes:
+ `name` is the name of the product in Service Catalog. This attribute is required.
+ `description` is a brief description of the product. This attribute is required.
+ `product_config_file` is the name of the blueprint product configuration file that is stored in the product repository. This attribute is required.
+ `owner` is the name of the team who owns the product. This attribute is required.
+ `stack_tags` are the tags applied to the product. This attribute is optional.
+ `portfolio_associations` are the target portfolios that contain the product. This attribute is optional.
**Note**
We recommend that you add products only to portfolios that are managed through the Enterprise Blueprint Factory. If you want to add products to portfolios that are not managed through the Enterprise Blueprint Factory, the user's IAM policy must allow the [AssociateProductWithPortfolio](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_AssociateProductWithPortfolio.html) action. However, as a security best practice, we recommend that you allow this action only for the Enterprise Blueprint Factory configuration pipeline.
+ `launch_constraint_role` is the [launch role](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html) that Service Catalog assumes when an end user launches the product. This attribute is required.

## Configuration pipeline
<a name="architecture-config-pipeline"></a>

The configuration pipeline (config pipeline) automates the configuration of the Service Catalog portfolio and portfolio shares. It also creates the release pipeline for each product. This pipeline is an [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) resource. An update to the config file invokes the configuration pipeline.

The first time that you invoke the config pipeline, it creates two additional portfolios that are not defined in your config file:
+ `Blueprint-portfolio` – Every product that you deploy through the Enterprise Blueprint Factory is added to this portfolio. This portfolio is available to the IAM principals and organizational units that you specify in the config file.
+ `Bootstrapping-Admin-Portfolio` – The `Bootstrapping-Admin-Product` product is associated with this portfolio. This product is a CloudFormation template for the release pipeline. Allow only the blueprint administrative team to access this portfolio so that they can manage administrative products.

### Configuration pipeline stages
<a name="configuration-pipeline-stages.594138e4-4e5d-5ff5-ba3f-343657b8a861"></a>

The following image shows the stages in the config pipeline and the resources that the pipeline interacts with. Each stage in the pipeline is an [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) project.

![The stages in the Enterprise Blueprint Factory configuration pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/d03071bf-14ba-46f5-b2ae-39eff7d105ea.png)

The following are the stages of the configuration pipeline:

1. **Deploy portfolios** – The config pipeline deploys any portfolios that have been added to the config file or deletes any portfolios that have been removed from the config file. If there are no changes to the portfolios, then the pipeline skips this stage.

1. **Share portfolios** – The config pipeline shares the portfolios with the target organizational units (OUs). If there are no changes to the portfolio shares, then the pipeline skips this stage.

1. **Deploy Blueprint-Admin-Bootstrapping-Product** – The config pipeline fetches the `bp-pipeline`** **blueprint from the `ServiceCatalog-CodeRepo` repo and deploys it to Service Catalog as `Bootstrapping-Admin-Product`.** **This product is the CloudFormation template that is used to create a release pipeline. Deploying this template** **as a Service Catalog product helps maintain version control. If there are no changes to the `bp-pipeline`** **blueprint, then the pipeline skips this stage.

1. **Create release pipelines** – Based on the product attributes in the config file, the config pipeline prepares the stack parameters and launches a CloudFormation stack that creates a release pipeline for the product. For more information, see [Release pipeline](#architecture-release-pipeline) in this guide.

1. **Deploy products** – The release pipeline deploys the blueprint as a Service Catalog product and associates it with the target portfolio. End users can now deploy the product in AWS accounts that are members of the target OU.

## Release pipeline
<a name="architecture-release-pipeline"></a>

The release pipeline automates the release of blueprints as Service Catalog products. This pipeline is an [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) resource. When your organization wants to release a new blueprint, a developer uploads the IaC template and its product config file to the product repo. Adding the product details to the config file triggers the config pipeline. The config pipeline creates a release pipeline for this blueprint. Any subsequent updates to the blueprint triggers this release pipeline to update the product in Service Catalog with a new version.

The release pipeline includes proactive controls that automate security and compliance checks for your blueprints. *Proactive controls* are designed to prevent the creation of noncompliant resources. These controls can reduce the number of security events handled by other types of security controls, such as responsive and detective controls. Because proactive controls make sure that deployed resources are compliant before they are deployed, there is no detection event that requires response or remediation.

The first time that you invoke the configuration pipeline, it creates a Service Catalog product that is named `Bootstrapping-Admin-Product`. This product is the CloudFormation template for the release pipeline. As shown in the following figure, the configuration pipeline uses the `Bootstrapping-Admin-Product` product to create a dedicated release pipeline for each new blueprint. There is a one-to-one relationship between blueprints and release pipelines.

![The config pipeline uses a product to create a release pipeline for each blueprint.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/49789395-fc19-437a-8cb2-53a73d808da2.png)

### Release pipeline stages
<a name="release-pipeline-stages.4491c7d1-0a80-5c32-8776-297c072471b7"></a>

The following image shows the default stages in the release pipeline and the resources that the pipeline interacts with. Each stage in the pipeline is a CodeBuild project.

![The stages in the Enterprise Blueprint Factory release pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/59809a25-bed7-4fb9-9f52-d57bcbd26121.png)

The following are the stages of the release pipeline:

1. **File alignment** – This stage verifies that the blueprint is an CloudFormation [template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html#cfn-concepts-templates) or an AWS Cloud Development Kit (AWS CDK) [construct](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html). If the blueprint is an AWS CDK construct, this stage synthesizes the AWS CDK construct into a CloudFormation template. This process automates and standardizes deployments through CloudFormation. If any errors are found, the pipeline fails.

1. **Syntax check** – Syntax error is a common cause of CloudFormation deployment errors. In this stage, [AWS CloudFormation Linter (cfn-lint)](https://github.com/aws-cloudformation/cfn-lint) checks for syntax errors by comparing the template to the [AWS CloudFormation resource specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html). It also performs other checks, such as checking for valid values for resource properties and adherence to best practices. If any errors are found, the pipeline fails, and cfn-lint returns suggestions.

1. **Control check** – In this stage, [cfn\_nag](https://github.com/stelligent/cfn_nag) checks for potential security issues by searching for patterns. For example, it checks for overly permissive security groups and AWS Identity and Access Management (IAM) policies, missing encryption, and password literals. If any errors are found, the pipeline fails, and cfn\_nag returns suggestions.

1. **Version check **– The release pipeline performs version control based on the version strategy that is defined in the product config file. If the product version is defined as immutable, Service Catalog inactivates the previous product version.

1. **Publish product** – The release pipeline releases the product in Service Catalog.

**Note**
The release pipeline is customizable. For example, you can remove any stages that are not applicable for your use case. You could also add more stages if you want to add other control checks, additional validations, or a manual approval step. This guide does not include instructions for modifying the release pipeline. For more information, see the [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) and [CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) documentation.
