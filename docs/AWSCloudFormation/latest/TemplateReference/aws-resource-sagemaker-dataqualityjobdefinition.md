---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-dataqualityjobdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition
<a name="aws-resource-sagemaker-dataqualityjobdefinition"></a>

Creates a definition for a job that monitors data quality and drift. For information about model monitor, see [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html).

## Syntax
<a name="aws-resource-sagemaker-dataqualityjobdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-dataqualityjobdefinition-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::DataQualityJobDefinition",
  "Properties" : {
      "[DataQualityAppSpecification](#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification)" : {{DataQualityAppSpecification}},
      "[DataQualityBaselineConfig](#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig)" : {{DataQualityBaselineConfig}},
      "[DataQualityJobInput](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput)" : {{DataQualityJobInput}},
      "[DataQualityJobOutputConfig](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig)" : {{MonitoringOutputConfig}},
      "[EndpointName](#cfn-sagemaker-dataqualityjobdefinition-endpointname)" : {{String}},
      "[JobDefinitionName](#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname)" : {{String}},
      "[JobResources](#cfn-sagemaker-dataqualityjobdefinition-jobresources)" : {{MonitoringResources}},
      "[NetworkConfig](#cfn-sagemaker-dataqualityjobdefinition-networkconfig)" : {{NetworkConfig}},
      "[RoleArn](#cfn-sagemaker-dataqualityjobdefinition-rolearn)" : {{String}},
      "[StoppingCondition](#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition)" : {{StoppingCondition}},
      "[Tags](#cfn-sagemaker-dataqualityjobdefinition-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-dataqualityjobdefinition-syntax.yaml"></a>

```
Type: AWS::SageMaker::DataQualityJobDefinition
Properties:
  [DataQualityAppSpecification](#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification): {{
    DataQualityAppSpecification}}
  [DataQualityBaselineConfig](#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig): {{
    DataQualityBaselineConfig}}
  [DataQualityJobInput](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput): {{
    DataQualityJobInput}}
  [DataQualityJobOutputConfig](#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig): {{
    MonitoringOutputConfig}}
  [EndpointName](#cfn-sagemaker-dataqualityjobdefinition-endpointname): {{String}}
  [JobDefinitionName](#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname): {{String}}
  [JobResources](#cfn-sagemaker-dataqualityjobdefinition-jobresources): {{
    MonitoringResources}}
  [NetworkConfig](#cfn-sagemaker-dataqualityjobdefinition-networkconfig): {{
    NetworkConfig}}
  [RoleArn](#cfn-sagemaker-dataqualityjobdefinition-rolearn): {{String}}
  [StoppingCondition](#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition): {{
    StoppingCondition}}
  [Tags](#cfn-sagemaker-dataqualityjobdefinition-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-dataqualityjobdefinition-properties"></a>

`DataQualityAppSpecification`  <a name="cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification"></a>
Specifies the container that runs the monitoring job.
*Required*: Yes
*Type*: [DataQualityAppSpecification](aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataQualityBaselineConfig`  <a name="cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig"></a>
Configures the constraints and baselines for the monitoring job.
*Required*: No
*Type*: [DataQualityBaselineConfig](aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataQualityJobInput`  <a name="cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput"></a>
A list of inputs for the monitoring job. Currently endpoints are supported as monitoring inputs.
*Required*: Yes
*Type*: [DataQualityJobInput](aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataQualityJobOutputConfig`  <a name="cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig"></a>
The output configuration for monitoring jobs.
*Required*: Yes
*Type*: [MonitoringOutputConfig](aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointName`  <a name="cfn-sagemaker-dataqualityjobdefinition-endpointname"></a>
The name of the endpoint used to run the monitoring job.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobDefinitionName`  <a name="cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname"></a>
The name for the monitoring job definition.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobResources`  <a name="cfn-sagemaker-dataqualityjobdefinition-jobresources"></a>
Identifies the resources to deploy for a monitoring job.
*Required*: Yes
*Type*: [MonitoringResources](aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfig`  <a name="cfn-sagemaker-dataqualityjobdefinition-networkconfig"></a>
Specifies networking configuration for the monitoring job.
*Required*: No
*Type*: [NetworkConfig](aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-dataqualityjobdefinition-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StoppingCondition`  <a name="cfn-sagemaker-dataqualityjobdefinition-stoppingcondition"></a>
A time limit for how long the monitoring job is allowed to run before stopping.
*Required*: No
*Type*: [StoppingCondition](aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-dataqualityjobdefinition-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-dataqualityjobdefinition-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-dataqualityjobdefinition-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-dataqualityjobdefinition-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the job definition.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-dataqualityjobdefinition-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-dataqualityjobdefinition-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when the job definition was created.

`JobDefinitionArn`  <a name="JobDefinitionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the job definition.

## Examples
<a name="aws-resource-sagemaker-dataqualityjobdefinition--examples"></a>

### SageMaker DataQualityJobDefinition Example
<a name="aws-resource-sagemaker-dataqualityjobdefinition--examples--SageMaker_DataQualityJobDefinition_Example"></a>

The following example creates a Data Quality monitoring job defintion.

#### JSON
<a name="aws-resource-sagemaker-dataqualityjobdefinition--examples--SageMaker_DataQualityJobDefinition_Example--json"></a>

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "Basic SageMaker Hosting entities to create a data quality job definition",
   "Mappings": {
      "RegionMap": {
         "us-west-2": {
            "MyModelImage": "123456789012.dkr.ecr.us-west-2.amazonaws.com/mymodel:latest"
         },
         "us-east-2": {
            "MyModelImage": "123456789012.dkr.ecr.us-east-2.amazonaws.com/mymodel:latest"
         },
         "us-east-1": {
            "MyModelImage": "123456789012.dkr.ecr.us-east-1.amazonaws.com/mymodel:latest"
         },
         "eu-west-1": {
            "MyModelImage": "123456789012.dkr.ecr.eu-west-1.amazonaws.com/mymodel:latest"
         },
         "ap-northeast-1": {
            "MyModelImage": "123456789012.dkr.ecr.ap-northeast-1.amazonaws.com/mymodel:latest"
         },
         "ap-northeast-2": {
            "MyModelImage": "123456789012.dkr.ecr.ap-northeast-2.amazonaws.com/mymodel:latest"
         },
         "ap-southeast-2": {
            "MyModelImage": "123456789012.dkr.ecr.ap-southeast-2.amazonaws.com/mymodel:latest"
         },
         "eu-central-1": {
            "MyModelImage": "123456789012.dkr.ecr.eu-central-1.amazonaws.com/mymodel:latest"
         }
      }
   },
   "Resources": {
      "Endpoint": {
         "Type": "AWS::SageMaker::Endpoint",
         "Properties": {
            "EndpointConfigName": {
            "Fn::GetAtt": [
              "EndpointConfigWithDataCapture",
              "EndpointConfigName"
             ]

            }
         }
      },
      "EndpointConfigWithDataCapture": {
         "Type": "AWS::SageMaker::EndpointConfig",
         "Properties": {
            "ProductionVariants": [
               {
                  "InitialInstanceCount": 1,
                  "InitialVariantWeight": 1,
                  "InstanceType": "ml.t2.large",
                  "ModelName": {
                     "Fn::GetAtt": [
                       "Model",
                       "ModelName"
                      ]

                },
                  "VariantName": {
                     "Fn::GetAtt": [
                       "Model",
                       "ModelName"
                      ]

                }
               }
            ],
            "DataCaptureConfig": {
               "EnableCapture": true,
               "InitialSamplingPercentage": 100,
               "DestinationS3Uri": "s3://bucket/prefix",
               "KmsKeyId": "kmskeyid",
               "CaptureOptions": [
                  {
                     "CaptureMode": "Input"
                  },
                  {
                     "CaptureMode": "Output"
                  }
               ],
               "CaptureContentTypeHeader": {
                  "CsvContentTypes": [
                     "text/csv"
                  ],
                  "JsonContentTypes": [
                     "appplication/json"
                  ]
               }
            }
         }
      },
      "Model": {
         "Type": "AWS::SageMaker::Model",
         "Properties": {
            "PrimaryContainer": {
               "Image": { "Fn::FindInMap": [
                  "RegionMap",
                  {"Ref": "AWS::Region"},
                  "MyModelImage"
                 ]
               }
            },
            "ExecutionRoleArn": {
                     "Fn::GetAtt": [
                       "ExecutionRole",
                       "Arn"
                      ]

                }
         }
      },
      "ExecutionRole": {
         "Type": "AWS::IAM::Role",
         "Properties": {
            "AssumeRolePolicyDocument": {
               "Version": "2012-10-17"		 	 	 ,
               "Statement": [
                  {
                     "Effect": "Allow",
                     "Principal": {
                        "Service": [
                           "sagemaker.amazonaws.com"
                        ]
                     },
                     "Action": [
                        "sts:AssumeRole"
                     ]
                  }
               ]
            },
            "Path": "/",
            "Policies": [
               {
                  "PolicyName": "root",
                  "PolicyDocument": {
                     "Version": "2012-10-17"		 	 	 ,
                     "Statement": [
                        {
                           "Effect": "Allow",
                           "Action": "*",
                           "Resource": "*"
                        }
                     ]
                  }
               }
            ]
         }
      },
      "JobDefinitionExecutionRole": {
         "Type": "AWS::IAM::Role",
         "Properties": {
            "AssumeRolePolicyDocument": {
               "Version": "2012-10-17"		 	 	 ,
               "Statement": [
                  {
                     "Effect": "Allow",
                     "Principal": {
                        "Service": [
                           "sagemaker.amazonaws.com"
                        ]
                     },
                     "Action": [
                        "sts:AssumeRole"
                     ]
                  }
               ]
            },
            "ManagedPolicyArns": [
               {
                  "Fn::Sub": "arn:${AWS::Partition}:iam::aws:policy/AmazonSageMakerFullAccess"
               },
               {
                  "Fn::Sub": "arn:${AWS::Partition}:iam::aws:policy/AmazonS3FullAccess"
               },
               {
                  "Fn::Sub": "arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
               }
            ]
         }
      },
      "DataQualityJobDefinition": {
         "Type": "AWS::SageMaker::DataQualityJobDefinition",
         "Properties": {
            "DataQualityAppSpecification": {
               "ImageUri": {
                  "Fn::Sub": "123456789012.dkr.ecr.${AWS::Partition}.amazonaws.com/sagemaker-model-monitor-analyzer:latest"
               }
            },
            "DataQualityJobInput": {
               "EndpointInput": {
                  "EndpointName": {
                     "Fn::GetAtt": [
                       "Endpoint",
                       "EndpointName"
                      ]

                },
                  "LocalPath": "/opt/ml/processing/endpointdata"
               }
            },
            "DataQualityJobOutputConfig": {
               "MonitoringOutputs": [
                  {
                     "S3Output": {
                        "LocalPath": "/opt/ml/processing/localpath",
                        "S3Uri": {
                           "Fn::Sub": "s3://data-quality-job-definition-${AWS::AccountId}/output"
                        }
                     }
                  }
               ]
            },
            "JobResources": {
               "ClusterConfig": {
                  "InstanceCount": 1,
                  "InstanceType": "ml.m5.large",
                  "VolumeSizeInGB": 50
               }
            },
            "RoleArn": null,
            "StoppingCondition": {
               "MaxRuntimeInSeconds": 2000
            }
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-sagemaker-dataqualityjobdefinition--examples--SageMaker_DataQualityJobDefinition_Example--yaml"></a>

```
---

AWSTemplateFormatVersion: '2010-09-09'
Description: Basic SageMaker Hosting entities to create a data quality job definition

Mappings:
  RegionMap:
    "us-west-2":
      "MyModelImage": "123456789012.dkr.ecr.us-west-2.amazonaws.com/mymodel:latest"
    "us-east-2":
      "MyModelImage": "123456789012.dkr.ecr.us-east-2.amazonaws.com/mymodel:latest"
    "us-east-1":
      "MyModelImage": "123456789012.dkr.ecr.us-east-1.amazonaws.com/mymodel:latest"
    "eu-west-1":
      "MyModelImage": "123456789012.dkr.ecr.eu-west-1.amazonaws.com/mymodel:latest"
    "ap-northeast-1":
      "MyModelImage": "123456789012.dkr.ecr.ap-northeast-1.amazonaws.com/mymodel:latest"
    "ap-northeast-2":
      "MyModelImage": "123456789012.dkr.ecr.ap-northeast-2.amazonaws.com/mymodel:latest"
    "ap-southeast-2":
      "MyModelImage": "123456789012.dkr.ecr.ap-southeast-2.amazonaws.com/mymodel:latest"
    "eu-central-1":
      "MyModelImage": "123456789012.dkr.ecr.eu-central-1.amazonaws.com/mymodel:latest"

Resources:
  Endpoint:
    Type: "AWS::SageMaker::Endpoint"
    Properties:
      EndpointConfigName:
        !GetAtt EndpointConfigWithDataCapture.EndpointConfigName

  EndpointConfigWithDataCapture:
    Type: "AWS::SageMaker::EndpointConfig"
    Properties:
      ProductionVariants:
        - InitialInstanceCount: 1
          InitialVariantWeight: 1.0
          InstanceType: ml.t2.large
          ModelName: !GetAtt Model.ModelName
          VariantName: !GetAtt Model.ModelName
      DataCaptureConfig:
        EnableCapture: true
        InitialSamplingPercentage: 100
        DestinationS3Uri: s3://bucket/prefix
        KmsKeyId: kmskeyid
        CaptureOptions:
          - CaptureMode: Input
          - CaptureMode: Output
        CaptureContentTypeHeader:
          CsvContentTypes:
            - "text/csv"
          JsonContentTypes:
            - "appplication/json"

  Model:
    Type: "AWS::SageMaker::Model"
    Properties:
      PrimaryContainer:
        Image: !FindInMap [RegionMap, !Ref "AWS::Region", "MyModelImage"]
      ExecutionRoleArn: !GetAtt ExecutionRole.Arn

  ExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "sagemaker.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Path: "/"
      Policies:
        -
          PolicyName: "root"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              -
                Effect: "Allow"
                Action: "*"
                Resource: "*"

  JobDefinitionExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "sagemaker.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      ManagedPolicyArns:
        - Fn::Sub: "arn:${AWS::Partition}:iam::aws:policy/AmazonSageMakerFullAccess"
        - Fn::Sub: "arn:${AWS::Partition}:iam::aws:policy/AmazonS3FullAccess"
        - Fn::Sub: "arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"

  DataQualityJobDefinition:
    Type: AWS::SageMaker::DataQualityJobDefinition
    Properties:
      DataQualityAppSpecification:
        ImageUri:
          Fn::Sub: "123456789012.dkr.ecr.${AWS::Partition}.amazonaws.com/sagemaker-model-monitor-analyzer:latest"
      DataQualityJobInput:
        EndpointInput:
          EndpointName: !GetAtt Endpoint.EndpointName
          LocalPath: "/opt/ml/processing/endpointdata"
      DataQualityJobOutputConfig:
        MonitoringOutputs:
          - S3Output:
              LocalPath: "/opt/ml/processing/localpath"
              S3Uri:
                Fn::Sub: "s3://data-quality-job-definition-${AWS::AccountId}/output"
      JobResources:
        ClusterConfig:
          InstanceCount: 1
          InstanceType: ml.m5.large
          VolumeSizeInGB: 50
      RoleArn: !GetAtt JobDefinitionExecutionRole.Arn
      StoppingCondition:
        MaxRuntimeInSeconds: 2000
```
