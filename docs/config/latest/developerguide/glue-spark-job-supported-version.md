---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/glue-spark-job-supported-version.html
---

# glue-spark-job-supported-version
<a name="glue-spark-job-supported-version"></a>

Checks if an AWS Glue Spark job is running on the specified minimum supported AWS Glue version. The rule is NON\_COMPLIANT if the AWS Glue Spark job is not running on the minimum supported AWS Glue version that you specify.

**Identifier:** GLUE\_SPARK\_JOB\_SUPPORTED\_VERSION

**Resource Types:** AWS::Glue::Job

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

minimumSupportedGlueVersionType: String
String value you must specify of the minimum supported AWS Glue version for the rule to check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d883c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
