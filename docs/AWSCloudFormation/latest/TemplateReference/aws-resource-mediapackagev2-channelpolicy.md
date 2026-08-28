---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediapackagev2-channelpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::ChannelPolicy
<a name="aws-resource-mediapackagev2-channelpolicy"></a>

Specifies the configuration parameters of a MediaPackage V2 channel policy.

## Syntax
<a name="aws-resource-mediapackagev2-channelpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediapackagev2-channelpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::MediaPackageV2::ChannelPolicy",
  "Properties" : {
      "[ChannelGroupName](#cfn-mediapackagev2-channelpolicy-channelgroupname)" : {{String}},
      "[ChannelName](#cfn-mediapackagev2-channelpolicy-channelname)" : {{String}},
      "[Policy](#cfn-mediapackagev2-channelpolicy-policy)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-mediapackagev2-channelpolicy-syntax.yaml"></a>

```
Type: AWS::MediaPackageV2::ChannelPolicy
Properties:
  [ChannelGroupName](#cfn-mediapackagev2-channelpolicy-channelgroupname): {{String}}
  [ChannelName](#cfn-mediapackagev2-channelpolicy-channelname): {{String}}
  [Policy](#cfn-mediapackagev2-channelpolicy-policy): {{Json}}
```

## Properties
<a name="aws-resource-mediapackagev2-channelpolicy-properties"></a>

`ChannelGroupName`  <a name="cfn-mediapackagev2-channelpolicy-channelgroupname"></a>
The name of the channel group associated with the channel policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ChannelName`  <a name="cfn-mediapackagev2-channelpolicy-channelname"></a>
The name of the channel associated with the channel policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-mediapackagev2-channelpolicy-policy"></a>
The policy associated with the channel.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediapackagev2-channelpolicy-return-values"></a>

### Ref
<a name="aws-resource-mediapackagev2-channelpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`ChannelGroupName/ChannelName`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
