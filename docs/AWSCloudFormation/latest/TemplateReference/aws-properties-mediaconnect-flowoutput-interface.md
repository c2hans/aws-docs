---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-interface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput Interface
<a name="aws-properties-mediaconnect-flowoutput-interface"></a>

 The VPC interface that is used for the media stream associated with the source or output.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-interface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-interface-syntax.json"></a>

```
{
  "[Name](#cfn-mediaconnect-flowoutput-interface-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-interface-syntax.yaml"></a>

```
  [Name](#cfn-mediaconnect-flowoutput-interface-name): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-interface-properties"></a>

`Name`  <a name="cfn-mediaconnect-flowoutput-interface-name"></a>
 The name of the VPC interface.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
