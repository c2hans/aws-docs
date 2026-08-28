---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp02.html
---

# ADVPERF06-BP02 Optimize your intake request format (like HTTP/2 or HTTP/3) for faster processing
<a name="advperf06-bp02"></a>

 Use optimization in next generation networking protocols to address low latency needs for advertising workloads.

## Implementation guidance
<a name="implementation-guidance-56"></a>

 Implement HTTP/2 protocol, which offers features like multiplexing (multiple requests and responses are sent over the same TCP connection), header compression, and binary protocol. These features improve latency and throughput.

 AWS services do support HTTP/2 and HTTP/3 protocols for gains in performance efficiency.

## Key AWS services
<a name="key-aws-services-31"></a>
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

## Resources
<a name="resources-50"></a>
+  [*New – HTTP/3 Support for Amazon CloudFront*](https://aws.amazon.com/blogs/aws/new-http-3-support-for-amazon-cloudfront/)
+  [*Application Load Balancers enables gRPC workloads with end to end HTTP/2 support*](https://aws.amazon.com/about-aws/whats-new/2020/10/application-load-balancers-enable-grpc-workloads-end-to-end-http-2-support/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
