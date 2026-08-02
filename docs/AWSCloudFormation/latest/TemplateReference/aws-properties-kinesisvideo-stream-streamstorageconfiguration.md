---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisvideo-stream-streamstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisVideo::Stream StreamStorageConfiguration
<a name="aws-properties-kinesisvideo-stream-streamstorageconfiguration"></a>

The configuration for stream storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.

## Syntax
<a name="aws-properties-kinesisvideo-stream-streamstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisvideo-stream-streamstorageconfiguration-syntax.json"></a>

```
{
  "[DefaultStorageTier](#cfn-kinesisvideo-stream-streamstorageconfiguration-defaultstoragetier)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisvideo-stream-streamstorageconfiguration-syntax.yaml"></a>

```
  [DefaultStorageTier](#cfn-kinesisvideo-stream-streamstorageconfiguration-defaultstoragetier): {{String}}
```

## Properties
<a name="aws-properties-kinesisvideo-stream-streamstorageconfiguration-properties"></a>

`DefaultStorageTier`  <a name="cfn-kinesisvideo-stream-streamstorageconfiguration-defaultstoragetier"></a>
The default storage tier for the stream data. This setting determines the storage class used for stream data, affecting both performance characteristics and storage costs.
Available storage tiers:
+ `HOT` - Optimized for frequent access with the lowest latency and highest performance. Ideal for real-time applications and frequently accessed data.
+ `WARM` - Balanced performance and cost for moderately accessed data. Suitable for data that is accessed regularly but not continuously.
*Required*: No
*Type*: String
*Allowed values*: `HOT | WARM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
