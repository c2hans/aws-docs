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
