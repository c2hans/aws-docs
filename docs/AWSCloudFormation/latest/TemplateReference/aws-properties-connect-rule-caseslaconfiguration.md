---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-caseslaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule CaseSlaConfiguration
<a name="aws-properties-connect-rule-caseslaconfiguration"></a>

The SLA configuration for Case SlaAssignmentType.

## Syntax
<a name="aws-properties-connect-rule-caseslaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-caseslaconfiguration-syntax.json"></a>

```
{
  "[FieldId](#cfn-connect-rule-caseslaconfiguration-fieldid)" : {{String}},
  "[Name](#cfn-connect-rule-caseslaconfiguration-name)" : {{String}},
  "[TargetFieldValues](#cfn-connect-rule-caseslaconfiguration-targetfieldvalues)" : {{[ SlaTargetFieldValue, ... ]}},
  "[TargetSlaMinutes](#cfn-connect-rule-caseslaconfiguration-targetslaminutes)" : {{Number}},
  "[Type](#cfn-connect-rule-caseslaconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-caseslaconfiguration-syntax.yaml"></a>

```
  [FieldId](#cfn-connect-rule-caseslaconfiguration-fieldid): {{String}}
  [Name](#cfn-connect-rule-caseslaconfiguration-name): {{String}}
  [TargetFieldValues](#cfn-connect-rule-caseslaconfiguration-targetfieldvalues): {{
    - SlaTargetFieldValue}}
  [TargetSlaMinutes](#cfn-connect-rule-caseslaconfiguration-targetslaminutes): {{Number}}
  [Type](#cfn-connect-rule-caseslaconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-caseslaconfiguration-properties"></a>

`FieldId`  <a name="cfn-connect-rule-caseslaconfiguration-fieldid"></a>
Unique identifier of a Case field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-rule-caseslaconfiguration-name"></a>
Name of an SLA.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetFieldValues`  <a name="cfn-connect-rule-caseslaconfiguration-targetfieldvalues"></a>
Represents a list of target field values for the fieldId specified in CaseSlaConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.
*Required*: No
*Type*: Array of [SlaTargetFieldValue](aws-properties-connect-rule-slatargetfieldvalue.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetSlaMinutes`  <a name="cfn-connect-rule-caseslaconfiguration-targetslaminutes"></a>
Target duration in minutes within which an SLA should be completed.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `1051200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-rule-caseslaconfiguration-type"></a>
Type of SLA for Case SlaAssignmentType.
*Required*: Yes
*Type*: String
*Allowed values*: `CaseField`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
