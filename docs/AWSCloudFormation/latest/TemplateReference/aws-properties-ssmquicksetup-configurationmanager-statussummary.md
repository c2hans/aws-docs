---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmquicksetup-configurationmanager-statussummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMQuickSetup::ConfigurationManager StatusSummary
<a name="aws-properties-ssmquicksetup-configurationmanager-statussummary"></a>

A summarized description of the status.

## Syntax
<a name="aws-properties-ssmquicksetup-configurationmanager-statussummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmquicksetup-configurationmanager-statussummary-syntax.json"></a>

```
{
  "[LastUpdatedAt](#cfn-ssmquicksetup-configurationmanager-statussummary-lastupdatedat)" : {{String}},
  "[Status](#cfn-ssmquicksetup-configurationmanager-statussummary-status)" : {{String}},
  "[StatusDetails](#cfn-ssmquicksetup-configurationmanager-statussummary-statusdetails)" : {{{{{Key}}: {{Value}}, ...}}},
  "[StatusMessage](#cfn-ssmquicksetup-configurationmanager-statussummary-statusmessage)" : {{String}},
  "[StatusType](#cfn-ssmquicksetup-configurationmanager-statussummary-statustype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmquicksetup-configurationmanager-statussummary-syntax.yaml"></a>

```
  [LastUpdatedAt](#cfn-ssmquicksetup-configurationmanager-statussummary-lastupdatedat): {{String}}
  [Status](#cfn-ssmquicksetup-configurationmanager-statussummary-status): {{String}}
  [StatusDetails](#cfn-ssmquicksetup-configurationmanager-statussummary-statusdetails): {{
    {{Key}}: {{Value}}}}
  [StatusMessage](#cfn-ssmquicksetup-configurationmanager-statussummary-statusmessage): {{String}}
  [StatusType](#cfn-ssmquicksetup-configurationmanager-statussummary-statustype): {{String}}
```

## Properties
<a name="aws-properties-ssmquicksetup-configurationmanager-statussummary-properties"></a>

`LastUpdatedAt`  <a name="cfn-ssmquicksetup-configurationmanager-statussummary-lastupdatedat"></a>
The datetime stamp when the status was last updated.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-ssmquicksetup-configurationmanager-statussummary-status"></a>
The current status.
*Required*: No
*Type*: String
*Allowed values*: `INITIALIZING | DEPLOYING | SUCCEEDED | DELETING | STOPPING | FAILED | STOPPED | DELETE_FAILED | STOP_FAILED | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusDetails`  <a name="cfn-ssmquicksetup-configurationmanager-statussummary-statusdetails"></a>
Details about the status.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusMessage`  <a name="cfn-ssmquicksetup-configurationmanager-statussummary-statusmessage"></a>
When applicable, returns an informational message relevant to the current status and status type of the status summary object. We don't recommend implementing parsing logic around this value since the messages returned can vary in format.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusType`  <a name="cfn-ssmquicksetup-configurationmanager-statussummary-statustype"></a>
The type of a status summary.
*Required*: Yes
*Type*: String
*Allowed values*: `Deployment | AsyncExecutions`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
