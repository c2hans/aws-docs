---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-successresponsehandlingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow SuccessResponseHandlingConfig
<a name="aws-properties-appflow-flow-successresponsehandlingconfig"></a>

Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.

For example, this setting would determine where to write the response from the destination connector upon a successful insert operation.

## Syntax
<a name="aws-properties-appflow-flow-successresponsehandlingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-successresponsehandlingconfig-syntax.json"></a>

```
{
  "[BucketName](#cfn-appflow-flow-successresponsehandlingconfig-bucketname)" : {{String}},
  "[BucketPrefix](#cfn-appflow-flow-successresponsehandlingconfig-bucketprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-successresponsehandlingconfig-syntax.yaml"></a>

```
  [BucketName](#cfn-appflow-flow-successresponsehandlingconfig-bucketname): {{String}}
  [BucketPrefix](#cfn-appflow-flow-successresponsehandlingconfig-bucketprefix): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-successresponsehandlingconfig-properties"></a>

`BucketName`  <a name="cfn-appflow-flow-successresponsehandlingconfig-bucketname"></a>
The name of the Amazon S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketPrefix`  <a name="cfn-appflow-flow-successresponsehandlingconfig-bucketprefix"></a>
The Amazon S3 bucket prefix.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
