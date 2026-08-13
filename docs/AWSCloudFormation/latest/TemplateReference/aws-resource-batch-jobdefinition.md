---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-jobdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition
<a name="aws-resource-batch-jobdefinition"></a>

The `AWS::Batch::JobDefinition` resource specifies the parameters for an AWS Batch job definition. For more information, see [Job Definitions](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html) in the * AWS Batch User Guide *.

## Syntax
<a name="aws-resource-batch-jobdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-batch-jobdefinition-syntax.json"></a>

```
{
  "Type" : "AWS::Batch::JobDefinition",
  "Properties" : {
      "[ConsumableResourceProperties](#cfn-batch-jobdefinition-consumableresourceproperties)" : {{ConsumableResourceProperties}},
      "[ContainerProperties](#cfn-batch-jobdefinition-containerproperties)" : {{ContainerProperties}},
      "[EcsProperties](#cfn-batch-jobdefinition-ecsproperties)" : {{EcsProperties}},
      "[EksProperties](#cfn-batch-jobdefinition-eksproperties)" : {{EksProperties}},
      "[JobDefinitionName](#cfn-batch-jobdefinition-jobdefinitionname)" : {{String}},
      "[NodeProperties](#cfn-batch-jobdefinition-nodeproperties)" : {{NodeProperties}},
      "[Parameters](#cfn-batch-jobdefinition-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[PlatformCapabilities](#cfn-batch-jobdefinition-platformcapabilities)" : {{[ String, ... ]}},
      "[PropagateTags](#cfn-batch-jobdefinition-propagatetags)" : {{Boolean}},
      "[ResourceRetentionPolicy](#cfn-batch-jobdefinition-resourceretentionpolicy)" : {{ResourceRetentionPolicy}},
      "[RetryStrategy](#cfn-batch-jobdefinition-retrystrategy)" : {{RetryStrategy}},
      "[SchedulingPriority](#cfn-batch-jobdefinition-schedulingpriority)" : {{Integer}},
      "[Tags](#cfn-batch-jobdefinition-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Timeout](#cfn-batch-jobdefinition-timeout)" : {{JobTimeout}},
      "[Type](#cfn-batch-jobdefinition-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-batch-jobdefinition-syntax.yaml"></a>

```
Type: AWS::Batch::JobDefinition
Properties:
  [ConsumableResourceProperties](#cfn-batch-jobdefinition-consumableresourceproperties): {{
    ConsumableResourceProperties}}
  [ContainerProperties](#cfn-batch-jobdefinition-containerproperties): {{
    ContainerProperties}}
  [EcsProperties](#cfn-batch-jobdefinition-ecsproperties): {{
    EcsProperties}}
  [EksProperties](#cfn-batch-jobdefinition-eksproperties): {{
    EksProperties}}
  [JobDefinitionName](#cfn-batch-jobdefinition-jobdefinitionname): {{String}}
  [NodeProperties](#cfn-batch-jobdefinition-nodeproperties): {{
    NodeProperties}}
  [Parameters](#cfn-batch-jobdefinition-parameters): {{
    {{Key}}: {{Value}}}}
  [PlatformCapabilities](#cfn-batch-jobdefinition-platformcapabilities): {{
    - String}}
  [PropagateTags](#cfn-batch-jobdefinition-propagatetags): {{Boolean}}
  [ResourceRetentionPolicy](#cfn-batch-jobdefinition-resourceretentionpolicy): {{
    ResourceRetentionPolicy}}
  [RetryStrategy](#cfn-batch-jobdefinition-retrystrategy): {{
    RetryStrategy}}
  [SchedulingPriority](#cfn-batch-jobdefinition-schedulingpriority): {{Integer}}
  [Tags](#cfn-batch-jobdefinition-tags): {{
    {{Key}}: {{Value}}}}
  [Timeout](#cfn-batch-jobdefinition-timeout): {{
    JobTimeout}}
  [Type](#cfn-batch-jobdefinition-type): {{String}}
```

## Properties
<a name="aws-resource-batch-jobdefinition-properties"></a>

`ConsumableResourceProperties`  <a name="cfn-batch-jobdefinition-consumableresourceproperties"></a>
Contains a list of consumable resources required by the job.
*Required*: No
*Type*: [ConsumableResourceProperties](aws-properties-batch-jobdefinition-consumableresourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerProperties`  <a name="cfn-batch-jobdefinition-containerproperties"></a>
An object with properties specific to Amazon ECS-based jobs. When `containerProperties` is used in the job definition, it can't be used in addition to `eksProperties`, `ecsProperties`, or `nodeProperties`.
*Required*: No
*Type*: [ContainerProperties](aws-properties-batch-jobdefinition-containerproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EcsProperties`  <a name="cfn-batch-jobdefinition-ecsproperties"></a>
An object that contains the properties for the Amazon ECS resources of a job.When `ecsProperties` is used in the job definition, it can't be used in addition to `containerProperties`, `eksProperties`, or `nodeProperties`.
*Required*: No
*Type*: [EcsProperties](aws-properties-batch-jobdefinition-ecsproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EksProperties`  <a name="cfn-batch-jobdefinition-eksproperties"></a>
An object with properties that are specific to Amazon EKS-based jobs. When `eksProperties` is used in the job definition, it can't be used in addition to `containerProperties`, `ecsProperties`, or `nodeProperties`.
*Required*: No
*Type*: [EksProperties](aws-properties-batch-jobdefinition-eksproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobDefinitionName`  <a name="cfn-batch-jobdefinition-jobdefinitionname"></a>
The name of the job definition.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NodeProperties`  <a name="cfn-batch-jobdefinition-nodeproperties"></a>
An object with properties that are specific to multi-node parallel jobs. When `nodeProperties` is used in the job definition, it can't be used in addition to `containerProperties`, `ecsProperties`, or `eksProperties`.
If the job runs on Fargate resources, don't specify `nodeProperties`. Use `containerProperties` instead.
*Required*: No
*Type*: [NodeProperties](aws-properties-batch-jobdefinition-nodeproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-batch-jobdefinition-parameters"></a>
Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a `SubmitJob` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see [Job definition parameters](https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlatformCapabilities`  <a name="cfn-batch-jobdefinition-platformcapabilities"></a>
The platform capabilities required by the job definition. If no value is specified, it defaults to `EC2`. Jobs run on Fargate resources specify `FARGATE`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateTags`  <a name="cfn-batch-jobdefinition-propagatetags"></a>
Specifies whether to propagate the tags from the job or job definition to the corresponding Amazon ECS task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the tasks when the tasks are created. For tags with the same name, job tags are given priority over job definitions tags. If the total number of combined tags from the job and job definition is over 50, the job is moved to the `FAILED` state.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceRetentionPolicy`  <a name="cfn-batch-jobdefinition-resourceretentionpolicy"></a>
Specifies the resource retention policy settings for the job definition.
*Required*: No
*Type*: [ResourceRetentionPolicy](aws-properties-batch-jobdefinition-resourceretentionpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryStrategy`  <a name="cfn-batch-jobdefinition-retrystrategy"></a>
The retry strategy to use for failed jobs that are submitted with this job definition.
*Required*: No
*Type*: [RetryStrategy](aws-properties-batch-jobdefinition-retrystrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchedulingPriority`  <a name="cfn-batch-jobdefinition-schedulingpriority"></a>
The scheduling priority of the job definition. This only affects jobs in job queues with a fair-share policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-batch-jobdefinition-tags"></a>
The tags that are applied to the job definition.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Timeout`  <a name="cfn-batch-jobdefinition-timeout"></a>
The timeout time for jobs that are submitted with this job definition. After the amount of time you specify passes, AWS Batch terminates your jobs if they aren't finished.
*Required*: No
*Type*: [JobTimeout](aws-properties-batch-jobdefinition-jobtimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-batch-jobdefinition-type"></a>
The type of job definition. For more information about multi-node parallel jobs, see [Creating a multi-node parallel job definition](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def.html) in the *AWS Batch User Guide*.
+ If the value is `container`, then one of the following is required: `containerProperties`, `ecsProperties`, or `eksProperties`.
+ If the value is `multinode`, then `nodeProperties` is required.
If the job is run on Fargate resources, then `multinode` isn't supported.
*Required*: Yes
*Type*: String
*Allowed values*: `container | multinode`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-batch-jobdefinition-return-values"></a>

### Ref
<a name="aws-resource-batch-jobdefinition-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the job definition ARN, such as `arn:aws:batch:us-east-1:111122223333:job-definition/test-gpu:2`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-batch-jobdefinition-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-batch-jobdefinition-return-values-fn--getatt-fn--getatt"></a>

`JobDefinitionArn`  <a name="JobDefinitionArn-fn::getatt"></a>
The job definition ARN, such as `arn:aws:batch:us-east-1:111122223333:job-definition/test-gpu:2`.

## Examples
<a name="aws-resource-batch-jobdefinition--examples"></a>

### Test nvidia-smi
<a name="aws-resource-batch-jobdefinition--examples--Test_nvidia-smi"></a>

The following example tests the `nvidia-smi` command on a GPU instance to verify that the GPU is working inside the container. For more information, see [Test GPU Functionality](https://docs.aws.amazon.com/batch/latest/userguide/example-job-definitions.html#example-test-gpu) in the * AWS Batch User Guide *.

#### JSON
<a name="aws-resource-batch-jobdefinition--examples--Test_nvidia-smi--json"></a>

```
{
  "JobDefinition": {
    "Type": "AWS::Batch::JobDefinition",
    "Properties": {
      "Type": "container",
      "JobDefinitionName": "nvidia-smi",
      "ContainerProperties": {
        "MountPoints": [
          {
            "ReadOnly": false,
            "SourceVolume": "nvidia",
            "ContainerPath": "/usr/local/nvidia"
          }
        ],
        "Volumes": [
          {
            "Host": {
              "SourcePath": "/var/lib/nvidia-docker/volumes/nvidia_driver/latest"
            },
            "Name": "nvidia"
          }
        ],
        "Command": [
          "nvidia-smi"
        ],
        "Privileged": true,
        "JobRoleArn": "String",
        "ReadonlyRootFilesystem": true,
        "ResourceRequirements": [
          {
            "Type": "MEMORY",
            "Value": "2000"
          },
          {
            "Type": "VCPU",
            "Value": "2"
          }
        ],
        "Image": "nvidia/cuda"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-batch-jobdefinition--examples--Test_nvidia-smi--yaml"></a>

```
JobDefinition:
  Type: 'AWS::Batch::JobDefinition'
  Properties:
    Type: container
    JobDefinitionName: nvidia-smi
    ContainerProperties:
      MountPoints:
        - ReadOnly: false
          SourceVolume: nvidia
          ContainerPath: /usr/local/nvidia
      Volumes:
        - Host:
            SourcePath: /var/lib/nvidia-docker/volumes/nvidia_driver/latest
          Name: nvidia
      Command:
        - nvidia-smi
      Privileged: true
      JobRoleArn: String
      ReadonlyRootFilesystem: true
      ResourceRequirements:
        - Type: MEMORY
          Value: '2000'
        - Type: VCPU
          Value: '2'
      Image: nvidia/cuda
```

## See also
<a name="aws-resource-batch-jobdefinition--seealso"></a>
+ [Job Definition Parameters](https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html) in the * AWS Batch User Guide *.
