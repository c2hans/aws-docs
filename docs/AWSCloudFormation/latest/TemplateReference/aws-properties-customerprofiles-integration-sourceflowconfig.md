---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-sourceflowconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration SourceFlowConfig
<a name="aws-properties-customerprofiles-integration-sourceflowconfig"></a>

The configuration that controls how Customer Profiles retrieves data from the source.

## Syntax
<a name="aws-properties-customerprofiles-integration-sourceflowconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-sourceflowconfig-syntax.json"></a>

```
{
  "[ConnectorProfileName](#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename)" : {{String}},
  "[ConnectorType](#cfn-customerprofiles-integration-sourceflowconfig-connectortype)" : {{String}},
  "[IncrementalPullConfig](#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig)" : {{IncrementalPullConfig}},
  "[SourceConnectorProperties](#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties)" : {{SourceConnectorProperties}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-sourceflowconfig-syntax.yaml"></a>

```
  [ConnectorProfileName](#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename): {{String}}
  [ConnectorType](#cfn-customerprofiles-integration-sourceflowconfig-connectortype): {{String}}
  [IncrementalPullConfig](#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig): {{
    IncrementalPullConfig}}
  [SourceConnectorProperties](#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties): {{
    SourceConnectorProperties}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-sourceflowconfig-properties"></a>

`ConnectorProfileName`  <a name="cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename"></a>
The name of the Amazon AppFlow connector profile. This name must be unique for each connector profile in the AWS account.
*Required*: No
*Type*: String
*Pattern*: `[\w/!@#+=.-]+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorType`  <a name="cfn-customerprofiles-integration-sourceflowconfig-connectortype"></a>
The type of connector, such as Salesforce, Marketo, and so on.
*Required*: Yes
*Type*: String
*Allowed values*: `Salesforce | Marketo | ServiceNow | Zendesk | S3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncrementalPullConfig`  <a name="cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig"></a>
Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.
*Required*: No
*Type*: [IncrementalPullConfig](aws-properties-customerprofiles-integration-incrementalpullconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceConnectorProperties`  <a name="cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties"></a>
Specifies the information that is required to query a particular source connector.
*Required*: Yes
*Type*: [SourceConnectorProperties](aws-properties-customerprofiles-integration-sourceconnectorproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
