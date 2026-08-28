---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cmk-backing-key-rotation-enabled.html
---

# cmk-backing-key-rotation-enabled
<a name="cmk-backing-key-rotation-enabled"></a>

Checks if automatic key rotation is enabled for each key and matches to the key ID of the customer created AWS KMS key. The rule is NON\_COMPLIANT if the AWS Config recorder role for a resource does not have the kms:DescribeKey permission.

**Note**
Automatic key rotation is not supported for asymmetric KMS keys, HMAC KMS keys, KMS keys with imported key material, or KMS keys in custom key stores.

**Identifier:** CMK\_BACKING\_KEY\_ROTATION\_ENABLED

**Resource Types:** AWS::KMS::Key

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d369c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
