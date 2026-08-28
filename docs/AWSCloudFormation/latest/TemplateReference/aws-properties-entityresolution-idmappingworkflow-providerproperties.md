---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-providerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow ProviderProperties
<a name="aws-properties-entityresolution-idmappingworkflow-providerproperties"></a>

An object containing the `providerServiceARN`, `intermediateSourceConfiguration`, and `providerConfiguration`.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-providerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-providerproperties-syntax.json"></a>

```
{
  "[IntermediateSourceConfiguration](#cfn-entityresolution-idmappingworkflow-providerproperties-intermediatesourceconfiguration)" : {{IntermediateSourceConfiguration}},
  "[ProviderConfiguration](#cfn-entityresolution-idmappingworkflow-providerproperties-providerconfiguration)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ProviderServiceArn](#cfn-entityresolution-idmappingworkflow-providerproperties-providerservicearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-providerproperties-syntax.yaml"></a>

```
  [IntermediateSourceConfiguration](#cfn-entityresolution-idmappingworkflow-providerproperties-intermediatesourceconfiguration): {{
    IntermediateSourceConfiguration}}
  [ProviderConfiguration](#cfn-entityresolution-idmappingworkflow-providerproperties-providerconfiguration): {{
    {{Key}}: {{Value}}}}
  [ProviderServiceArn](#cfn-entityresolution-idmappingworkflow-providerproperties-providerservicearn): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-providerproperties-properties"></a>

`IntermediateSourceConfiguration`  <a name="cfn-entityresolution-idmappingworkflow-providerproperties-intermediatesourceconfiguration"></a>
The Amazon S3 location that temporarily stores your data while it processes. Your information won't be saved permanently.
*Required*: No
*Type*: [IntermediateSourceConfiguration](aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderConfiguration`  <a name="cfn-entityresolution-idmappingworkflow-providerproperties-providerconfiguration"></a>
The required configuration fields to use with the provider service.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderServiceArn`  <a name="cfn-entityresolution-idmappingworkflow-providerproperties-providerservicearn"></a>
The ARN of the provider service.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
