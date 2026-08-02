---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-automatic-minor-version-upgrade-enabled.html
---

# rds-automatic-minor-version-upgrade-enabled
<a name="rds-automatic-minor-version-upgrade-enabled"></a>

Checks if Amazon Relational Database Service (RDS) database instances are configured for automatic minor version upgrades. The rule is NON\_COMPLIANT if the value of 'autoMinorVersionUpgrade' is false.

**Identifier:** RDS\_AUTOMATIC\_MINOR\_VERSION\_UPGRADE\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## Proactive Evaluation
<a name="w2aac20c16c17b7e1219c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
    "AutoMinorVersionUpgrade": {{BOOLEAN}}*,
    "Engine": {{String}}*
}
...
```

\*For more information on valid values for these inputs, see [ AutoMinorVersionUpgrade ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-autominorversionupgrade) and [Engine](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-engine) in the AWS CloudFormation User Guide.

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html).

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1219c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
