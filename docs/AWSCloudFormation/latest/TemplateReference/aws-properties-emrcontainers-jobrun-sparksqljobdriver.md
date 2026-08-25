---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-sparksqljobdriver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun SparkSqlJobDriver
<a name="aws-properties-emrcontainers-jobrun-sparksqljobdriver"></a>

The job driver for job type.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-sparksqljobdriver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-sparksqljobdriver-syntax.json"></a>

```
{
  "[EntryPoint](#cfn-emrcontainers-jobrun-sparksqljobdriver-entrypoint)" : {{String}},
  "[SparkSqlParameters](#cfn-emrcontainers-jobrun-sparksqljobdriver-sparksqlparameters)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-sparksqljobdriver-syntax.yaml"></a>

```
  [EntryPoint](#cfn-emrcontainers-jobrun-sparksqljobdriver-entrypoint): {{String}}
  [SparkSqlParameters](#cfn-emrcontainers-jobrun-sparksqljobdriver-sparksqlparameters): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-sparksqljobdriver-properties"></a>

`EntryPoint`  <a name="cfn-emrcontainers-jobrun-sparksqljobdriver-entrypoint"></a>
The SQL file to be executed.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SparkSqlParameters`  <a name="cfn-emrcontainers-jobrun-sparksqljobdriver-sparksqlparameters"></a>
The Spark parameters to be included in the Spark SQL command.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
