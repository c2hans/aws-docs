---
source_url: https://docs.aws.amazon.com/marketplace/latest/developerguide/discovery-service-quotas.html
---

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Service quotas for AWS Marketplace Discovery API
<a name="discovery-service-quotas"></a>

Your AWS account has the following quotas related to the AWS Marketplace Discovery API.

**Request quotas**

| **API operation** | **Request rate (per AWS account)** |
| --- | --- |
| GetListing | 5 per second |
| GetProduct | 5 per second |
| GetOffer | 5 per second |
| GetOfferTerms | 5 per second |
| GetOfferSet | 5 per second |
| ListPurchaseOptions | 5 per second |
| ListFulfillmentOptions | 5 per second |
| SearchListings | 10 per second |
| SearchFacets | 10 per second |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
