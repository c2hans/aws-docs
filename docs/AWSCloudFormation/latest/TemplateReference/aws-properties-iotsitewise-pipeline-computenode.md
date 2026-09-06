---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-pipeline-computenode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Pipeline ComputeNode
<a name="aws-properties-iotsitewise-pipeline-computenode"></a>

<a name="aws-properties-iotsitewise-pipeline-computenode-description"></a>The `ComputeNode` property type specifies Property description not available. for an [AWS::IoTSiteWise::Pipeline](aws-resource-iotsitewise-pipeline.md).

## Syntax
<a name="aws-properties-iotsitewise-pipeline-computenode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-pipeline-computenode-syntax.json"></a>

```
{
  "[ComputeNodeName](#cfn-iotsitewise-pipeline-computenode-computenodename)" : {{String}},
  "[DependsOn](#cfn-iotsitewise-pipeline-computenode-dependson)" : {{[ String, ... ]}},
  "[EnvironmentVariables](#cfn-iotsitewise-pipeline-computenode-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TaskName](#cfn-iotsitewise-pipeline-computenode-taskname)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-pipeline-computenode-syntax.yaml"></a>

```
  [ComputeNodeName](#cfn-iotsitewise-pipeline-computenode-computenodename): {{String}}
  [DependsOn](#cfn-iotsitewise-pipeline-computenode-dependson): {{
    - String}}
  [EnvironmentVariables](#cfn-iotsitewise-pipeline-computenode-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [TaskName](#cfn-iotsitewise-pipeline-computenode-taskname): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-pipeline-computenode-properties"></a>

`ComputeNodeName`  <a name="cfn-iotsitewise-pipeline-computenode-computenodename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependsOn`  <a name="cfn-iotsitewise-pipeline-computenode-dependson"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-iotsitewise-pipeline-computenode-environmentvariables"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskName`  <a name="cfn-iotsitewise-pipeline-computenode-taskname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
