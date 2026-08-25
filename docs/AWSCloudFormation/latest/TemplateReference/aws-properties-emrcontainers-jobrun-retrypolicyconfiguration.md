---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-retrypolicyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun RetryPolicyConfiguration
<a name="aws-properties-emrcontainers-jobrun-retrypolicyconfiguration"></a>

The configuration of the retry policy that the job runs on.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-retrypolicyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-retrypolicyconfiguration-syntax.json"></a>

```
{
  "[MaxAttempts](#cfn-emrcontainers-jobrun-retrypolicyconfiguration-maxattempts)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-retrypolicyconfiguration-syntax.yaml"></a>

```
  [MaxAttempts](#cfn-emrcontainers-jobrun-retrypolicyconfiguration-maxattempts): {{Integer}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-retrypolicyconfiguration-properties"></a>

`MaxAttempts`  <a name="cfn-emrcontainers-jobrun-retrypolicyconfiguration-maxattempts"></a>
The maximum number of attempts on the job's driver.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
