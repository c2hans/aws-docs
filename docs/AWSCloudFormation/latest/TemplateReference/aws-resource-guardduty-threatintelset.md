---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-threatintelset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::ThreatIntelSet
<a name="aws-resource-guardduty-threatintelset"></a>

The `AWS::GuardDuty::ThreatIntelSet` resource helps you create a list of known malicious IP addresses in your AWS environment. Once you activate this list, GuardDuty will use list the entries in this list as an additional source for threat detection and generate findings when there is an activity associated with these known malicious IP addresses. GuardDuty continues to monitor independently of this custom threat intelligence set.

Only the users of the GuardDuty administrator account can manage this list. These settings automatically apply to the member accounts.

## Syntax
<a name="aws-resource-guardduty-threatintelset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-threatintelset-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::ThreatIntelSet",
  "Properties" : {
      "[Activate](#cfn-guardduty-threatintelset-activate)" : {{Boolean}},
      "[DetectorId](#cfn-guardduty-threatintelset-detectorid)" : {{String}},
      "[ExpectedBucketOwner](#cfn-guardduty-threatintelset-expectedbucketowner)" : {{String}},
      "[Format](#cfn-guardduty-threatintelset-format)" : {{String}},
      "[Location](#cfn-guardduty-threatintelset-location)" : {{String}},
      "[Name](#cfn-guardduty-threatintelset-name)" : {{String}},
      "[Tags](#cfn-guardduty-threatintelset-tags)" : {{[ TagItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-threatintelset-syntax.yaml"></a>

```
Type: AWS::GuardDuty::ThreatIntelSet
Properties:
  [Activate](#cfn-guardduty-threatintelset-activate): {{Boolean}}
  [DetectorId](#cfn-guardduty-threatintelset-detectorid): {{String}}
  [ExpectedBucketOwner](#cfn-guardduty-threatintelset-expectedbucketowner): {{String}}
  [Format](#cfn-guardduty-threatintelset-format): {{String}}
  [Location](#cfn-guardduty-threatintelset-location): {{String}}
  [Name](#cfn-guardduty-threatintelset-name): {{String}}
  [Tags](#cfn-guardduty-threatintelset-tags): {{
    - TagItem}}
```

## Properties
<a name="aws-resource-guardduty-threatintelset-properties"></a>

`Activate`  <a name="cfn-guardduty-threatintelset-activate"></a>
A boolean value that determines if GuardDuty can start using this list for custom threat detection. For GuardDuty to be able to generate findings based on an activity associated with these entries, this list must be active.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorId`  <a name="cfn-guardduty-threatintelset-detectorid"></a>
The unique ID of the detector of the GuardDuty account for which you want to create a `threatIntelSet`.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpectedBucketOwner`  <a name="cfn-guardduty-threatintelset-expectedbucketowner"></a>
The AWS account ID that owns the Amazon S3 bucket specified in the *Location* field.
When you provide this account ID, GuardDuty will validate that the S3 bucket belongs to this account. If you don't specify an account ID owner, GuardDuty doesn't perform any validation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-guardduty-threatintelset-format"></a>
The format of the file that contains the `ThreatIntelSet`. For information about supported formats, see [List formats](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html#prepare_list) in the *Amazon GuardDuty User Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-guardduty-threatintelset-location"></a>
The URI of the file that contains the ThreatIntelSet.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-guardduty-threatintelset-name"></a>
The user-friendly name to identify the ThreatIntelSet.
The name of your list must be unique within an AWS account and Region. Valid characters are alphanumeric, whitespace, dash (-), and underscores (\_).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-guardduty-threatintelset-tags"></a>
The tags to be added to a new threat entity set resource. Each tag consists of a key and an optional value, both of which you define.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [TagItem](aws-properties-guardduty-threatintelset-tagitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-guardduty-threatintelset-return-values"></a>

### Ref
<a name="aws-resource-guardduty-threatintelset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique ID of the `ThreatIntelSet`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-guardduty-threatintelset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-guardduty-threatintelset-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The unique ID of the `threatIntelSet`.

## Examples
<a name="aws-resource-guardduty-threatintelset--examples"></a>

### Declare a ThreatIntelSet Resource
<a name="aws-resource-guardduty-threatintelset--examples--Declare_a_ThreatIntelSet_Resource"></a>

The following example shows how to declare a GuardDuty`ThreatIntelSet` resource:

#### JSON
<a name="aws-resource-guardduty-threatintelset--examples--Declare_a_ThreatIntelSet_Resource--json"></a>

```
"mythreatintelset": {
    "Type": "AWS::GuardDuty::ThreatIntelSet",
    "Properties": {
        "Activate": true,
        "DetectorId": "12abc34d567e8f4912ab3d45e67891f2",
        "ExpectedBucketOwner" : "111122223333",
        "Format": "TXT",
        "Location": "https://s3-us-west-2.amazonaws.com/amzn-s3-demo-bucket1/mythreatintelset.txt",
        "Name": "MyThreatIntelSet"
    }
}
```

#### YAML
<a name="aws-resource-guardduty-threatintelset--examples--Declare_a_ThreatIntelSet_Resource--yaml"></a>

```
mythreatintelset:
    Type: AWS::GuardDuty::ThreatIntelSet
    Properties:
        Activate: true
        DetectorId: "12abc34d567e8f4912ab3d45e67891f2"
        ExpectedBucketOwner : "111122223333"
        Format: "TXT"
        Location: "https://s3-us-west-2.amazonaws.com/amzn-s3-demo-bucket1/mythreatintelset.txt"
        Name: "MyThreatIntelSet"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
