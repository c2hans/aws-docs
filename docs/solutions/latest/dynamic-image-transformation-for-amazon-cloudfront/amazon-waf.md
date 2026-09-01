---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/amazon-waf.html
---

# AWS WAF and rate-based rules
<a name="amazon-waf"></a>

This solution’s default configuration doesn’t deploy an AWS WAF web application firewall (WAF) in front of the image endpoint or the API endpoints, and we strongly recommend adding one. The solution can’t attach a web ACL on your behalf to a CloudFront distribution or custom endpoint that you own or place in front of the solution, so this is a step to configure in your own account for proper protection.

For that reason, we strongly recommend associating a WAF web ACL that includes a [rate-based rule](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html) with the distribution that serves your images. A rate-based rule caps the request rate from any single source, which both increases distributed denial of service (DDoS) protection and bounds the cost impact of automated traffic against the unauthenticated image endpoint (see [Smart cropping cost exposure (ECS architecture)](rekognition-cost-exposure.md)). Because the image endpoint is unauthenticated by default, a rate-based rule is the primary control for limiting abusive request volume.

For instructions on implementing AWS WAF in front of Amazon API Gateway, see [Using AWS WAF to protect your APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html) in the *Amazon API Gateway Developer Guide*. For CloudFront, see [Using AWS WAF to control access to your content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-aws-waf.html) in the *Amazon CloudFront Developer Guide*.

 [Get started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
