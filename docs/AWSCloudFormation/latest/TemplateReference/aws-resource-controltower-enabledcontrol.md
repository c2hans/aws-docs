---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-controltower-enabledcontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::EnabledControl
<a name="aws-resource-controltower-enabledcontrol"></a>

The resource represents an enabled control. It specifies an asynchronous operation that creates AWS resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify.

## Syntax
<a name="aws-resource-controltower-enabledcontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-controltower-enabledcontrol-syntax.json"></a>

```
{
  "Type" : "AWS::ControlTower::EnabledControl",
  "Properties" : {
      "[ControlIdentifier](#cfn-controltower-enabledcontrol-controlidentifier)" : {{String}},
      "[Parameters](#cfn-controltower-enabledcontrol-parameters)" : {{[ EnabledControlParameter, ... ]}},
      "[Tags](#cfn-controltower-enabledcontrol-tags)" : {{[ Tag, ... ]}},
      "[TargetIdentifier](#cfn-controltower-enabledcontrol-targetidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-controltower-enabledcontrol-syntax.yaml"></a>

```
Type: AWS::ControlTower::EnabledControl
Properties:
  [ControlIdentifier](#cfn-controltower-enabledcontrol-controlidentifier): {{String}}
  [Parameters](#cfn-controltower-enabledcontrol-parameters): {{
    - EnabledControlParameter}}
  [Tags](#cfn-controltower-enabledcontrol-tags): {{
    - Tag}}
  [TargetIdentifier](#cfn-controltower-enabledcontrol-targetidentifier): {{String}}
```

## Properties
<a name="aws-resource-controltower-enabledcontrol-properties"></a>

`ControlIdentifier`  <a name="cfn-controltower-enabledcontrol-controlidentifier"></a>
The ARN of the control. Only **Strongly recommended** and **Elective** controls are permitted, with the exception of the **Region deny** control. For information on how to find the `controlIdentifier`, see [the overview page](https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-controltower-enabledcontrol-parameters"></a>
Array of `EnabledControlParameter` objects.
*Required*: No
*Type*: Array of [EnabledControlParameter](aws-properties-controltower-enabledcontrol-enabledcontrolparameter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-controltower-enabledcontrol-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-controltower-enabledcontrol-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetIdentifier`  <a name="cfn-controltower-enabledcontrol-targetidentifier"></a>
The ARN of the organizational unit. For information on how to find the `targetIdentifier`, see [the overview page](https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-controltower-enabledcontrol-return-values"></a>

### Ref
<a name="aws-resource-controltower-enabledcontrol-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the physical ID of the resource. The format is of the form `target | control`. For example:

 `arn:aws:organizations::123456789012:ou/o-myorg/ou-my-ouid | arn:aws:controltower:us-west-2::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-controltower-enabledcontrol--examples"></a>

### Example
<a name="aws-resource-controltower-enabledcontrol--examples--Example"></a>

The following example creates an enabled control named *MyExampleControl* for an OU named *ou-zzxx-zzx0zzz2*.

#### JSON
<a name="aws-resource-controltower-enabledcontrol--examples--Example--json"></a>

```
{
    "Resources": {
        "MyExampleControl": {
            "Properties": {
                "ControlIdentifier": "arn:aws:controltower:us-east-2::control/EXAMPLE_NAME",
                 "TargetIdentifier": "arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2"
            },
            "Type": "AWS::ControlTower::EnabledControl"
        }
    }
}
```

#### YAML
<a name="aws-resource-controltower-enabledcontrol--examples--Example--yaml"></a>

```
Resources:
  MyExampleControl:
    Properties:
      ControlIdentifier: 'arn:aws:controltower:us-east-2::control/EXAMPLE_NAME'
      TargetIdentifier: 'arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2'
    Type: 'AWS::ControlTower::EnabledControl'
```
