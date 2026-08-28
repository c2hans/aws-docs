---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elbv2-targetgroup-protocol-encrypted.html
---

# elbv2-targetgroup-protocol-encrypted
<a name="elbv2-targetgroup-protocol-encrypted"></a>

Checks the target groups for application and network load balancers use an encrypted transport protocol. The rule is NON\_COMPLIANT if configuration.protocol is not HTTPS, TLS, or QUIC. Lambda and ALB target types are not applicable.

**Identifier:** ELBV2\_TARGETGROUP\_PROTOCOL\_ENCRYPTED

**Resource Types:** AWS::ElasticLoadBalancingV2::TargetGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d785c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
