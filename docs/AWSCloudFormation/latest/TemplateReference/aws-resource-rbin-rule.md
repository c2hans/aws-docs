---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rbin-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rbin::Rule
<a name="aws-resource-rbin-rule"></a>

Creates a Recycle Bin retention rule. You can create two types of retention rules:
+ **Tag-level retention rules** - These retention rules use resource tags to identify the resources to protect. For each retention rule, you specify one or more tag key and value pairs. Resources (of the specified type) that have at least one of these tag key and value pairs are automatically retained in the Recycle Bin upon deletion. Use this type of retention rule to protect specific resources in your account based on their tags.
+ **Region-level retention rules** - These retention rules, by default, apply to all of the resources (of the specified type) in the Region, even if the resources are not tagged. However, you can specify exclusion tags to exclude resources that have specific tags. Use this type of retention rule to protect all resources of a specific type in a Region.

For more information, see [ Create Recycle Bin retention rules](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin.html) in the *Amazon EBS User Guide*.

## Syntax
<a name="aws-resource-rbin-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rbin-rule-syntax.json"></a>

```
{
  "Type" : "AWS::Rbin::Rule",
  "Properties" : {
      "[Description](#cfn-rbin-rule-description)" : {{String}},
      "[ExcludeResourceTags](#cfn-rbin-rule-excluderesourcetags)" : {{[ ResourceTag, ... ]}},
      "[LockConfiguration](#cfn-rbin-rule-lockconfiguration)" : {{UnlockDelay}},
      "[ResourceTags](#cfn-rbin-rule-resourcetags)" : {{[ ResourceTag, ... ]}},
      "[ResourceType](#cfn-rbin-rule-resourcetype)" : {{String}},
      "[RetentionPeriod](#cfn-rbin-rule-retentionperiod)" : {{RetentionPeriod}},
      "[Status](#cfn-rbin-rule-status)" : {{String}},
      "[Tags](#cfn-rbin-rule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rbin-rule-syntax.yaml"></a>

```
Type: AWS::Rbin::Rule
Properties:
  [Description](#cfn-rbin-rule-description): {{String}}
  [ExcludeResourceTags](#cfn-rbin-rule-excluderesourcetags): {{
    - ResourceTag}}
  [LockConfiguration](#cfn-rbin-rule-lockconfiguration): {{
    UnlockDelay}}
  [ResourceTags](#cfn-rbin-rule-resourcetags): {{
    - ResourceTag}}
  [ResourceType](#cfn-rbin-rule-resourcetype): {{String}}
  [RetentionPeriod](#cfn-rbin-rule-retentionperiod): {{
    RetentionPeriod}}
  [Status](#cfn-rbin-rule-status): {{String}}
  [Tags](#cfn-rbin-rule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rbin-rule-properties"></a>

`Description`  <a name="cfn-rbin-rule-description"></a>
The retention rule description.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeResourceTags`  <a name="cfn-rbin-rule-excluderesourcetags"></a>
[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.
You can't specify exclusion tags for tag-level retention rules.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-rbin-rule-resourcetag.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LockConfiguration`  <a name="cfn-rbin-rule-lockconfiguration"></a>
Information about the retention rule lock configuration.
*Required*: No
*Type*: [UnlockDelay](aws-properties-rbin-rule-unlockdelay.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-rbin-rule-resourcetags"></a>
[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.
You can add the same tag key and value pair to a maximum or five retention rules.
To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-rbin-rule-resourcetag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-rbin-rule-resourcetype"></a>
The resource type to be retained by the retention rule. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.
+ To retain EBS volumes, specify `EBS_VOLUME`.
+ To retain EBS snapshots, specify `EBS_SNAPSHOT`
+ To retain EBS-backed AMIs, specify `EC2_IMAGE`.
*Required*: Yes
*Type*: String
*Allowed values*: `EBS_SNAPSHOT | EC2_IMAGE | EBS_VOLUME`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionPeriod`  <a name="cfn-rbin-rule-retentionperiod"></a>
Information about the retention period for which the retention rule is to retain resources.
*Required*: Yes
*Type*: [RetentionPeriod](aws-properties-rbin-rule-retentionperiod.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-rbin-rule-status"></a>
The state of the retention rule. Only retention rules that are in the `available` state retain resources.
*Required*: No
*Type*: String
*Pattern*: `pending|available`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rbin-rule-tags"></a>
Information about the tags to assign to the retention rule.
*Required*: No
*Type*: Array of [Tag](aws-properties-rbin-rule-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rbin-rule-return-values"></a>

### Ref
<a name="aws-resource-rbin-rule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the retention rule.

### Fn::GetAtt
<a name="aws-resource-rbin-rule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rbin-rule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the retention rule.

`Identifier`  <a name="Identifier-fn::getatt"></a>
The unique ID of the retention rule.

`LockState`  <a name="LockState-fn::getatt"></a>
[Region-level retention rules only] The lock state for the retention rule.
+ `locked` - The retention rule is locked and can't be modified or deleted.
+ `pending_unlock` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
+ `unlocked` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
+ `null` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the `locked` and `unlocked` states only; it can never transition back to `null`.

## Examples
<a name="aws-resource-rbin-rule--examples"></a>

### Create a retention rule
<a name="aws-resource-rbin-rule--examples--Create_a_retention_rule"></a>

This example creates a retention rule that retains EBS snapshots for 7 days after deletion.

#### JSON
<a name="aws-resource-rbin-rule--examples--Create_a_retention_rule--json"></a>

```
"MyRule" : {
  "Type": "AWS::Rbin::Rule",
  "Properties": {
    "Description": "my new retention rule",
    "LockConfiguration": {
      "UnlockDelayUnit": "DAYS",
      "UnlockDelayValue": 15
    },
    "ResourceTags": [{
      "Key": "environment",
      "Value": "testing"
    }],
    "ResourceType": "EBS_SNAPSHOT",
    "RetentionPeriod": {
      "RetentionPeriodUnit": "DAYS",
      "RetentionPeriodValue": 7
    },
    "Status": "available",
    "Tags": [{
      "Key": "purpose",
      "Value": "testing"
    }]
  }
}
```

#### YAML
<a name="aws-resource-rbin-rule--examples--Create_a_retention_rule--yaml"></a>

```
MyRule:
  Type: AWS::Rbin::Rule
  Properties:
    Description: my new retention rule
    LockConfiguration:
      UnlockDelayUnit: DAYS
      UnlockDelayValue: 15
    ResourceTags:
    - Key: environment
      Value: testing
    ResourceType: EBS_SNAPSHOT
    RetentionPeriod:
      RetentionPeriodUnit: DAYS
      RetentionPeriodValue: 7
    Status: available
    Tags:
    - Key: purpose
      Value: testing
```
