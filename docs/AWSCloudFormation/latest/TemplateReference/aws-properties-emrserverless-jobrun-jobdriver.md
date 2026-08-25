---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-jobdriver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun JobDriver
<a name="aws-properties-emrserverless-jobrun-jobdriver"></a>

The driver that the job runs on.

## Syntax
<a name="aws-properties-emrserverless-jobrun-jobdriver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-jobdriver-syntax.json"></a>

```
{
  "[Hive](#cfn-emrserverless-jobrun-jobdriver-hive)" : {{Hive}},
  "[SparkSubmit](#cfn-emrserverless-jobrun-jobdriver-sparksubmit)" : {{SparkSubmit}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-jobdriver-syntax.yaml"></a>

```
  [Hive](#cfn-emrserverless-jobrun-jobdriver-hive): {{
    Hive}}
  [SparkSubmit](#cfn-emrserverless-jobrun-jobdriver-sparksubmit): {{
    SparkSubmit}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-jobdriver-properties"></a>

`Hive`  <a name="cfn-emrserverless-jobrun-jobdriver-hive"></a>
The job driver parameters specified for Hive.
*Required*: No
*Type*: [Hive](aws-properties-emrserverless-jobrun-hive.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SparkSubmit`  <a name="cfn-emrserverless-jobrun-jobdriver-sparksubmit"></a>
The job driver parameters specified for Spark.
*Required*: No
*Type*: [SparkSubmit](aws-properties-emrserverless-jobrun-sparksubmit.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
