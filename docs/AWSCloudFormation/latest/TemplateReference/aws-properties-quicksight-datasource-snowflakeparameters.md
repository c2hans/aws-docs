---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-snowflakeparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource SnowflakeParameters
<a name="aws-properties-quicksight-datasource-snowflakeparameters"></a>

The parameters for Snowflake.

## Syntax
<a name="aws-properties-quicksight-datasource-snowflakeparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-snowflakeparameters-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-quicksight-datasource-snowflakeparameters-authenticationtype)" : {{String}},
  "[Database](#cfn-quicksight-datasource-snowflakeparameters-database)" : {{String}},
  "[DatabaseAccessControlRole](#cfn-quicksight-datasource-snowflakeparameters-databaseaccesscontrolrole)" : {{String}},
  "[Host](#cfn-quicksight-datasource-snowflakeparameters-host)" : {{String}},
  "[OAuthParameters](#cfn-quicksight-datasource-snowflakeparameters-oauthparameters)" : {{OAuthParameters}},
  "[Warehouse](#cfn-quicksight-datasource-snowflakeparameters-warehouse)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-snowflakeparameters-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-quicksight-datasource-snowflakeparameters-authenticationtype): {{String}}
  [Database](#cfn-quicksight-datasource-snowflakeparameters-database): {{String}}
  [DatabaseAccessControlRole](#cfn-quicksight-datasource-snowflakeparameters-databaseaccesscontrolrole): {{String}}
  [Host](#cfn-quicksight-datasource-snowflakeparameters-host): {{String}}
  [OAuthParameters](#cfn-quicksight-datasource-snowflakeparameters-oauthparameters): {{
    OAuthParameters}}
  [Warehouse](#cfn-quicksight-datasource-snowflakeparameters-warehouse): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-snowflakeparameters-properties"></a>

`AuthenticationType`  <a name="cfn-quicksight-datasource-snowflakeparameters-authenticationtype"></a>
The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.
*Required*: No
*Type*: String
*Allowed values*: `PASSWORD | TOKEN | X509 | KEYPAIR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Database`  <a name="cfn-quicksight-datasource-snowflakeparameters-database"></a>
Database.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseAccessControlRole`  <a name="cfn-quicksight-datasource-snowflakeparameters-databaseaccesscontrolrole"></a>
The database access control role.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-snowflakeparameters-host"></a>
Host.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthParameters`  <a name="cfn-quicksight-datasource-snowflakeparameters-oauthparameters"></a>
An object that contains information needed to create a data source connection between an Quick Sight account and Snowflake.
*Required*: No
*Type*: [OAuthParameters](aws-properties-quicksight-datasource-oauthparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Warehouse`  <a name="cfn-quicksight-datasource-snowflakeparameters-warehouse"></a>
Warehouse.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
