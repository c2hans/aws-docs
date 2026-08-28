---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediatailor-channelpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::ChannelPolicy
<a name="aws-resource-mediatailor-channelpolicy"></a>

Specifies an IAM policy for the channel. IAM policies are used to control access to your channel.

## Syntax
<a name="aws-resource-mediatailor-channelpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediatailor-channelpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::MediaTailor::ChannelPolicy",
  "Properties" : {
      "[ChannelName](#cfn-mediatailor-channelpolicy-channelname)" : {{String}},
      "[Policy](#cfn-mediatailor-channelpolicy-policy)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-mediatailor-channelpolicy-syntax.yaml"></a>

```
Type: AWS::MediaTailor::ChannelPolicy
Properties:
  [ChannelName](#cfn-mediatailor-channelpolicy-channelname): {{String}}
  [Policy](#cfn-mediatailor-channelpolicy-policy): {{Json}}
```

## Properties
<a name="aws-resource-mediatailor-channelpolicy-properties"></a>

`ChannelName`  <a name="cfn-mediatailor-channelpolicy-channelname"></a>
The name of the channel associated with this Channel Policy.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-mediatailor-channelpolicy-policy"></a>
The IAM policy for the channel. IAM policies are used to control access to your channel.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediatailor-channelpolicy-return-values"></a>

### Ref
<a name="aws-resource-mediatailor-channelpolicy-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
