---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow IntermediateSourceConfiguration
<a name="aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration"></a>

The Amazon S3 location that temporarily stores your data while it processes. Your information won't be saved permanently.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration-syntax.json"></a>

```
{
  "[IntermediateS3Path](#cfn-entityresolution-idmappingworkflow-intermediatesourceconfiguration-intermediates3path)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration-syntax.yaml"></a>

```
  [IntermediateS3Path](#cfn-entityresolution-idmappingworkflow-intermediatesourceconfiguration-intermediates3path): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration-properties"></a>

`IntermediateS3Path`  <a name="cfn-entityresolution-idmappingworkflow-intermediatesourceconfiguration-intermediates3path"></a>
The Amazon S3 location (bucket and prefix). For example: `s3://provider_bucket/DOC-EXAMPLE-BUCKET`
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
