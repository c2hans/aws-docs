---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/protecting-api-endpoints-bp4.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Protecting API endpoints (BP4)
<a name="protecting-api-endpoints-bp4"></a>

When you must expose an API to the public, there is a risk that the API frontend could be targeted by a DDoS attack. To help reduce the risk, you can use [Amazon API Gateway](https://aws.amazon.com/api-gateway/) as an entryway to applications running on Amazon EC2, AWS Lambda, or elsewhere. By using Amazon API Gateway, you don’t need your own servers for the API frontend and you can obfuscate other components of your application. By making it harder to detect your application’s components, you can help prevent those AWS resources from being targeted by a DDoS attack.

 When you use Amazon API Gateway, you can choose from two types of API endpoints. The first is the default option: edge-optimized API endpoints that are accessed through an Amazon CloudFront distribution. The distribution is created and managed by API Gateway, however, so you don’t have control over it. The second option is to use a regional API endpoint that is accessed from the same AWS Region in which your REST API is deployed. AWS recommends that you use the second type of endpoint and associate it with your own Amazon CloudFront distribution. This gives you control over the Amazon CloudFront distribution and the ability to use AWS WAF for application layer protection. This mode provides you with access to scaled DDoS mitigation capacity across the AWS global edge network.

 When using Amazon CloudFront and AWS WAF with Amazon API Gateway, configure the following options:
+  Configure the cache behavior for your distributions to forward all headers to the API Gateway regional endpoint. By doing this, CloudFront will treat the content as dynamic and skip caching the content.
+  Protect your API Gateway against direct access by configuring the distribution to include the origin custom header x-api-key, by setting the [API key](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-key-with-console.html) value in API Gateway.
+  Protect the backend from excess traffic by configuring standard or burst rate limits for each method in your REST APIs.

 For more information about creating APIs with Amazon API Gateway, refer to [Amazon API Gateway](https://aws.amazon.com/api-gateway/getting-started/) [Getting Started](https://aws.amazon.com/api-gateway/getting-started/).
