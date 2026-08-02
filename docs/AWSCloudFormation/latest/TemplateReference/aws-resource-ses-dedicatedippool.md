---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-dedicatedippool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::DedicatedIpPool
<a name="aws-resource-ses-dedicatedippool"></a>

Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your AWS account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, the message is sent from one of the addresses in the associated pool.

**Important**
You can't delete dedicated IP pools that have a `STANDARD` scaling mode with one or more dedicated IP addresses. This constraint doesn't apply to dedicated IP pools that have a `MANAGED` scaling mode.

## Syntax
<a name="aws-resource-ses-dedicatedippool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-dedicatedippool-syntax.json"></a>

```
{
  "Type" : "AWS::SES::DedicatedIpPool",
  "Properties" : {
      "[PoolName](#cfn-ses-dedicatedippool-poolname)" : {{String}},
      "[ScalingMode](#cfn-ses-dedicatedippool-scalingmode)" : {{String}},
      "[Tags](#cfn-ses-dedicatedippool-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-dedicatedippool-syntax.yaml"></a>

```
Type: AWS::SES::DedicatedIpPool
Properties:
  [PoolName](#cfn-ses-dedicatedippool-poolname): {{String}}
  [ScalingMode](#cfn-ses-dedicatedippool-scalingmode): {{String}}
  [Tags](#cfn-ses-dedicatedippool-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-dedicatedippool-properties"></a>

`PoolName`  <a name="cfn-ses-dedicatedippool-poolname"></a>
The name of the dedicated IP pool that the IP address is associated with.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9_-]{0,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScalingMode`  <a name="cfn-ses-dedicatedippool-scalingmode"></a>
The type of scaling mode.
The following options are available:
+ `STANDARD` - The customer controls which IPs are part of the dedicated IP pool.
+ `MANAGED` - The reputation and number of IPs are automatically managed by Amazon SES.
The `STANDARD` option is selected by default if no value is specified.
Updating *ScalingMode* doesn't require a replacement if you're updating its value from `STANDARD` to `MANAGED`. However, updating *ScalingMode* from `MANAGED` to `STANDARD` is not supported.
*Required*: No
*Type*: String
*Pattern*: `^(STANDARD|MANAGED)$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-ses-dedicatedippool-tags"></a>
An object that defines the tags (keys and values) that you want to associate with the pool.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-dedicatedippool-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-dedicatedippool-return-values"></a>

### Ref
<a name="aws-resource-ses-dedicatedippool-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
