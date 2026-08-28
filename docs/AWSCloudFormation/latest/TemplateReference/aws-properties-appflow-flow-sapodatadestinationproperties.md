---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-sapodatadestinationproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow SAPODataDestinationProperties
<a name="aws-properties-appflow-flow-sapodatadestinationproperties"></a>

The properties that are applied when using SAPOData as a flow destination

## Syntax
<a name="aws-properties-appflow-flow-sapodatadestinationproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-sapodatadestinationproperties-syntax.json"></a>

```
{
  "[ErrorHandlingConfig](#cfn-appflow-flow-sapodatadestinationproperties-errorhandlingconfig)" : {{ErrorHandlingConfig}},
  "[IdFieldNames](#cfn-appflow-flow-sapodatadestinationproperties-idfieldnames)" : {{[ String, ... ]}},
  "[ObjectPath](#cfn-appflow-flow-sapodatadestinationproperties-objectpath)" : {{String}},
  "[SuccessResponseHandlingConfig](#cfn-appflow-flow-sapodatadestinationproperties-successresponsehandlingconfig)" : {{SuccessResponseHandlingConfig}},
  "[WriteOperationType](#cfn-appflow-flow-sapodatadestinationproperties-writeoperationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-sapodatadestinationproperties-syntax.yaml"></a>

```
  [ErrorHandlingConfig](#cfn-appflow-flow-sapodatadestinationproperties-errorhandlingconfig): {{
    ErrorHandlingConfig}}
  [IdFieldNames](#cfn-appflow-flow-sapodatadestinationproperties-idfieldnames): {{
    - String}}
  [ObjectPath](#cfn-appflow-flow-sapodatadestinationproperties-objectpath): {{String}}
  [SuccessResponseHandlingConfig](#cfn-appflow-flow-sapodatadestinationproperties-successresponsehandlingconfig): {{
    SuccessResponseHandlingConfig}}
  [WriteOperationType](#cfn-appflow-flow-sapodatadestinationproperties-writeoperationtype): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-sapodatadestinationproperties-properties"></a>

`ErrorHandlingConfig`  <a name="cfn-appflow-flow-sapodatadestinationproperties-errorhandlingconfig"></a>
 The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.
*Required*: No
*Type*: [ErrorHandlingConfig](aws-properties-appflow-flow-errorhandlingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdFieldNames`  <a name="cfn-appflow-flow-sapodatadestinationproperties-idfieldnames"></a>
 A list of field names that can be used as an ID field when performing a write operation.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectPath`  <a name="cfn-appflow-flow-sapodatadestinationproperties-objectpath"></a>
The object path specified in the SAPOData flow destination.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessResponseHandlingConfig`  <a name="cfn-appflow-flow-sapodatadestinationproperties-successresponsehandlingconfig"></a>
Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.
For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.
*Required*: No
*Type*: [SuccessResponseHandlingConfig](aws-properties-appflow-flow-successresponsehandlingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteOperationType`  <a name="cfn-appflow-flow-sapodatadestinationproperties-writeoperationtype"></a>
 The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.
*Required*: No
*Type*: String
*Allowed values*: `INSERT | UPSERT | UPDATE | DELETE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
