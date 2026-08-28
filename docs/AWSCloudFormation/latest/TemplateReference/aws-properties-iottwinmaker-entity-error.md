---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-error.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity Error
<a name="aws-properties-iottwinmaker-entity-error"></a>

The entity error.

## Syntax
<a name="aws-properties-iottwinmaker-entity-error-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-error-syntax.json"></a>

```
{
  "[Code](#cfn-iottwinmaker-entity-error-code)" : {{String}},
  "[Message](#cfn-iottwinmaker-entity-error-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-error-syntax.yaml"></a>

```
  [Code](#cfn-iottwinmaker-entity-error-code): {{String}}
  [Message](#cfn-iottwinmaker-entity-error-message): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-error-properties"></a>

`Code`  <a name="cfn-iottwinmaker-entity-error-code"></a>
The entity error code.
*Required*: No
*Type*: String
*Allowed values*: `VALIDATION_ERROR | INTERNAL_FAILURE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-iottwinmaker-entity-error-message"></a>
The entity error message.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
