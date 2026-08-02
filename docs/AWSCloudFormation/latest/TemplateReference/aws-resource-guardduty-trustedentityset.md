---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-trustedentityset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::TrustedEntitySet
<a name="aws-resource-guardduty-trustedentityset"></a>

Creates a new trusted entity set. In the trusted entity set, you can provide IP addresses and domains that you believe are secure for communication in your AWS environment. GuardDuty will not generate findings for the entries that are specified in a trusted entity set. At any given time, you can have only one trusted entity set.

Only users of the administrator account can manage the entity sets, which automatically apply to member accounts.

## Syntax
<a name="aws-resource-guardduty-trustedentityset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-trustedentityset-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::TrustedEntitySet",
  "Properties" : {
      "[Activate](#cfn-guardduty-trustedentityset-activate)" : {{Boolean}},
      "[DetectorId](#cfn-guardduty-trustedentityset-detectorid)" : {{String}},
      "[ExpectedBucketOwner](#cfn-guardduty-trustedentityset-expectedbucketowner)" : {{String}},
      "[Format](#cfn-guardduty-trustedentityset-format)" : {{String}},
      "[Location](#cfn-guardduty-trustedentityset-location)" : {{String}},
      "[Name](#cfn-guardduty-trustedentityset-name)" : {{String}},
      "[Tags](#cfn-guardduty-trustedentityset-tags)" : {{[ TagItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-trustedentityset-syntax.yaml"></a>

```
Type: AWS::GuardDuty::TrustedEntitySet
Properties:
  [Activate](#cfn-guardduty-trustedentityset-activate): {{Boolean}}
  [DetectorId](#cfn-guardduty-trustedentityset-detectorid): {{String}}
  [ExpectedBucketOwner](#cfn-guardduty-trustedentityset-expectedbucketowner): {{String}}
  [Format](#cfn-guardduty-trustedentityset-format): {{String}}
  [Location](#cfn-guardduty-trustedentityset-location): {{String}}
  [Name](#cfn-guardduty-trustedentityset-name): {{String}}
  [Tags](#cfn-guardduty-trustedentityset-tags): {{
    - TagItem}}
```

## Properties
<a name="aws-resource-guardduty-trustedentityset-properties"></a>

`Activate`  <a name="cfn-guardduty-trustedentityset-activate"></a>
A boolean value that determines if GuardDuty can start using this list for custom threat detection. For GuardDuty to prevent generating findings based on an activity associated with these entries, this list must be active.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorId`  <a name="cfn-guardduty-trustedentityset-detectorid"></a>
The unique regional detector ID of the GuardDuty account for which you want to create a trusted entity set.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-guardduty-trustedentityset-expectedbucketowner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the *Location* field.
Whether or not you provide the account ID for this optional field, GuardDuty validates that the account ID associated with the `DetectorId` value owns the S3 bucket in the `Location` field. If GuardDuty finds that this S3 bucket doesn't belong to the specified account ID, you will get an error at the time of activating this list.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-guardduty-trustedentityset-format"></a>
The format of the file that contains the trusted entity set. For information about supported formats, see [List formats](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html#prepare_list) in the *Amazon GuardDuty User Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-guardduty-trustedentityset-location"></a>
The URI of the file that contains the trusted entity set.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-guardduty-trustedentityset-name"></a>
A user-friendly name to identify the trusted entity set. Valid characters include lowercase letters, uppercase letters, numbers, dash(-), and underscore (\_).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-guardduty-trustedentityset-tags"></a>
The tags to be added to a new trusted entity set resource. Each tag consists of a key and an optional value, both of which you define.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [TagItem](aws-properties-guardduty-trustedentityset-tagitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-guardduty-trustedentityset-return-values"></a>

### Ref
<a name="aws-resource-guardduty-trustedentityset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique ID of the `TrustedEntitySet`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-guardduty-trustedentityset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-guardduty-trustedentityset-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the trusted entity set was created.

`ErrorDetails`  <a name="ErrorDetails-fn::getatt"></a>
Specifies the error details when the status of the trusted entity set shows as **Error**.

`Status`  <a name="Status-fn::getatt"></a>
The status of your `TrustedEntitySet`. For information about valid status values, see [Understanding list statuses](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html#guardduty-entity-list-statuses) in the *Amazon GuardDuty User Guide*.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the trusted entity set was updated.
