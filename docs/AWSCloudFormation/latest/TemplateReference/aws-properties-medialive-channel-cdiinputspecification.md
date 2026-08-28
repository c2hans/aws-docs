---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-cdiinputspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CdiInputSpecification
<a name="aws-properties-medialive-channel-cdiinputspecification"></a>

The input specification for this channel. It specifies the key characteristics of CDI inputs for this channel, when those characteristics are different from other inputs.

This entity is at the top level in the channel.

## Syntax
<a name="aws-properties-medialive-channel-cdiinputspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-cdiinputspecification-syntax.json"></a>

```
{
  "[Resolution](#cfn-medialive-channel-cdiinputspecification-resolution)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-cdiinputspecification-syntax.yaml"></a>

```
  [Resolution](#cfn-medialive-channel-cdiinputspecification-resolution): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-cdiinputspecification-properties"></a>

`Resolution`  <a name="cfn-medialive-channel-cdiinputspecification-resolution"></a>
Maximum CDI input resolution
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
