---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-dataconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType DataConnector
<a name="aws-properties-iottwinmaker-componenttype-dataconnector"></a>

The data connector.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-dataconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-dataconnector-syntax.json"></a>

```
{
  "[IsNative](#cfn-iottwinmaker-componenttype-dataconnector-isnative)" : {{Boolean}},
  "[Lambda](#cfn-iottwinmaker-componenttype-dataconnector-lambda)" : {{LambdaFunction}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-dataconnector-syntax.yaml"></a>

```
  [IsNative](#cfn-iottwinmaker-componenttype-dataconnector-isnative): {{Boolean}}
  [Lambda](#cfn-iottwinmaker-componenttype-dataconnector-lambda): {{
    LambdaFunction}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-dataconnector-properties"></a>

`IsNative`  <a name="cfn-iottwinmaker-componenttype-dataconnector-isnative"></a>
A boolean value that specifies whether the data connector is native to IoT TwinMaker.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lambda`  <a name="cfn-iottwinmaker-componenttype-dataconnector-lambda"></a>
The Lambda function associated with the data connector.
*Required*: No
*Type*: [LambdaFunction](aws-properties-iottwinmaker-componenttype-lambdafunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
