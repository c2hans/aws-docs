---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-securitycontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::SecurityControl
<a name="aws-resource-securityhub-securitycontrol"></a>

The `AWS::SecurityHub::SecurityControl` resource specifies custom parameter values for an AWS Security Hub CSPM control. For a list of controls that support custom parameters, see [Security Hub CSPM controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html). You can also use this resource to specify the use of default parameter values for a control. For more information about custom parameters, see [Custom control parameters](https://docs.aws.amazon.com/securityhub/latest/userguide/custom-control-parameters.html) in the *AWS Security Hub CSPM User Guide*.

Tags aren't supported for this resource.

## Syntax
<a name="aws-resource-securityhub-securitycontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-securitycontrol-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::SecurityControl",
  "Properties" : {
      "[LastUpdateReason](#cfn-securityhub-securitycontrol-lastupdatereason)" : {{String}},
      "[Parameters](#cfn-securityhub-securitycontrol-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[SecurityControlArn](#cfn-securityhub-securitycontrol-securitycontrolarn)" : {{String}},
      "[SecurityControlId](#cfn-securityhub-securitycontrol-securitycontrolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-securitycontrol-syntax.yaml"></a>

```
Type: AWS::SecurityHub::SecurityControl
Properties:
  [LastUpdateReason](#cfn-securityhub-securitycontrol-lastupdatereason): {{String}}
  [Parameters](#cfn-securityhub-securitycontrol-parameters): {{
    {{Key}}: {{Value}}}}
  [SecurityControlArn](#cfn-securityhub-securitycontrol-securitycontrolarn): {{String}}
  [SecurityControlId](#cfn-securityhub-securitycontrol-securitycontrolid): {{String}}
```

## Properties
<a name="aws-resource-securityhub-securitycontrol-properties"></a>

`LastUpdateReason`  <a name="cfn-securityhub-securitycontrol-lastupdatereason"></a>
 The most recent reason for updating the customizable properties of a security control. This differs from the `UpdateReason` field of the [`BatchUpdateStandardsControlAssociations`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.
*Required*: No
*Type*: String
*Pattern*: `^([^-]|[-_ a-zA-Z0-9])+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-securityhub-securitycontrol-parameters"></a>
 An object that identifies the name of a control parameter, its current value, and whether it has been customized.
*Required*: Yes
*Type*: Object of [ParameterConfiguration](aws-properties-securityhub-securitycontrol-parameterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityControlArn`  <a name="cfn-securityhub-securitycontrol-securitycontrolarn"></a>
 The Amazon Resource Name (ARN) for a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityControlId`  <a name="cfn-securityhub-securitycontrol-securitycontrolid"></a>
 The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number, such as APIGateway.3.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-securityhub-securitycontrol-return-values"></a>

### Ref
<a name="aws-resource-securityhub-securitycontrol-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the identifier of the security control. For example, `Config.1`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-securityhub-securitycontrol--examples"></a>

### Configuring control parameters
<a name="aws-resource-securityhub-securitycontrol--examples--Configuring_control_parameters"></a>

This example configures a parameter for the control ACM.1.

#### JSON
<a name="aws-resource-securityhub-securitycontrol--examples--Configuring_control_parameters--json"></a>

```
{
  "Description": "Example template to configure control parameters",
  "Resources": {
    "ExampleSecurityControl": {
      "Type": "AWS::SecurityHub::SecurityControl",
      "Properties": {
        "SecurityControlId": "ACM.1",
        "Parameters": {
          "daysToExpiration": {
            "ValueType": "CUSTOM",
            "Value": {
              "Integer": 15
            }
          }
        },
        "LastUpdateReason": "Internal compliance requirement"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-securityhub-securitycontrol--examples--Configuring_control_parameters--yaml"></a>

```
Description: Example template to configure control parameters
Resources:
  ExampleSecurityControl:
    Type: 'AWS::SecurityHub::SecurityControl'
    Properties:
      SecurityControlId: 'ACM.1'
      Parameters:
        daysToExpiration:
          ValueType: 'CUSTOM'
          Value:
            Integer: 15
      LastUpdateReason: 'Internal compliance requirement'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
