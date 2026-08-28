---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/route53-query-logging-enabled.html
---

# route53-query-logging-enabled
<a name="route53-query-logging-enabled"></a>

Checks if DNS query logging is enabled for your Amazon Route 53 public hosted zones. The rule is NON\_COMPLIANT if DNS query logging is not enabled for your Amazon Route 53 public hosted zones.

**Identifier:** ROUTE53\_QUERY\_LOGGING\_ENABLED

**Resource Types:** AWS::Route53::HostedZone

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1349c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
