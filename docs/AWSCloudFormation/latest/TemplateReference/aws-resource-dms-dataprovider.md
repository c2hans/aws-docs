---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-dataprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider
<a name="aws-resource-dms-dataprovider"></a>

Provides information that defines a data provider.

## Syntax
<a name="aws-resource-dms-dataprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dms-dataprovider-syntax.json"></a>

```
{
  "Type" : "AWS::DMS::DataProvider",
  "Properties" : {
      "[DataProviderIdentifier](#cfn-dms-dataprovider-dataprovideridentifier)" : {{String}},
      "[DataProviderName](#cfn-dms-dataprovider-dataprovidername)" : {{String}},
      "[Description](#cfn-dms-dataprovider-description)" : {{String}},
      "[Engine](#cfn-dms-dataprovider-engine)" : {{String}},
      "[ExactSettings](#cfn-dms-dataprovider-exactsettings)" : {{Boolean}},
      "[Settings](#cfn-dms-dataprovider-settings)" : {{Settings}},
      "[Tags](#cfn-dms-dataprovider-tags)" : {{[ Tag, ... ]}},
      "[Virtual](#cfn-dms-dataprovider-virtual)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-dms-dataprovider-syntax.yaml"></a>

```
Type: AWS::DMS::DataProvider
Properties:
  [DataProviderIdentifier](#cfn-dms-dataprovider-dataprovideridentifier): {{String}}
  [DataProviderName](#cfn-dms-dataprovider-dataprovidername): {{String}}
  [Description](#cfn-dms-dataprovider-description): {{String}}
  [Engine](#cfn-dms-dataprovider-engine): {{String}}
  [ExactSettings](#cfn-dms-dataprovider-exactsettings): {{Boolean}}
  [Settings](#cfn-dms-dataprovider-settings): {{
    Settings}}
  [Tags](#cfn-dms-dataprovider-tags): {{
    - Tag}}
  [Virtual](#cfn-dms-dataprovider-virtual): {{Boolean}}
```

## Properties
<a name="aws-resource-dms-dataprovider-properties"></a>

`DataProviderIdentifier`  <a name="cfn-dms-dataprovider-dataprovideridentifier"></a>
The name or Amazon Resource Name (ARN) of the data provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataProviderName`  <a name="cfn-dms-dataprovider-dataprovidername"></a>
The name of the data provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-dms-dataprovider-description"></a>
A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-dms-dataprovider-engine"></a>
The type of database engine for the data provider.
Valid values: `aurora`, `aurora-postgresql`, `db2`, `db2-zos`, `docdb`, `mariadb`, `mongodb`, `mysql`, `oracle`, `postgres`, `redshift`, `sqlserver`, and `sybase`. A value of `aurora` represents Amazon Aurora MySQL-Compatible Edition.
*Required*: Yes
*Type*: String
*Allowed values*: `aurora | aurora_postgresql | mysql | oracle | postgres | sqlserver | redshift | mariadb | mongodb | docdb | db2 | db2_zos | sybase`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExactSettings`  <a name="cfn-dms-dataprovider-exactsettings"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-dms-dataprovider-settings"></a>
The settings in JSON format for a data provider.
*Required*: No
*Type*: [Settings](aws-properties-dms-dataprovider-settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dms-dataprovider-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-dms-dataprovider-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Virtual`  <a name="cfn-dms-dataprovider-virtual"></a>
Indicates whether the data provider is virtual.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dms-dataprovider-return-values"></a>

### Ref
<a name="aws-resource-dms-dataprovider-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dms-dataprovider-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dms-dataprovider-return-values-fn--getatt-fn--getatt"></a>

`DataProviderArn`  <a name="DataProviderArn-fn::getatt"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the data provider.

`DataProviderCreationTime`  <a name="DataProviderCreationTime-fn::getatt"></a>
The time the data provider was created.
