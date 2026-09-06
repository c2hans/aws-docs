---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-task.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Task
<a name="aws-resource-iotsitewise-task"></a>

<a name="aws-resource-iotsitewise-task-description"></a>The `AWS::IoTSiteWise::Task` resource Property description not available. for IoTSiteWise.

## Syntax
<a name="aws-resource-iotsitewise-task-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-task-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Task",
  "Properties" : {
      "[Description](#cfn-iotsitewise-task-description)" : {{String}},
      "[Tags](#cfn-iotsitewise-task-tags)" : {{[ Tag, ... ]}},
      "[TaskConfiguration](#cfn-iotsitewise-task-taskconfiguration)" : {{TaskConfiguration}},
      "[TaskName](#cfn-iotsitewise-task-taskname)" : {{String}},
      "[WorkspaceName](#cfn-iotsitewise-task-workspacename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-task-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Task
Properties:
  [Description](#cfn-iotsitewise-task-description): {{String}}
  [Tags](#cfn-iotsitewise-task-tags): {{
    - Tag}}
  [TaskConfiguration](#cfn-iotsitewise-task-taskconfiguration): {{
    TaskConfiguration}}
  [TaskName](#cfn-iotsitewise-task-taskname): {{String}}
  [WorkspaceName](#cfn-iotsitewise-task-workspacename): {{String}}
```

## Properties
<a name="aws-resource-iotsitewise-task-properties"></a>

`Description`  <a name="cfn-iotsitewise-task-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotsitewise-task-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-task-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskConfiguration`  <a name="cfn-iotsitewise-task-taskconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [TaskConfiguration](aws-properties-iotsitewise-task-taskconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskName`  <a name="cfn-iotsitewise-task-taskname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkspaceName`  <a name="cfn-iotsitewise-task-workspacename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotsitewise-task-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-task-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iotsitewise-task-return-values-fn--getatt"></a>

####
<a name="aws-resource-iotsitewise-task-return-values-fn--getatt-fn--getatt"></a>

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`TaskArn`  <a name="TaskArn-fn::getatt"></a>
Property description not available.
