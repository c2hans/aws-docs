---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-instrumentationconfig-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::InstrumentationConfig Location
<a name="aws-properties-applicationsignals-instrumentationconfig-location"></a>

A union that identifies the location to instrument. Specify a `CodeLocation` for code-level instrumentation.

## Syntax
<a name="aws-properties-applicationsignals-instrumentationconfig-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-instrumentationconfig-location-syntax.json"></a>

```
{
  "[CodeLocation](#cfn-applicationsignals-instrumentationconfig-location-codelocation)" : {{CodeLocation}}
}
```

### YAML
<a name="aws-properties-applicationsignals-instrumentationconfig-location-syntax.yaml"></a>

```
  [CodeLocation](#cfn-applicationsignals-instrumentationconfig-location-codelocation): {{
    CodeLocation}}
```

## Properties
<a name="aws-properties-applicationsignals-instrumentationconfig-location-properties"></a>

`CodeLocation`  <a name="cfn-applicationsignals-instrumentationconfig-location-codelocation"></a>
A code location for code-level instrumentation, including language, code unit, class, method, file path, and optional line number.
*Required*: Yes
*Type*: [CodeLocation](aws-properties-applicationsignals-instrumentationconfig-codelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
