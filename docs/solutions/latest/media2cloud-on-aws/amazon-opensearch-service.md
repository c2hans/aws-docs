---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/amazon-opensearch-service.html
---

# Amazon OpenSearch Service
<a name="amazon-opensearch-service"></a>

 The solution configures an Amazon OpenSearch Service cluster to index ingestion technical metadata and analysis metadata. The solution creates indices per type of the machine learning categories such as `celeb`, `label`, `face`, `faceMatch`, `segment`, `moderation`, `person`, `textract`, `transcribe`, `keyphrase`, `entity`, and `ingest `to allow the end user to fine tune the search results. The indexed documents are encrypted at rest. [Node-to-node encryption](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html) is also activated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
