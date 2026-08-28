---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/clb-desync-mode-check.html
---

# clb-desync-mode-check
<a name="clb-desync-mode-check"></a>

Checks if Classic Load Balancers (CLB) are configured with a user defined Desync mitigation mode. The rule is NON\_COMPLIANT if CLB Desync mitigation mode does not match with user defined Desync mitigation mode.

**Identifier:** CLB\_DESYNC\_MODE\_CHECK

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

desyncModeType: CSV
Comma-separated list of values. You can select a max of two. Valid values include 'Defensive', 'Strictest', and 'Monitor'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d289c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
