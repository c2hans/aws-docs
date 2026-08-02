---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-responseplan-ssmautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ResponsePlan SsmAutomation
<a name="aws-properties-ssmincidents-responseplan-ssmautomation"></a>

The `SsmAutomation` property type specifies details about the Systems Manager Automation runbook that will be used as the runbook during an incident.

## Syntax
<a name="aws-properties-ssmincidents-responseplan-ssmautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-responseplan-ssmautomation-syntax.json"></a>

```
{
  "[DocumentName](#cfn-ssmincidents-responseplan-ssmautomation-documentname)" : {{String}},
  "[DocumentVersion](#cfn-ssmincidents-responseplan-ssmautomation-documentversion)" : {{String}},
  "[DynamicParameters](#cfn-ssmincidents-responseplan-ssmautomation-dynamicparameters)" : {{[ DynamicSsmParameter, ... ]}},
  "[Parameters](#cfn-ssmincidents-responseplan-ssmautomation-parameters)" : {{[ SsmParameter, ... ]}},
  "[RoleArn](#cfn-ssmincidents-responseplan-ssmautomation-rolearn)" : {{String}},
  "[TargetAccount](#cfn-ssmincidents-responseplan-ssmautomation-targetaccount)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-responseplan-ssmautomation-syntax.yaml"></a>

```
  [DocumentName](#cfn-ssmincidents-responseplan-ssmautomation-documentname): {{String}}
  [DocumentVersion](#cfn-ssmincidents-responseplan-ssmautomation-documentversion): {{String}}
  [DynamicParameters](#cfn-ssmincidents-responseplan-ssmautomation-dynamicparameters): {{
    - DynamicSsmParameter}}
  [Parameters](#cfn-ssmincidents-responseplan-ssmautomation-parameters): {{
    - SsmParameter}}
  [RoleArn](#cfn-ssmincidents-responseplan-ssmautomation-rolearn): {{String}}
  [TargetAccount](#cfn-ssmincidents-responseplan-ssmautomation-targetaccount): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-responseplan-ssmautomation-properties"></a>

`DocumentName`  <a name="cfn-ssmincidents-responseplan-ssmautomation-documentname"></a>
The automation document's name.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentVersion`  <a name="cfn-ssmincidents-responseplan-ssmautomation-documentversion"></a>
The version of the runbook to use when running.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DynamicParameters`  <a name="cfn-ssmincidents-responseplan-ssmautomation-dynamicparameters"></a>
The key-value pairs to resolve dynamic parameter values when processing a Systems Manager Automation runbook.
*Required*: No
*Type*: Array of [DynamicSsmParameter](aws-properties-ssmincidents-responseplan-dynamicssmparameter.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-ssmincidents-responseplan-ssmautomation-parameters"></a>
The key-value pair parameters to use when running the runbook.
*Required*: No
*Type*: Array of [SsmParameter](aws-properties-ssmincidents-responseplan-ssmparameter.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ssmincidents-responseplan-ssmautomation-rolearn"></a>
The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov))?:[a-z-]+:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetAccount`  <a name="cfn-ssmincidents-responseplan-ssmautomation-targetaccount"></a>
The account that the automation document will be run in. This can be in either the management account or an application account.
*Required*: No
*Type*: String
*Allowed values*: `IMPACTED_ACCOUNT | RESPONSE_PLAN_OWNER_ACCOUNT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
