---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate SparkSubmitJobDriver
<a name="aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver"></a>

The information about job driver for Spark submit.

## Syntax
<a name="aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver-syntax.json"></a>

```
{
  "[EntryPoint](#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypoint)" : {{String}},
  "[EntryPointArguments](#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypointarguments)" : {{[ String, ... ]}},
  "[SparkSubmitParameters](#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-sparksubmitparameters)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver-syntax.yaml"></a>

```
  [EntryPoint](#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypoint): {{String}}
  [EntryPointArguments](#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypointarguments): {{
    - String}}
  [SparkSubmitParameters](#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-sparksubmitparameters): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver-properties"></a>

`EntryPoint`  <a name="cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypoint"></a>
The entry point of job application.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntryPointArguments`  <a name="cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypointarguments"></a>
The arguments for job application.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SparkSubmitParameters`  <a name="cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-sparksubmitparameters"></a>
The Spark submit parameters that are used for job runs.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
