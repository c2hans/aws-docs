---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-pipeline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Pipeline
<a name="aws-resource-iotsitewise-pipeline"></a>

<a name="aws-resource-iotsitewise-pipeline-description"></a>The `AWS::IoTSiteWise::Pipeline` resource Property description not available. for IoTSiteWise.

## Syntax
<a name="aws-resource-iotsitewise-pipeline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-pipeline-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Pipeline",
  "Properties" : {
      "[Computations](#cfn-iotsitewise-pipeline-computations)" : {{[ ComputeNode, ... ]}},
      "[Description](#cfn-iotsitewise-pipeline-description)" : {{String}},
      "[EnvironmentVariables](#cfn-iotsitewise-pipeline-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
      "[PipelineName](#cfn-iotsitewise-pipeline-pipelinename)" : {{String}},
      "[Tags](#cfn-iotsitewise-pipeline-tags)" : {{[ Tag, ... ]}},
      "[WorkspaceName](#cfn-iotsitewise-pipeline-workspacename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-pipeline-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Pipeline
Properties:
  [Computations](#cfn-iotsitewise-pipeline-computations): {{
    - ComputeNode}}
  [Description](#cfn-iotsitewise-pipeline-description): {{String}}
  [EnvironmentVariables](#cfn-iotsitewise-pipeline-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [PipelineName](#cfn-iotsitewise-pipeline-pipelinename): {{String}}
  [Tags](#cfn-iotsitewise-pipeline-tags): {{
    - Tag}}
  [WorkspaceName](#cfn-iotsitewise-pipeline-workspacename): {{String}}
```

## Properties
<a name="aws-resource-iotsitewise-pipeline-properties"></a>

`Computations`  <a name="cfn-iotsitewise-pipeline-computations"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [ComputeNode](aws-properties-iotsitewise-pipeline-computenode.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iotsitewise-pipeline-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-iotsitewise-pipeline-environmentvariables"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineName`  <a name="cfn-iotsitewise-pipeline-pipelinename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotsitewise-pipeline-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-pipeline-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceName`  <a name="cfn-iotsitewise-pipeline-workspacename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotsitewise-pipeline-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-pipeline-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iotsitewise-pipeline-return-values-fn--getatt"></a>

####
<a name="aws-resource-iotsitewise-pipeline-return-values-fn--getatt-fn--getatt"></a>

`PipelineArn`  <a name="PipelineArn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
