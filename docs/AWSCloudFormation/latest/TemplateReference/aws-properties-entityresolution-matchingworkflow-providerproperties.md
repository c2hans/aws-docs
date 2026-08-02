---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-providerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow ProviderProperties
<a name="aws-properties-entityresolution-matchingworkflow-providerproperties"></a>

An object containing the `providerServiceARN`, `intermediateSourceConfiguration`, and `providerConfiguration`.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-providerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-providerproperties-syntax.json"></a>

```
{
  "[IntermediateSourceConfiguration](#cfn-entityresolution-matchingworkflow-providerproperties-intermediatesourceconfiguration)" : {{IntermediateSourceConfiguration}},
  "[ProviderConfiguration](#cfn-entityresolution-matchingworkflow-providerproperties-providerconfiguration)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ProviderServiceArn](#cfn-entityresolution-matchingworkflow-providerproperties-providerservicearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-providerproperties-syntax.yaml"></a>

```
  [IntermediateSourceConfiguration](#cfn-entityresolution-matchingworkflow-providerproperties-intermediatesourceconfiguration): {{
    IntermediateSourceConfiguration}}
  [ProviderConfiguration](#cfn-entityresolution-matchingworkflow-providerproperties-providerconfiguration): {{
    {{Key}}: {{Value}}}}
  [ProviderServiceArn](#cfn-entityresolution-matchingworkflow-providerproperties-providerservicearn): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-providerproperties-properties"></a>

`IntermediateSourceConfiguration`  <a name="cfn-entityresolution-matchingworkflow-providerproperties-intermediatesourceconfiguration"></a>
The Amazon S3 location that temporarily stores your data while it processes. Your information won't be saved permanently.
*Required*: No
*Type*: [IntermediateSourceConfiguration](aws-properties-entityresolution-matchingworkflow-intermediatesourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderConfiguration`  <a name="cfn-entityresolution-matchingworkflow-providerproperties-providerconfiguration"></a>
The required configuration fields to use with the provider service.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderServiceArn`  <a name="cfn-entityresolution-matchingworkflow-providerproperties-providerservicearn"></a>
The ARN of the provider service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
