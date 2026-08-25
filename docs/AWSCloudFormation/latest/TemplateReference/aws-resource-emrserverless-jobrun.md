---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emrserverless-jobrun.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun
<a name="aws-resource-emrserverless-jobrun"></a>

Information about a job run. A job run is a unit of work, such as a Spark JAR, Hive query, or SparkSQL query, that you submit to an Amazon EMR Serverless application.

## Syntax
<a name="aws-resource-emrserverless-jobrun-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emrserverless-jobrun-syntax.json"></a>

```
{
  "Type" : "AWS::EMRServerless::JobRun",
  "Properties" : {
      "[ApplicationId](#cfn-emrserverless-jobrun-applicationid)" : {{String}},
      "[ConfigurationOverrides](#cfn-emrserverless-jobrun-configurationoverrides)" : {{ConfigurationOverrides}},
      "[ExecutionRoleArn](#cfn-emrserverless-jobrun-executionrolearn)" : {{String}},
      "[ExecutionTimeoutMinutes](#cfn-emrserverless-jobrun-executiontimeoutminutes)" : {{Integer}},
      "[JobDriver](#cfn-emrserverless-jobrun-jobdriver)" : {{JobDriver}},
      "[Mode](#cfn-emrserverless-jobrun-mode)" : {{String}},
      "[Name](#cfn-emrserverless-jobrun-name)" : {{String}},
      "[Tags](#cfn-emrserverless-jobrun-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-emrserverless-jobrun-syntax.yaml"></a>

```
Type: AWS::EMRServerless::JobRun
Properties:
  [ApplicationId](#cfn-emrserverless-jobrun-applicationid): {{String}}
  [ConfigurationOverrides](#cfn-emrserverless-jobrun-configurationoverrides): {{
    ConfigurationOverrides}}
  [ExecutionRoleArn](#cfn-emrserverless-jobrun-executionrolearn): {{String}}
  [ExecutionTimeoutMinutes](#cfn-emrserverless-jobrun-executiontimeoutminutes): {{Integer}}
  [JobDriver](#cfn-emrserverless-jobrun-jobdriver): {{
    JobDriver}}
  [Mode](#cfn-emrserverless-jobrun-mode): {{String}}
  [Name](#cfn-emrserverless-jobrun-name): {{String}}
  [Tags](#cfn-emrserverless-jobrun-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-emrserverless-jobrun-properties"></a>

`ApplicationId`  <a name="cfn-emrserverless-jobrun-applicationid"></a>
The ID of the application the job is running on.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-z]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationOverrides`  <a name="cfn-emrserverless-jobrun-configurationoverrides"></a>
The configuration settings that are used to override default configuration.
*Required*: No
*Type*: [ConfigurationOverrides](aws-properties-emrserverless-jobrun-configurationoverrides.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-emrserverless-jobrun-executionrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionTimeoutMinutes`  <a name="cfn-emrserverless-jobrun-executiontimeoutminutes"></a>
Returns the job run timeout value from the `StartJobRun` call. If you didn't specify a timeout, this value defaults to 720 minutes.
For BATCH mode job runs, the maximum value is 10080 minutes (7 days) starting with Amazon EMR release 7.11.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobDriver`  <a name="cfn-emrserverless-jobrun-jobdriver"></a>
The job driver for the job run.
*Required*: No
*Type*: [JobDriver](aws-properties-emrserverless-jobrun-jobdriver.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Mode`  <a name="cfn-emrserverless-jobrun-mode"></a>
The mode of the job run.
*Required*: No
*Type*: String
*Allowed values*: `BATCH | STREAMING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emrserverless-jobrun-name"></a>
The optional job run name. This doesn't have to be unique.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emrserverless-jobrun-tags"></a>
The tags assigned to the job run.
*Required*: No
*Type*: Array of [Tag](aws-properties-emrserverless-jobrun-tag.md)
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emrserverless-jobrun-return-values"></a>

### Ref
<a name="aws-resource-emrserverless-jobrun-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-emrserverless-jobrun-return-values-fn--getatt"></a>

####
<a name="aws-resource-emrserverless-jobrun-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The execution role ARN of the job run.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the job run was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The user who created the job run.

`JobRunId`  <a name="JobRunId-fn::getatt"></a>
The ID of the job run.

`ReleaseLabel`  <a name="ReleaseLabel-fn::getatt"></a>
The Amazon EMR release associated with the application your job is running on.

`State`  <a name="State-fn::getatt"></a>
The state of the job run.

`StateDetails`  <a name="StateDetails-fn::getatt"></a>
The state details of the job run.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the job run was updated.
