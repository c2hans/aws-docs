---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-eksproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksProperties
<a name="aws-properties-batch-jobdefinition-eksproperties"></a>

An object that contains the properties for the Kubernetes resources of a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-eksproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-eksproperties-syntax.json"></a>

```
{
  "[PodProperties](#cfn-batch-jobdefinition-eksproperties-podproperties)" : {{EksPodProperties}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-eksproperties-syntax.yaml"></a>

```
  [PodProperties](#cfn-batch-jobdefinition-eksproperties-podproperties): {{
    EksPodProperties}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-eksproperties-properties"></a>

`PodProperties`  <a name="cfn-batch-jobdefinition-eksproperties-podproperties"></a>
The properties for the Kubernetes pod resources of a job.
*Required*: No
*Type*: [EksPodProperties](aws-properties-batch-jobdefinition-ekspodproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
