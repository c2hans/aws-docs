---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-quotas.html
---

# Quotas for API Portal

The following quotas apply to API Portal. For more information, see [API Portal in API Gateway](apiportal.md).

| Resource or operation | Default quota | Can be increased |
| --- | --- | --- |
| Discovery configurations per account per Region | 1 | No |
| Organization discovery configurations per organization per Region | 1 | No |
| Delegated administrators for API Portal per organization | 1 | No |
| Resource ARNs, account IDs, or organizational unit IDs per discovery filter | 50 each | No |
| Managed APIs per account | 5,000 | No |
| Managed APIs per product | 200 | No |
| Products a managed API can belong to | 50 | No |
| Managed APIs per associate or disassociate request | 25 | No |
| Rule filters per rule-based product | 6 (one per attribute) | No |
| Values per rule filter | 10 | No |
| Documentation portals per account | 15 | Yes |
| Products per documentation portal | 200 | No |
| Products per account | 500 | No |
| Product pages and product API pages per product | 40 each | Yes |
| Page content size | 32,000 characters | No |
| Portal logo size | 200 KB | No |
| Custom domain names per documentation portal | 1 | No |
| Tags per resource | 50 | No |

## API request rate limits
<a name="apiportal-quotas-rate-limits"></a>

API Portal throttles requests to its API per account per Region. Each operation has a steady-state rate and a burst limit. Requests over the limit are rejected with HTTP status code 429 (`TooManyRequestsException`); retry with exponential backoff. Rates below one request per second are shown per minute.

| Operations | Rate | Burst |
| --- | --- | --- |
| All operations combined (account total) | 10 per second | 40 |
| GetPortal, ListPortals, GetProduct, GetProductSharingPolicy, GetProductPage, ListProductPages, GetProductApiPage, ListProductApiPages, GetManagedApi, GetApiInventoryItem, ListTagsForResource | 10 per second | 10 |
| ListProducts, ListManagedApis, ListManagedApiEvents, ListApiInventoryItems, ListDiscoveryStatuses, GetDiscoveryConfiguration, GetOrganizationDiscoveryConfiguration, TagResource, UntagResource | 5 per second | 5 |
| CreateProduct, CreateManagedApi | 2 per second | 2 |
| DeleteProduct, AssociateManagedApis, DisassociateManagedApis | 1 per second | 1 |
| UpdateProduct | 30 per minute | 1 |
| CreateProductPage, UpdateProductPage, DeleteProductPage, CreateProductApiPage, UpdateProductApiPage, DeleteProductApiPage, PutProductSharingPolicy, DeleteProductSharingPolicy, PutDiscoveryConfiguration, DeleteDiscoveryConfiguration | 20 per minute | 1 |
| CreatePortal | 6 per minute | 1 |
| UpdatePortal, UpdatePortalPublishStatus, DeletePortal, CreatePortalPreview, DeleteManagedApi, PutOrganizationDiscoveryConfiguration, DeleteOrganizationDiscoveryConfiguration, StartDiscovery, StopDiscovery | 2 per minute | 1 |
