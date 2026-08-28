---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-kms-enabled.html
---

# redshift-cluster-kms-enabled
<a name="redshift-cluster-kms-enabled"></a>

Checks if Amazon Redshift clusters are using a specified AWS Key Management Service (AWS KMS) key for encryption. The rule is COMPLIANT if encryption is enabled and the cluster is encrypted with the key provided in the `kmsKeyArn` parameter. The rule is NON\_COMPLIANT if the cluster is not encrypted or encrypted with another key.

**Identifier:** REDSHIFT\_CLUSTER\_KMS\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV
Comma-separated list of AWS KMS key Amazon Resource Names (ARNs) used in Amazon Redshift clusters for encryption.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1297c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
