---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-dashboard-widget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Dashboard Widget
<a name="aws-properties-cloudtrail-dashboard-widget"></a>

 Contains information about a widget on a CloudTrail Lake dashboard.

## Syntax
<a name="aws-properties-cloudtrail-dashboard-widget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-dashboard-widget-syntax.json"></a>

```
{
  "[QueryParameters](#cfn-cloudtrail-dashboard-widget-queryparameters)" : {{[ String, ... ]}},
  "[QueryStatement](#cfn-cloudtrail-dashboard-widget-querystatement)" : {{String}},
  "[ViewProperties](#cfn-cloudtrail-dashboard-widget-viewproperties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-cloudtrail-dashboard-widget-syntax.yaml"></a>

```
  [QueryParameters](#cfn-cloudtrail-dashboard-widget-queryparameters): {{
    - String}}
  [QueryStatement](#cfn-cloudtrail-dashboard-widget-querystatement): {{String}}
  [ViewProperties](#cfn-cloudtrail-dashboard-widget-viewproperties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-cloudtrail-dashboard-widget-properties"></a>

`QueryParameters`  <a name="cfn-cloudtrail-dashboard-widget-queryparameters"></a>
 The optional query parameters. The following query parameters are valid: `$StartTime$`, `$EndTime$`, and `$Period$`.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStatement`  <a name="cfn-cloudtrail-dashboard-widget-querystatement"></a>
 The query statement for the widget. For custom dashboard widgets, you can query across multiple event data stores as long as all event data stores exist in your account.
When a query uses `?` with `eventTime`, `?` must be surrounded by single quotes as follows: `'?'`.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewProperties`  <a name="cfn-cloudtrail-dashboard-widget-viewproperties"></a>
 The view properties for the widget. For more information about view properties, see [ View properties for widgets ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html) in the *AWS CloudTrail User Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9._-]{3,128}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
