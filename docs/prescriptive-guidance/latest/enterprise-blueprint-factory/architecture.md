---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/architecture.html
---

# Enterprise Blueprint Factory architecture
<a name="architecture"></a>

An infrastructure as code (IaC) template, also called a *blueprint*, is a configuration file that helps you provision and manage cloud resources. A blueprint might provision a single resource, or it might provision the architecture for a complex, multi-tier application. IaC is designed to help you centralize infrastructure management, standardize resources, and scale quickly.

The Enterprise Blueprint Factory helps you streamline the creation, validation, publishing, distribution, and consumption of blueprints across your organization. In addition to providing an architectural overview, this section reviews the [architectural components](architecture-components.md) of the solution and the [blueprint life cycle](architecture-blueprint-lifecycle.md).

When you release a blueprint through the Enterprise Blueprint Factory, the blueprint becomes a [product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html#what-is_concepts-product) in [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html). You collect products into one or more [portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html#what-is_concepts-portfolio) and then grant permissions that allow end users to access the products in that portfolio. You can use a [portfolio share](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.html) to allow a Service Catalog administrator for another AWS account to distribute your products to end users.

The following diagram shows a high-level overview of the Enterprise Blueprint Factory architecture. This workflow releases the blueprint as a product in Service Catalog. It also creates or updates the portfolios and portfolio shares in order to make the blueprint available to the target end users.

![The components and flow of the Enterprise Blueprint Factory solution.](http://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/images/guide-img/fbe4d444-882e-464d-9768-c5b4c6cfd79b/images/4572fa98-f921-48d8-bb0e-3f3c02a8200d.png)

This diagram shows the following workflow:

1. A developer builds the blueprint. They create a feature branch in the product repository, push the blueprint to the branch, and then create a pull request. A blueprint administrative team and security team review the pull request to make sure that the blueprint meets organizational and security requirements. These teams approve the pull request. The developer merges the feature branch into the main branch. For more information, see [Product repository](architecture-components.md#architecture-product-repo) in this guide.

1. The developer adds or updates the blueprint information in the config file that is located the configuration repo. For more information, see [Configuration repository](architecture-components.md#architecture-config-repo) and [Configuration file](architecture-components.md#architecture-config-file) in this guide.

1. The update to the config file invokes the configuration pipeline. This pipeline uses [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) and [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) projects to create or update the Service Catalog portfolios and portfolio shares. It also creates a release pipeline for the blueprint. For more information, see [Configuration pipeline](architecture-components.md#architecture-config-pipeline) in this guide.

1. The release pipeline performs various security checks on the blueprint. If the blueprint passes, the release pipeline deploys the blueprint as a product in Service Catalog. For more information, see [Release pipeline](architecture-components.md#architecture-release-pipeline) in this guide.

1. By accessing the product through portfolios and portfolio shares, end users deploy the blueprint in their target consumer accounts.
