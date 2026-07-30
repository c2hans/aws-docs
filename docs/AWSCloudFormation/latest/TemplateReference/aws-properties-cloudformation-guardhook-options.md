---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-guardhook-options.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GuardHook Options
<a name="aws-properties-cloudformation-guardhook-options"></a>

Specifies the input parameters for a Guard Hook.

## Syntax
<a name="aws-properties-cloudformation-guardhook-options-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-guardhook-options-syntax.json"></a>

```
{
  "[InputParams](#cfn-cloudformation-guardhook-options-inputparams)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-cloudformation-guardhook-options-syntax.yaml"></a>

```
  [InputParams](#cfn-cloudformation-guardhook-options-inputparams): {{
    S3Location}}
```

## Properties
<a name="aws-properties-cloudformation-guardhook-options-properties"></a>

`InputParams`  <a name="cfn-cloudformation-guardhook-options-inputparams"></a>
Specifies the S3 location of input parameter files for your Guard rules. You can specify either a single S3 location or an array of up to 10 S3 locations.
If you specify multiple input parameter files, each file must contain unique top-level keys. If duplicate top-level keys exist across files, Guard returns a failure status.
*Required*: No
*Type*: [S3Location](aws-properties-cloudformation-guardhook-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
