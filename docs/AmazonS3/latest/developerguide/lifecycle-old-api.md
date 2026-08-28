---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/lifecycle-old-api.html
---

# Appendix: Lifecycle Configuration APIs (Deprecated)
<a name="lifecycle-old-api"></a>

Bucket lifecycle configuration is updated to support filters based on object tags. That is, you can now specify a rule that specifies key name prefix, one or more object tags, or both to select a subset of objects to which the rule applies. The APIs have been updated accordingly. The following topics describe the prior version of the PUT and GET bucket lifecycle operations for backward compatibility.

**Topics**
+ [PUT Bucket lifecycle (Deprecated)](v1-rel-RESTBucketPUTlifecycle.md)
+ [GET Bucket lifecycle (Deprecated)](v1-rel-RESTBucketGETlifecycle.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
