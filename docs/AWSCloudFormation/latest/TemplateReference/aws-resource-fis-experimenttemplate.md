---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fis-experimenttemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate
<a name="aws-resource-fis-experimenttemplate"></a>

Specifies an experiment template.

An experiment template includes the following components:
+ **Targets**: A target can be a specific resource in your AWS environment, or one or more resources that match criteria that you specify, for example, resources that have specific tags.
+ **Actions**: The actions to carry out on the target. You can specify multiple actions, the duration of each action, and when to start each action during an experiment.
+ **Stop conditions**: If a stop condition is triggered while an experiment is running, the experiment is automatically stopped. You can define a stop condition as a CloudWatch alarm.

For more information, see [Experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) in the *AWS Fault Injection Service User Guide*.

## Syntax
<a name="aws-resource-fis-experimenttemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fis-experimenttemplate-syntax.json"></a>

```
{
  "Type" : "AWS::FIS::ExperimentTemplate",
  "Properties" : {
      "[Actions](#cfn-fis-experimenttemplate-actions)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Description](#cfn-fis-experimenttemplate-description)" : {{String}},
      "[ExperimentOptions](#cfn-fis-experimenttemplate-experimentoptions)" : {{ExperimentTemplateExperimentOptions}},
      "[ExperimentReportConfiguration](#cfn-fis-experimenttemplate-experimentreportconfiguration)" : {{ExperimentTemplateExperimentReportConfiguration}},
      "[LogConfiguration](#cfn-fis-experimenttemplate-logconfiguration)" : {{ExperimentTemplateLogConfiguration}},
      "[RoleArn](#cfn-fis-experimenttemplate-rolearn)" : {{String}},
      "[StopConditions](#cfn-fis-experimenttemplate-stopconditions)" : {{[ ExperimentTemplateStopCondition, ... ]}},
      "[Tags](#cfn-fis-experimenttemplate-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Targets](#cfn-fis-experimenttemplate-targets)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-fis-experimenttemplate-syntax.yaml"></a>

```
Type: AWS::FIS::ExperimentTemplate
Properties:
  [Actions](#cfn-fis-experimenttemplate-actions): {{
    {{Key}}: {{Value}}}}
  [Description](#cfn-fis-experimenttemplate-description): {{String}}
  [ExperimentOptions](#cfn-fis-experimenttemplate-experimentoptions): {{
    ExperimentTemplateExperimentOptions}}
  [ExperimentReportConfiguration](#cfn-fis-experimenttemplate-experimentreportconfiguration): {{
    ExperimentTemplateExperimentReportConfiguration}}
  [LogConfiguration](#cfn-fis-experimenttemplate-logconfiguration): {{
    ExperimentTemplateLogConfiguration}}
  [RoleArn](#cfn-fis-experimenttemplate-rolearn): {{String}}
  [StopConditions](#cfn-fis-experimenttemplate-stopconditions): {{
    - ExperimentTemplateStopCondition}}
  [Tags](#cfn-fis-experimenttemplate-tags): {{
    {{Key}}: {{Value}}}}
  [Targets](#cfn-fis-experimenttemplate-targets): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-fis-experimenttemplate-properties"></a>

`Actions`  <a name="cfn-fis-experimenttemplate-actions"></a>
The actions for the experiment.
*Required*: No
*Type*: Object of [ExperimentTemplateAction](aws-properties-fis-experimenttemplate-experimenttemplateaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-fis-experimenttemplate-description"></a>
The description for the experiment template.
*Required*: Yes
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExperimentOptions`  <a name="cfn-fis-experimenttemplate-experimentoptions"></a>
The experiment options for an experiment template.
*Required*: No
*Type*: [ExperimentTemplateExperimentOptions](aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExperimentReportConfiguration`  <a name="cfn-fis-experimenttemplate-experimentreportconfiguration"></a>
Describes the report configuration for the experiment template.
*Required*: No
*Type*: [ExperimentTemplateExperimentReportConfiguration](aws-properties-fis-experimenttemplate-experimenttemplateexperimentreportconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-fis-experimenttemplate-logconfiguration"></a>
The configuration for experiment logging.
*Required*: No
*Type*: [ExperimentTemplateLogConfiguration](aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-fis-experimenttemplate-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role.
*Required*: Yes
*Type*: String
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StopConditions`  <a name="cfn-fis-experimenttemplate-stopconditions"></a>
The stop conditions for the experiment.
*Required*: Yes
*Type*: Array of [ExperimentTemplateStopCondition](aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-fis-experimenttemplate-tags"></a>
The tags for the experiment template.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,128}`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-fis-experimenttemplate-targets"></a>
The targets for the experiment.
*Required*: Yes
*Type*: Object of [ExperimentTemplateTarget](aws-properties-fis-experimenttemplate-experimenttemplatetarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fis-experimenttemplate-return-values"></a>

### Ref
<a name="aws-resource-fis-experimenttemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the experiment template ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-fis-experimenttemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-fis-experimenttemplate-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the experiment template.

## Examples
<a name="aws-resource-fis-experimenttemplate--examples"></a>

### Stop and start an instance based on a tag
<a name="aws-resource-fis-experimenttemplate--examples--Stop_and_start_an_instance_based_on_a_tag"></a>

The following example creates an experiment template that stops and starts one instance with the tag env=prod, chosen at random.

#### YAML
<a name="aws-resource-fis-experimenttemplate--examples--Stop_and_start_an_instance_based_on_a_tag--yaml"></a>

```
Resources:
  ExperimentTemplate:
    Type: 'AWS::FIS::ExperimentTemplate'
    Properties:
      Description: 'stop an instance based on a tag'
      Actions:
        stopInstances:
          ActionId: 'aws:ec2:stop-instances'
          Parameters:
            startInstancesAfterDuration: 'PT2M'
          Targets:
            Instances: oneRandomInstance
      Targets:
        oneRandomInstance:
          ResourceTags:
            'env': 'prod'
          ResourceType: 'aws:ec2:instance'
          SelectionMode: 'COUNT(1)'
      StopConditions:
        - Source: 'none'
      Tags:
        Name: 'fisStopInstances'
      RoleArn: !GetAtt FISRole.Arn
  FISRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Effect: Allow
            Principal:
              Service: 'fis.amazonaws.com'
            Action: 'sts:AssumeRole'
      Policies:
        - PolicyName: 'FISRoleEC2Actions'
          PolicyDocument:
            Version: '2012-10-17		 	 	 '
            Statement:
              - Effect: Allow
                Action:
                  - 'ec2:RebootInstances'
                  - 'ec2:StopInstances'
                  - 'ec2:StartInstances'
                  - 'ec2:TerminateInstances'
                Resource: 'arn:aws:ec2:*:*:instance/*'
```

#### JSON
<a name="aws-resource-fis-experimenttemplate--examples--Stop_and_start_an_instance_based_on_a_tag--json"></a>

```
{
  "Resources": {
    "ExperimentTemplate": {
      "Type": "AWS::FIS::ExperimentTemplate",
      "DeletionPolicy": "Retain",
      "Properties": {
        "Description": "stop an instance based on a tag",
        "Actions": {
          "stopInstances": {
            "ActionId": "aws:ec2:stop-instances",
            "Parameters": {
              "startInstancesAfterDuration": "PT2M"
            },
            "Targets": {
              "Instances": "oneRandomInstance"
            }
          }
        },
        "Targets": {
          "oneRandomInstance": {
            "ResourceTags": {
              "env": "prod"
            },
            "ResourceType": "aws:ec2:instance",
            "SelectionMode": "COUNT(1)"
          }
        },
        "StopConditions": [
          {
            "Source": "none"
          }
        ],
        "Tags": {
          "Name": "fisStopInstancesJson"
        },
        "RoleArn": {
          "Fn::GetAtt": ["FISRole", "Arn"]
        }
      }
    },
    "FISRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                  "Service": "fis.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
          ]
        },
        "Policies": [
          {
            "PolicyName": "FISRoleEC2Actions",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Action": [
                    "ec2:RebootInstances",
                    "ec2:StopInstances",
                    "ec2:StartInstances",
                    "ec2:TerminateInstances"
                  ],
                  "Resource": "arn:aws:ec2:*:*:instance/*"
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```
