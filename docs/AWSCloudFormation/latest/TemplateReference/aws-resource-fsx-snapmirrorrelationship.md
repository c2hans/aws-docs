---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-snapmirrorrelationship.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapmirrorRelationship

Describes an Amazon FSx for NetApp ONTAP SnapMirror relationship.

## Syntax
<a name="aws-resource-fsx-snapmirrorrelationship-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-snapmirrorrelationship-syntax.json"></a>

```json
{
  "Type" : "AWS::FSx::SnapmirrorRelationship",
  "Properties" : {
      "[Destination](#cfn-fsx-snapmirrorrelationship-destination)" : {{Destination}},
      "[PolicyId](#cfn-fsx-snapmirrorrelationship-policyid)" : {{String}},
      "[Source](#cfn-fsx-snapmirrorrelationship-source)" : {{Source}},
      "[Tags](#cfn-fsx-snapmirrorrelationship-tags)" : {{[ Tag, ... ]}},
      "[ThrottleInKbps](#cfn-fsx-snapmirrorrelationship-throttleinkbps)" : {{Integer}},
      "[TransferSchedule](#cfn-fsx-snapmirrorrelationship-transferschedule)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-fsx-snapmirrorrelationship-syntax.yaml"></a>

```yaml
Type: AWS::FSx::SnapmirrorRelationship
Properties:
  [Destination](#cfn-fsx-snapmirrorrelationship-destination): {{
    Destination}}
  [PolicyId](#cfn-fsx-snapmirrorrelationship-policyid): {{String}}
  [Source](#cfn-fsx-snapmirrorrelationship-source): {{
    Source}}
  [Tags](#cfn-fsx-snapmirrorrelationship-tags): {{
    - Tag}}
  [ThrottleInKbps](#cfn-fsx-snapmirrorrelationship-throttleinkbps): {{Integer}}
  [TransferSchedule](#cfn-fsx-snapmirrorrelationship-transferschedule): {{String}}
```

## Properties
<a name="aws-resource-fsx-snapmirrorrelationship-properties"></a>

`Destination`  <a name="cfn-fsx-snapmirrorrelationship-destination"></a>
The destination endpoint of the SnapMirror relationship.
*Required*: Yes
*Type*: [Destination](aws-properties-fsx-snapmirrorrelationship-destination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyId`  <a name="cfn-fsx-snapmirrorrelationship-policyid"></a>
The ID of the SnapMirror policy.
*Required*: No
*Type*: String
*Pattern*: `^(snapmirrorpol-[0-9a-f]{17})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-fsx-snapmirrorrelationship-source"></a>
The source endpoint of the SnapMirror relationship.
*Required*: Yes
*Type*: [Source](aws-properties-fsx-snapmirrorrelationship-source.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-fsx-snapmirrorrelationship-tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-snapmirrorrelationship-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottleInKbps`  <a name="cfn-fsx-snapmirrorrelationship-throttleinkbps"></a>
The maximum bandwidth, in kilobytes per second (KBps), that SnapMirror uses to transfer data for the relationship. A value of `0` means that the bandwidth is unlimited. This value overrides the throttle of the SnapMirror policy.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransferSchedule`  <a name="cfn-fsx-snapmirrorrelationship-transferschedule"></a>
The name of the ONTAP schedule that determines when SnapMirror transfers data for the relationship. This schedule overrides the transfer schedule of the SnapMirror policy.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_:.-]{0,256}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-snapmirrorrelationship-return-values"></a>

### Ref
<a name="aws-resource-fsx-snapmirrorrelationship-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-snapmirrorrelationship-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-snapmirrorrelationship-return-values-fn--getatt-fn--getatt"></a>

`Destination.Path`  <a name="Destination.Path-fn::getatt"></a>
Property description not available.

`FileSystemId`  <a name="FileSystemId-fn::getatt"></a>
The globally unique ID of the file system that the destination volume is on, assigned by Amazon FSx.

`Healthy`  <a name="Healthy-fn::getatt"></a>
Indicates whether ONTAP reports the SnapMirror relationship as healthy.

`LagTimeInMinutes`  <a name="LagTimeInMinutes-fn::getatt"></a>
The time, in minutes, since ONTAP created the latest snapshot that SnapMirror transferred to the destination volume.

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the SnapMirror relationship can be one of the following:
+ `CREATED` – The SnapMirror relationship is fully available for use.
+ `CREATING` – Amazon FSx is creating the SnapMirror relationship.
+ `DELETING` – Amazon FSx is deleting the SnapMirror relationship.
+ `FAILED` – Amazon FSx was unable to create the SnapMirror relationship.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`SnapmirrorRelationshipId`  <a name="SnapmirrorRelationshipId-fn::getatt"></a>
The system-generated, unique ID of the SnapMirror relationship.

`State`  <a name="State-fn::getatt"></a>
The state of the SnapMirror relationship in ONTAP can be one of the following:
+ `UNINITIALIZED` – SnapMirror hasn't transferred the baseline copy of the source volume to the destination volume.
+ `TRANSFERRING` – SnapMirror is transferring data to the destination volume.
+ `SNAPMIRRORED` – SnapMirror transferred the baseline copy, and the destination volume receives updates from the source volume.
+ `PAUSED` – SnapMirror transfers for the relationship are paused.
+ `BROKEN_OFF` – The relationship is broken off, and the destination volume is writable. SnapMirror doesn't transfer data to the destination volume.

`UUID`  <a name="UUID-fn::getatt"></a>
The SnapMirror relationship's universally unique identifier (UUID).
