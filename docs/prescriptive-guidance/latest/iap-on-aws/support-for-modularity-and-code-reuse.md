---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/support-for-modularity-and-code-reuse.html
---

# Support for modularity and code reuse
<a name="support-for-modularity-and-code-reuse"></a>

You can assemble a product from many different AWS resources or even from other products. Ideally, you define resources in a modular way so you can reuse them in multiple products. Resource-level reuse enables you to make any future changes in one place rather than across every product that uses that resource type.

Service Catalog provides a feature called *chaining* to support reusability at the product level. You can chain a product to one or more other products. For example, you might want to chain an S3 logging bucket product to a higher-level monitoring product. Although chaining supports modularity, it imposes some operational complexities because you have to manage dependencies. Service Catalog doesn't automatically maintain versioning between chained products, so it can't ensure that changes to one product don't break other products that depend on it.  Use chaining with care, and develop your own mechanisms for ensuring versioning and maintaining dependencies.

Service Catalog uses CloudFormation natively to deploy a product provisioning template as a CloudFormation stack. However, Service Catalog imposes some limitations on CloudFormation deployment of the product stack. In particular, Service Catalog provisioning doesn't support the CloudFormation include macro for inserting reusable script segments or referencing nested CloudFormation scripts (or stacks) to more than one level. These Service Catalog restrictions limit the ability to define products from reusable CloudFormation templates or components, which is a standard best practice when you define stacks natively in CloudFormation.

**Note**
Service Catalog allows you to successfully *define* products with provisioning templates that use these CloudFormation constructs. However, you will encounter *provision-time errors* if you use the include macro or nest multiple levels of scripts in a Service Catalog CloudFormation template.

These restrictions might make it difficult to implement modular and reusable products in Service Catalog. If modularity is a requirement, you might explore using the AWS CDK to implement your products and their provisioning templates, or use the provisioning workflows and engine in the AWS Labs Service Catalog Tools project, as described later in this guide.
