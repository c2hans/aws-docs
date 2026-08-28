---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-starburstparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource StarburstParameters
<a name="aws-properties-quicksight-datasource-starburstparameters"></a>

The parameters that are required to connect to a Starburst data source.

## Syntax
<a name="aws-properties-quicksight-datasource-starburstparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-starburstparameters-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-quicksight-datasource-starburstparameters-authenticationtype)" : {{String}},
  "[Catalog](#cfn-quicksight-datasource-starburstparameters-catalog)" : {{String}},
  "[DatabaseAccessControlRole](#cfn-quicksight-datasource-starburstparameters-databaseaccesscontrolrole)" : {{String}},
  "[Host](#cfn-quicksight-datasource-starburstparameters-host)" : {{String}},
  "[OAuthParameters](#cfn-quicksight-datasource-starburstparameters-oauthparameters)" : {{OAuthParameters}},
  "[Port](#cfn-quicksight-datasource-starburstparameters-port)" : {{Number}},
  "[ProductType](#cfn-quicksight-datasource-starburstparameters-producttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-starburstparameters-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-quicksight-datasource-starburstparameters-authenticationtype): {{String}}
  [Catalog](#cfn-quicksight-datasource-starburstparameters-catalog): {{String}}
  [DatabaseAccessControlRole](#cfn-quicksight-datasource-starburstparameters-databaseaccesscontrolrole): {{String}}
  [Host](#cfn-quicksight-datasource-starburstparameters-host): {{String}}
  [OAuthParameters](#cfn-quicksight-datasource-starburstparameters-oauthparameters): {{
    OAuthParameters}}
  [Port](#cfn-quicksight-datasource-starburstparameters-port): {{Number}}
  [ProductType](#cfn-quicksight-datasource-starburstparameters-producttype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-starburstparameters-properties"></a>

`AuthenticationType`  <a name="cfn-quicksight-datasource-starburstparameters-authenticationtype"></a>
The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.
*Required*: No
*Type*: String
*Allowed values*: `PASSWORD | TOKEN | X509 | KEYPAIR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Catalog`  <a name="cfn-quicksight-datasource-starburstparameters-catalog"></a>
The catalog name for the Starburst data source.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseAccessControlRole`  <a name="cfn-quicksight-datasource-starburstparameters-databaseaccesscontrolrole"></a>
The database access control role.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-starburstparameters-host"></a>
The host name of the Starburst data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthParameters`  <a name="cfn-quicksight-datasource-starburstparameters-oauthparameters"></a>
An object that contains information needed to create a data source connection between an Quick Sight account and Starburst.
*Required*: No
*Type*: [OAuthParameters](aws-properties-quicksight-datasource-oauthparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-starburstparameters-port"></a>
The port for the Starburst data source.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductType`  <a name="cfn-quicksight-datasource-starburstparameters-producttype"></a>
The product type for the Starburst data source.
*Required*: No
*Type*: String
*Allowed values*: `GALAXY | ENTERPRISE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
