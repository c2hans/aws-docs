---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aosperf06-bp03.html
---

# AOSPERF06-BP03 Implement HTTP compression
<a name="aosperf06-bp03"></a>

 Reduce request and response payload sizes by enabling GZIP compression.

 **Level of risk exposed if this best practice is not established:** Low

 **Desired outcome**: GZIP compression is enabled in the OpenSearch Service domain, reducing the size of data being ingested or requested.

 **Benefits of establishing this best practice:** Reduce the payload size of requests and responses.

## Implementation guidance
<a name="implementation-guidance-44"></a>

 In OpenSearch Service domains, GZIP compression can be used to compress HTTP requests and responses. This compression helps reduce document size, lowering bandwidth usage and latency, resulting in improved transfer speeds.

### Implementation steps
<a name="implementation-steps-28"></a>
+  To use compression, include the following headers in the HTTP requests of your application:

```
'Accept-Encoding': 'gzip'
```

```
'Content-Encoding': 'gzip'
```

## Resources
<a name="resources-42"></a>
+  [Compressing HTTP requests in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gzip.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
