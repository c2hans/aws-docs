---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-queue-errorinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Queue ErrorInfo
<a name="aws-properties-pcs-queue-errorinfo"></a>

An error that occurred during resource creation.

## Syntax
<a name="aws-properties-pcs-queue-errorinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-queue-errorinfo-syntax.json"></a>

```
{
  "[Code](#cfn-pcs-queue-errorinfo-code)" : {{String}},
  "[Message](#cfn-pcs-queue-errorinfo-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-queue-errorinfo-syntax.yaml"></a>

```
  [Code](#cfn-pcs-queue-errorinfo-code): {{String}}
  [Message](#cfn-pcs-queue-errorinfo-message): {{String}}
```

## Properties
<a name="aws-properties-pcs-queue-errorinfo-properties"></a>

`Code`  <a name="cfn-pcs-queue-errorinfo-code"></a>
The short-form error code.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-pcs-queue-errorinfo-message"></a>
The detailed error information.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
