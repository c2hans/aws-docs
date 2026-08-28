---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-list.html
---

# List Your Algorithm or Model Package on AWS Marketplace
<a name="sagemaker-mkt-list"></a>

After creating and validating your algorithm or model in Amazon SageMaker AI, list your product on AWS Marketplace. The listing process makes your products available in the AWS Marketplace and the SageMaker AI console.

To list products on AWS Marketplace, you must be a registered seller. To register, use the self-registration process from the AWS Marketplace Management Portal (AMMP). For information, see [Getting Started as a Seller](https://docs.aws.amazon.com/marketplace/latest/userguide/user-guide-for-sellers.html) in the *User Guide for AWS Marketplace Providers*. When you start the product listing process from the Amazon SageMaker AI console, we check your seller registration status. If you have not registered, we direct you to do so.

To start the listing process, do one of the following:
+ From the SageMaker AI console, choose the product, choose **Actions**, and choose **Publish new ML Marketplace listing**. This carries over your product reference, the Amazon Resource Name (ARN), and directs you to the AMMP to create the listing.
+ Go to [ML listing process](https://aws.amazon.com/marketplace/management/ml-products/), manually enter the Amazon Resource Name (ARN), and start your product listing. This process carries over the product metadata that you entered when creating the product in SageMaker AI. For an algorithm listing, the information includes the supported instance types and hyperparameters. In addition, you can enter a product description, promotional information, and support information as you would with other AWS Marketplace products.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
