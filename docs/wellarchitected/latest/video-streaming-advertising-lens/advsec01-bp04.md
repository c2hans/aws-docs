---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp04.html
---

# ADVSEC01-BP04 Implement authorization by setting access policies, and implement least privilege access to protect programmatic workloads
<a name="advsec01-bp04"></a>

 Address the risk of authenticated advertisers and SSPs access to data they should not reach.

## Implementation guidance
<a name="implementation-guidance-12"></a>

 Implement strong [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) policies when you deploy a global advertising technology workload. Use the principle of least privilege, and enforce the separation of duties for good security posture. Administrative access should only be given to a small number of secured administrators.

 Use [ IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) to validate IAM policies and verify that they match IAM best practices and your organization's security standards. IAM Access Analyzer can help your organization review and removed unused or external access across your AWS resources with continuous monitoring. IAM Access Analyzer can also assist administrators by validating your IAM policies against IAM policy grammar and AWS best practices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
