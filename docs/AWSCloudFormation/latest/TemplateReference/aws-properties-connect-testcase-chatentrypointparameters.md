---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-testcase-chatentrypointparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TestCase ChatEntryPointParameters
<a name="aws-properties-connect-testcase-chatentrypointparameters"></a>

Parameters for initiating a chat test.

## Syntax
<a name="aws-properties-connect-testcase-chatentrypointparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-testcase-chatentrypointparameters-syntax.json"></a>

```
{
  "[FlowId](#cfn-connect-testcase-chatentrypointparameters-flowid)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-testcase-chatentrypointparameters-syntax.yaml"></a>

```
  [FlowId](#cfn-connect-testcase-chatentrypointparameters-flowid): {{String}}
```

## Properties
<a name="aws-properties-connect-testcase-chatentrypointparameters-properties"></a>

`FlowId`  <a name="cfn-connect-testcase-chatentrypointparameters-flowid"></a>
The flow identifier for the test.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
