---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/aws-service-catalog-and-tools-capabilities-summary.html
---

# Summary and next steps
<a name="aws-service-catalog-and-tools-capabilities-summary"></a>

Service Catalog helps you quickly and reliably provision your infrastructure as a product. You can self-serve infrastructure from a defined catalog of products or push products to designated target accounts in a hub-and-spoke model. You can define Service Catalog products and their provisioning templates by using CloudFormation scripting or by using the AWS CDK.  In both approaches, Service Catalog provisions a product by calling CloudFormation to deploy a stack that represents the product's provisioning template. The stack is deployed to all designated target accounts within a CloudFormation stack set.

The AWS CDK approach for Service Catalog development supports greater modularization and reuse than CloudFormation, because you can define products and their resources by using predefined Service Catalog product and portfolio classes as well as predefined resource types. An AWS CDK implementation requires more advanced programming skills. This might be justified if your organization wants to establish its own reusable product framework with standardized resource configurations and behaviors as a foundation for your AWS infrastructure development.

You can use Service Catalog Puppet and Service Catalog Factory to augment Service Catalog functionality, primarily for provisioning. Service Catalog Puppet features declarative and tag-based product provisioning specifications; built-in, customizable, high-performance, and purpose-built provisioning workflows; and built-in, customizable, action-based CI/CD and SDLC pipelines. By using the workflow dependency management and built-in test automation features, you can chain Service Catalog products with less operational risk. Service Catalog Puppet helps you provision products to hundreds of accounts within aggressive time windows reliably. Service Catalog Factory is similar to AWS Control Tower. It generates accounts and calls Service Catalog to provision IaP within those accounts.

AWS Service Catalog and Service Catalog Tools provide extensive functionality to help you manage IaP on AWS. Service Catalog and these tools are undergoing constant improvements. For the latest features, see [AWS Service Catalog features](https://aws.amazon.com/servicecatalog/features/) and the [AWS Service Catalog Products repository](https://github.com/awslabs/aws-service-catalog-products).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
