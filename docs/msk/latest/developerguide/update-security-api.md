---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/update-security-api.html
---

# Updating a cluster's security settings using the API
<a name="update-security-api"></a>

To update the security settings for a Amazon MSK cluster using the API, see [UpdateSecurity](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-security.html#UpdateSecurity).

**Note**
The AWS CLI and API operations for updating the security settings of a MSK cluster are idempotent. This means that if you invoke the security update operation and specify an authentication or encryption setting that is the same setting that the cluster currently has, that setting won't change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
