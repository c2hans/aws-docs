---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/aws-service-catalog-for-managing-infrastructure-as-products.html
---

# Using AWS Service Catalog to manage IaP
<a name="aws-service-catalog-for-managing-infrastructure-as-products"></a>

AWS provides a service called [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) that supports managing and provisioning AWS infrastructure as a product. You can use Service Catalog to rapidly define the infrastructure you need to provision as a set of products, grant permission for those products to desired parties, and implement the provisioning and update patterns required for individual products.

Service Catalog is backed by [AWS CloudFormation](https://aws.amazon.com/cloudformation/). Service Catalog portfolios, products, and their provisioning templates are managed as CloudFormation stacks. You can define these stacks in four ways:
+ By using standard CloudFormation templates.
+ By using the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) and the [Service Catalog Construct Library](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_servicecatalog-readme.html) with a supported programming language that you prefer.
+ By using a framework provided by a third-party tool to generate the CloudFormation stack definitions from declarative metadata that describes the stacks.
+ By using the [Service Catalog API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Reference.html). This API provides methods for everything except for building the product. You can add products to portfolios, remove products from portfolios, tag products and portfolios, define administrative and operational product [service actions](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-actions.html), and browse and search for portfolio and product definitions.

At its core, a Service Catalog product is a set of one or more AWS resources that are configured to provide a collective, customizable (through parameterization) capability. For example, you can define a Service Catalog product to provision a private Amazon Simple Storage Service (Amazon S3) bucket in a target account. The S3 bucket is a product that might have input parameters such as the bucket name, an internet address range to allow access from, a set of users who can access the bucket, a lifecycle tiering policy, or a bucket versioning specification. You can also define an AWS Identity and Access Management (IAM) role to provide access to the bucket as part of the product.

You can add a Service Catalog product to one or more *portfolios*. A Service Catalog portfolio is a collection of products that are grouped together, generally because they serve a similar purpose (for example, analysis, development, client access services, partner access services, and so on).

You provide permissions for a user, group, or role to have access to provision a product at the portfolio level. For provisioning, products are associated with either a launch IAM role (for launching the product in a self-serve manner to anyone who can assume the role), or with a [stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-stackset) that defines one or more accounts that the product can be provisioned to. To use a stack set, you must define a Service Catalog administrator role in the Service Catalog hub account and a Service Catalog product provisioning execution role in each target account of the stack set.

The following sections discuss Service Catalog IaP functionality in more detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
