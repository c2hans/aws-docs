---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/beanstalk-enhanced-health-reporting-enabled.html
---

# beanstalk-enhanced-health-reporting-enabled
<a name="beanstalk-enhanced-health-reporting-enabled"></a>

Checks if an AWS Elastic Beanstalk environment is configured for enhanced health reporting. The rule is COMPLIANT if the environment is configured for enhanced health reporting. The rule is NON\_COMPLIANT if the environment is configured for basic health reporting.

**Identifier:** BEANSTALK\_ENHANCED\_HEALTH\_REPORTING\_ENABLED

**Resource Types:** AWS::ElasticBeanstalk::Environment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d275c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
