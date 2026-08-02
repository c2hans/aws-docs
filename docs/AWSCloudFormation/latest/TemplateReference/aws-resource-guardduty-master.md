---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-master.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Master
<a name="aws-resource-guardduty-master"></a>

You can use the `AWS::GuardDuty::Master` resource in a GuardDuty member account to accept an invitation from a GuardDuty administrator account. The invitation to the member account must be sent prior to using the `AWS::GuardDuty::Master` resource to accept the administrator account's invitation. You can invite a member account by using the `InviteMembers` operation of the GuardDuty API, or by creating an `AWS::GuardDuty::Member` resource.

## Syntax
<a name="aws-resource-guardduty-master-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-master-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::Master",
  "Properties" : {
      "[DetectorId](#cfn-guardduty-master-detectorid)" : {{String}},
      "[InvitationId](#cfn-guardduty-master-invitationid)" : {{String}},
      "[MasterId](#cfn-guardduty-master-masterid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-master-syntax.yaml"></a>

```
Type: AWS::GuardDuty::Master
Properties:
  [DetectorId](#cfn-guardduty-master-detectorid): {{String}}
  [InvitationId](#cfn-guardduty-master-invitationid): {{String}}
  [MasterId](#cfn-guardduty-master-masterid): {{String}}
```

## Properties
<a name="aws-resource-guardduty-master-properties"></a>

`DetectorId`  <a name="cfn-guardduty-master-detectorid"></a>
The unique ID of the detector of the GuardDuty member account.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InvitationId`  <a name="cfn-guardduty-master-invitationid"></a>
The ID of the invitation that is sent to the account designated as a member account. You can find the invitation ID by running the [ListInvitations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvitations.html) in the *GuardDuty API Reference*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MasterId`  <a name="cfn-guardduty-master-masterid"></a>
The AWS account ID of the account designated as the GuardDuty administrator account.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-guardduty-master-return-values"></a>

### Ref
<a name="aws-resource-guardduty-master-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique ID of the GuardDuty administrator account, such as `111122223333`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-guardduty-master--examples"></a>

### Declare a Master Resource
<a name="aws-resource-guardduty-master--examples--Declare_a_Master_Resource"></a>

To declare a GuardDuty`Master` resource:

#### JSON
<a name="aws-resource-guardduty-master--examples--Declare_a_Master_Resource--json"></a>

```
"GDMaster": {
    "Type" : "AWS::GuardDuty::Master",
    "Properties" : {
        "DetectorId" : "a12abc34d567e8fa901bc2d34e56789f0",
        "MasterId" : "111122223333",
        "InvitationId" : "84b097800250d17d1872b34c4daadcf5"
    }
}
```

#### YAML
<a name="aws-resource-guardduty-master--examples--Declare_a_Master_Resource--yaml"></a>

```
GDMaster:
    Type: AWS::GuardDuty::Master
    Properties:
        DetectorId: "a12abc34d567e8fa901bc2d34e56789f0"
        MasterId: "111122223333"
        InvitationId: "84b097800250d17d1872b34c4daadcf5"
```
