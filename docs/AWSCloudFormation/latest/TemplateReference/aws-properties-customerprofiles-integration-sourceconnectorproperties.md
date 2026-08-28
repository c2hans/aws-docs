---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-sourceconnectorproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration SourceConnectorProperties
<a name="aws-properties-customerprofiles-integration-sourceconnectorproperties"></a>

Specifies the information that is required to query a particular Amazon AppFlow connector. Customer Profiles supports Salesforce, Zendesk, Marketo, ServiceNow and Amazon S3.

## Syntax
<a name="aws-properties-customerprofiles-integration-sourceconnectorproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-sourceconnectorproperties-syntax.json"></a>

```
{
  "[Marketo](#cfn-customerprofiles-integration-sourceconnectorproperties-marketo)" : {{MarketoSourceProperties}},
  "[S3](#cfn-customerprofiles-integration-sourceconnectorproperties-s3)" : {{S3SourceProperties}},
  "[Salesforce](#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce)" : {{SalesforceSourceProperties}},
  "[ServiceNow](#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow)" : {{ServiceNowSourceProperties}},
  "[Zendesk](#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk)" : {{ZendeskSourceProperties}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-sourceconnectorproperties-syntax.yaml"></a>

```
  [Marketo](#cfn-customerprofiles-integration-sourceconnectorproperties-marketo): {{
    MarketoSourceProperties}}
  [S3](#cfn-customerprofiles-integration-sourceconnectorproperties-s3): {{
    S3SourceProperties}}
  [Salesforce](#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce): {{
    SalesforceSourceProperties}}
  [ServiceNow](#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow): {{
    ServiceNowSourceProperties}}
  [Zendesk](#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk): {{
    ZendeskSourceProperties}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-sourceconnectorproperties-properties"></a>

`Marketo`  <a name="cfn-customerprofiles-integration-sourceconnectorproperties-marketo"></a>
The properties that are applied when Marketo is being used as a source.
*Required*: No
*Type*: [MarketoSourceProperties](aws-properties-customerprofiles-integration-marketosourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-customerprofiles-integration-sourceconnectorproperties-s3"></a>
The properties that are applied when Amazon S3 is being used as the flow source.
*Required*: No
*Type*: [S3SourceProperties](aws-properties-customerprofiles-integration-s3sourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Salesforce`  <a name="cfn-customerprofiles-integration-sourceconnectorproperties-salesforce"></a>
The properties that are applied when Salesforce is being used as a source.
*Required*: No
*Type*: [SalesforceSourceProperties](aws-properties-customerprofiles-integration-salesforcesourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNow`  <a name="cfn-customerprofiles-integration-sourceconnectorproperties-servicenow"></a>
The properties that are applied when ServiceNow is being used as a source.
*Required*: No
*Type*: [ServiceNowSourceProperties](aws-properties-customerprofiles-integration-servicenowsourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Zendesk`  <a name="cfn-customerprofiles-integration-sourceconnectorproperties-zendesk"></a>
The properties that are applied when using Zendesk as a flow source.
*Required*: No
*Type*: [ZendeskSourceProperties](aws-properties-customerprofiles-integration-zendesksourceproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
