---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost04-bp03.html
---

# HNCOST04-BP03 Implement compression and caching for repetitive data transfers
<a name="hncost04-bp03"></a>

 Reduce data transfer volumes by compressing in-transit data and caching frequently accessed content at the edge.

 **Desired outcome:** Reduction in data transfer volumes and associated costs.

 **Level of risk exposed if this best practice is not established:** Low

 **Benefits of establishing this best practice:**
+  Lower bandwidth consumption
+  Faster transfer times
+  Reduced storage costs for compressed data

## Implementation guidance
<a name="implementation-guidance-54"></a>
+  Enable compression for payloads
+  Configure TTL for static assets in content delivery network such as Amazon CloudFront
+  Use compression for file/volume syncs using services such as AWS Storage Gateway

## Resources
<a name="resources-45"></a>
+  [Manage how long content stays in the cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
+  [Payload compression for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html)
+  [AWS Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
