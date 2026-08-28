---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-input-sources-actions.html
---

# Input sources
<a name="next-gen-api-input-sources-actions"></a>

| Action | Method | Description |
| --- | --- | --- |
| CreateInputSource | POST | Configure a resource discovery source (resource tags, CloudFormation stack, Terraform state file, EKS cluster, or design file). For a single tag-based input source with multiple tags, the service discovers only resources that match all specified tags. For multiple tag-based input sources, the service discovers resources that match any of them. |
| ListInputSources | GET | List input sources for a service. |
| DeleteInputSource | POST | Delete an input source. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
