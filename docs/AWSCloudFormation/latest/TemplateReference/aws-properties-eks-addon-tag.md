---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-addon-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Addon Tag
<a name="aws-properties-eks-addon-tag"></a>

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.

The following basic restrictions apply to tags:
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

## Syntax
<a name="aws-properties-eks-addon-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-addon-tag-syntax.json"></a>

```
{
  "[Key](#cfn-eks-addon-tag-key)" : {{String}},
  "[Value](#cfn-eks-addon-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-addon-tag-syntax.yaml"></a>

```
  [Key](#cfn-eks-addon-tag-key): {{String}}
  [Value](#cfn-eks-addon-tag-value): {{String}}
```

## Properties
<a name="aws-properties-eks-addon-tag-properties"></a>

`Key`  <a name="cfn-eks-addon-tag-key"></a>
One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-eks-addon-tag-value"></a>
The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-eks-addon-tag--examples"></a>

###
<a name="aws-properties-eks-addon-tag--examples--"></a>

#### JSON
<a name="aws-properties-eks-addon-tag--examples----json"></a>

```
"Tags" : [
   {
      "Key" : "keyname1",
      "Value" : "value1"
   },
   {
      "Key" : "keyname2",
      "Value" : "value2"
   }
]
```

#### YAML
<a name="aws-properties-eks-addon-tag--examples----yaml"></a>

```
Tags:
  - Key: "keyname1"
    Value: "value1"
  - Key: "keyname2"
    Value: "value2"
```

## See also
<a name="aws-properties-eks-addon-tag--seealso"></a>
+  [Setting CloudFormation stack options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.html)
+  [Viewing CloudFormation stack data and resources on the AWS Management Console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
