---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-catalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog
<a name="aws-resource-glue-catalog"></a>

The `AWS::Glue::Catalog` resource specifies a catalog object that represents a logical grouping of databases in the AWS Glue Data Catalog or a federated source. You can create a Redshift-federated catalog or a catalog containing resource links to Redshift databases in another account or region.

## Syntax
<a name="aws-resource-glue-catalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-catalog-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::Catalog",
  "Properties" : {
      "[AllowFullTableExternalDataAccess](#cfn-glue-catalog-allowfulltableexternaldataaccess)" : {{String}},
      "[CatalogProperties](#cfn-glue-catalog-catalogproperties)" : {{CatalogProperties}},
      "[CreateDatabaseDefaultPermissions](#cfn-glue-catalog-createdatabasedefaultpermissions)" : {{[ PrincipalPermissions, ... ]}},
      "[CreateTableDefaultPermissions](#cfn-glue-catalog-createtabledefaultpermissions)" : {{[ PrincipalPermissions, ... ]}},
      "[Description](#cfn-glue-catalog-description)" : {{String}},
      "[FederatedCatalog](#cfn-glue-catalog-federatedcatalog)" : {{FederatedCatalog}},
      "[Name](#cfn-glue-catalog-name)" : {{String}},
      "[OverwriteChildResourcePermissionsWithDefault](#cfn-glue-catalog-overwritechildresourcepermissionswithdefault)" : {{String}},
      "[Parameters](#cfn-glue-catalog-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Tags](#cfn-glue-catalog-tags)" : {{[ Tag, ... ]}},
      "[TargetRedshiftCatalog](#cfn-glue-catalog-targetredshiftcatalog)" : {{TargetRedshiftCatalog}}
    }
}
```

### YAML
<a name="aws-resource-glue-catalog-syntax.yaml"></a>

```
Type: AWS::Glue::Catalog
Properties:
  [AllowFullTableExternalDataAccess](#cfn-glue-catalog-allowfulltableexternaldataaccess): {{String}}
  [CatalogProperties](#cfn-glue-catalog-catalogproperties): {{
    CatalogProperties}}
  [CreateDatabaseDefaultPermissions](#cfn-glue-catalog-createdatabasedefaultpermissions): {{
    - PrincipalPermissions}}
  [CreateTableDefaultPermissions](#cfn-glue-catalog-createtabledefaultpermissions): {{
    - PrincipalPermissions}}
  [Description](#cfn-glue-catalog-description): {{String}}
  [FederatedCatalog](#cfn-glue-catalog-federatedcatalog): {{
    FederatedCatalog}}
  [Name](#cfn-glue-catalog-name): {{String}}
  [OverwriteChildResourcePermissionsWithDefault](#cfn-glue-catalog-overwritechildresourcepermissionswithdefault): {{String}}
  [Parameters](#cfn-glue-catalog-parameters): {{
    {{Key}}: {{Value}}}}
  [Tags](#cfn-glue-catalog-tags): {{
    - Tag}}
  [TargetRedshiftCatalog](#cfn-glue-catalog-targetredshiftcatalog): {{
    TargetRedshiftCatalog}}
```

## Properties
<a name="aws-resource-glue-catalog-properties"></a>

`AllowFullTableExternalDataAccess`  <a name="cfn-glue-catalog-allowfulltableexternaldataaccess"></a>
Allows third-party engines to access data in Amazon S3 locations that are registered with AWS Lake Formation.
This property is write-only. The value is not returned by `Fn::GetAtt` or `Ref`.
*Required*: No
*Type*: String
*Allowed values*: `True | False`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CatalogProperties`  <a name="cfn-glue-catalog-catalogproperties"></a>
A `CatalogProperties` object that specifies data lake access properties and other custom properties.
*Required*: No
*Type*: [CatalogProperties](aws-properties-glue-catalog-catalogproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateDatabaseDefaultPermissions`  <a name="cfn-glue-catalog-createdatabasedefaultpermissions"></a>
An array of `PrincipalPermissions` objects. Creates a set of default permissions on the database(s) for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.
*Required*: No
*Type*: Array of [PrincipalPermissions](aws-properties-glue-catalog-principalpermissions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateTableDefaultPermissions`  <a name="cfn-glue-catalog-createtabledefaultpermissions"></a>
An array of `PrincipalPermissions` objects. Creates a set of default permissions on the table(s) for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.
*Required*: No
*Type*: Array of [PrincipalPermissions](aws-properties-glue-catalog-principalpermissions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-glue-catalog-description"></a>
A description of the catalog, not more than 2048 bytes long.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FederatedCatalog`  <a name="cfn-glue-catalog-federatedcatalog"></a>
A `FederatedCatalog` object that points to an entity outside the AWS Glue Data Catalog.
*Required*: No
*Type*: [FederatedCatalog](aws-properties-glue-catalog-federatedcatalog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-catalog-name"></a>
The name of the catalog. Cannot be the same as the account ID.
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverwriteChildResourcePermissionsWithDefault`  <a name="cfn-glue-catalog-overwritechildresourcepermissionswithdefault"></a>
Specifies whether to overwrite child resource permissions with the default permissions. Valid values are `Accept` and `Deny`.
This property is write-only. The value is not returned by `Fn::GetAtt` or `Ref`.
*Required*: No
*Type*: String
*Allowed values*: `Accept | Deny`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-glue-catalog-parameters"></a>
 A map array of key-value pairs that define parameters and properties of the catalog.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-glue-catalog-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-catalog-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRedshiftCatalog`  <a name="cfn-glue-catalog-targetredshiftcatalog"></a>
A `TargetRedshiftCatalog` object that describes a target catalog for database resource linking.
*Required*: No
*Type*: [TargetRedshiftCatalog](aws-properties-glue-catalog-targetredshiftcatalog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-catalog-return-values"></a>

### Ref
<a name="aws-resource-glue-catalog-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the catalog, such as `arn:aws:glue:us-east-1:123456789012:catalog/my-catalog`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-glue-catalog-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-glue-catalog-return-values-fn--getatt-fn--getatt"></a>

`CatalogId`  <a name="CatalogId-fn::getatt"></a>
The ID of the catalog.

`CatalogProperties.DataLakeAccessProperties.ManagedWorkgroupName`  <a name="CatalogProperties.DataLakeAccessProperties.ManagedWorkgroupName-fn::getatt"></a>
The name of the managed workgroup associated with the catalog.

`CatalogProperties.DataLakeAccessProperties.ManagedWorkgroupStatus`  <a name="CatalogProperties.DataLakeAccessProperties.ManagedWorkgroupStatus-fn::getatt"></a>
The status of the managed workgroup.

`CatalogProperties.DataLakeAccessProperties.RedshiftDatabaseName`  <a name="CatalogProperties.DataLakeAccessProperties.RedshiftDatabaseName-fn::getatt"></a>
The name of the Redshift database associated with the catalog.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The time at which the catalog was created.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) assigned to the catalog resource.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
The time at which the catalog was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
