---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-conformancepack-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConformancePack Source
<a name="aws-properties-config-conformancepack-source"></a>

Provides the CustomPolicyDetails, the rule owner (` AWS ` for managed rules, `CUSTOM_POLICY` for Custom Policy rules, and `CUSTOM_LAMBDA` for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your AWS resources.

## Syntax
<a name="aws-properties-config-conformancepack-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-conformancepack-source-syntax.json"></a>

```
{
  "[SourceIdentifier](#cfn-config-conformancepack-source-sourceidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-conformancepack-source-syntax.yaml"></a>

```
  [SourceIdentifier](#cfn-config-conformancepack-source-sourceidentifier): {{String}}
```

## Properties
<a name="aws-properties-config-conformancepack-source-properties"></a>

`SourceIdentifier`  <a name="cfn-config-conformancepack-source-sourceidentifier"></a>
For AWS Config Managed rules, a predefined identifier from a list. For example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed rule, see [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).
For AWS Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as `arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`.
For AWS Config Custom Policy rules, this field will be ignored.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
