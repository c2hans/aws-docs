---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emrcontainers-jobrun.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun
<a name="aws-resource-emrcontainers-jobrun"></a>

This entity describes a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.

## Syntax
<a name="aws-resource-emrcontainers-jobrun-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emrcontainers-jobrun-syntax.json"></a>

```
{
  "Type" : "AWS::EMRContainers::JobRun",
  "Properties" : {
      "[ConfigurationOverrides](#cfn-emrcontainers-jobrun-configurationoverrides)" : {{ConfigurationOverrides}},
      "[ExecutionRoleArn](#cfn-emrcontainers-jobrun-executionrolearn)" : {{String}},
      "[JobDriver](#cfn-emrcontainers-jobrun-jobdriver)" : {{JobDriver}},
      "[Name](#cfn-emrcontainers-jobrun-name)" : {{String}},
      "[ReleaseLabel](#cfn-emrcontainers-jobrun-releaselabel)" : {{String}},
      "[RetryPolicyConfiguration](#cfn-emrcontainers-jobrun-retrypolicyconfiguration)" : {{RetryPolicyConfiguration}},
      "[Tags](#cfn-emrcontainers-jobrun-tags)" : {{[ Tag, ... ]}},
      "[VirtualClusterId](#cfn-emrcontainers-jobrun-virtualclusterid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-emrcontainers-jobrun-syntax.yaml"></a>

```
Type: AWS::EMRContainers::JobRun
Properties:
  [ConfigurationOverrides](#cfn-emrcontainers-jobrun-configurationoverrides): {{
    ConfigurationOverrides}}
  [ExecutionRoleArn](#cfn-emrcontainers-jobrun-executionrolearn): {{String}}
  [JobDriver](#cfn-emrcontainers-jobrun-jobdriver): {{
    JobDriver}}
  [Name](#cfn-emrcontainers-jobrun-name): {{String}}
  [ReleaseLabel](#cfn-emrcontainers-jobrun-releaselabel): {{String}}
  [RetryPolicyConfiguration](#cfn-emrcontainers-jobrun-retrypolicyconfiguration): {{
    RetryPolicyConfiguration}}
  [Tags](#cfn-emrcontainers-jobrun-tags): {{
    - Tag}}
  [VirtualClusterId](#cfn-emrcontainers-jobrun-virtualclusterid): {{String}}
```

## Properties
<a name="aws-resource-emrcontainers-jobrun-properties"></a>

`ConfigurationOverrides`  <a name="cfn-emrcontainers-jobrun-configurationoverrides"></a>
The configuration settings that are used to override default configuration.
*Required*: No
*Type*: [ConfigurationOverrides](aws-properties-emrcontainers-jobrun-configurationoverrides.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-emrcontainers-jobrun-executionrolearn"></a>
The execution role ARN of the job run.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobDriver`  <a name="cfn-emrcontainers-jobrun-jobdriver"></a>
Parameters of job driver for the job run.
*Required*: No
*Type*: [JobDriver](aws-properties-emrcontainers-jobrun-jobdriver.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emrcontainers-jobrun-name"></a>
The name of the job run.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLabel`  <a name="cfn-emrcontainers-jobrun-releaselabel"></a>
The release version of Amazon EMR.
*Required*: No
*Type*: String
*Pattern*: `^[\.\-_/A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetryPolicyConfiguration`  <a name="cfn-emrcontainers-jobrun-retrypolicyconfiguration"></a>
The configuration of the retry policy that the job runs on.
*Required*: No
*Type*: [RetryPolicyConfiguration](aws-properties-emrcontainers-jobrun-retrypolicyconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emrcontainers-jobrun-tags"></a>
The assigned tags of the job run.
*Required*: No
*Type*: Array of [Tag](aws-properties-emrcontainers-jobrun-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualClusterId`  <a name="cfn-emrcontainers-jobrun-virtualclusterid"></a>
The ID of the job run's virtual cluster.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emrcontainers-jobrun-return-values"></a>

### Ref
<a name="aws-resource-emrcontainers-jobrun-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-emrcontainers-jobrun-return-values-fn--getatt"></a>

####
<a name="aws-resource-emrcontainers-jobrun-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of job run.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the job run was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The user who created the job run.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reasons why the job run has failed.

`FinishedAt`  <a name="FinishedAt-fn::getatt"></a>
The date and time when the job run has finished.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the job run.

`State`  <a name="State-fn::getatt"></a>
The state of the job run.
