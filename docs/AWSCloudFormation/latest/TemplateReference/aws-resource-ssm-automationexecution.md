---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-automationexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::AutomationExecution
<a name="aws-resource-ssm-automationexecution"></a>

Detailed information about the current state of an individual Automation execution.

## Syntax
<a name="aws-resource-ssm-automationexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-automationexecution-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::AutomationExecution",
  "Properties" : {
      "[DocumentName](#cfn-ssm-automationexecution-documentname)" : {{String}},
      "[Tags](#cfn-ssm-automationexecution-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssm-automationexecution-syntax.yaml"></a>

```
Type: AWS::SSM::AutomationExecution
Properties:
  [DocumentName](#cfn-ssm-automationexecution-documentname): {{String}}
  [Tags](#cfn-ssm-automationexecution-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ssm-automationexecution-properties"></a>

`DocumentName`  <a name="cfn-ssm-automationexecution-documentname"></a>
The name of the Automation runbook used during the execution.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-.]{3,128}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ssm-automationexecution-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssm-automationexecution-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ssm-automationexecution-return-values"></a>

### Ref
<a name="aws-resource-ssm-automationexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-automationexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-automationexecution-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`AutomationExecutionId`  <a name="AutomationExecutionId-fn::getatt"></a>
The execution ID.

`AutomationExecutionStatus`  <a name="AutomationExecutionStatus-fn::getatt"></a>
The execution status of the Automation.

`DocumentVersion`  <a name="DocumentVersion-fn::getatt"></a>
The version of the document to use during execution.

`ExecutedBy`  <a name="ExecutedBy-fn::getatt"></a>
The Amazon Resource Name (ARN) of the user who ran the automation.

`ExecutionStartTime`  <a name="ExecutionStartTime-fn::getatt"></a>
The time the execution started.

`Mode`  <a name="Mode-fn::getatt"></a>
The automation execution mode.
