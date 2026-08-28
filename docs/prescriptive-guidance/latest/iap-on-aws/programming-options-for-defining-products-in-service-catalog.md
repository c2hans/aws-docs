---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/programming-options-for-defining-products-in-service-catalog.html
---

# Programming options for defining products in Service Catalog
<a name="programming-options-for-defining-products-in-service-catalog"></a>

Two programming options for using Service Catalog to provision AWS infrastructure are CloudFormation templates or the AWS CDK. Currently there are no declarative or no-code mechanisms for defining a Service Catalog product.

## CloudFormation scripting
<a name="cloudformation-scripting.10234171-dcfd-5879-8045-371b39797bbc"></a>

AWS CloudFormation is a tried and true IaC native scripting language for provisioning AWS infrastructure. You can develop a CloudFormation script in the AWS Management Console or by using a development tool such as Visual Studio Code (or a simple text editor) and the AWS Command Language Interface (AWS CLI).

For more information, see the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html). For more information about using a CloudFormation template to specify a Service Catalog product, see the [AWS::ServiceCatalog::CloudFormationProduct resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html) in the CloudFormation documentation.

## Programmatic approach with the AWS CDK
<a name="programmatic-approach-with-the-aws-cdk.59edc3ab-bd82-568b-8fc0-23aa17f6d41d"></a>

The AWS CDK provides an elegant and powerful object-oriented programming framework for defining and maintaining AWS infrastructure by using a selection of programming languages. You can use the AWS CDK to develop object-oriented, fine-grained customizations and extensions to the AWS class framework. The AWS CDK is for users who want to customize AWS services for more sophisticated infrastructure needs, and who have the requisite programming skills and experience.

To implement Service Catalog solutions by using the AWS CDK, you use the built-in Service Catalog classes to define your products and portfolios.  These classes are provided by the AWS CDK [aws-cdk-lib.aws\_servicecatalog module](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_servicecatalog-readme.html).

You can use the AWS CDK to implement products in many ways. To avoid having to write the provisioning template for a product in CloudFormation and to maintain reusability, we recommend that you use the AWS CDK [ProductStack class](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_servicecatalog.ProductStack.html) to represent the provisioning template. A `ProductStack `instance is an AWS CDK stack that you programmatically add resources to. For example, you can add an S3 bucket, IAM roles, or an Amazon CloudWatch log. When you add the ProductStack instance to a defined `servicecatalog.CloudFormationProduct` instance as its provisioning template by calling `servicecatalog.CloudFormationTemplate.fromProductStack (<ProductStack instance>)`,  the AWS CDK automatically generates the CloudFormation template.

Here's an example of the Java `ProductStack `implementation for an Amazon S3 product.

```
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cdk from 'aws-cdk-lib';

class S3BucketProduct extends servicecatalog.ProductStack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    new s3.Bucket(this, 'BucketProduct');
  }
}

const product = new servicecatalog.CloudFormationProduct(this, 'Product', {
  productName: "My Product",
  owner: "Product Owner",
  productVersions: [
    {
      productVersionName: "v1",
      cloudFormationTemplate: servicecatalog.CloudFormationTemplate.fromProductStack(new S3BucketProduct(this, 'S3BucketProduct')),
    },
  ],
});
```

The AWS CDK provides built-in continuous integration and continuous deployment (CI/CD) pipelines. You can customize these built-in pipelines and software development lifecycle (SDLC) processes to meet your own process standards and objectives.

Custom AWS CDK classes can inherit from other classes to provide specialized functions, and a class may be composed from instances of other classes. If you use shared AWS CDK class frameworks to implement multiple Service Catalog products, consider any versioning or compatibility implications, especially across multiple development teams. You will have to ensure that changes are backward compatible, or that you have a versioning scheme that is being followed so that class changes you make for one product's doesn't break another product.

For more information, see the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
