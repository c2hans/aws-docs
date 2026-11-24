---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-how-it-fits.html
---

# How API Portal resources fit together

API Portal has four main resource types. Each builds on the one before it.

| Resource | What it is | ARN |
| --- | --- | --- |
| Discovered API | One HTTP method and path on a front-door resource, found by discovery. Discovered APIs are rows in the inventory, not resources you create; every one starts as a shadow API. | None (inventory item) |
| Managed API | A discovered API that you promoted. Managed APIs are evaluated for security posture and are the unit that additional capabilities attach to. Only managed APIs can be added to a product. | …:apiportal:…:managedapis/{{id}} |
| Product | A named group of managed APIs with documentation: an overview page, an API reference page for each API that you choose to document, and custom pages. Consumers browse a documentation portal by product. Products can be shared across accounts. | …:apiportal:…:products/{{id}} |
| Documentation portal | The website that consumers visit. A portal contains one or more products, has its own authorization and domain settings, and serves a snapshot that you publish. | …:apiportal:…:portals/{{id}} |

A product also has three child resources, each with its own ARN under the product's ARN: product pages (`…:products/{{id}}/productpages/{{page-id}}`), product API pages (`…:products/{{id}}/apipages/{{page-id}}`), and the product sharing policy (`…:products/{{id}}/sharingpolicy`). For the full list of ARN formats, see [Identity and access management for API Portal](security-iam-apiportal.md).

Discovery itself is controlled by a *discovery configuration*: one per account per Region (`…:apiportal:…:discoveryconfiguration`), or one per organization per Region owned by the management account (`…:apiportal:…:orgdiscoveryconfiguration`). It records which services to scan, what to exclude, and whether AI endpoint identification is on. See [Enable API discovery in API Portal](apiportal-enable-discovery.md).

In the console and in this guide, portals are called *documentation portals* because documentation is what they do today. In ARNs, IAM policies, and the API, the resource type is `portals`.

API Portal has its own API namespace, `apiportal`, with its own IAM actions, ARNs, and AWS CLI commands (`aws apiportal`). It's separate from the `apigateway` and `apigatewayv2` namespaces that you use to build APIs.

## API Portal and API Gateway Portals
<a name="apiportal-how-it-fits-portals"></a>

API Gateway Portals publish APIs that you build on API Gateway to developers. Documentation portals in API Portal do the same job for any managed API, whether it runs on API Gateway, Application Load Balancer, or CloudFront, and are priced per API rather than per portal product. The two live under different ARN paths today: API Gateway Portals under `apigateway`, documentation portals under `apiportal`. They are separate resources: APIs published in an API Gateway Portal don't automatically become managed APIs, and there is no migration between API Gateway Portals and documentation portals at launch.
+ **If you have API Gateway Portals today:** they continue to work, with the same features and the same pricing. You manage them from the **Documentation portals** section of API Portal in the API Gateway console. New portals that you create there are API Portal documentation portals. You don't have to enable discovery to keep using your existing portals. For the existing portal documentation, see [API Gateway Portals](apigateway-portals.md).
+ **If you evaluated API Gateway Portals and want more:** API Portal adds discovery of APIs you didn't build on API Gateway, security posture findings, and granular authorization in portals. Start with [Enable API discovery in API Portal](apiportal-enable-discovery.md), then publish a documentation portal from the APIs you promote.
+ **If you're new to both:** enable discovery, review the inventory, promote the APIs your teams should use, and publish them in a documentation portal. See [Next steps](apiportal-enable-discovery.md#apiportal-enable-discovery-next-steps).

## How API Portal is billed
<a name="apiportal-how-it-fits-pricing"></a>

API Portal has two charges, and an API is never billed under both.
+ **Discovery** is billed per discovered API per month, to the account that enabled discovery (the management account for organization-wide discovery), with a monthly minimum per account or organization in each Region where discovery is enabled.
+ **Documentation portals** are billed per documentation portal per month, to the account that owns the portal, with a number of APIs included per portal and a per-API charge above that.

An API that is documented in one of your organization's documentation portals is billed under Documentation Portals and is removed from your discovered-API count. Each documentation portal also covers a block of your discovered APIs, whether or not they're documented in it, so you pay for discovered APIs only beyond that coverage. An account or organization with at least one documentation portal doesn't pay the discovery minimum. Discovered APIs that aren't documented in a portal are still billed under Discovery. APIs shared into your portal from another organization are billed through the portal only. Your bill shows documented APIs as a $0.00 line item under Discovery so you can see how many were excluded.

Monthly charges are prorated daily. For rates and worked examples, see [API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/).
