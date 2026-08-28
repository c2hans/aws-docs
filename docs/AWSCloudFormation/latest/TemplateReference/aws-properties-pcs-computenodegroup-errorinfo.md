---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-errorinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup ErrorInfo
<a name="aws-properties-pcs-computenodegroup-errorinfo"></a>

An error that occurred during resource creation.

## Syntax
<a name="aws-properties-pcs-computenodegroup-errorinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-errorinfo-syntax.json"></a>

```
{
  "[Code](#cfn-pcs-computenodegroup-errorinfo-code)" : {{String}},
  "[Message](#cfn-pcs-computenodegroup-errorinfo-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-errorinfo-syntax.yaml"></a>

```
  [Code](#cfn-pcs-computenodegroup-errorinfo-code): {{String}}
  [Message](#cfn-pcs-computenodegroup-errorinfo-message): {{String}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-errorinfo-properties"></a>

`Code`  <a name="cfn-pcs-computenodegroup-errorinfo-code"></a>
The short-form error code.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-pcs-computenodegroup-errorinfo-message"></a>
The detailed error information.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
