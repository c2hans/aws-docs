---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-hoursofoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation
<a name="aws-resource-connect-hoursofoperation"></a>

Specifies hours of operation.

## Syntax
<a name="aws-resource-connect-hoursofoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-hoursofoperation-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::HoursOfOperation",
  "Properties" : {
      "[ChildHoursOfOperations](#cfn-connect-hoursofoperation-childhoursofoperations)" : {{[ HoursOfOperationsIdentifier, ... ]}},
      "[Config](#cfn-connect-hoursofoperation-config)" : {{[ HoursOfOperationConfig, ... ]}},
      "[Description](#cfn-connect-hoursofoperation-description)" : {{String}},
      "[HoursOfOperationOverrides](#cfn-connect-hoursofoperation-hoursofoperationoverrides)" : {{[ HoursOfOperationOverride, ... ]}},
      "[InstanceArn](#cfn-connect-hoursofoperation-instancearn)" : {{String}},
      "[Name](#cfn-connect-hoursofoperation-name)" : {{String}},
      "[ParentHoursOfOperations](#cfn-connect-hoursofoperation-parenthoursofoperations)" : {{[ HoursOfOperationsIdentifier, ... ]}},
      "[Tags](#cfn-connect-hoursofoperation-tags)" : {{[ Tag, ... ]}},
      "[TimeZone](#cfn-connect-hoursofoperation-timezone)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-hoursofoperation-syntax.yaml"></a>

```
Type: AWS::Connect::HoursOfOperation
Properties:
  [ChildHoursOfOperations](#cfn-connect-hoursofoperation-childhoursofoperations): {{
    - HoursOfOperationsIdentifier}}
  [Config](#cfn-connect-hoursofoperation-config): {{
    - HoursOfOperationConfig}}
  [Description](#cfn-connect-hoursofoperation-description): {{String}}
  [HoursOfOperationOverrides](#cfn-connect-hoursofoperation-hoursofoperationoverrides): {{
    - HoursOfOperationOverride}}
  [InstanceArn](#cfn-connect-hoursofoperation-instancearn): {{String}}
  [Name](#cfn-connect-hoursofoperation-name): {{String}}
  [ParentHoursOfOperations](#cfn-connect-hoursofoperation-parenthoursofoperations): {{
    - HoursOfOperationsIdentifier}}
  [Tags](#cfn-connect-hoursofoperation-tags): {{
    - Tag}}
  [TimeZone](#cfn-connect-hoursofoperation-timezone): {{String}}
```

## Properties
<a name="aws-resource-connect-hoursofoperation-properties"></a>

`ChildHoursOfOperations`  <a name="cfn-connect-hoursofoperation-childhoursofoperations"></a>
Information about child hours of operations.
*Required*: No
*Type*: Array of [HoursOfOperationsIdentifier](aws-properties-connect-hoursofoperation-hoursofoperationsidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Config`  <a name="cfn-connect-hoursofoperation-config"></a>
Configuration information for the hours of operation.
*Required*: Yes
*Type*: Array of [HoursOfOperationConfig](aws-properties-connect-hoursofoperation-hoursofoperationconfig.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-hoursofoperation-description"></a>
The description for the hours of operation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HoursOfOperationOverrides`  <a name="cfn-connect-hoursofoperation-hoursofoperationoverrides"></a>
Property description not available.
*Required*: No
*Type*: Array of [HoursOfOperationOverride](aws-properties-connect-hoursofoperation-hoursofoperationoverride.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-hoursofoperation-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-hoursofoperation-name"></a>
The name for the hours of operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParentHoursOfOperations`  <a name="cfn-connect-hoursofoperation-parenthoursofoperations"></a>
Information about parent hours of operations.
*Required*: No
*Type*: Array of [HoursOfOperationsIdentifier](aws-properties-connect-hoursofoperation-hoursofoperationsidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-hoursofoperation-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-hoursofoperation-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-connect-hoursofoperation-timezone"></a>
The time zone for the hours of operation.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-hoursofoperation-return-values"></a>

### Ref
<a name="aws-resource-connect-hoursofoperation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the hours of operation. For example:

 `{ "Ref": "myHoursOfOperation" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-hoursofoperation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-hoursofoperation-return-values-fn--getatt-fn--getatt"></a>

`HoursOfOperationArn`  <a name="HoursOfOperationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the hours of operation.

## Examples
<a name="aws-resource-connect-hoursofoperation--examples"></a>

### Specify an hours of operation resource
<a name="aws-resource-connect-hoursofoperation--examples--Specify_an_hours_of_operation_resource"></a>

The following example specifies an hours of operation resource for an Connect Customer instance. In the following example, the hours of operation claimed operates in Sunday 10:01 to 11:59 AM Pacific Standard Time.

#### YAML
<a name="aws-resource-connect-hoursofoperation--examples--Specify_an_hours_of_operation_resource--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies an hours of operation for an Connect Customer instance
Resources:
  HoursOfOperation:
    Type: 'AWS::Connect::HoursOfOperation'
    Properties:
      Name: 'ExampleHoursOfOperation'
      Description: 'hours of operation created using cfn'
      InstanceArn: 'arn:aws:connect:region-name:aws-account-id:instance/instance-arn'
      TimeZone: 'Pacific/Midway'
      Config:
        - Day: 'SUNDAY'
          EndTime:
            Hours: 11
            Minutes: 59
          StartTime:
            Hours: 10
            Minutes: 1
      Tags:
        - Key: 'tagKey'
          Value: 'tagValue'
```
