---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-resources.html
---

# Other supported resources in Amazon OpenSearch Service
<a name="supported-resources"></a>

This topic describes additional resources that Amazon OpenSearch Service supports.

**bootstrap.memory\_lock**
OpenSearch Service enables `bootstrap.memory_lock` in `opensearch.yml`, which locks JVM memory and prevents the operating system from swapping it to disk. This applies to all supported instance types except for the following:
+ `t2.micro.search`
+ `t2.small.search`
+ `t2.medium.search`
+ `t3.small.search`
+ `t3.medium.search`

**Scripting module**
OpenSearch Service supports scripting for Elasticsearch 5.*x* and later domains. It does not support scripting for 1.5 or 2.3.
Supported scripting options include the following:
+ Painless
+ Lucene Expressions
+ Mustache
For Elasticsearch 5.5 and later domains, and all OpenSearch domains, OpenSearch Service supports stored scripts using the `_scripts` endpoint. Elasticsearch 5.3 and 5.1 domains support inline scripts only.

**TLS transport**
OpenSearch Service supports HTTP on port 80 and HTTPS over port 443, but does not support TLS transport.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
