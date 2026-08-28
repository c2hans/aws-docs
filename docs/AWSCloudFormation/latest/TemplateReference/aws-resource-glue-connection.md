---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection
<a name="aws-resource-glue-connection"></a>

The `AWS::Glue::Connection` resource specifies an AWS Glue connection to a data source. For more information, see [Adding a Connection to Your Data Store](https://docs.aws.amazon.com/glue/latest/dg/populate-add-connection.html) and [Connection Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-Connection) in the *AWS Glue Developer Guide*.

## Syntax
<a name="aws-resource-glue-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-connection-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::Connection",
  "Properties" : {
      "[CatalogId](#cfn-glue-connection-catalogid)" : {{String}},
      "[ConnectionInput](#cfn-glue-connection-connectioninput)" : {{ConnectionInput}},
      "[Tags](#cfn-glue-connection-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}}
    }
}
```

### YAML
<a name="aws-resource-glue-connection-syntax.yaml"></a>

```
Type: AWS::Glue::Connection
Properties:
  [CatalogId](#cfn-glue-connection-catalogid): {{String}}
  [ConnectionInput](#cfn-glue-connection-connectioninput): {{
    ConnectionInput}}
  [Tags](#cfn-glue-connection-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
```

## Properties
<a name="aws-resource-glue-connection-properties"></a>

`CatalogId`  <a name="cfn-glue-connection-catalogid"></a>
The ID of the data catalog to create the catalog object in. Currently, this should be the AWS account ID.
To specify the account ID, you can use the `Ref` intrinsic function with the `AWS::AccountId` pseudo parameter. For example: `!Ref AWS::AccountId`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectionInput`  <a name="cfn-glue-connection-connectioninput"></a>
The connection that you want to create.
*Required*: Yes
*Type*: [ConnectionInput](aws-properties-glue-connection-connectioninput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-glue-connection-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-connection-return-values"></a>

### Ref
<a name="aws-resource-glue-connection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the connection name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-glue-connection-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-connection-return-values-fn--getatt-fn--getatt"></a>

`Name`  <a name="Name-fn::getatt"></a>
The name of the connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
