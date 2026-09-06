---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-datatransferapi.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow DataTransferApi
<a name="aws-properties-appflow-flow-datatransferapi"></a>

The API of the connector application that Amazon AppFlow uses to transfer your data.

## Syntax
<a name="aws-properties-appflow-flow-datatransferapi-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-datatransferapi-syntax.json"></a>

```
{
  "[Name](#cfn-appflow-flow-datatransferapi-name)" : {{String}},
  "[Type](#cfn-appflow-flow-datatransferapi-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-datatransferapi-syntax.yaml"></a>

```
  [Name](#cfn-appflow-flow-datatransferapi-name): {{String}}
  [Type](#cfn-appflow-flow-datatransferapi-type): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-datatransferapi-properties"></a>

`Name`  <a name="cfn-appflow-flow-datatransferapi-name"></a>
The name of the connector application API.
*Required*: Yes
*Type*: String
*Pattern*: `[\w/-]+`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-appflow-flow-datatransferapi-type"></a>
You can specify one of the following types:
AUTOMATIC
The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers.
SYNC
A synchronous API. This type of API optimizes a flow for small to medium-sized datasets.
ASYNC
An asynchronous API. This type of API optimizes a flow for large datasets.
*Required*: Yes
*Type*: String
*Allowed values*: `SYNC | ASYNC | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
