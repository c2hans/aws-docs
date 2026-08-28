---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/appendices.html
---

# Using AWS Data Exchange with the AWS Marketplace Catalog API
<a name="appendices"></a>

This chapter contains supplemental information for using AWS Data Exchange and the AWS Marketplace Catalog API. The AWS Marketplace Catalog API service provides an API interface for you as a provider to programmatically access the AWS Marketplace self-service publishing capabilities.

The API supports a wide range of operations for you to view and manage your products. You can extend your internal build or deployment pipeline to AWS Marketplace through API integration to automate your product update process. You can also create your own internal user interface on top of the API to manage your products on the AWS Marketplace.

You can use the AWS Marketplace Catalog API to update your AWS Data Exchange products. To view your products, you can use the `ListEntities` and `DescribeEntity` API operations. To update your AWS Data Exchange product, you need to create a new change set, which is the Catalog API resource that represents an asynchronous operation used to manage products. For more information, see the [AWS Marketplace Catalog API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Catalog_Service.html).

Keep the following in mind when working with the Catalog API:
+ Each AWS Data Exchange product is represented in the Catalog API as an [Entity](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_Entity.html).
+ AWS Data Exchange products have `DataProduct` as the `EntityType`.
+ Each product can have only one concurrently running change set at a time. This means that you can't create a second change set until the first one has finished running.

**Topics**
+ [Add data sets to AWS Data Exchange](add-data-sets.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
