---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowSource VpcInterfaceAttachment
<a name="aws-properties-mediaconnect-flowsource-vpcinterfaceattachment"></a>

 The settings for attaching a VPC interface to an resource.

## Syntax
<a name="aws-properties-mediaconnect-flowsource-vpcinterfaceattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowsource-vpcinterfaceattachment-syntax.json"></a>

```
{
  "[VpcInterfaceName](#cfn-mediaconnect-flowsource-vpcinterfaceattachment-vpcinterfacename)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowsource-vpcinterfaceattachment-syntax.yaml"></a>

```
  [VpcInterfaceName](#cfn-mediaconnect-flowsource-vpcinterfaceattachment-vpcinterfacename): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowsource-vpcinterfaceattachment-properties"></a>

`VpcInterfaceName`  <a name="cfn-mediaconnect-flowsource-vpcinterfaceattachment-vpcinterfacename"></a>
 The name of the VPC interface to use for this resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
