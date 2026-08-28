---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-migration-limitations.html
---

# Known limitations during migration
<a name="next-gen-migration-limitations"></a>

The following limitations apply during the migration period from AWS Resilience Hub v1 to the next generation of Resilience Hub.

| Limitation | Description | Workaround |
| --- | --- | --- |
| Assessment history | v1 assessment results are not automatically migrated to the next generation of Resilience Hub format | v1 results remain accessible through v1 APIs during the transition period |
| Custom resilience checks | v1 custom checks are not migrated | Review failure mode findings – GenAI assessments typically cover the same concerns |
| AppRegistry input source | AppRegistry is not supported as an input source in the next generation of Resilience Hub | Use alternative input sources such as CloudFormation stacks or resource tags |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
