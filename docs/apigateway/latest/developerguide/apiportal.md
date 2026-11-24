---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal.html
---

# API Portal in API Gateway

API Portal is a feature of Amazon API Gateway that discovers the APIs running behind API Gateway, Application Load Balancer, and Amazon CloudFront across one AWS account or your entire organization in AWS Organizations, evaluates their security posture, and lets you publish *documentation portals* for the APIs that your teams use. API Portal builds a continuously updated inventory from traffic logs and service configuration records. You don't need to reroute traffic, forward logs, or register APIs by hand.

To use API Portal, you need an AWS account with at least one API running behind API Gateway, Application Load Balancer, or CloudFront, and IAM permissions for API Portal. To discover APIs across all accounts in your organization at once, without enabling discovery in each account, you also need AWS Organizations. For more information, see [Prerequisites for API Portal](apiportal-prerequisites.md).

## Features of API Portal
<a name="apiportal-features"></a>

*API discovery*
Builds and continuously updates an inventory of every API behind API Gateway REST APIs, Application Load Balancer, and CloudFront in your account or organization, including APIs that receive traffic but that no one registered in your API catalog. See [Enable API discovery in API Portal](apiportal-enable-discovery.md).

*Classification*
Every discovered API starts as a *shadow API*. You promote the APIs that you want to govern to *managed APIs*. API Portal then flags managed APIs that become zombie or orphaned. See [API Portal concepts](apiportal-concepts.md).

*AI endpoint identification*
Optionally identifies AI-facing endpoints in your inventory, such as MCP servers, A2A servers, and LLM-backed APIs, from the protocols seen in their traffic. See [Identify AI-facing endpoints with API Portal](apiportal-ai-discovery.md).

*Security posture*
Evaluates each managed API against a set of security postures, such as authentication, request validation, throttling, TLS version, and AWS WAF protection, and reports findings. See [Review security posture in API Portal](apiportal-security-posture.md). When you use AWS WAF API Security on the web ACL in front of an API, API Portal also shows the threats that AWS WAF detected on that managed API. For more information, see [AWS WAF API Security](https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security.html) in the *AWS WAF Developer Guide*.

*Documentation portals*
Groups managed APIs into products with API reference pages (content generated from each API definition) and your own documentation, and publishes them as a documentation portal for internal teams or external partners. See [Documentation portals in API Portal](apiportal-documentation-portals.md).

## How this chapter is organized
<a name="apiportal-topics"></a>
+ [Get started with API Portal](apiportal-get-started.md): how resources fit together, concepts, prerequisites.
+ [Discover APIs with API Portal](apiportal-discover.md): enable discovery, AI discovery, the API inventory, managed APIs, zombie and orphaned APIs.
+ [Review the security of your APIs with API Portal](apiportal-secure.md): security posture findings and AWS WAF API Security.
+ [Document and publish APIs with API Portal](apiportal-document.md): products, rule-based products, documentation portals, access control, publishing.
+ [Troubleshoot API Portal](apiportal-troubleshooting.md).
+ Elsewhere in this guide: [Identity and access management for API Portal](security-iam-apiportal.md), [Quotas for API Portal](apiportal-quotas.md).

## How API Portal defines an API
<a name="apiportal-how-it-defines-an-api"></a>

API Portal defines an API as an HTTP method and a URI path on a front-door resource (identified by its hostname and port, and for API Gateway, the deployed stage), for example `GET /v1/payments`. This is the unit that appears as a row in the API inventory. It differs from the API Gateway `RestApi` resource, which can include multiple domains, stages, paths, and methods. API Portal uses the method-and-path definition so that APIs from API Gateway, Application Load Balancer, and CloudFront are represented the same way and align with the OpenAPI Specification. As a result, one API Gateway `RestApi` typically appears in the inventory as several rows, one for each method and path.

## How APIs are discovered
<a name="apiportal-how-discovery-works"></a>

