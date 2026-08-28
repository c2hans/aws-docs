---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-destinationflowconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow DestinationFlowConfig
<a name="aws-properties-appflow-flow-destinationflowconfig"></a>

 Contains information about the configuration of destination connectors present in the flow.

## Syntax
<a name="aws-properties-appflow-flow-destinationflowconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-destinationflowconfig-syntax.json"></a>

```
{
  "[ApiVersion](#cfn-appflow-flow-destinationflowconfig-apiversion)" : {{String}},
  "[ConnectorProfileName](#cfn-appflow-flow-destinationflowconfig-connectorprofilename)" : {{String}},
  "[ConnectorType](#cfn-appflow-flow-destinationflowconfig-connectortype)" : {{String}},
  "[DestinationConnectorProperties](#cfn-appflow-flow-destinationflowconfig-destinationconnectorproperties)" : {{DestinationConnectorProperties}}
}
```

### YAML
<a name="aws-properties-appflow-flow-destinationflowconfig-syntax.yaml"></a>

```
  [ApiVersion](#cfn-appflow-flow-destinationflowconfig-apiversion): {{String}}
  [ConnectorProfileName](#cfn-appflow-flow-destinationflowconfig-connectorprofilename): {{String}}
  [ConnectorType](#cfn-appflow-flow-destinationflowconfig-connectortype): {{String}}
  [DestinationConnectorProperties](#cfn-appflow-flow-destinationflowconfig-destinationconnectorproperties): {{
    DestinationConnectorProperties}}
```

## Properties
<a name="aws-properties-appflow-flow-destinationflowconfig-properties"></a>

`ApiVersion`  <a name="cfn-appflow-flow-destinationflowconfig-apiversion"></a>
The API version that the destination connector uses.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorProfileName`  <a name="cfn-appflow-flow-destinationflowconfig-connectorprofilename"></a>
 The name of the connector profile. This name must be unique for each connector profile in the AWS account.
*Required*: No
*Type*: String
*Pattern*: `[\w/!@#+=.-]+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorType`  <a name="cfn-appflow-flow-destinationflowconfig-connectortype"></a>
 The type of destination connector, such as Sales force, Amazon S3, and so on.
*Required*: Yes
*Type*: String
*Allowed values*: `SAPOData | Salesforce | Pardot | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | CustomConnector | EventBridge | Upsolver | LookoutMetrics`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationConnectorProperties`  <a name="cfn-appflow-flow-destinationflowconfig-destinationconnectorproperties"></a>
 This stores the information that is required to query a particular connector.
*Required*: Yes
*Type*: [DestinationConnectorProperties](aws-properties-appflow-flow-destinationconnectorproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-destinationflowconfig--seealso"></a>
+ [DestinationConnectorProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DestinationConnectorProperties.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
