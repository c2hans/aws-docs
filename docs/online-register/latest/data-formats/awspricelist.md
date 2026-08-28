---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awspricelist.html
---

# Data retrieval APIs for AWS Price List
<a name="awspricelist"></a>

AWS Price List provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="pricing-DescribeServices"></a>[DescribeServices](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html) | Retrieve service details for all (paginated) services (if serviceCode is not set) or service detail for a particular service (if given serviceCode) | Read |
| <a name="pricing-GetAttributeValues"></a>[GetAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html) | Retrieve all (paginated) possible values for a given attribute | Read |
| <a name="pricing-GetPriceListFileUrl"></a>[GetPriceListFileUrl](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html) | Retrieve the price list file URL for the given parameters | Read |
| <a name="pricing-GetProducts"></a>[GetProducts](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetProducts.html) | Retrieve all matching products with given search criteria | Read |
| <a name="pricing-ListPriceLists"></a>[ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html) | List all (paginated) eligible price lists for the given parameters | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
