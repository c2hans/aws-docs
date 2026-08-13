---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-publishingdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::PublishingDestination
<a name="aws-resource-guardduty-publishingdestination"></a>

Creates a publishing destination where you can export your GuardDuty findings. Before you start exporting the findings, the destination resource must exist.

For more information about considerations and permissions, see [Exporting GuardDuty findings to Amazon S3 buckets](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html) in the *Amazon GuardDuty User Guide*.

## Syntax
<a name="aws-resource-guardduty-publishingdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-guardduty-publishingdestination-syntax.json"></a>

```
{
  "Type" : "AWS::GuardDuty::PublishingDestination",
  "Properties" : {
      "[DestinationProperties](#cfn-guardduty-publishingdestination-destinationproperties)" : {{CFNDestinationProperties}},
      "[DestinationType](#cfn-guardduty-publishingdestination-destinationtype)" : {{String}},
      "[DetectorId](#cfn-guardduty-publishingdestination-detectorid)" : {{String}},
      "[Tags](#cfn-guardduty-publishingdestination-tags)" : {{[ TagItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-guardduty-publishingdestination-syntax.yaml"></a>

```
Type: AWS::GuardDuty::PublishingDestination
Properties:
  [DestinationProperties](#cfn-guardduty-publishingdestination-destinationproperties): {{
    CFNDestinationProperties}}
  [DestinationType](#cfn-guardduty-publishingdestination-destinationtype): {{String}}
  [DetectorId](#cfn-guardduty-publishingdestination-detectorid): {{String}}
  [Tags](#cfn-guardduty-publishingdestination-tags): {{
    - TagItem}}
```

## Properties
<a name="aws-resource-guardduty-publishingdestination-properties"></a>

`DestinationProperties`  <a name="cfn-guardduty-publishingdestination-destinationproperties"></a>
Contains the Amazon Resource Name (ARN) of the resource to publish to, such as an S3 bucket, and the ARN of the KMS key to use to encrypt published findings.
*Required*: Yes
*Type*: [CFNDestinationProperties](aws-properties-guardduty-publishingdestination-cfndestinationproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationType`  <a name="cfn-guardduty-publishingdestination-destinationtype"></a>
The type of publishing destination. GuardDuty supports Amazon S3 buckets as a publishing destination.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectorId`  <a name="cfn-guardduty-publishingdestination-detectorid"></a>
The ID of the GuardDuty detector where the publishing destination exists.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-guardduty-publishingdestination-tags"></a>
Describes a tag.
*Required*: No
*Type*: Array of [TagItem](aws-properties-guardduty-publishingdestination-tagitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-guardduty-publishingdestination-return-values"></a>

### Ref
<a name="aws-resource-guardduty-publishingdestination-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource publishing destination ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-guardduty-publishingdestination-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-guardduty-publishingdestination-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the publishing destination.

`PublishingFailureStartTimestamp`  <a name="PublishingFailureStartTimestamp-fn::getatt"></a>
The time, in epoch millisecond format, at which GuardDuty was first unable to publish findings to the destination.

`Status`  <a name="Status-fn::getatt"></a>
The status of the publishing destination.
