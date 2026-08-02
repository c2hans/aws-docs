---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-maprun.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::MapRun
<a name="aws-resource-stepfunctions-maprun"></a>

<a name="aws-resource-stepfunctions-maprun-description"></a>The `AWS::StepFunctions::MapRun` resource Property description not available. for StepFunctions.

## Syntax
<a name="aws-resource-stepfunctions-maprun-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-stepfunctions-maprun-syntax.json"></a>

```
{
  "Type" : "AWS::StepFunctions::MapRun",
  "Properties" : {
      "[ExecutionArn](#cfn-stepfunctions-maprun-executionarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-stepfunctions-maprun-syntax.yaml"></a>

```
Type: AWS::StepFunctions::MapRun
Properties:
  [ExecutionArn](#cfn-stepfunctions-maprun-executionarn): {{String}}
```

## Properties
<a name="aws-resource-stepfunctions-maprun-properties"></a>

`ExecutionArn`  <a name="cfn-stepfunctions-maprun-executionarn"></a>
The `executionArn` of the execution from which the Map Run was started.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-stepfunctions-maprun-return-values"></a>

### Ref
<a name="aws-resource-stepfunctions-maprun-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-stepfunctions-maprun-return-values-fn--getatt"></a>

####
<a name="aws-resource-stepfunctions-maprun-return-values-fn--getatt-fn--getatt"></a>

`MapRunArn`  <a name="MapRunArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Map Run.

`MaxConcurrency`  <a name="MaxConcurrency-fn::getatt"></a>
Property description not available.

`StartDate`  <a name="StartDate-fn::getatt"></a>
The date on which the Map Run started.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`StopDate`  <a name="StopDate-fn::getatt"></a>
The date on which the Map Run stopped.

`ToleratedFailureCount`  <a name="ToleratedFailureCount-fn::getatt"></a>
Property description not available.

`ToleratedFailurePercentage`  <a name="ToleratedFailurePercentage-fn::getatt"></a>
Property description not available.
