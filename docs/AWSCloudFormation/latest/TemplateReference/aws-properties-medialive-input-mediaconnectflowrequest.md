---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-mediaconnectflowrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input MediaConnectFlowRequest
<a name="aws-properties-medialive-input-mediaconnectflowrequest"></a>

Settings that apply only if the input is a MediaConnect input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-mediaconnectflowrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-mediaconnectflowrequest-syntax.json"></a>

```
{
  "[FlowArn](#cfn-medialive-input-mediaconnectflowrequest-flowarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-mediaconnectflowrequest-syntax.yaml"></a>

```
  [FlowArn](#cfn-medialive-input-mediaconnectflowrequest-flowarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-mediaconnectflowrequest-properties"></a>

`FlowArn`  <a name="cfn-medialive-input-mediaconnectflowrequest-flowarn"></a>
The ARN of one or two MediaConnect flows that are the sources for this MediaConnect input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
