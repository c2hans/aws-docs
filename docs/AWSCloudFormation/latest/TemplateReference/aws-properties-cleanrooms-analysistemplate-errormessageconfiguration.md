---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-errormessageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate ErrorMessageConfiguration
<a name="aws-properties-cleanrooms-analysistemplate-errormessageconfiguration"></a>

A structure that defines the level of detail included in error messages returned by PySpark jobs. This configuration allows you to control the verbosity of error messages to help with troubleshooting PySpark jobs while maintaining appropriate security controls.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-errormessageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-errormessageconfiguration-syntax.json"></a>

```
{
  "[Type](#cfn-cleanrooms-analysistemplate-errormessageconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-errormessageconfiguration-syntax.yaml"></a>

```
  [Type](#cfn-cleanrooms-analysistemplate-errormessageconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-errormessageconfiguration-properties"></a>

`Type`  <a name="cfn-cleanrooms-analysistemplate-errormessageconfiguration-type"></a>
The level of detail for error messages returned by the PySpark job. When set to DETAILED, error messages include more information to help troubleshoot issues with your PySpark job.
Because this setting may expose sensitive data, it is recommended for development and testing environments.
*Required*: Yes
*Type*: String
*Allowed values*: `DETAILED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
