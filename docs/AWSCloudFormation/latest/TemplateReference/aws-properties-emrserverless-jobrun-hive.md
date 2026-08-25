---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-hive.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun Hive
<a name="aws-properties-emrserverless-jobrun-hive"></a>

The configurations for the Hive job driver.

## Syntax
<a name="aws-properties-emrserverless-jobrun-hive-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-hive-syntax.json"></a>

```
{
  "[InitQueryFile](#cfn-emrserverless-jobrun-hive-initqueryfile)" : {{String}},
  "[Parameters](#cfn-emrserverless-jobrun-hive-parameters)" : {{String}},
  "[Query](#cfn-emrserverless-jobrun-hive-query)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-hive-syntax.yaml"></a>

```
  [InitQueryFile](#cfn-emrserverless-jobrun-hive-initqueryfile): {{String}}
  [Parameters](#cfn-emrserverless-jobrun-hive-parameters): {{String}}
  [Query](#cfn-emrserverless-jobrun-hive-query): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-hive-properties"></a>

`InitQueryFile`  <a name="cfn-emrserverless-jobrun-hive-initqueryfile"></a>
The query file for the Hive job run.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-emrserverless-jobrun-hive-parameters"></a>
The parameters for the Hive job run.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Query`  <a name="cfn-emrserverless-jobrun-hive-query"></a>
The query for the Hive job run.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
