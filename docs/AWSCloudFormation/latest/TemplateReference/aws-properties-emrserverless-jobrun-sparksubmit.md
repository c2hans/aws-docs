---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-sparksubmit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun SparkSubmit
<a name="aws-properties-emrserverless-jobrun-sparksubmit"></a>

The configurations for the Spark submit job driver.

## Syntax
<a name="aws-properties-emrserverless-jobrun-sparksubmit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-sparksubmit-syntax.json"></a>

```
{
  "[EntryPoint](#cfn-emrserverless-jobrun-sparksubmit-entrypoint)" : {{String}},
  "[EntryPointArguments](#cfn-emrserverless-jobrun-sparksubmit-entrypointarguments)" : {{[ String, ... ]}},
  "[SparkSubmitParameters](#cfn-emrserverless-jobrun-sparksubmit-sparksubmitparameters)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-sparksubmit-syntax.yaml"></a>

```
  [EntryPoint](#cfn-emrserverless-jobrun-sparksubmit-entrypoint): {{String}}
  [EntryPointArguments](#cfn-emrserverless-jobrun-sparksubmit-entrypointarguments): {{
    - String}}
  [SparkSubmitParameters](#cfn-emrserverless-jobrun-sparksubmit-sparksubmitparameters): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-sparksubmit-properties"></a>

`EntryPoint`  <a name="cfn-emrserverless-jobrun-sparksubmit-entrypoint"></a>
The entry point for the Spark submit job run.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntryPointArguments`  <a name="cfn-emrserverless-jobrun-sparksubmit-entrypointarguments"></a>
The arguments for the Spark submit job run.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SparkSubmitParameters`  <a name="cfn-emrserverless-jobrun-sparksubmit-sparksubmitparameters"></a>
The parameters for the Spark submit job run.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
