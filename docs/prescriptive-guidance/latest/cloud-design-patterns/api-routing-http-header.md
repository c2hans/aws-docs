---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-http-header.html
---

# HTTP header routing pattern
<a name="api-routing-http-header"></a>

Header-based routing enables you to target the correct service for each request by specifying an HTTP header in the HTTP request. For example, sending the header `x-service-a-action: get-thing` would enable you to `get thing` from `Service A`. The path of the request is still important, because it offers guidance on which resource you're trying to work on.

In addition to using HTTP header routing for actions, you can use it as a mechanism for version routing, enabling feature flags, A/B tests, or similar needs. In reality, you will likely use header routing with one of the other routing methods to create robust APIs.

The architecture for HTTP header routing typically has a thin routing layer in front of microservices that routes to the correct service and returns a response, as illustrated in the following diagram. This routing layer could cover all services or just a few services to enable an operation such as version-based routing.

![HTTP header routing.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/93e01f76-328c-4ea5-9108-4066d1a3fe94.png)

## Pros
<a name="pros.5168efcb-e88a-50a5-af1e-118df0e981d2"></a>

Configuration changes require minimal effort and can be automated easily. This method is also flexible and supports creative ways to expose only specific operations you would want from a service.

## Cons
<a name="cons.1ef0f1df-4558-50d4-9598-a1e3d8264131"></a>

As with the hostname routing method, HTTP header routing assumes that you have full control over the client and can manipulate custom HTTP headers. Proxies, content delivery networks (CDNs), and load balancers can limit the header size. Although this is unlikely to be a concern, it could be an issue depending on how many headers and cookies you add.
