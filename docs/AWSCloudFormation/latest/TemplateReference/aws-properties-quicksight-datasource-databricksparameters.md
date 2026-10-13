---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-databricksparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource DatabricksParameters
<a name="aws-properties-quicksight-datasource-databricksparameters"></a>

The required parameters that are needed to connect to a Databricks data source.

## Syntax
<a name="aws-properties-quicksight-datasource-databricksparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-databricksparameters-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-quicksight-datasource-databricksparameters-authenticationtype)" : {{String}},
  "[Host](#cfn-quicksight-datasource-databricksparameters-host)" : {{String}},
  "[OAuthParameters](#cfn-quicksight-datasource-databricksparameters-oauthparameters)" : {{OAuthParameters}},
  "[Port](#cfn-quicksight-datasource-databricksparameters-port)" : {{Number}},
  "[SqlEndpointPath](#cfn-quicksight-datasource-databricksparameters-sqlendpointpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-databricksparameters-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-quicksight-datasource-databricksparameters-authenticationtype): {{String}}
  [Host](#cfn-quicksight-datasource-databricksparameters-host): {{String}}
  [OAuthParameters](#cfn-quicksight-datasource-databricksparameters-oauthparameters): {{
    OAuthParameters}}
  [Port](#cfn-quicksight-datasource-databricksparameters-port): {{Number}}
  [SqlEndpointPath](#cfn-quicksight-datasource-databricksparameters-sqlendpointpath): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-databricksparameters-properties"></a>

`AuthenticationType`  <a name="cfn-quicksight-datasource-databricksparameters-authenticationtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PASSWORD | TOKEN | X509 | KEYPAIR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-databricksparameters-host"></a>
The host name of the Databricks data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthParameters`  <a name="cfn-quicksight-datasource-databricksparameters-oauthparameters"></a>
Property description not available.
*Required*: No
*Type*: [OAuthParameters](aws-properties-quicksight-datasource-oauthparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-databricksparameters-port"></a>
The port for the Databricks data source.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqlEndpointPath`  <a name="cfn-quicksight-datasource-databricksparameters-sqlendpointpath"></a>
The HTTP path of the Databricks data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
