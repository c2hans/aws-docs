---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-path.html
---

# Path routing pattern
<a name="api-routing-path"></a>

Routing by paths is the mechanism of grouping multiple or all APIs under the same hostname, and using a request URI to isolate services; for example, `api.example.com/service-a` or `api.example.com/service-b`.

## Typical use case
<a name="path-routing-use-case"></a>

Most teams opt for this method because they want a simple architecture―a developer has to remember only one URL such as `api.example.com` to interact with the HTTP API. API documentation is often easier to digest because it is often kept together instead of being split across different portals or PDFs.

Path-based routing is considered a simple mechanism for sharing an HTTP API. However, it involves operational overhead such as configuration, authorization, integrations, and additional latency due to multiple hops. It also requires mature change management processes to ensure that a misconfiguration doesn't disrupt all services.

On AWS, there are multiple ways to share an API and route effectively to the correct service. The following sections discuss three approaches: HTTP service reverse proxy, API Gateway, and AWS CloudFront. None of the suggested approaches for unifying API services relies on the downstream services running on AWS. The services could run anywhere without issue or on any technology, as long as they're HTTP-compatible.

## HTTP service reverse proxy
<a name="path-routing-proxy"></a>

You can use an HTTP server such as [NGINX](https://www.f5.com/go/product/welcome-to-nginx) to create dynamic routing configurations. In a [Kubernetes](https://kubernetes.io/) architecture, you can also create an ingress rule to match a path to a service. (This guide doesn't cover Kubernetes ingress; see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/#the-ingress-resource) for more information.)

The following configuration for NGINX dynamically maps an HTTP request of `api.example.com/my-service/` to `my-service.internal.api.example.com`.

```
server {
    listen  80;

    location (^/[\w-]+)/(.*) {
        proxy_pass $scheme://$1.internal.api.example.com/$2;
    }
}
```

The following diagram illustrates the HTTP service reverse proxy method.

![Using an HTTP service reverse proxy for path routing.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/9470aa6b-8f8f-4d71-8402-29c57b6e5727.png)

This approach might be sufficient for some use cases that don't use additional configurations to start processing requests, allowing for the downstream API to collect metrics and logs.

To get ready for operational production readiness, you will want to be able to add observability to every level of your stack, add additional configuration, or add scripts to customize your API ingress point to allow for more advanced features such as rate limiting or usage tokens.

**Pros**

The ultimate aim of the HTTP service reverse proxy method is to create a scalable and manageable approach to unifying APIs into a single domain so it appears coherent to any API consumer. This approach also enables your service teams to deploy and manage their own APIs, with minimal overhead after deployment. AWS managed services for tracing, such as [AWS X-Ray](https://aws.amazon.com/xray/) or [AWS WAF](https://aws.amazon.com/waf/), are still applicable here.

**Cons**

The major downside of this approach is the extensive testing and management of infrastructure components that are required, although this might not be an issue if you have site reliability engineering (SRE) teams in place.

There is a cost tipping point with this method. At low to medium volumes, it is more expensive than some of the other methods discussed in this guide. At high volumes, it is very cost-effective (around 100K transactions per second or better).

## API Gateway
<a name="path-routing-gateway"></a>

The [Amazon API Gateway](https://aws.amazon.com/api-gateway/) service (REST APIs and HTTP APIs) can route traffic in a way that's similar to the HTTP service reverse proxy method. Using an API gateway in HTTP proxy mode provides a simple way to wrap many services into an entry point to the top-level subdomain `api.example.com`, and then proxy requests to the nested service; for example, `billing.internal.api.example.com`.

You probably don't want to get too granular by mapping every path in every service in the root or core API gateway. Instead, opt for wildcard paths such as `/billing/*` to forward requests to the billing service. By not mapping every path in the root or core API gateway, you gain more flexibility over your APIs, because you don't have to update the root API gateway with every API change.

![Path routing through API Gateway.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/ebde498e-50ef-4c74-9688-626d9e30795c.png)

**Pros**

For control over more complex workflows, such as changing request attributes, REST APIs expose the Apache Velocity Template Language (VTL) to allow you to modify the request and response. REST APIs can provide additional benefits such as these:
+ [Auth N/Z with AWS Identity and Access Management (IAM),](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications-security/authentication.html) [Amazon Cognito](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications-security/cognito.html), or [AWS Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
+ [AWS X-Ray for tracing](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-understanding-xray-traces.html)
+ [Integration with AWS WAF](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html)
+ [Basic rate limiting](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
+ Usage tokens for bucketing consumers into different tiers (see [Throttle API requests for better throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) in the API Gateway documentation)

**Cons**

At high volumes, cost might be an issue for some users.

## CloudFront
<a name="path-routing-cloudfront"></a>

You can use the [dynamic origin selection feature](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html) in [Amazon CloudFront](https://aws.amazon.com/cloudfront/) to conditionally select an origin (a service) to forward the request. You can use this feature to route a number of services through a single hostname such as `api.example.com`.

**Typical use case**

The routing logic lives as code within the Lambda@Edge function, so it supports highly customizable routing mechanisms such as A/B testing, canary releases, feature flagging, and path rewriting. This is illustrated in the following diagram.

![Path routing through Amazon CloudFront.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/0e0a6fbf-6813-4365-8e0e-b8fa1fc69b21.png)

**Pros**

If you require caching API responses, this method is good way to unify a collection of services behind a single endpoint. It is a cost-effective method to unify collections of APIs.

Also, CloudFront supports [field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html) as well as integration with AWS WAF for basic rate limiting and basic ACLs.

**Cons**

This method supports a maximum of 250 origins (services) that can be unified. This limit is sufficient for most deployments, but it might cause issues with a large number of APIs as you grow your portfolio of services.

Updating Lambda@Edge functions currently takes a few minutes. CloudFront also takes up to 30 minutes to complete propagating changes to all points of presence. This ultimately blocks further updates until they complete.
