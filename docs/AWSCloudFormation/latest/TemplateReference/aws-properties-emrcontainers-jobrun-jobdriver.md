---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-jobdriver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun JobDriver
<a name="aws-properties-emrcontainers-jobrun-jobdriver"></a>

Specify the driver that the job runs on. Exactly one of the two available job drivers is required, either sparkSqlJobDriver or sparkSubmitJobDriver.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-jobdriver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-jobdriver-syntax.json"></a>

```
{
  "[SparkSqlJobDriver](#cfn-emrcontainers-jobrun-jobdriver-sparksqljobdriver)" : {{SparkSqlJobDriver}},
  "[SparkSubmitJobDriver](#cfn-emrcontainers-jobrun-jobdriver-sparksubmitjobdriver)" : {{SparkSubmitJobDriver}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-jobdriver-syntax.yaml"></a>

```
  [SparkSqlJobDriver](#cfn-emrcontainers-jobrun-jobdriver-sparksqljobdriver): {{
    SparkSqlJobDriver}}
  [SparkSubmitJobDriver](#cfn-emrcontainers-jobrun-jobdriver-sparksubmitjobdriver): {{
    SparkSubmitJobDriver}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-jobdriver-properties"></a>

`SparkSqlJobDriver`  <a name="cfn-emrcontainers-jobrun-jobdriver-sparksqljobdriver"></a>
The job driver for job type.
*Required*: No
*Type*: [SparkSqlJobDriver](aws-properties-emrcontainers-jobrun-sparksqljobdriver.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SparkSubmitJobDriver`  <a name="cfn-emrcontainers-jobrun-jobdriver-sparksubmitjobdriver"></a>
The job driver parameters specified for spark submit.
*Required*: No
*Type*: [SparkSubmitJobDriver](aws-properties-emrcontainers-jobrun-sparksubmitjobdriver.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
