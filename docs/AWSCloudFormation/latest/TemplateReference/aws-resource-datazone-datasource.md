---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource
<a name="aws-resource-datazone-datasource"></a>

The `AWS::DataZone::DataSource`resource specifies an Amazon DataZone data source that is used to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone.

## Syntax
<a name="aws-resource-datazone-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-datasource-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::DataSource",
  "Properties" : {
      "[AssetFormsInput](#cfn-datazone-datasource-assetformsinput)" : {{[ FormInput, ... ]}},
      "[Configuration](#cfn-datazone-datasource-configuration)" : {{DataSourceConfigurationInput}},
      "[ConnectionIdentifier](#cfn-datazone-datasource-connectionidentifier)" : {{String}},
      "[Description](#cfn-datazone-datasource-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-datasource-domainidentifier)" : {{String}},
      "[EnableSetting](#cfn-datazone-datasource-enablesetting)" : {{String}},
      "[EnvironmentIdentifier](#cfn-datazone-datasource-environmentidentifier)" : {{String}},
      "[Name](#cfn-datazone-datasource-name)" : {{String}},
      "[ProjectIdentifier](#cfn-datazone-datasource-projectidentifier)" : {{String}},
      "[PublishOnImport](#cfn-datazone-datasource-publishonimport)" : {{Boolean}},
      "[Recommendation](#cfn-datazone-datasource-recommendation)" : {{RecommendationConfiguration}},
      "[Schedule](#cfn-datazone-datasource-schedule)" : {{ScheduleConfiguration}},
      "[Type](#cfn-datazone-datasource-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-datasource-syntax.yaml"></a>

```
Type: AWS::DataZone::DataSource
Properties:
  [AssetFormsInput](#cfn-datazone-datasource-assetformsinput): {{
    - FormInput}}
  [Configuration](#cfn-datazone-datasource-configuration): {{
    DataSourceConfigurationInput}}
  [ConnectionIdentifier](#cfn-datazone-datasource-connectionidentifier): {{String}}
  [Description](#cfn-datazone-datasource-description): {{String}}
  [DomainIdentifier](#cfn-datazone-datasource-domainidentifier): {{String}}
  [EnableSetting](#cfn-datazone-datasource-enablesetting): {{String}}
  [EnvironmentIdentifier](#cfn-datazone-datasource-environmentidentifier): {{String}}
  [Name](#cfn-datazone-datasource-name): {{String}}
  [ProjectIdentifier](#cfn-datazone-datasource-projectidentifier): {{String}}
  [PublishOnImport](#cfn-datazone-datasource-publishonimport): {{Boolean}}
  [Recommendation](#cfn-datazone-datasource-recommendation): {{
    RecommendationConfiguration}}
  [Schedule](#cfn-datazone-datasource-schedule): {{
    ScheduleConfiguration}}
  [Type](#cfn-datazone-datasource-type): {{String}}
```

## Properties
<a name="aws-resource-datazone-datasource-properties"></a>

`AssetFormsInput`  <a name="cfn-datazone-datasource-assetformsinput"></a>
The metadata forms attached to the assets that the data source works with.
*Required*: No
*Type*: Array of [FormInput](aws-properties-datazone-datasource-forminput.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-datazone-datasource-configuration"></a>
The configuration of the data source.
*Required*: No
*Type*: [DataSourceConfigurationInput](aws-properties-datazone-datasource-datasourceconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionIdentifier`  <a name="cfn-datazone-datasource-connectionidentifier"></a>
The ID of the connection.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-datazone-datasource-description"></a>
The description of the data source.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-datasource-domainidentifier"></a>
The ID of the Amazon DataZone domain where the data source is created.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableSetting`  <a name="cfn-datazone-datasource-enablesetting"></a>
Specifies whether the data source is enabled.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentIdentifier`  <a name="cfn-datazone-datasource-environmentidentifier"></a>
The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-datazone-datasource-name"></a>
The name of the data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectIdentifier`  <a name="cfn-datazone-datasource-projectidentifier"></a>
The identifier of the Amazon DataZone project in which you want to add this data source.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublishOnImport`  <a name="cfn-datazone-datasource-publishonimport"></a>
Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Recommendation`  <a name="cfn-datazone-datasource-recommendation"></a>
Specifies whether the business name generation is to be enabled for this data source.
*Required*: No
*Type*: [RecommendationConfiguration](aws-properties-datazone-datasource-recommendationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-datazone-datasource-schedule"></a>
The schedule of the data source runs.
*Required*: No
*Type*: [ScheduleConfiguration](aws-properties-datazone-datasource-scheduleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-datazone-datasource-type"></a>
The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for AWS Glue and Amazon Redshift.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-datasource-return-values"></a>

### Ref
<a name="aws-resource-datazone-datasource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and the `DataSourceId`, which uniquely identifies the data source. For example: `{ "Ref": "MyDataSource" }` for the resource with the logical ID `MyDataSource`, `Ref` returns `DomainId|DataSourceId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-datasource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-datasource-return-values-fn--getatt-fn--getatt"></a>

`ConnectionId`  <a name="ConnectionId-fn::getatt"></a>
The connection ID that's part of the data source summary.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the data source was created.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The ID of the Amazon DataZone domain in which the data source exists.

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The ID of the environment in which the data source exists.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the data source run.

`LastRunAssetCount`  <a name="LastRunAssetCount-fn::getatt"></a>
The count of the assets created during the last data source run.

`LastRunAt`  <a name="LastRunAt-fn::getatt"></a>
The timestamp of when the data source run was last performed.

`LastRunStatus`  <a name="LastRunStatus-fn::getatt"></a>
The status of the last data source run.

`ProjectId`  <a name="ProjectId-fn::getatt"></a>
The project ID included in the data source run activity.

`Status`  <a name="Status-fn::getatt"></a>
The status of the data source.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp of when the data source was updated.
