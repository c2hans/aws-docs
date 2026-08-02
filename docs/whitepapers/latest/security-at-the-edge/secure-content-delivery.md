---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-at-the-edge/secure-content-delivery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Secure content delivery
<a name="secure-content-delivery"></a>

 Secure content delivery provides content, such as data, videos, applications, and APIs, quickly and securely to customers. These should be delivered over secure transport, using the recommended version of Transport Layer Security (TLS) to encrypt communications between endpoints. If necessary, there are a number of methods that you can use to help secure that same content through restricted access, including signed URLs, signed cookies, and token authentication.

 [Amazon CloudFront](https://aws.amazon.com/cloudfront/), a global content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to viewers with low latency and high transfer speeds, addresses these areas of security when it is deployed at AWS edge locations.

 To create a more secure CDN, organizations can gain protection against L3/L4 DDoS attacks using [AWS Shield](https://aws.amazon.com/shield/). AWS also offers AWS Shield Advanced, which provides additional detection and mitigation against large and sophisticated DDoS attacks, near-real-time visibility into attacks, and integration with [AWS WAF](https://aws.amazon.com/waf/), a web application firewall service, to protect against application layer (L7) attacks. Together, these services create a flexible, layered security perimeter.

 CloudFront offers security capabilities, including field-level encryption and HTTPS support, seamlessly running with AWS Shield Advanced, AWS WAF, and [Amazon Route 53](https://aws.amazon.com/route53/) to protect against multiple types of attacks, including network and application layer DDoS attacks. For more details about CloudFront and Route 53, see the [Appendix](appendix-aws-services-for-edge-computing.md).
