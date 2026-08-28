---
source_url: https://docs.aws.amazon.com/finops-agent/latest/userguide/cross-region-inference.html
---

AWS FinOps Agent is in preview release and is subject to change.

# Amazon Bedrock usage and cross-region inference
<a name="cross-region-inference"></a>

During preview, AWS FinOps Agent runs in the US East (N. Virginia) Region (`us-east-1`). Your data, including context files, conversations, memory, and artifacts, remains stored in `us-east-1`.

AWS FinOps Agent uses Amazon Bedrock cross-region inference to improve performance and reliability. Cross-region inference requests are kept within the geography where the request originated. For example, requests from AWS Regions in the United States stay within AWS Regions in the United States. Agent inference may be processed outside the specific Region but remains within the same geography. All data is encrypted in transit. Cross-region inference does not change where your data is stored.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS FinOps Agent (preview). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finops-agent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
