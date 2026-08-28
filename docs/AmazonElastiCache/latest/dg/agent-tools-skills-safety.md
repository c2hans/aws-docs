---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agent-tools-skills-safety.html
---

# Guardrails and tracking usage
<a name="agent-tools-skills-safety"></a>

The ElastiCache skill includes safety guidance for high-impact operations so agents do not treat destructive or disruptive changes as routine setup steps. The skill identifies high-impact operations that must not be run automatically, including cache deletion, flushing data, snapshot deletion, production credential or AUTH token changes, security group rule removal, user or user group deletion, migration cutover execution, and manual failover on production caches. For such operations, the skill instructs agents to explain the expected impact and require direct user confirmation before proceeding. For changes that can affect availability, such as engine upgrades, scaling changes, security group updates, failover tests, or migration cutovers, the skill instructs agents to explain the expected impact, recommend staging validation or a maintenance window where appropriate, and prefer safer alternatives when available.

Before generating commands that create, modify, or delete resources, the skill instructs agents to validate user-provided values. If required information is missing or ambiguous, the skill instructs agents to stop and ask for the missing values instead of generating commands with placeholders, inferred settings, or incomplete resource identifiers.

## Tracking agent activity
<a name="agent-tools-skills-tracking"></a>

You can identify actions performed by an agent using the ElastiCache skill through the AWS CloudTrail `userAgent` field and ElastiCache resource tags.

For AWS API calls generated through the AWS Command Line Interface, AWS SDKs, or bundled scripts, the skill instructs agents to set `AWS_SDK_UA_APP_ID` to `AWSSkill-ElastiCache`. This identifier appears in the `User-Agent` HTTP header and in the CloudTrail `userAgent` field for each API call.

For resources created by an agent using the ElastiCache skill, review the resource tags in the ElastiCache console or by using `list-tags-for-resource`. The skill instructs agents to apply the following standard tags when creating resources:
+ `managed_by=aws-skills`
+ `skill=elasticache`
+ `skill_version=<skill-version>`
+ `created_by=elasticache-skill`
+ `generation_model=<model-id>`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
