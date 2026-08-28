---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/sns-encrypted-kms.html
---

# sns-encrypted-kms
<a name="sns-encrypted-kms"></a>

Checks if SNS topics are encrypted with AWS Key Management Service (AWS KMS). The rule is NON\_COMPLIANT if an SNS topic is not encrypted with AWS KMS. Optionally, specify the key ARNs, the alias ARNs, the alias name, or the key IDs for the rule to check.

**Identifier:** SNS\_ENCRYPTED\_KMS

**Resource Types:** AWS::SNS::Topic

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyIds (Optional)Type: CSV
Comma-separated list of AWS KMS key Amazon Resource Names (ARNs), KMS alias ARNs, KMS alias names, or KMS key IDs for the rule to check.

## Proactive Evaluation
<a name="w2aac20c16c17b7e1535c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
   "KmsMasterKeyId": "{{my-kms-key-Id}}"
}
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html).

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1535c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
