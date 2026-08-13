---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-limit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Limit
<a name="aws-resource-deadline-limit"></a>

Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues.

You must add the `amountRequirementName` to a step in a job template to declare the limit requirement.

## Syntax
<a name="aws-resource-deadline-limit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-limit-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Limit",
  "Properties" : {
      "[AmountRequirementName](#cfn-deadline-limit-amountrequirementname)" : {{String}},
      "[Description](#cfn-deadline-limit-description)" : {{String}},
      "[DisplayName](#cfn-deadline-limit-displayname)" : {{String}},
      "[FarmId](#cfn-deadline-limit-farmid)" : {{String}},
      "[MaxCount](#cfn-deadline-limit-maxcount)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-deadline-limit-syntax.yaml"></a>

```
Type: AWS::Deadline::Limit
Properties:
  [AmountRequirementName](#cfn-deadline-limit-amountrequirementname): {{String}}
  [Description](#cfn-deadline-limit-description): {{String}}
  [DisplayName](#cfn-deadline-limit-displayname): {{String}}
  [FarmId](#cfn-deadline-limit-farmid): {{String}}
  [MaxCount](#cfn-deadline-limit-maxcount): {{Integer}}
```

## Properties
<a name="aws-resource-deadline-limit-properties"></a>

`AmountRequirementName`  <a name="cfn-deadline-limit-amountrequirementname"></a>
The value that you specify as the `name` in the `amounts` field of the `hostRequirements` in a step of a job template to declare the limit requirement.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-deadline-limit-description"></a>
A description of the limit. A clear description helps you identify the purpose of the limit.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-deadline-limit-displayname"></a>
The name of the limit used in lists to identify the limit.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FarmId`  <a name="cfn-deadline-limit-farmid"></a>
The unique identifier of the farm that contains the limit.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxCount`  <a name="cfn-deadline-limit-maxcount"></a>
The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.
The `maxValue` must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.
*Required*: Yes
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-limit-return-values"></a>

### Ref
<a name="aws-resource-deadline-limit-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the limit.

### Fn::GetAtt
<a name="aws-resource-deadline-limit-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-limit-return-values-fn--getatt-fn--getatt"></a>

`CurrentCount`  <a name="CurrentCount-fn::getatt"></a>
The number of resources from the limit that are being used by jobs. The result is delayed and may not be the count at the time that you called the operation.

`LimitId`  <a name="LimitId-fn::getatt"></a>
The unique identifier of the limit.
