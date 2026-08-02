---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow IdMappingIncrementalRunConfig
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig"></a>

 Incremental run configuration for an ID mapping workflow.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-syntax.json"></a>

```
{
  "[IncrementalRunType](#cfn-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-incrementalruntype)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-syntax.yaml"></a>

```
  [IncrementalRunType](#cfn-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-incrementalruntype): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-properties"></a>

`IncrementalRunType`  <a name="cfn-entityresolution-idmappingworkflow-idmappingincrementalrunconfig-incrementalruntype"></a>
 The incremental run type for an ID mapping workflow.
It takes only one value: `ON_DEMAND`. This setting runs the ID mapping workflow when it's manually triggered through the `StartIdMappingJob` API.
*Required*: Yes
*Type*: String
*Allowed values*: `ON_DEMAND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
