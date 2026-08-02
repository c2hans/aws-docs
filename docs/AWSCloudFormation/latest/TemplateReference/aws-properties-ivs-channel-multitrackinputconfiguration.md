---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-channel-multitrackinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Channel MultitrackInputConfiguration
<a name="aws-properties-ivs-channel-multitrackinputconfiguration"></a>

A complex type that specifies multitrack input configuration.

## Syntax
<a name="aws-properties-ivs-channel-multitrackinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-channel-multitrackinputconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-ivs-channel-multitrackinputconfiguration-enabled)" : {{Boolean}},
  "[MaximumResolution](#cfn-ivs-channel-multitrackinputconfiguration-maximumresolution)" : {{String}},
  "[Policy](#cfn-ivs-channel-multitrackinputconfiguration-policy)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-channel-multitrackinputconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-ivs-channel-multitrackinputconfiguration-enabled): {{Boolean}}
  [MaximumResolution](#cfn-ivs-channel-multitrackinputconfiguration-maximumresolution): {{String}}
  [Policy](#cfn-ivs-channel-multitrackinputconfiguration-policy): {{String}}
```

## Properties
<a name="aws-properties-ivs-channel-multitrackinputconfiguration-properties"></a>

`Enabled`  <a name="cfn-ivs-channel-multitrackinputconfiguration-enabled"></a>
Indicates whether multitrack input is enabled. Can be set to `true` only if channel type is `STANDARD`. Setting `enabled` to `true` with any other channel type will cause an exception. If `true`, then `policy`, `maximumResolution`, and `containerFormat` are required, and `containerFormat` must be set to `FRAGMENTED_MP4`. Default: `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumResolution`  <a name="cfn-ivs-channel-multitrackinputconfiguration-maximumresolution"></a>
Maximum resolution for multitrack input. Required if `enabled` is `true`.
*Required*: No
*Type*: String
*Allowed values*: `SD | HD | FULL_HD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policy`  <a name="cfn-ivs-channel-multitrackinputconfiguration-policy"></a>
Indicates whether multitrack input is allowed or required. Required if `enabled` is `true`.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | REQUIRE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