Discovery works differently for each source service, which affects what appears in your inventory.
+ **API Gateway**: REST APIs are discovered from their configuration (the AWS Config configuration items for the REST API and its deployed stages) and from traffic. HTTP APIs and WebSocket APIs aren't discovered. APIs with explicit methods on literal paths appear in the inventory whether or not they receive requests.
+ **Application Load Balancer**: APIs are discovered from observed traffic. A load balancer endpoint that receives no requests doesn't appear in the inventory.
+ **CloudFront**: APIs are discovered from observed traffic. Because CloudFront is a global service, APIs fronted by CloudFront are discovered only in the us-east-1 Region.

Discovery runs continuously but isn't instantaneous. New APIs typically appear within a few hours; allow up to 24 hours after you first enable discovery for an account or organization. Allow time for newly created APIs, or APIs that have recently started receiving traffic, to appear. Discovery is read-only: it doesn't change your APIs, and promoting an API to managed doesn't modify the underlying API Gateway, Application Load Balancer, or CloudFront resource.

## API Portal and API Gateway Portals
<a name="apiportal-and-portals"></a>

API Gateway Portals publish APIs that you build on API Gateway to developers. Documentation portals in API Portal do the same for any managed API, whether it runs on API Gateway, Application Load Balancer, or CloudFront. API Gateway Portals and API Portal documentation portals are separate resources: APIs published in an existing API Gateway Portal don't automatically become managed APIs, and there is no migration between the two at launch. If you have existing API Gateway Portals, they continue to work under their current pricing, and you manage them from the **Documentation portals** section of API Portal in the API Gateway console. For how the two relate and where to start, see [How API Portal resources fit together](apiportal-how-it-fits.md).

## Pricing for API Portal
<a name="apiportal-pricing"></a>

API Portal has two charges, discovery and documentation portals, and an API is never billed under both. For how billing works, see [How API Portal is billed](apiportal-how-it-fits.md#apiportal-how-it-fits-pricing). For rates, see [API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/).

## Considerations
<a name="apiportal-considerations"></a>
+ For API Gateway, API Portal discovers REST APIs only. HTTP APIs and WebSocket APIs aren't discovered and can't be added to documentation portals.
+ Configuration-based discovery of API Gateway REST APIs covers explicit methods on literal paths. A method of `ANY` or a greedy path such as `/{proxy+}` doesn't describe one endpoint, so it isn't discovered from configuration; it appears only after it receives traffic, as the concrete method and path that were called.
+ Application Load Balancer and CloudFront APIs are discovered from traffic only. An endpoint that receives little or no traffic doesn't appear. Allow sustained traffic over several hours before you expect a new endpoint in the inventory.
+ When you delete an API or stop sending traffic to it, its row stays in the inventory for about 30 days before it's removed. Deleting the discovery configuration doesn't remove inventory rows sooner.
+ When an API is reachable through more than one front door (for example, an API Gateway REST API behind a CloudFront distribution), the inventory shows one row per front door.
+ CloudFront is a global service, so APIs fronted by CloudFront appear in the inventory in the US East (N. Virginia) Region only.
+ API Gateway Portals and API Portal documentation portals are separate resources. There is no migration between them at launch; existing API Gateway Portals continue to work and are managed from the **Documentation portals** section of API Portal.
+ Changes to products, pages, and portal settings take effect in a documentation portal only after you publish the portal.

## Region availability
<a name="apiportal-regions"></a>

API Portal is available in the following AWS Regions: Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (New Zealand), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Taipei), Asia Pacific (Thailand), Asia Pacific (Tokyo), Canada (Central), Canada West (Calgary), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Israel (Tel Aviv), Mexico (Central), South America (São Paulo), US East (N. Virginia), US East (Ohio), US West (N. California), and US West (Oregon).

API Portal resources are Regional. APIs fronted by CloudFront are discovered only in the us-east-1 Region.
