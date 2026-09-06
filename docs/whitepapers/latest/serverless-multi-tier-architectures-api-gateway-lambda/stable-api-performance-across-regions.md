---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/stable-api-performance-across-regions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Stable API performance across regions
<a name="stable-api-performance-across-regions"></a>

 Each deployment of Amazon API Gateway includes a [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution under the hood. CloudFront is a content delivery service that uses Amazon’s global network of edge locations as connection points for clients using your API. This helps decrease the response latency of your API. By using multiple edge locations across the world, Amazon CloudFront also provides capabilities to combat distributed denial of service (DDoS) attack scenarios. For more information, review the [AWS Best Practices for DDoS Resiliency](https://d1.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf) whitepaper.

 You can improve the performance of specific API requests by using API Gateway to store responses in an optional in-memory cache. This approach not only provides performance benefits for repeated API requests, but it also reduces the number of times your Lambda functions are invoked, which can reduce your overall cost.
