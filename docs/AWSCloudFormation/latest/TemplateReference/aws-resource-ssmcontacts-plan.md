---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmcontacts-plan.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Plan
<a name="aws-resource-ssmcontacts-plan"></a>

Information about the stages and on-call rotation teams associated with an escalation plan or engagement plan.

**Note**
**Template example**: We recommend creating all Incident Manager`Contacts` resources using a single AWS CloudFormation template. For a demonstration, see the examples for [AWS::SSMContacts::Contacts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html).

## Syntax
<a name="aws-resource-ssmcontacts-plan-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmcontacts-plan-syntax.json"></a>

```
{
  "Type" : "AWS::SSMContacts::Plan",
  "Properties" : {
      "[ContactId](#cfn-ssmcontacts-plan-contactid)" : {{String}},
      "[RotationIds](#cfn-ssmcontacts-plan-rotationids)" : {{[ String, ... ]}},
      "[Stages](#cfn-ssmcontacts-plan-stages)" : {{[ Stage, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssmcontacts-plan-syntax.yaml"></a>

```
Type: AWS::SSMContacts::Plan
Properties:
  [ContactId](#cfn-ssmcontacts-plan-contactid): {{String}}
  [RotationIds](#cfn-ssmcontacts-plan-rotationids): {{
    - String}}
  [Stages](#cfn-ssmcontacts-plan-stages): {{
    - Stage}}
```

## Properties
<a name="aws-resource-ssmcontacts-plan-properties"></a>

`ContactId`  <a name="cfn-ssmcontacts-plan-contactid"></a>
The Amazon Resource Name (ARN) of the contact.
*Required*: No
*Type*: String
*Pattern*: `arn:[-\w+=\/,.@]+:[-\w+=\/,.@]+:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-]+)*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RotationIds`  <a name="cfn-ssmcontacts-plan-rotationids"></a>
The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stages`  <a name="cfn-ssmcontacts-plan-stages"></a>
A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.
*Required*: No
*Type*: Array of [Stage](aws-properties-ssmcontacts-plan-stage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssmcontacts-plan-return-values"></a>

### Ref
<a name="aws-resource-ssmcontacts-plan-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssmcontacts-plan-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssmcontacts-plan-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the `Plan` resource.
