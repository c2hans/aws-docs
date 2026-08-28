---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode AwsCloudMapInstanceAttribute
<a name="aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute"></a>

An object that represents the AWS Cloud Map attribute information for your virtual node.

**Note**
AWS Cloud Map is not available in the eu-south-1 Region.

## Syntax
<a name="aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute-syntax.json"></a>

```
{
  "[Key](#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key)" : {{String}},
  "[Value](#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute-syntax.yaml"></a>

```
  [Key](#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key): {{String}}
  [Value](#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute-properties"></a>

`Key`  <a name="cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key"></a>
The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9!-~]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value"></a>
The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.
*Required*: Yes
*Type*: String
*Pattern*: `([a-zA-Z0-9!-~][ a-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
