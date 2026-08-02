---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-ipset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::IPSet
<a name="aws-resource-guardduty-ipset"></a>

The `AWS::GuardDuty::IPSet` resource helps you create a list of trusted IP addresses that you can use for secure communication with AWS infrastructure and applications. Once you activate this list, GuardDuty will not generate findings when there is an activity associated with these safe IP addresses.

Only the users of the GuardDuty administrator account can manage this list. These settings are also applied to the member accounts.

## Syntax
<a name="aws-resource-guardduty-ipset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-ipset-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::IPSet",
  "Properties" : {
      "[Activate](#cfn-guardduty-ipset-activate)" : {{Boolean}},
      "[DetectorId](#cfn-guardduty-ipset-detectorid)" : {{String}},
      "[ExpectedBucketOwner](#cfn-guardduty-ipset-expectedbucketowner)" : {{String}},
      "[Format](#cfn-guardduty-ipset-format)" : {{String}},
      "[Location](#cfn-guardduty-ipset-location)" : {{String}},
      "[Name](#cfn-guardduty-ipset-name)" : {{String}},
      "[Tags](#cfn-guardduty-ipset-tags)" : {{[ TagItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-ipset-syntax.yaml"></a>

```
Type: AWS::GuardDuty::IPSet
Properties:
  [Activate](#cfn-guardduty-ipset-activate): {{Boolean}}
  [DetectorId](#cfn-guardduty-ipset-detectorid): {{String}}
  [ExpectedBucketOwner](#cfn-guardduty-ipset-expectedbucketowner): {{String}}
  [Format](#cfn-guardduty-ipset-format): {{String}}
  [Location](#cfn-guardduty-ipset-location): {{String}}
  [Name](#cfn-guardduty-ipset-name): {{String}}
  [Tags](#cfn-guardduty-ipset-tags): {{
    - TagItem}}
```

## Properties
<a name="aws-resource-guardduty-ipset-properties"></a>

`Activate`  <a name="cfn-guardduty-ipset-activate"></a>
A boolean value that determines if GuardDuty can start using this list for custom threat detection. For GuardDuty to prevent generating findings based on an activity associated with these entries, this list must be active.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorId`  <a name="cfn-guardduty-ipset-detectorid"></a>
The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-guardduty-ipset-expectedbucketowner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the *Location* field.
When you provide this account ID, GuardDuty will validate that the S3 bucket belongs to this account. If you don't specify an account ID owner, GuardDuty doesn't perform any validation.
*Required*: No
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-guardduty-ipset-format"></a>
The format of the file that contains the IPSet. For information about supported formats, see [List formats](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html#prepare_list) in the *Amazon GuardDuty User Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `TXT | STIX | OTX_CSV | ALIEN_VAULT | PROOF_POINT | FIRE_EYE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-guardduty-ipset-location"></a>
The URI of the file that contains the IPSet.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-guardduty-ipset-name"></a>
The user-friendly name to identify the IPSet.
The name of your list must be unique within an AWS account and Region. Valid characters are alphanumeric, whitespace, dash (-), and underscores (\_).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-guardduty-ipset-tags"></a>
The tags to be added to a new threat entity set resource. Each tag consists of a key and an optional value, both of which you define.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [TagItem](aws-properties-guardduty-ipset-tagitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-guardduty-ipset-return-values"></a>

### Ref
<a name="aws-resource-guardduty-ipset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique ID of the `IPSet`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-guardduty-ipset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

## Examples
<a name="aws-resource-guardduty-ipset--examples"></a>

### Declare an IPSet Resource
<a name="aws-resource-guardduty-ipset--examples--Declare_an_IPSet_Resource"></a>

The following example shows how to declare a GuardDuty`IPSet` resource:

#### JSON
<a name="aws-resource-guardduty-ipset--examples--Declare_an_IPSet_Resource--json"></a>

```
"myipset": {
    "Type" : "AWS::GuardDuty::IPSet",
    "Properties" : {
        "Activate" : True,
        "DetectorId" : "12abc34d567e8f4912ab3d45e67891f2",
        "ExpectedBucketOwner" : "111122223333",
        "Format" : "TXT",
        "Location" : "https://s3-us-west-2.amazonaws.com/amzn-s3-demo-bucket/myipset.txt",
        "Name" : "MyIPSet"
    }
}
```

#### YAML
<a name="aws-resource-guardduty-ipset--examples--Declare_an_IPSet_Resource--yaml"></a>

```
myipset:
    Type: AWS::GuardDuty::IPSet
    Properties:
        Activate: True
        DetectorId: "12abc34d567e8f4912ab3d45e67891f2"
        ExpectedBucketOwner : "111122223333"
        Format: "TXT"
        Location: "https://s3-us-west-2.amazonaws.com/amzn-s3-demo-bucket/myipset.txt"
        Name: "MyIPSet"
```
