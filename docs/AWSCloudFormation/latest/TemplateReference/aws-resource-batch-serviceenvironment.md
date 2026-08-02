---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-serviceenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ServiceEnvironment
<a name="aws-resource-batch-serviceenvironment"></a>

Creates a service environment for running service jobs. Service environments define capacity limits for specific service types such as SageMaker Training jobs.

## Syntax
<a name="aws-resource-batch-serviceenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-batch-serviceenvironment-syntax.json"></a>

```
{
  "Type" : "AWS::Batch::ServiceEnvironment",
  "Properties" : {
      "[CapacityLimits](#cfn-batch-serviceenvironment-capacitylimits)" : {{[ CapacityLimit, ... ]}},
      "[ServiceEnvironmentName](#cfn-batch-serviceenvironment-serviceenvironmentname)" : {{String}},
      "[ServiceEnvironmentType](#cfn-batch-serviceenvironment-serviceenvironmenttype)" : {{String}},
      "[State](#cfn-batch-serviceenvironment-state)" : {{String}},
      "[Tags](#cfn-batch-serviceenvironment-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-batch-serviceenvironment-syntax.yaml"></a>

```
Type: AWS::Batch::ServiceEnvironment
Properties:
  [CapacityLimits](#cfn-batch-serviceenvironment-capacitylimits): {{
    - CapacityLimit}}
  [ServiceEnvironmentName](#cfn-batch-serviceenvironment-serviceenvironmentname): {{String}}
  [ServiceEnvironmentType](#cfn-batch-serviceenvironment-serviceenvironmenttype): {{String}}
  [State](#cfn-batch-serviceenvironment-state): {{String}}
  [Tags](#cfn-batch-serviceenvironment-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-batch-serviceenvironment-properties"></a>

`CapacityLimits`  <a name="cfn-batch-serviceenvironment-capacitylimits"></a>
The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.
*Required*: Yes
*Type*: Array of [CapacityLimit](aws-properties-batch-serviceenvironment-capacitylimit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceEnvironmentName`  <a name="cfn-batch-serviceenvironment-serviceenvironmentname"></a>
The name of the service environment.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceEnvironmentType`  <a name="cfn-batch-serviceenvironment-serviceenvironmenttype"></a>
The type of service environment. For SageMaker Training jobs, this value is `SAGEMAKER_TRAINING`.
*Required*: Yes
*Type*: String
*Allowed values*: `SAGEMAKER_TRAINING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`State`  <a name="cfn-batch-serviceenvironment-state"></a>
The state of the service environment. Valid values are `ENABLED` and `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-batch-serviceenvironment-tags"></a>
The tags associated with the service environment. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-batch-serviceenvironment-return-values"></a>

### Ref
<a name="aws-resource-batch-serviceenvironment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the compute environment ARN, such as `arn:aws:batch:us-east-1:555555555555:service-environment/ServiceEnvirnonment`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-batch-serviceenvironment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-batch-serviceenvironment-return-values-fn--getatt-fn--getatt"></a>

`ServiceEnvironmentArn`  <a name="ServiceEnvironmentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service environment.

## Examples
<a name="aws-resource-batch-serviceenvironment--examples"></a>

### Service Environment
<a name="aws-resource-batch-serviceenvironment--examples--Service_Environment"></a>

The following example creates a service environment called `SageMakerTrainingEnv`.

#### JSON
<a name="aws-resource-batch-serviceenvironment--examples--Service_Environment--json"></a>

```
{
    "ServiceEnvironment": {
        "Type": "AWS::Batch::ServiceEnvironment",
        "Properties": {
            "serviceEnvironmentName": "SageMakerTrainingEnv",
            "serviceEnvironmentType": "SAGEMAKER_TRAINING",
            "capacityLimits": [
                {
                "maxCapacity": 50,
                "capacityUnit": "NUM_INSTANCES"
                }
            ]
        }
    }
}
```
