---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-mltransform-transformparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::MLTransform TransformParameters
<a name="aws-properties-glue-mltransform-transformparameters"></a>

The algorithm-specific parameters that are associated with the machine learning transform.

## Syntax
<a name="aws-properties-glue-mltransform-transformparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-mltransform-transformparameters-syntax.json"></a>

```
{
  "[FindMatchesParameters](#cfn-glue-mltransform-transformparameters-findmatchesparameters)" : {{FindMatchesParameters}},
  "[TransformType](#cfn-glue-mltransform-transformparameters-transformtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-mltransform-transformparameters-syntax.yaml"></a>

```
  [FindMatchesParameters](#cfn-glue-mltransform-transformparameters-findmatchesparameters): {{
    FindMatchesParameters}}
  [TransformType](#cfn-glue-mltransform-transformparameters-transformtype): {{String}}
```

## Properties
<a name="aws-properties-glue-mltransform-transformparameters-properties"></a>

`FindMatchesParameters`  <a name="cfn-glue-mltransform-transformparameters-findmatchesparameters"></a>
The parameters for the find matches algorithm.
*Required*: No
*Type*: [FindMatchesParameters](aws-properties-glue-mltransform-findmatchesparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransformType`  <a name="cfn-glue-mltransform-transformparameters-transformtype"></a>
The type of machine learning transform. `FIND_MATCHES` is the only option.
For information about the types of machine learning transforms, see [Working with machine learning transforms](https://docs.aws.amazon.com/glue/latest/dg/console-machine-learning-transforms.html).
*Required*: Yes
*Type*: String
*Allowed values*: `FIND_MATCHES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
