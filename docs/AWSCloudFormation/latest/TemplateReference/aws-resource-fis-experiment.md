---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fis-experiment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::Experiment
<a name="aws-resource-fis-experiment"></a>

Describes an experiment.

## Syntax
<a name="aws-resource-fis-experiment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fis-experiment-syntax.json"></a>

```
{
  "Type" : "AWS::FIS::Experiment",
  "Properties" : {
      "[ExperimentOptions](#cfn-fis-experiment-experimentoptions)" : {{ExperimentOptions}},
      "[ExperimentTemplateId](#cfn-fis-experiment-experimenttemplateid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-fis-experiment-syntax.yaml"></a>

```
Type: AWS::FIS::Experiment
Properties:
  [ExperimentOptions](#cfn-fis-experiment-experimentoptions): {{
    ExperimentOptions}}
  [ExperimentTemplateId](#cfn-fis-experiment-experimenttemplateid): {{String}}
```

## Properties
<a name="aws-resource-fis-experiment-properties"></a>

`ExperimentOptions`  <a name="cfn-fis-experiment-experimentoptions"></a>
The experiment options for the experiment.
*Required*: No
*Type*: [ExperimentOptions](aws-properties-fis-experiment-experimentoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExperimentTemplateId`  <a name="cfn-fis-experiment-experimenttemplateid"></a>
The ID of the experiment template.
*Required*: No
*Type*: String
*Pattern*: `^[\S]+$`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-fis-experiment-return-values"></a>

### Ref
<a name="aws-resource-fis-experiment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fis-experiment-return-values-fn--getatt"></a>

####
<a name="aws-resource-fis-experiment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the experiment.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time that the experiment was created.

`EndTime`  <a name="EndTime-fn::getatt"></a>
The time that the experiment ended.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the experiment.

`RoleArn`  <a name="RoleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of an IAM role that grants the AWS FIS service permission to perform service actions on your behalf.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time that the experiment started.

`Tags`  <a name="Tags-fn::getatt"></a>
The tags for the experiment.
