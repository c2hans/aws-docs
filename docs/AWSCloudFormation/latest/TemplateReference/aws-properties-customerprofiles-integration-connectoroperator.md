---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-connectoroperator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration ConnectorOperator
<a name="aws-properties-customerprofiles-integration-connectoroperator"></a>

The operation to be performed on the provided source fields.

## Syntax
<a name="aws-properties-customerprofiles-integration-connectoroperator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-connectoroperator-syntax.json"></a>

```
{
  "[Marketo](#cfn-customerprofiles-integration-connectoroperator-marketo)" : {{String}},
  "[S3](#cfn-customerprofiles-integration-connectoroperator-s3)" : {{String}},
  "[Salesforce](#cfn-customerprofiles-integration-connectoroperator-salesforce)" : {{String}},
  "[ServiceNow](#cfn-customerprofiles-integration-connectoroperator-servicenow)" : {{String}},
  "[Zendesk](#cfn-customerprofiles-integration-connectoroperator-zendesk)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-connectoroperator-syntax.yaml"></a>

```
  [Marketo](#cfn-customerprofiles-integration-connectoroperator-marketo): {{String}}
  [S3](#cfn-customerprofiles-integration-connectoroperator-s3): {{String}}
  [Salesforce](#cfn-customerprofiles-integration-connectoroperator-salesforce): {{String}}
  [ServiceNow](#cfn-customerprofiles-integration-connectoroperator-servicenow): {{String}}
  [Zendesk](#cfn-customerprofiles-integration-connectoroperator-zendesk): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-connectoroperator-properties"></a>

`Marketo`  <a name="cfn-customerprofiles-integration-connectoroperator-marketo"></a>
The operation to be performed on the provided Marketo source fields.
*Required*: No
*Type*: String
*Allowed values*: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-customerprofiles-integration-connectoroperator-s3"></a>
The operation to be performed on the provided Amazon S3 source fields.
*Required*: No
*Type*: String
*Allowed values*: `PROJECTION | LESS_THAN | GREATER_THAN | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Salesforce`  <a name="cfn-customerprofiles-integration-connectoroperator-salesforce"></a>
The operation to be performed on the provided Salesforce source fields.
*Required*: No
*Type*: String
*Allowed values*: `PROJECTION | LESS_THAN | GREATER_THAN | CONTAINS | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNow`  <a name="cfn-customerprofiles-integration-connectoroperator-servicenow"></a>
The operation to be performed on the provided ServiceNow source fields.
*Required*: No
*Type*: String
*Allowed values*: `PROJECTION | LESS_THAN | GREATER_THAN | CONTAINS | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Zendesk`  <a name="cfn-customerprofiles-integration-connectoroperator-zendesk"></a>
The operation to be performed on the provided Zendesk source fields.
*Required*: No
*Type*: String
*Allowed values*: `PROJECTION | GREATER_THAN | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
