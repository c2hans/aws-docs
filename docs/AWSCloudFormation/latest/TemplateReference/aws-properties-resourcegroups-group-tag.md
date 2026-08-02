---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resourcegroups-group-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResourceGroups::Group Tag
<a name="aws-properties-resourcegroups-group-tag"></a>

Adds tags to a resource group with the specified Amazon resource name (ARN). Existing tags on a resource group are not changed if they are not specified in the request parameters.

**Important**
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

 **Minimum permissions**

To run this command, you must have the following permissions:
+  `resource-groups:Tag`

## Syntax
<a name="aws-properties-resourcegroups-group-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resourcegroups-group-tag-syntax.json"></a>

```
{
  "[Key](#cfn-resourcegroups-group-tag-key)" : {{String}},
  "[Value](#cfn-resourcegroups-group-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-resourcegroups-group-tag-syntax.yaml"></a>

```
  [Key](#cfn-resourcegroups-group-tag-key): {{String}}
  [Value](#cfn-resourcegroups-group-tag-value): {{String}}
```

## Properties
<a name="aws-properties-resourcegroups-group-tag-properties"></a>

`Key`  <a name="cfn-resourcegroups-group-tag-key"></a>
The tag key.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:).+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-resourcegroups-group-tag-value"></a>
The tag value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
