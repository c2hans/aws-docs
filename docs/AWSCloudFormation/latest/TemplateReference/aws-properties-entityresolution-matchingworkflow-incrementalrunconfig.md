---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-incrementalrunconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow IncrementalRunConfig
<a name="aws-properties-entityresolution-matchingworkflow-incrementalrunconfig"></a>

Optional. An object that defines the incremental run type. This object contains only the `incrementalRunType` field, which appears as "Automatic" in the console.

**Important**
For workflows where `resolutionType` is `PROVIDER`, incremental processing is not supported.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-incrementalrunconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-incrementalrunconfig-syntax.json"></a>

```
{
  "[IncrementalRunType](#cfn-entityresolution-matchingworkflow-incrementalrunconfig-incrementalruntype)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-incrementalrunconfig-syntax.yaml"></a>

```
  [IncrementalRunType](#cfn-entityresolution-matchingworkflow-incrementalrunconfig-incrementalruntype): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-incrementalrunconfig-properties"></a>

`IncrementalRunType`  <a name="cfn-entityresolution-matchingworkflow-incrementalrunconfig-incrementalruntype"></a>
The type of incremental run. The only valid value is `IMMEDIATE`. This appears as "Automatic" in the console.
For workflows where `resolutionType` is `PROVIDER`, incremental processing is not supported.
*Required*: Yes
*Type*: String
*Allowed values*: `IMMEDIATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
