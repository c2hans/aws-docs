---
source_url: https://docs.aws.amazon.com/application-discovery/latest/userguide/arn-formats.html
---

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# AWS Application Discovery Service ARN formats
<a name="arn-formats"></a>

An Amazon Resource Name (ARN) is a string that uniquely identifies an AWS resource. AWS requires an ARN when you want to specify a resource unambiguously across all of AWS. AWS Application Discovery Service defines the following ARNs.
+ **Discovery Agent**: `arn:aws:discovery:{{region}}:{{account}}:agent/discovery-agent/{{agentId}}`
+ **Agentless Collector**: `arn:aws:discovery:{{region}}:{{account}}:agent/agentless-collector/{{agentId}}`
+ **Migration Evaluator Collector**: `arn:aws:discovery:{{region}}:{{account}}:agent/migration-evaluator-collector/{{agentId}}`
+ **Discovery Connector**: `arn:aws:discovery:{{region}}:{{account}}:agent/discovery-connector/{{agentId}}`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
