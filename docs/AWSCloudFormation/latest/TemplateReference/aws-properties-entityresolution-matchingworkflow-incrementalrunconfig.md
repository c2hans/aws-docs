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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
