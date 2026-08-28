---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/fsx-openzfs-deployment-type-check.html
---

# fsx-openzfs-deployment-type-check
<a name="fsx-openzfs-deployment-type-check"></a>

Checks if the Amazon FSx for OpenZFS file systems are configured with certain deployment types. The rule is NON\_COMPLIANT if FSx for OpenZFS file systems are not configured with the deployment types you specify.

**Identifier:** FSX\_OPENZFS\_DEPLOYMENT\_TYPE\_CHECK

**Resource Types:** AWS::FSx::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Melbourne), Canada West (Calgary) Region

**Parameters:**

deploymentTypesType: CSV
Comma-separated list of allowed Deployment types for the rule to check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d863c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
