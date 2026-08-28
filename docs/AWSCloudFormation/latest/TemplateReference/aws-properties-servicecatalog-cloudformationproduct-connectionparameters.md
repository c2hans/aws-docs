---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicecatalog-cloudformationproduct-connectionparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::CloudFormationProduct ConnectionParameters
<a name="aws-properties-servicecatalog-cloudformationproduct-connectionparameters"></a>

Provides connection details.

## Syntax
<a name="aws-properties-servicecatalog-cloudformationproduct-connectionparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicecatalog-cloudformationproduct-connectionparameters-syntax.json"></a>

```
{
  "[CodeStar](#cfn-servicecatalog-cloudformationproduct-connectionparameters-codestar)" : {{CodeStarParameters}}
}
```

### YAML
<a name="aws-properties-servicecatalog-cloudformationproduct-connectionparameters-syntax.yaml"></a>

```
  [CodeStar](#cfn-servicecatalog-cloudformationproduct-connectionparameters-codestar): {{
    CodeStarParameters}}
```

## Properties
<a name="aws-properties-servicecatalog-cloudformationproduct-connectionparameters-properties"></a>

`CodeStar`  <a name="cfn-servicecatalog-cloudformationproduct-connectionparameters-codestar"></a>
Provides `ConnectionType` details.
*Required*: No
*Type*: [CodeStarParameters](aws-properties-servicecatalog-cloudformationproduct-codestarparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
