---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-taskaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule TaskAction
<a name="aws-properties-connect-rule-taskaction"></a>

Information about the task action. This field is required if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate`

## Syntax
<a name="aws-properties-connect-rule-taskaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-taskaction-syntax.json"></a>

```
{
  "[ContactFlowArn](#cfn-connect-rule-taskaction-contactflowarn)" : {{String}},
  "[Description](#cfn-connect-rule-taskaction-description)" : {{String}},
  "[Name](#cfn-connect-rule-taskaction-name)" : {{String}},
  "[References](#cfn-connect-rule-taskaction-references)" : {{Reference}}
}
```

### YAML
<a name="aws-properties-connect-rule-taskaction-syntax.yaml"></a>

```
  [ContactFlowArn](#cfn-connect-rule-taskaction-contactflowarn): {{String}}
  [Description](#cfn-connect-rule-taskaction-description): {{String}}
  [Name](#cfn-connect-rule-taskaction-name): {{String}}
  [References](#cfn-connect-rule-taskaction-references): {{
    Reference}}
```

## Properties
<a name="aws-properties-connect-rule-taskaction-properties"></a>

`ContactFlowArn`  <a name="cfn-connect-rule-taskaction-contactflowarn"></a>
The Amazon Resource Name (ARN) of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^$|arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-rule-taskaction-description"></a>
The description. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-rule-taskaction-name"></a>
 The name. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Connect Customer Administrators Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`References`  <a name="cfn-connect-rule-taskaction-references"></a>
Information about the reference when the `referenceType` is `URL`. Otherwise, null. `URL` is the only accepted type. (Supports variable injection in the `Value` field.)
*Required*: No
*Type*: [Reference](aws-properties-connect-rule-reference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
