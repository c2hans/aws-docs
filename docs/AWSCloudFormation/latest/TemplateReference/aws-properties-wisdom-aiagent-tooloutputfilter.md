---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tooloutputfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolOutputFilter
<a name="aws-properties-wisdom-aiagent-tooloutputfilter"></a>

Filter configuration for tool output.

## Syntax
<a name="aws-properties-wisdom-aiagent-tooloutputfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tooloutputfilter-syntax.json"></a>

```
{
  "[JsonPath](#cfn-wisdom-aiagent-tooloutputfilter-jsonpath)" : {{String}},
  "[OutputConfiguration](#cfn-wisdom-aiagent-tooloutputfilter-outputconfiguration)" : {{ToolOutputConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tooloutputfilter-syntax.yaml"></a>

```
  [JsonPath](#cfn-wisdom-aiagent-tooloutputfilter-jsonpath): {{String}}
  [OutputConfiguration](#cfn-wisdom-aiagent-tooloutputfilter-outputconfiguration): {{
    ToolOutputConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tooloutputfilter-properties"></a>

`JsonPath`  <a name="cfn-wisdom-aiagent-tooloutputfilter-jsonpath"></a>
The JSON path for filtering tool output.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputConfiguration`  <a name="cfn-wisdom-aiagent-tooloutputfilter-outputconfiguration"></a>
The output configuration for the filter.
*Required*: No
*Type*: [ToolOutputConfiguration](aws-properties-wisdom-aiagent-tooloutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
