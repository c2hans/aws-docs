---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-threatentityset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::ThreatEntitySet
<a name="aws-resource-guardduty-threatentityset"></a>

The `AWS::GuardDuty::ThreatEntitySet` resource helps you create a list of known malicious threat entities in your AWS environment. Once you activate this list, GuardDuty will use the entries in this list as an additional source of threat detection and generate findings when there is an activity associated with these known malicious threat entities. GuardDuty continues to monitor independently of this custom threat entity set.

Only the users of the GuardDuty administrator account can manage this list. These settings automatically apply to the member accounts.

## Syntax
<a name="aws-resource-guardduty-threatentityset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-threatentityset-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::ThreatEntitySet",
  "Properties" : {
      "[Activate](#cfn-guardduty-threatentityset-activate)" : {{Boolean}},
      "[DetectorId](#cfn-guardduty-threatentityset-detectorid)" : {{String}},
      "[ExpectedBucketOwner](#cfn-guardduty-threatentityset-expectedbucketowner)" : {{String}},
      "[Format](#cfn-guardduty-threatentityset-format)" : {{String}},
      "[Location](#cfn-guardduty-threatentityset-location)" : {{String}},
      "[Name](#cfn-guardduty-threatentityset-name)" : {{String}},
      "[Tags](#cfn-guardduty-threatentityset-tags)" : {{[ TagItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-threatentityset-syntax.yaml"></a>

```
Type: AWS::GuardDuty::ThreatEntitySet
Properties:
  [Activate](#cfn-guardduty-threatentityset-activate): {{Boolean}}
  [DetectorId](#cfn-guardduty-threatentityset-detectorid): {{String}}
  [ExpectedBucketOwner](#cfn-guardduty-threatentityset-expectedbucketowner): {{String}}
  [Format](#cfn-guardduty-threatentityset-format): {{String}}
  [Location](#cfn-guardduty-threatentityset-location): {{String}}
  [Name](#cfn-guardduty-threatentityset-name): {{String}}
  [Tags](#cfn-guardduty-threatentityset-tags): {{
    - TagItem}}
```

## Properties
<a name="aws-resource-guardduty-threatentityset-properties"></a>

`Activate`  <a name="cfn-guardduty-threatentityset-activate"></a>
A boolean value that determines if GuardDuty can start using this list for custom threat detection. For GuardDuty to consider the entries in this list and generate findings based on associated activity, this list must be active.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorId`  <a name="cfn-guardduty-threatentityset-detectorid"></a>
The unique regional detector ID of the GuardDuty account for which you want to create a threat entity set.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-guardduty-threatentityset-expectedbucketowner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the *Location* field.
Whether or not you provide the account ID for this optional field, GuardDuty validates that the account ID associated with the `DetectorId` owns the S3 bucket in the `Location` field. If GuardDuty finds that this S3 bucket doesn't belong to the specified account ID, you will get an error at the time of activating this list.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-guardduty-threatentityset-format"></a>
The format of the file that contains the threat entity set. For information about supported formats, see [List formats](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html#prepare_list) in the *Amazon GuardDuty User Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-guardduty-threatentityset-location"></a>
The URI of the file that contains the threat entity set.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-guardduty-threatentityset-name"></a>
The user-friendly name to identify the threat entity set. Valid characters are alphanumeric, whitespace, dash (-), and underscores (\_).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-guardduty-threatentityset-tags"></a>
The tags to be added to a new threat entity set resource. Each tag consists of a key and an optional value, both of which you define.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [TagItem](aws-properties-guardduty-threatentityset-tagitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-guardduty-threatentityset-return-values"></a>

### Ref
<a name="aws-resource-guardduty-threatentityset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique ID associated with the newly created threat entity set.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-guardduty-threatentityset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-guardduty-threatentityset-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the threat entity set was created.

`ErrorDetails`  <a name="ErrorDetails-fn::getatt"></a>
The details associated with the **Error** status of your threat entity list.

`Id`  <a name="Id-fn::getatt"></a>
Returns the unique ID associated with the newly created threat entity set.

`Status`  <a name="Status-fn::getatt"></a>
The status of your `ThreatEntitySet`. For information about valid status values, see [Understanding list statuses](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html#guardduty-entity-list-statuses) in the *Amazon GuardDuty User Guide*.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the threat entity set was updated.
