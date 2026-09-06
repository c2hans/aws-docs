---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/log-correlation-for-ddos-resilient-architectures.html
---

# Log correlation for DDoS resilient architectures
<a name="log-correlation-for-ddos-resilient-architectures"></a>

For DDoS resilient architectures, it's crucial to be able to correlate the logs between the services in the scope. For a typical web application setup, those services can be CloudFront, AWS WAF, and ALB.

When CloudFront forwards an HTTP request to its origin, it automatically injects the `X-Amz-Cf-Id` header, which contains an opaque string uniquely identifying the request. This value is logged in the CloudFront access logs under the `x-edge-request-id` field.

Similarly, ALB automatically injects the `X-Amzn-Trace-Id` header when forwarding a request to the target group. This header's value is logged in the ALB access logs under the `trace_id` field.

When a CloudFront distribution has a WAF web ACL attached, the WAF includes a `requestId` field in the WAF logs that contains the value of `X-Amz-Cf-Id` from CloudFront.

To see the relationship of the three services, see the following table:

| CloudFront logs | WAF (CloudFront) | ALB logs | Backend server log |
| --- | --- | --- | --- |
| X-Amz-Cf-Id = 'Ed0AiHF\_CGYF-DA=' | requestId = 'Ed0AiHF\_CGYF-DA=' | X-Amzn-Trace-Id = 'Root=1-67891233-abcdef012345678912345678' | X-Amz-Cf-Id = Ed0AiHF\_CGYF-DA= X-Amzn-Trace-Id = 'Root=1-67891233-abcdef012345678912345678' |

Similarly, when you attach a WAF web ACL to ALB, you will have `X-Amzn-Trace-Id` in the WAF logs that you can correlate with an ALB log value. For WAF logs examples, see [Log examples for web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging-examples.html).

| WAF (ALB) | ALB logs | Backend server Log |
| --- | --- | --- |
| X-Amzn-Trace-Id = 'Root=1-67891233-abcdef012345678912345678' | X-Amzn-Trace-Id = 'Root=1-67891233-abcdef012345678912345678' | X-Amzn-Trace-Id = 'Root=1-67891233-abcdef012345678912345678' |

For useful examples of WAF queries using Athena, see [How to use Amazon Athena queries to analyze AWS WAF logs and provide the visibility needed for threat detection](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-use-amazon-athena-queries-to-analyze-aws-waf-logs-and-provide-the-visibility-needed-for-threat-detection/).
