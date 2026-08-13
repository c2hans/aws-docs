---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-run.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Run
<a name="aws-resource-omics-run"></a>

Creates a run group to limit the compute resources for the runs that are added to the group. Returns an ARN, ID, and tags for the run group.

## Syntax
<a name="aws-resource-omics-run-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-run-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::Run",
  "Properties" : {
      "[CacheBehavior](#cfn-omics-run-cachebehavior)" : {{String}},
      "[CacheId](#cfn-omics-run-cacheid)" : {{String}},
      "[LogLevel](#cfn-omics-run-loglevel)" : {{String}},
      "[Name](#cfn-omics-run-name)" : {{String}},
      "[NetworkingMode](#cfn-omics-run-networkingmode)" : {{String}},
      "[OutputUri](#cfn-omics-run-outputuri)" : {{String}},
      "[Priority](#cfn-omics-run-priority)" : {{Integer}},
      "[RetentionMode](#cfn-omics-run-retentionmode)" : {{String}},
      "[RoleArn](#cfn-omics-run-rolearn)" : {{String}},
      "[RunGroupId](#cfn-omics-run-rungroupid)" : {{String}},
      "[StorageCapacity](#cfn-omics-run-storagecapacity)" : {{Integer}},
      "[StorageType](#cfn-omics-run-storagetype)" : {{String}},
      "[Tags](#cfn-omics-run-tags)" : {{[ Tag, ... ]}},
      "[WorkflowId](#cfn-omics-run-workflowid)" : {{String}},
      "[WorkflowOwnerId](#cfn-omics-run-workflowownerid)" : {{String}},
      "[WorkflowType](#cfn-omics-run-workflowtype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-omics-run-syntax.yaml"></a>

```
Type: AWS::Omics::Run
Properties:
  [CacheBehavior](#cfn-omics-run-cachebehavior): {{String}}
  [CacheId](#cfn-omics-run-cacheid): {{String}}
  [LogLevel](#cfn-omics-run-loglevel): {{String}}
  [Name](#cfn-omics-run-name): {{String}}
  [NetworkingMode](#cfn-omics-run-networkingmode): {{String}}
  [OutputUri](#cfn-omics-run-outputuri): {{String}}
  [Priority](#cfn-omics-run-priority): {{Integer}}
  [RetentionMode](#cfn-omics-run-retentionmode): {{String}}
  [RoleArn](#cfn-omics-run-rolearn): {{String}}
  [RunGroupId](#cfn-omics-run-rungroupid): {{String}}
  [StorageCapacity](#cfn-omics-run-storagecapacity): {{Integer}}
  [StorageType](#cfn-omics-run-storagetype): {{String}}
  [Tags](#cfn-omics-run-tags): {{
    - Tag}}
  [WorkflowId](#cfn-omics-run-workflowid): {{String}}
  [WorkflowOwnerId](#cfn-omics-run-workflowownerid): {{String}}
  [WorkflowType](#cfn-omics-run-workflowtype): {{String}}
```

## Properties
<a name="aws-resource-omics-run-properties"></a>

`CacheBehavior`  <a name="cfn-omics-run-cachebehavior"></a>
The cache behavior for the runs. Requires `cacheId` to be set.
*Required*: No
*Type*: String
*Allowed values*: `CACHE_ON_FAILURE | CACHE_ALWAYS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CacheId`  <a name="cfn-omics-run-cacheid"></a>
The identifier of the run cache to associate with the runs.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogLevel`  <a name="cfn-omics-run-loglevel"></a>
The verbosity level for CloudWatch Logs emitted during each run.
*Required*: No
*Type*: String
*Allowed values*: `OFF | FATAL | ERROR | ALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-omics-run-name"></a>
An optional user-friendly name applied to each workflow run. Can be overridden per run.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkingMode`  <a name="cfn-omics-run-networkingmode"></a>
Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.
*Required*: No
*Type*: String
*Allowed values*: `RESTRICTED | VPC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputUri`  <a name="cfn-omics-run-outputuri"></a>
The destination S3 URI for workflow outputs. Must begin with `s3://`. The `roleArn` must grant write permissions to this bucket. Can be overridden per run.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `750`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-omics-run-priority"></a>
An integer priority for the workflow runs. Higher values correspond to higher priority. A value of 0 corresponds to the lowest priority. Can be overridden per run.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionMode`  <a name="cfn-omics-run-retentionmode"></a>
The retention behavior for runs after completion.
*Required*: No
*Type*: String
*Allowed values*: `RETAIN | REMOVE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-omics-run-rolearn"></a>
The IAM role ARN that grants HealthOmics permissions to access required AWS resources such as Amazon S3 and CloudWatch. The role must have the same permissions required for individual `StartRun` calls.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunGroupId`  <a name="cfn-omics-run-rungroupid"></a>
The ID of the run group to contain all workflow runs in the batch.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageCapacity`  <a name="cfn-omics-run-storagecapacity"></a>
The filesystem size in gibibytes (GiB) provisioned for each workflow run and shared by all tasks in that run. Defaults to 1200 GiB if not specified.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageType`  <a name="cfn-omics-run-storagetype"></a>
The storage type for the workflow runs.
*Required*: No
*Type*: String
*Allowed values*: `STATIC | DYNAMIC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-omics-run-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-omics-run-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkflowId`  <a name="cfn-omics-run-workflowid"></a>
The identifier of the workflow to run.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `1`
*Maximum*: `18`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkflowOwnerId`  <a name="cfn-omics-run-workflowownerid"></a>
The AWS account ID of the workflow owner, used for cross-account workflow sharing.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkflowType`  <a name="cfn-omics-run-workflowtype"></a>
The type of the originating workflow. Batch runs are not supported with `READY2RUN` workflows.
*Required*: No
*Type*: String
*Allowed values*: `PRIVATE | READY2RUN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-run-return-values"></a>

### Ref
<a name="aws-resource-omics-run-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-run-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-run-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The run's ARN.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the run was created.

`Id`  <a name="Id-fn::getatt"></a>
The run's ID.

`RunOutputUri`  <a name="RunOutputUri-fn::getatt"></a>
Property description not available.

`StartedBy`  <a name="StartedBy-fn::getatt"></a>
Property description not available.

`StartTime`  <a name="StartTime-fn::getatt"></a>
When the run started.

`Status`  <a name="Status-fn::getatt"></a>
The run's status.

`Uuid`  <a name="Uuid-fn::getatt"></a>
Property description not available.
