---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-sequencestore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::SequenceStore
<a name="aws-resource-omics-sequencestore"></a>

Creates a sequence store.

## Syntax
<a name="aws-resource-omics-sequencestore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-sequencestore-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::SequenceStore",
  "Properties" : {
      "[AccessLogLocation](#cfn-omics-sequencestore-accessloglocation)" : {{String}},
      "[Description](#cfn-omics-sequencestore-description)" : {{String}},
      "[ETagAlgorithmFamily](#cfn-omics-sequencestore-etagalgorithmfamily)" : {{String}},
      "[FallbackLocation](#cfn-omics-sequencestore-fallbacklocation)" : {{String}},
      "[Name](#cfn-omics-sequencestore-name)" : {{String}},
      "[PropagatedSetLevelTags](#cfn-omics-sequencestore-propagatedsetleveltags)" : {{[ String, ... ]}},
      "[S3AccessPolicy](#cfn-omics-sequencestore-s3accesspolicy)" : {{Json}},
      "[SseConfig](#cfn-omics-sequencestore-sseconfig)" : {{SseConfig}},
      "[Tags](#cfn-omics-sequencestore-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-omics-sequencestore-syntax.yaml"></a>

```
Type: AWS::Omics::SequenceStore
Properties:
  [AccessLogLocation](#cfn-omics-sequencestore-accessloglocation): {{String}}
  [Description](#cfn-omics-sequencestore-description): {{String}}
  [ETagAlgorithmFamily](#cfn-omics-sequencestore-etagalgorithmfamily): {{String}}
  [FallbackLocation](#cfn-omics-sequencestore-fallbacklocation): {{String}}
  [Name](#cfn-omics-sequencestore-name): {{String}}
  [PropagatedSetLevelTags](#cfn-omics-sequencestore-propagatedsetleveltags): {{
    - String}}
  [S3AccessPolicy](#cfn-omics-sequencestore-s3accesspolicy): {{Json}}
  [SseConfig](#cfn-omics-sequencestore-sseconfig): {{
    SseConfig}}
  [Tags](#cfn-omics-sequencestore-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-omics-sequencestore-properties"></a>

`AccessLogLocation`  <a name="cfn-omics-sequencestore-accessloglocation"></a>
Location of the access logs.
*Required*: No
*Type*: String
*Pattern*: `^$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,800})/)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-omics-sequencestore-description"></a>
A description for the store.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ETagAlgorithmFamily`  <a name="cfn-omics-sequencestore-etagalgorithmfamily"></a>
The algorithm family of the ETag.
*Required*: No
*Type*: String
*Allowed values*: `MD5up | SHA256up | SHA512up`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FallbackLocation`  <a name="cfn-omics-sequencestore-fallbacklocation"></a>
 An S3 location that is used to store files that have failed a direct upload.
*Required*: No
*Type*: String
*Pattern*: `^$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?$`
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-omics-sequencestore-name"></a>
A name for the store.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagatedSetLevelTags`  <a name="cfn-omics-sequencestore-propagatedsetleveltags"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `128 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3AccessPolicy`  <a name="cfn-omics-sequencestore-s3accesspolicy"></a>
Property description not available.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SseConfig`  <a name="cfn-omics-sequencestore-sseconfig"></a>
Server-side encryption (SSE) settings for the store.
*Required*: No
*Type*: [SseConfig](aws-properties-omics-sequencestore-sseconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-omics-sequencestore-tags"></a>
Tags for the store.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-omics-sequencestore-return-values"></a>

### Ref
<a name="aws-resource-omics-sequencestore-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the details of this resource. For example:

`{ "Ref": "SequenceStore.CreationTime" }``Ref` returns the timestamp for when the sequence store was created.

### Fn::GetAtt
<a name="aws-resource-omics-sequencestore-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-omics-sequencestore-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The store's ARN.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the store was created.

`S3AccessPointArn`  <a name="S3AccessPointArn-fn::getatt"></a>
This is ARN of the access point associated with the S3 bucket storing read sets.

`S3Uri`  <a name="S3Uri-fn::getatt"></a>
The S3 URI of the sequence store.

`SequenceStoreId`  <a name="SequenceStoreId-fn::getatt"></a>
The store's ID.

`Status`  <a name="Status-fn::getatt"></a>
Status of the sequence store.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
The status message of the sequence store.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
The last-updated time of the Sequence Store.
