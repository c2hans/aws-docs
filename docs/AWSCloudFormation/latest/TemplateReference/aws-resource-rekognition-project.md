---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rekognition-project.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::Project
<a name="aws-resource-rekognition-project"></a>

The `AWS::Rekognition::Project` type creates an Amazon Rekognition Custom Labels project. A project is a group of resources needed to create and manage versions of an Amazon Rekognition Custom Labels model.

## Syntax
<a name="aws-resource-rekognition-project-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rekognition-project-syntax.json"></a>

```
{
  "Type" : "AWS::Rekognition::Project",
  "Properties" : {
      "[ProjectName](#cfn-rekognition-project-projectname)" : {{String}},
      "[Tags](#cfn-rekognition-project-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rekognition-project-syntax.yaml"></a>

```
Type: AWS::Rekognition::Project
Properties:
  [ProjectName](#cfn-rekognition-project-projectname): {{String}}
  [Tags](#cfn-rekognition-project-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rekognition-project-properties"></a>

`ProjectName`  <a name="cfn-rekognition-project-projectname"></a>
The name of the project to create.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9][a-zA-Z0-9_\-]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rekognition-project-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rekognition-project-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rekognition-project-return-values"></a>

### Ref
<a name="aws-resource-rekognition-project-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the project name. For example:

 `{ "Ref": "CircuitBoardProject" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rekognition-project-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values. For more information about using `Fn::GetAtt`, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rekognition-project-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name of the project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
