---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL AWSManagedRulesBotControlRuleSet
<a name="aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset"></a>

Details for your use of the Bot Control managed rule group, `AWSManagedRulesBotControlRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

For additional information about this and the other intelligent threat mitigation rule groups, see [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections) and [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list) in the *AWS WAF Developer Guide*.

## Syntax
<a name="aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset-syntax.json"></a>

```
{
  "[EnableMachineLearning](#cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-enablemachinelearning)" : {{Boolean}},
  "[InspectionLevel](#cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-inspectionlevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset-syntax.yaml"></a>

```
  [EnableMachineLearning](#cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-enablemachinelearning): {{Boolean}}
  [InspectionLevel](#cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-inspectionlevel): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset-properties"></a>

`EnableMachineLearning`  <a name="cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-enablemachinelearning"></a>
Applies only to the targeted inspection level.
Determines whether to use machine learning (ML) to analyze your web traffic for bot-related activity. Machine learning is required for the Bot Control rules `TGT_ML_CoordinatedActivityLow` and `TGT_ML_CoordinatedActivityMedium`, which inspect for anomalous behavior that might indicate distributed, coordinated bot activity.
For more information about this choice, see the listing for these rules in the table at [Bot Control rules listing](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html#aws-managed-rule-groups-bot-rules) in the *AWS WAF Developer Guide*.
Default: `TRUE`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InspectionLevel`  <a name="cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-inspectionlevel"></a>
The inspection level to use for the Bot Control rule group. The common level is the least expensive. The targeted level includes all common level rules and adds rules with more advanced inspection criteria. For details, see [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) in the *AWS WAF Developer Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `COMMON | TARGETED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
