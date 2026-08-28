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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
