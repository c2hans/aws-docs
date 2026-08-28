---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-sessionlogger-eventfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::SessionLogger EventFilter
<a name="aws-properties-workspacesweb-sessionlogger-eventfilter"></a>

The filter that specifies the events to monitor.

## Syntax
<a name="aws-properties-workspacesweb-sessionlogger-eventfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-sessionlogger-eventfilter-syntax.json"></a>

```
{
  "[All](#cfn-workspacesweb-sessionlogger-eventfilter-all)" : {{Json}},
  "[Include](#cfn-workspacesweb-sessionlogger-eventfilter-include)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-workspacesweb-sessionlogger-eventfilter-syntax.yaml"></a>

```
  [All](#cfn-workspacesweb-sessionlogger-eventfilter-all): {{Json}}
  [Include](#cfn-workspacesweb-sessionlogger-eventfilter-include): {{
    - String}}
```

## Properties
<a name="aws-properties-workspacesweb-sessionlogger-eventfilter-properties"></a>

`All`  <a name="cfn-workspacesweb-sessionlogger-eventfilter-all"></a>
The filter that monitors all of the available events, including any new events emitted in the future. The `All` and `Include` properties are not required, but one of them should be present. `{}` is a valid input.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Include`  <a name="cfn-workspacesweb-sessionlogger-eventfilter-include"></a>
The filter that monitors only the listed set of events. New events are not auto-monitored. The `All` and `Include` properties are not required, but one of them should be present.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
