---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-hoursofoperation-hoursofoperationsidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::HoursOfOperation HoursOfOperationsIdentifier
<a name="aws-properties-connect-hoursofoperation-hoursofoperationsidentifier"></a>

Identifier for a hours of operations resource: ARN, ID, Name

## Syntax
<a name="aws-properties-connect-hoursofoperation-hoursofoperationsidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-hoursofoperation-hoursofoperationsidentifier-syntax.json"></a>

```
{
  "[Id](#cfn-connect-hoursofoperation-hoursofoperationsidentifier-id)" : {{String}},
  "[Name](#cfn-connect-hoursofoperation-hoursofoperationsidentifier-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-hoursofoperation-hoursofoperationsidentifier-syntax.yaml"></a>

```
  [Id](#cfn-connect-hoursofoperation-hoursofoperationsidentifier-id): {{String}}
  [Name](#cfn-connect-hoursofoperation-hoursofoperationsidentifier-name): {{String}}
```

## Properties
<a name="aws-properties-connect-hoursofoperation-hoursofoperationsidentifier-properties"></a>

`Id`  <a name="cfn-connect-hoursofoperation-hoursofoperationsidentifier-id"></a>
Unique identifier of the hours of operation.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-hoursofoperation-hoursofoperationsidentifier-name"></a>
Name of the hours of operation
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
